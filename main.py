import bpy, bmesh



bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))

obj = bpy.context.active_object
obj_name = bpy.context.active_object.name
print(obj_name)
bpy.ops.transform.translate(value=(-0, -5.9719, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)


if obj.mode == 'EDIT':
    bm = bmesh.from_edit_mesh(obj.data)
    vertices = bm.verts

else:
    vertices = obj.data.vertices

verts = [obj.matrix_world @ vert.co for vert in vertices] 

# coordinates as tuples
plain_verts = [vert.to_tuple() for vert in verts]

for verts in plain_verts:
    
    if verts[2] < 0 and verts[0]>0:
        print(verts[2])
        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(verts))
        empty_obj_name = bpy.context.active_object.name
        bpy.ops.object.select_all(action='DESELECT')
        #bpy.ops.object.select_all(action='SELECT')
        #bpy.data.objects[empty_obj_name].select_set(state=True)
        
        bpy.data.objects[obj_name].select_set(state=True)
        #bpy.ops.object.editmode_toggle()
        
        #bpy.ops.object.hook_add_selob(use_bone=False)
        #bpy.ops.object.editmode_toggle()

       
       


   


    


    

