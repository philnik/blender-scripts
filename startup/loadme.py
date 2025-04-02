import bpy
import sys
sys.path.append("C:/Users/filip/AppData/Roaming/python/Python311/site-packages/")
sys.path.append("C:/Users/filip/AppData/Roaming/python/cad2/blender/")
sys.path.append("C:/Users/filip/AppData/Roaming/python/cad2/draw/")
fname_list = ["c:/Users/filip/AppData/Roaming/blender/scripts/startup/loadme.py",
              "c:/Users/filip/AppData/Roaming/python/cad2/draw/org2json.py",
              "c:/Users/filip/AppData/Roaming/python/cad2/blender/pset.py",
              "c:/Users/filip/AppData/Roaming/python/cad2/blender/mymain.py",
              "c:/Users/filip/AppData/Roaming/python/cad2/blender/add_materials.py",
              "c:/Users/filip/AppData/Roaming/python/cad2/blender/custom_panel2.py"]

filepath = "c:/Users/filip/AppData/Roaming/python/cad2/draw/org2json.py"

with open(filepath, "r") as f:
            code = f.read()

exec(code, sys.modules["__main__"].__dict__)  # Executes in Blender's global scope

def r0():
    for filepath in fname_list:
        with open(filepath, "r") as f:
            code = f.read()
            exec(code, sys.modules["__main__"].__dict__)  # Executes in Blender's global scope
