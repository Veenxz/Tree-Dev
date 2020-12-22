import bpy


def clear_all():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)


def bool(obj, obj_c, type):
    bool = obj.modifiers.new(name='Bool', type='BOOLEAN')
    bool.operation = type
    bool.object = obj_c


clear_all()

sm = 256
# H = r[0] * sc [2]
r = [2.0, 0.2]
sc = [1.8, 1.5, 2, 1.4, 1]
# h is the hight below the conpy
h = 0.5
z = 0.5 * sc[3] * r[0] + h

bpy.ops.mesh.primitive_uv_sphere_add(segments=sm,
                                     ring_count=0.5 * sm,
                                     radius=r[0],
                                     enter_editmode=False,
                                     align='WORLD',
                                     location=(0, 0, z),
                                     scale=(sc[0], sc[1], sc[2]))

bpy.ops.mesh.primitive_uv_sphere_add(segments=sm,
                                     ring_count=0.5 * sm,
                                     radius=r[0],
                                     enter_editmode=False,
                                     align='WORLD',
                                     location=(0, 0, z),
                                     scale=(sc[0], sc[1], sc[3]))

bpy.ops.mesh.primitive_cylinder_add(vertices=0.5 * sm,
                                    radius=r[1],
                                    depth=1.2 * h,
                                    end_fill_type='NGON',
                                    calc_uvs=True,
                                    enter_editmode=False,
                                    align='WORLD',
                                    location=(0.0, 0.0, 0.6 * h),
                                    rotation=(0.0, 0.0, 0.0),
                                    scale=(sc[4], sc[4], sc[4]))

bpy.ops.mesh.primitive_plane_add(size=max(r) * max(sc),
                                 calc_uvs=True,
                                 enter_editmode=False,
                                 align='WORLD',
                                 location=(0, 0, z),
                                 scale=(1, 1, 1))

obj = bpy.data.objects
sphere0 = obj['Sphere']
sphere1 = obj['Sphere.001']
plane = obj['Plane']
cylinder = obj['Cylinder']

bool(sphere0, plane, 'DIFFERENCE')
bool(sphere1, sphere0, 'DIFFERENCE')
bool(sphere1, sphere0, 'UNION')
bool(sphere1, cylinder, 'UNION')

sphere1.name = 'Tree'
plane.select_set(False)
obj['Tree'].select_set(True)

bpy.ops.export_mesh.stl(filepath='./constant/triSurface/Tree.stl',
                        check_existing=True,
                        filter_glob='*.stl',
                        use_selection=True,
                        global_scale=1.0,
                        use_scene_unit=False,
                        ascii=False,
                        use_mesh_modifiers=True,
                        batch_mode='OFF',
                        axis_forward='Y',
                        axis_up='Z')

#clear_all()
#bpy.ops.import_mesh.stl(filepath='Tree.stl')

print('Tree Geometry Generation Finshed!')
