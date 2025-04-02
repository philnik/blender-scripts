import bpy

# 1. Define the Operators
class OperatorOne(bpy.types.Operator):
    bl_idname = "object.operator_one"
    bl_label = "Button 1"

    def execute(self, context):
        self.report({'INFO'}, "Button 1 clicked!")
        print("Button 1 was clicked!")
        return {'FINISHED'}

class OperatorTwo(bpy.types.Operator):
    bl_idname = "object.operator_two"
    bl_label = "Button 2"

    def execute(self, context):
        self.report({'INFO'}, "Button 2 clicked!")
        print("Button 2 was clicked!")
        return {'FINISHED'}

class OperatorThree(bpy.types.Operator):
    bl_idname = "object.operator_three"
    bl_label = "Button 3"

    def execute(self, context):
        self.report({'INFO'}, "Button 3 clicked!")
        print("Button 3 was clicked!")
        return {'FINISHED'}



class OperatorFour(bpy.types.Operator):
    bl_idname = "object.operator_four"
    bl_label = "Button 4"

    def execute(self, context):
        self.report({'INFO'}, "Button 4 clicked!")
        print("Button 4 was clicked!")
        return {'FINISHED'}


# 2. Create a Panel with multiple buttons
class IFC_PANEL(bpy.types.Panel):
    bl_label = "IFC_FILTERS_PANEL"
    bl_idname = "OBJECT_PT_IFC_FILTERS"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'  # You can set the tab name where the panel appears

    def draw(self, context):
        layout = self.layout
        # Add buttons for each operator
        layout.operator("object.operator_one")  # Button 1
        layout.operator("object.operator_two")  # Button 2
        layout.operator("object.operator_three")  # Button 3
        layout.operator("object.operator_four")  # Button 3

# 3. Register and unregister the classes
def register_ifc():
    bpy.utils.register_class(OperatorOne)
    bpy.utils.register_class(OperatorTwo)
    bpy.utils.register_class(OperatorThree)
    bpy.utils.register_class(OperatorFour)
    bpy.utils.register_class(IFC_PANEL)

def unregister_ifc():
    bpy.utils.unregister_class(OperatorOne)
    bpy.utils.unregister_class(OperatorTwo)
    bpy.utils.unregister_class(OperatorThree)
    bpy.utils.unregister_class(OperatorFour)
    bpy.utils.unregister_class(IFC_PANEL)

if __name__ == "__main__":
    register_ifc()
