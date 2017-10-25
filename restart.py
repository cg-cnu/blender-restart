bl_info = {
    "name": "Restart",
    "description": "Restart blender file",
    "author": "Sreenivas Alapati (cg-cnu)",
    "version": (1, 0),
    "blender": (2, 9, 0),
    "category": "3D View"}

import bpy
import subprocess
import atexit

def launch():
    # get the binary path of blender
    binary_path=  bpy.app.binary_path
    # get current blender file
    subprocess.Popen([binary_path, file_path])

def main(context):
    # check if the file is not saved
    # ask for confirmation

    launch_code = launch
    atexit.register(launch_code)
    # quit blender

class restart(bpy.types.Operator):
    bl_idname = "object.restart"
    bl_label = "Restart"

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(restart)
   
def unregister():
    bpy.utils.unregister_class(restart)

if __name__ == "__main__":
    register()