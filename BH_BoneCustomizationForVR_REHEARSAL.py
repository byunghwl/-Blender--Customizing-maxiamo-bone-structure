bl_info = {
"name":         "BH_boneRoll_editor",
"author":       "Byunghwan Lee",
"blender":      (2,7,5),
"version":      (0,0,1),
"location":     "View3D > Object > BH",
"description":  "Customize to change boneRoll from maxiam-auto-rig to ni-mate mocap",
"category":     "Rigging"
}


import bpy  
import math
    
def rad2deg(radians):
        	pi = math.pi
        	degrees = 180 * radians / pi
        	return degrees

def deg2rad(degrees):
	pi = math.pi
	radians = pi * degrees / 180
	return radians  
  
class BH_boneRoll_editor(bpy.types.Operator):  
    """Customize boneRoll change"""  
    #bl_idname = "object.move2_operator"
    bl_idname = "object.customized_bone_roll"  
    bl_label = "Customize boneRoll"  
  
    def execute(self, context):  
         # the name list of bones which roll should be 180 degree
        boneNameList_roll_180 = ['mixamorig:Head', 
                                'mixamorig:Neck',
                                'mixamorig:Spine2',
                                'mixamorig:Spine1',
                                'mixamorig:Spine'  ]
                                
        # the name list of bones which roll should be 0 degree
        boneNameList_roll_0 =['mixamorig:LeftShoulder',
                             'mixamorig:LeftArm',
                             'mixamorig:LeftForeArm',
                             'mixamorig:LeftHand',
                             'mixamorig:LeftHandThumb1',
                             'mixamorig:LeftHandThumb2',
                             'mixamorig:LeftHandThumb3',
                             'mixamorig:LeftHandThumb4',
                             'mixamorig:LeftHandIndex1',
                             'mixamorig:LeftHandIndex2',
                             'mixamorig:LeftHandIndex3',
                             'mixamorig:LeftHandIndex4',
                             
                             'mixamorig:RightShoulder',
                             'mixamorig:RightArm',
                             'mixamorig:RightForeArm',
                             'mixamorig:RightHand',
                             'mixamorig:RightHandThumb1',
                             'mixamorig:RightHandThumb2',
                             'mixamorig:RightHandThumb3',
                             'mixamorig:RightHandThumb4',
                             'mixamorig:RightHandIndex1',
                             'mixamorig:RightHandIndex2',
                             'mixamorig:RightHandIndex3',
                             'mixamorig:RightHandIndex4',
                             ]

        print('\n------------------------------------------------------------\n')

        # 0. Get Scene Context
        scene = bpy.context.scene
        scene.layers = [True] * 20 # Show all layers

        # 1. Find Armature
        for obj in scene.objects:
            if obj.name == "Armature" and obj.type == "ARMATURE":
                bpy.context.scene.objects.active = obj
                
        # 2. Access to Editmode        
        bpy.ops.object.mode_set(mode = 'EDIT')    
        edit_bones = bpy.context.object.data.edit_bones

        # 3. Find bones in the list and change the roll of the bone
        for bone in edit_bones:
            for boneList in boneNameList_roll_180:
                 if bone.name == boneList:
                    bone.roll = deg2rad(180)  

            for boneList in boneNameList_roll_0:
                 if bone.name == boneList:
                    bone.roll = deg2rad(0)    
                          
        bpy.ops.object.mode_set(mode = 'OBJECT')       
        return {'FINISHED'}  
    
  
def add_object_button(self, context):  
    self.layout.operator(  
        BH_boneRoll_editor.bl_idname,  
        text=BH_boneRoll_editor.__doc__,  
        icon='PLUGIN')  
  
def register():  
    bpy.utils.register_class(BH_boneRoll_editor)  
    bpy.types.VIEW3D_MT_object.append(add_object_button)  
    
def unregister():
    bpy.utils.register_class(BH_boneRoll_editor)      
    
if __name__ == "__main__":  
    register()  