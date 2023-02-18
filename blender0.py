# Create a new mesh
import bpy

from random import random

# Add a new cube object


import bpy
print("------")

class Material:

    def set_cycles(self):
        scn = bpy.context.scene
        if not scn.render.engine == 'CYCLES':
            scn.render.engine = 'CYCLES'
           
    def make_material(self, name):
        self.mat = bpy.data.materials.new(name)
        self.mat.use_nodes = True
        self.nodes = self.mat.node_tree.nodes
       
    def link(self, from_node, from_slot_name, to_node, to_slot_name):
        input = to_node.inputs[to_slot_name]
        output = from_node.outputs[from_slot_name]
        self.mat.node_tree.links.new(input, output)
       
    def makeNode(self, type, name):
        self.node = self.nodes.new(type)
        self.node.name = name
        self.xpos += 200
        self.node.location = self.xpos, self.ypos
        return self.node
   
    def dump_node(self, node):
        print(node.name)
        print("Inputs:")
        for n in node.inputs: print("	", n)
        print("Outputs:")
        for n in node.outputs: print("	", n)
   
    def new_row():
        self.xpos = 0
        self.ypos += 200        
       
    def __init__(self):
        self.xpos = 0
        self.ypos = 0


        
def add_this():
    m = Material()
    m.set_cycles()
    m.make_material('ch1a')
    diffuseBSDF = m.nodes['Principled BSDF']
    #diffuseBSDF.inputs["Color"].default_value = [0.3, 0.2, 0.4, 0.5]
    materialOutput = m.nodes['Material Output']
    glossyBSDF = m.makeNode('ShaderNodeBsdfGlossy', 'Glossy BSDF')
    #glossyBSDF.inputs["Color"].default_value = [0.4, 0.3, 0.5, 0.5]
    mixShader = m.makeNode('ShaderNodeMixShader', 'Mix Shader')
    m.dump_node(mixShader)
    mixShader.inputs['Fac'].default_value = 0.3
    m.link(glossyBSDF, 'BSDF', mixShader, 1)
    m.link(diffuseBSDF, 'BSDF', mixShader, 2)
    m.link(mixShader, 'Shader', materialOutput, 'Surface')
    return m




def add_cubes():
    for i in range(0,100):
        bpy.ops.mesh.primitive_cube_add()
        cube = bpy.context.active_object
        cube.location =(30*random(), 30*random(), 30*random()) 
        cube.scale = (random(),random(),random())
        obj = bpy.context.active_object
        mat = obj.active_material
        new_mat = add_this()
        obj.active_material = new_mat
        new_mat.diffuse_color = (random(), random(), random(),1.0)
        
      
def delme():  
    for obj in bpy.data.objects:
        if obj.name.startswith("Cube"):
            obj.select_set(True)   


def work_on_materials():
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

