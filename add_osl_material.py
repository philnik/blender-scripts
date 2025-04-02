import bpy

# Create material
mat = bpy.data.materials.new("BlenderMirror")
mat.use_nodes = True
nodes = mat.node_tree.nodes
nodes.clear()

# Add OSL node
osl_node = nodes.new('ShaderNodeScript')
osl_node.mode = 'EXTERNAL'
osl_node.filepath = 'c:/Users/filip/AppData/Roaming/blender/scripts/osl/mirror.osl'


# Add Material Output
output_node = nodes.new('ShaderNodeOutputMaterial')
output_node.location = (400, 0)

# Connect nodes
mat.node_tree.links.new(
    osl_node.outputs['BSDF'],
    output_node.inputs['Surface']
)

# Assign to object
bpy.context.object.data.materials.append(mat)
