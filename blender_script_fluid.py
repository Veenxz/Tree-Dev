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

# Tree hight
H = 4
# basic mesh size
deltax = 0.2
# [-xscale, xscale, -yscale, ysacle, -zscale, zscale]
# [-x>=2, x>=2, -y>=4, y [8~25], -z=0, z>= 2.5]
ls = [-1.5, 1.5, -2.5, 6, 0, 2.5]
ll = []
ld = []
la = []
for i in ls:
    ll.append(H * i)
for i in range(3):
    l = -ll[2 * i] + ll[2 * i + 1]
    ld.append(l)
for i in range(3):
    l = ll[2 * i] + ll[2 * i + 1]
    la.append(l)

bpy.ops.mesh.primitive_cube_add(size=H,
                                calc_uvs=True,
                                enter_editmode=False,
                                align='WORLD',
                                location=(la[0], la[1], la[2]),
                                scale=(ld[0], ld[1], ld[2]))

bpy.ops.import_mesh.stl(filepath='./constant/triSurface/Tree.stl')
obj = bpy.data.objects
cube = obj['Cube']
tree = obj['Tree']
bool(cube, tree, 'DIFFERENCE')

cube.name = 'Fluid'
tree.select_set(False)
obj['Fluid'].select_set(True)

bpy.ops.export_mesh.stl(filepath='./constant/triSurface/Fluid.stl',
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

print('Fluid Geometry Generation Finshed!')
