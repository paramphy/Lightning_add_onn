import bpy, bmesh

import random

def normal_extrude(excount):
    count = 0
    while count < excount:
    #scale = scale - s_scale
        bpy.ops.mesh.extrude_region_shrink_fatten(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_shrink_fatten={"value":5, "use_even_offset":False, "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":True, "use_accurate":False})
        bpy.ops.transform.translate(value=(2*random.random(), 2*random.random(), 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)

    #for face in bm.faces:
        #face.select = False
        #print(face.index)
        #i += 1

    #bm.faces.ensure_lookup_table()
    #bm.faces[random.randint(0,i)].select = True
    #=0
            

        bpy.ops.transform.resize(value=(.9, .9, .9), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            

        print(count)
        count += 1
    print("Done")


normal_extrude(10)

