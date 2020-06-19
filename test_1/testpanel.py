import bpy

class Test_PT_Panel(bpy.types.Panel):
     bl_idname = "test_pt_panel"
     bl_label = "Test panel"
     bl_catagory = "Test Addon"
     bl_space_type = "VIEW_3D"
     bl_region_type = "UI"

     def draw(self, context):
          layout = self.layout

          row = layout.row()
          row.operator('view3d.cursor_center', text="Center 3D Cursor")