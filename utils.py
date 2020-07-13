import bpy, bmesh

import random

def random_extrude(co = 20, face_area_thres = 0.1, s_scale = 0.05):
    
    face_area = 1
    scale = 1

    #Extruding and Looping through face area and position

    while face_area > face_area_thres:
        scale = scale - s_scale
        bpy.ops.mesh.extrude_context_move(MESH_OT_extrude_context={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(random.randint(-co, co)*random.random(), random.randint(-co, co)*random.random(), random.randint(-co, co)*random.random()), "orient_type":'NORMAL', "orient_matrix":((-1, 0, 0), (0, -0, 1), (0, 1, 0)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":True, "use_accurate":False})
            

        bpy.ops.transform.resize(value=(scale, scale, scale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            
        face_area = face_area*scale
        print(face_area)
        print(scale)
        
        
#Normal Extrude Function
def normal_extrude(excount,o):
    count = 0
    while count < excount:
        bpy.ops.mesh.extrude_region_shrink_fatten(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_shrink_fatten={"value":1, "use_even_offset":False, "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":True, "use_accurate":False})
        bpy.ops.transform.translate(value=(2*random.random(), 2*random.random(), o), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
        bpy.ops.transform.resize(value=(.9, .9, .9), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        print(count)
        count += 1
    print("Done")

def object_extrude():
    
    obj = bpy.context.active_object
    me = obj.data
    print("Object Detected")
    bm = bmesh.from_edit_mesh(me)
    i = 0

    for face in bm.faces:
        i += 1
        print(i)
            
    rand_face = random.randint(0,i)

    print(rand_face)
    for face in bm.faces:
        face.select = False
        print(face.index)

    bm.faces.ensure_lookup_table()
    bm.faces[rand_face].select = True
    count = 0
    #random_extrude(co = 20)
    normal_extrude(20,count)
    bmesh.update_edit_mesh(me, True)
    #bpy.ops.object.editmode_toggle()
    count = 0
    
def lightning(location=(0, 0, 0)):
    
    bpy.ops.mesh.primitive_cube_add(size=5, enter_editmode=True, align='WORLD', location=(0, 0, 0))
    count = 0
    while count < 10:
        object_extrude()
        count += 1
        print("Count", count)
        
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.ops.object.shade_smooth()
    print("Lightning is summoned")

count = 0 
while count < 10:
    lightning()
    count += 1
    
