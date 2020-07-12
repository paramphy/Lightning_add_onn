import bpy, bmesh

import random


#add Cube
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=True, align='WORLD', location=(0, 0, 0))

# Get the active mesh
obj = bpy.context.edit_object
me = obj.data


# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)

#selecting mesh
for face in bm.faces:
    face.select = False
    print(face.index)
    
bm.faces.ensure_lookup_table()
#bm.faces[1].select = True

face_area = 1
scale = 1
branch = 10

#Extruding and Looping through face area and position
while branch > 0:
    bm.faces.ensure_lookup_table()
    bm.faces[random.randint(0, 5)].select = True
    while face_area > .01:
        scale = scale - .05
        bpy.ops.mesh.extrude_context_move(MESH_OT_extrude_context={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(random.random(), random.random(), random.random()), "orient_type":'NORMAL', "orient_matrix":((-1, 0, 0), (0, -0, 1), (0, 1, 0)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":True, "use_accurate":False})

        bpy.ops.transform.resize(value=(scale, scale, scale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        
        face_area = face_area*scale
        print(face_area)
        print(scale)
        
    bpy.ops.transform.rotate(value=random.randint(0, 360), orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
    branch -= 1
    print(branch)



bm.faces.active = None

# Show the updates in the viewport
# and recalculate n-gon tessellation.
bmesh.update_edit_mesh(me, True)
bpy.ops.object.editmode_toggle()
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.ops.object.shade_smooth()
bpy.context.object.data.use_auto_smooth = True



