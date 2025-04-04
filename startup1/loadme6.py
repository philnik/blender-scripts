import bpy
import sys
packages_path = "C:/Users/filip/anaconda3/Lib/site-packages/"
sys.path.insert(0, packages_path )
from jinja2 import Template
#from draw.org2json import org2dict, d0

def load_pip():
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "jinja2"])


fname_list = ["c:/Users/filip/AppData/Roaming/blender/scripts/startup/loadme6.py",
              "c:/Users/filip/AppData/Roaming/blender/scripts/startup/loadme6.py",
#              "C:/Users/filip/AppData/Roaming/python/cad2/draw/org2json.py",
              "c:/Users/filip/AppData/Roaming/blender/scripts/startup/custom_panel2.py"]

filepath = "c:/Users/filip/AppData/Roaming/python/cad2/draw/org2json.py"
with open(filepath, "r") as f:
            code = f.read()

exec(code, sys.modules["__main__"].__dict__)  # Executes in Blender's global scope

def r0():
    for filepath in fname_list:
        with open(filepath, "r") as f:
            code = f.read()
            exec(code, sys.modules["__main__"].__dict__)  # Executes in Blender's global scope


def hello():
    print("it works")



obj_name = "IfcFilter/Sphere"  # Replace with your actual object name

def select_object(obj_name):
    if obj_name in bpy.data.objects:
        bpy.context.view_layer.objects.active = bpy.data.objects[obj_name]  # Make it active
        bpy.data.objects[obj_name].select_set(True)  # Select it
        print(f"Selected: {obj_name}")
    else:
        print(f"Object '{obj_name}' not found!")

def add_pset_properties(object_name):
    #object_name = "IfcFilter/Sphere"
    bpy.data.objects[object_name].PsetProperties.pset_name = 'Pset_FilterTypeCommon'
    bpy.ops.bim.enable_pset_editing(pset_id=0, pset_name="Pset_FilterTypeCommon", pset_type="PSET", obj=object_name, obj_type="Object")
    bpy.ops.bim.enable_pset_editing(pset_id=0, pset_name="Pset_FilterTypeCommon", pset_type="PSET", obj=object_name, obj_type="Object")


def make_ifc_filter():
    """
    reads mesh selection and converts it to IfcFilter
    returns the name of the object
    """
    bpy.context.scene.BIMRootProperties.ifc_product = 'IfcElement'
    bpy.context.scene.BIMRootProperties.ifc_class = 'IfcFilter'
    bpy.ops.bim.assign_class(ifc_class="IfcFilter", predefined_type="AIRPARTICLEFILTER", userdefined_type="")
    bpy.ops.bim.assign_class(ifc_class="IfcFilter", predefined_type="AIRPARTICLEFILTER", userdefined_type="")
    return bpy.context.view_layer.objects.active.name
    

    
class h():
    def __init__(self):
        self.my = ""
        
    def p(self):
        print("hello")

    def p0(self):
        print("hello0")
        

def deselect_all_objects():
    # Ensure we are in Object Mode
    bpy.ops.object.mode_set(mode='OBJECT')
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

        
def make_them_filters():
    for obj in bpy.data.objects:
        name = obj.name
        substrings = ['F8', 'G2', 'G4', 'H12']
        for ss in substrings:
            if ss in name:
                select_object(name)
                make_ifc_filter()
                deselect_all_objects()


def pset_H12(ifc_obj_name,d0):
    bpy.data.objects[ifc_obj_name].PsetProperties.pset_name = 'Pset_FilterTypeCommon'
    bpy.ops.bim.enable_pset_editing(pset_id=0, pset_name="Pset_FilterTypeCommon", pset_type="PSET", obj=ifc_obj_name, obj_type="Object")
    bpy.ops.bim.add_pset(obj=ifc_obj_name, obj_type="Object")
    for key,value in d0.items():
        ddx = value['id']
        dtype = value['type']
        dval = value['val']
        bpy.data.objects[ifc_obj_name].PsetProperties.properties[ddx].metadata.float_value = dval
    bpy.ops.bim.edit_pset(obj=ifc_obj_name, obj_type="Object", pset_id=0)




def import_gltf():
    file_path = "C:/Users/filip/AppData/Roaming/python/cad2/draw/free/step/boxes2.gltf"
    bpy.ops.import_scene.gltf(filepath=file_path)

