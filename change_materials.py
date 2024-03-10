import bpy


material_name = 'white_silver'
material = bpy.data.materials.get(material_name)

# ob.data.materials.append = material
# ob.data.materials[0] = material


def change_name():
    """
    move data name to object name
    this is because name makes no sense,
    while data name is the actually imported name from CAD file
    """
    obj_list = [i for i in bpy.context.scene.objects]
    for i in obj_list:
        if i.type == 'MESH':
            i.name = i.data.name


def change_material(reg, material_name):
    """
    change material of objects that include pattern `reg'
    """
    obj_list = [i for i in bpy.context.scene.objects]
    # material_name = 'white_silver'
    material = bpy.data.materials.get(material_name)
    for i in obj_list:
        if i.type == 'MESH':
            mesh_material = i.data.materials
            mesh_material.append(material)
            if reg in i.data.name:
                if mesh_material:
                    mesh_material[0]=material 
                else:
                    mesh_material.append(material)


def make_all_variables_global():
    # Get the current global namespace
    global_namespace = globals()

    # Iterate through all local variables in the function
    for var_name in locals():
        # Check if the variable is not a special variable (e.g., '__name__', '__doc__', etc.)
        if var_name != '__name__' and var_name != '__doc__':
            # Update the global namespace with the local variable
            global_namespace[var_name] = locals()[var_name]


# code = exec(open('/home/me/blender/blender.py').read())

def run_script():
    code = exec(open('/home/me/blender/blender-scripts/blender.py').read())
    # make_all_variables_global()


def get_object_names():
    res = []
    for i in obj_list:d
        try:
            mydata = i.data.name
            res.append(mydata)
        except:
            pass    
    return res    


def get_blender_objects():
    objects = []
    for obj in bpy.context.scene.objects:
        objects.append(obj.name)
    return objects


blender_objects = get_blender_objects()

#print(blender_objects)


def get_all_materials():
    ALL_MATS = []
    # Intentional double materials
    for m in bpy.data.materials:
        ALL_MATS.append(m)
        ALL_MATS.append(m)
    s1 = [*set(ALL_MATS)]
    return s1


k=6

a=1
st = get_all_materials()
print(st)
print('k='+str(k))



def get_all_meshes():
    # Clear selection
    bpy.ops.object.select_all(action='DESELECT')

    # Iterate through all objects in the scene
    for obj in bpy.context.scene.objects:
        # Check if the object is a mesh
        if obj.type == 'MESH':
            # Select the mesh object
            obj.select_set(True)

    # Get all selected objects
    selected_objects = bpy.context.selected_objects

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Output the names of all mesh objects
    mesh_names = [obj.name for obj in selected_objects]
    print("Meshes in the scene:", mesh_names)
