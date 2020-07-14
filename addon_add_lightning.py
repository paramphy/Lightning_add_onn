bl_info = {
    "name": "Add Lightning",
    "author": "Paramesh Chandra",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Lightning Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy,bmesh
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
import random



        
        
#Normal Extrude Function
def normal_extrude(excount,o):
    count = 0
    while count < excount:
        bpy.ops.mesh.extrude_region_shrink_fatten(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_shrink_fatten={"value":1, "use_even_offset":False, "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":True, "use_accurate":False})
        bpy.ops.transform.translate(value=(2*random.random(), 2*random.random(), o), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
        bpy.ops.transform.resize(value=(.9, .9, .9), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        print(count)
        count += 1
    print("Done Normal Extruding")

def object_extrude():
    
    obj = bpy.context.active_object
    me = obj.data
    print("Object Detected")
    bm = bmesh.from_edit_mesh(me)
    i = 0

    for face in bm.faces:
        i += 1
        #print(i)
         
    rand_face = random.randint(0,i)
    print(rand_face)
    for face in bm.faces:
        face.select = False
        #print(face.index)

    bm.faces.ensure_lookup_table()
    bm.faces[rand_face].select = True
    count = 0
    normal_extrude(20,count)
    bmesh.update_edit_mesh(me, True)
    
    
    
def lightning_mesh(location=(0, 0, 0)):
    
    bpy.ops.mesh.primitive_cube_add(size=5, enter_editmode=True, align='WORLD', location=(0, 0, 0))
    count = 0
    while count < 10:
        object_extrude()
        count += 1
        print("Count", count)
        
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.modifier_add(type='DISPLACE')
    bpy.ops.texture.new()
    bpy.data.textures["Texture.001"].type = 'CLOUDS'
    bpy.data.textures["Texture.001"].noise_scale = 0.5
    bpy.context.object.modifiers["Displace"].keyframe_insert(data_path="strength", frame=1)
    #node_emission.select = True
    #print(node_emission.name)
    dpath = 'bpy.context.object.modifiers["Displace"].strength'

    fc = bpy.context.object.animation_data.action.fcurves[0]
    #if fc:
    nmod = fc.modifiers.new("NOISE")
    nmod.scale = 10
    nmod.scale = 10
    nmod.phase = 0
    nmod.strength = 2
    nmod.depth = 1.35
    nmod.offset = 0.23
    
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.ops.object.shade_smooth()
    bpy.ops.object.modifier_add(type='BUILD')
    bpy.context.object.modifiers["Build"].frame_duration = 20
    
    print("Lightning is summoned")

    
#Material
def lightning_material():
    so = bpy.context.active_object
    l_mat = bpy.data.materials.new(name = "Lightning Material")
    so.data.materials.append(l_mat)
    l_mat.use_nodes = True
    nodes =l_mat.node_tree.nodes
    material_output = nodes.get("Material Output")
    node_emission = nodes.new(type = 'ShaderNodeEmission')

    node_emission.inputs[0].default_value = [0,0.3,1,1]
    node_emission.inputs[1].default_value = 1
    
    links = l_mat.node_tree.links
    new_link = links.new(node_emission.outputs[0],material_output.inputs[0])
    bpy.context.scene.eevee.use_bloom = True
    
    node_emission.inputs[1].keyframe_insert(data_path="default_value", frame=1)
    node_emission.select = True
    #print(node_emission.name)
    dpath = 'nodes["Emission"].inputs[1].default_value'

    fc = l_mat.node_tree.animation_data.action.fcurves.find(dpath)
    if fc:
        nmod = fc.modifiers.new("NOISE")
        nmod.scale = 10
        nmod.phase = 0
        nmod.strength = 500
        nmod.depth = 1.35
        nmod.offset = 0.23
    

    
def lightning():

    lightning_mesh()
    lightning_material()
    

class AddLightningObject(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_object"
    bl_label = "Add Lghtning Object"
    bl_options = {'REGISTER', 'UNDO'}

    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):

        lightning()

        return {'FINISHED'}


# Registration

def add_object_button(self, context):
    self.layout.operator(
        AddLightningObject.bl_idname,
        text="Add Lightning Object",
        icon='MOD_NOISE')


# This allows you to right click on a button and link to documentation
def add_object_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/latest/"
    url_manual_mapping = (
        ("bpy.ops.mesh.add_object", "scene_layout/object/types.html"),
    )
    return url_manual_prefix, url_manual_mapping


def register():
    bpy.utils.register_class(AddLightningObject)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_button)


def unregister():
    bpy.utils.unregister_class(AddLightningObject)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
    register()