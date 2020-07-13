import bpy, bmesh

import random


bpy.ops.mesh.primitive_cube_add(size=5, enter_editmode=True, align='WORLD', location=(0, 0, 0))

obj = bpy.context.edit_object
obj = bpy.context.edit_object
me = obj.data
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
bm.faces[0].select = True

    
face_area = 1
scale = 1
count = 0
co = 10

#Extruding and Looping through face area and position

while count < 50:
    #scale = scale - s_scale
    bpy.ops.mesh.extrude_context_move(MESH_OT_extrude_context={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(random.randint(-co, co)*random.random(), random.randint(-co, co)*random.random(), random.randint(-co, co)*random.random()), "orient_type":'NORMAL', "orient_matrix":((-1, 0, 0), (0, -0, 1), (0, 1, 0)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":True, "use_accurate":False})
            

#    bpy.ops.transform.resize(value=(scale, scale, scale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            
    #face_area = face_area*scale
    #print(face_area)
    #print(scale)
    print(count)
    
    
bmesh.update_edit_mesh(me, True)
bpy.ops.object.editmode_toggle()
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.ops.object.shade_smooth()
bpy.context.object.data.use_auto_smooth = False
    