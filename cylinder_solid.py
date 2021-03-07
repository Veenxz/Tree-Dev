import bpy


def clear_all():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)


def bool(obj, obj_c, type):
    bool = obj.modifiers.new(name='Bool', type='BOOLEAN')
    bool.operation = type
    bool.object = obj_c
    
clear_all()

rs = 128
D = 1.0

bpy.ops.mesh.primitive_cylinder_add(vertices=rs,
                                    radius=0.5*D,
                                    depth=D,
                                    end_fill_type='NGON',
                                    calc_uvs=True,
                                    enter_editmode=False,
                                    align='WORLD',
                                    location=(0.0, 0.0, 0.0),
                                    rotation=(0.0, 0.0, 0.0),
                                    scale=(1.0, 1.0, 1.0))


bpy.ops.mesh.primitive_cube_add(size=2*D,
                                calc_uvs=True,
                                enter_editmode=False,
                                align='WORLD',
                                location=(0.0, 8.0, 0.0),
                                scale=(12, 38, 1.0))
                                
obj = bpy.data.objects
cube = obj['Cube']
cylinder = obj['Cylinder']
bool(cube, cylinder, 'DIFFERENCE')

cube.name = 'Fluid'

bpy.ops.export_mesh.stl(filepath='Fluid.stl',
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
