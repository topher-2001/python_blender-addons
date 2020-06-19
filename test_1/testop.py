import bpy
import pyautogui

class Test_OT_Operator(bpy.types.Operator):
     bl_idname = "view3d.cursor_center"
     bl_label = "Simple Operator"
     bl_description = "Center 3d cursor"

     def execute(self, centext):
          bpy.ops.view3d.snap_cursor_to_center()
          
          # Take screenshot.
          pic = pyautogui. screenshot()
          # Save the image.
          pic. save('Screenshot. png')
          return{'FINISHED'}