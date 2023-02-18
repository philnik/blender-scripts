# Create a new mesh
import bpy

from random import random

# Add a new cube object

def add_cubes():
    for i in range(0,100):
        bpy.ops.mesh.primitive_cube_add()
        cube = bpy.context.active_object
        cube.location =(30*random(), 30*random(), 30*random()) 
        cube.scale = (random(),random(),random())
        obj = bpy.context.active_object
        mat = obj.active_material
        new_mat = bpy.data.materials.new(name="NewMaterial")
        obj.active_material = new_mat
        new_mat.diffuse_color = (random(), random(), random(),1.0)
        
      
def delme():  
    for obj in bpy.data.objects:
    # Check if the object's name starts with "Cube"
        if obj.name.startswith("Cube"):
            obj.select_set(True)   
        

def work_on_materials()
            materials = bpy.data.materials

            for material in materials:
                try:
                    print(material.name)
                    node_tree = material.node_tree
                    output_node = node_tree.nodes["Material Output"]
                    surface_node = node_tree.nodes["Principled BSDF"]
                    glossy_node = node_tree.nodes.new("ShaderNodeBsdfGlossy")
                    glossy_node.location = surface_node.location
                    node_tree.links.new(output_node.inputs["Surface"], glossy_node.outputs["BSDF"])
                    node_tree.links.remove(surface_node.outputs["BSDF"].links[0])
                except:
                    pass

    
#delme()
