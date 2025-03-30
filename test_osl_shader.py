import bpy

# Clear existing data
bpy.ops.wm.read_factory_settings(use_empty=True)

# Load the OSL shader
shader_path = "./osl/simple_material.osl"
material = bpy.data.materials.new(name="OSL_Test")
material.use_nodes = True
nodes = material.node_tree.nodes
links = material.node_tree.links

# Remove default Principled BSDF
nodes.remove(nodes.get("Principled BSDF"))

# Add the OSL shader node
osl_node = nodes.new("ShaderNodeScript")
osl_node.mode = 'EXTERNAL'
osl_node.filepath = shader_path
osl_node.location = (0, 0)

# Add Material Output and connect
output_node = nodes.get("Material Output")
links.new(osl_node.outputs["Output"], output_node.inputs["Surface"])

# Assign material to default cube
bpy.context.object.data.materials.append(material)

# Render settings
scene = bpy.context.scene
scene.render.resolution_x = 800
scene.render.resolution_y = 600
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = "./render_test/render_test.png"  # Update this path!

# Render
bpy.ops.render.render(write_still=True)
