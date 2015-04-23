__author__ = 'bbb_jiunhao'
import maya.cmds as cmds

# ep112sh036

ZIP_GEO_001 = ("CHAR_Zip_hrc")
cmds.createRenderLayer(ZIP_GEO_001, name = "Taxi_letter_geo_LYR", noRecurse = True)
cmds.editRenderLayerGlobals(currentRenderLayer = "Taxi_letter_geo_LYR")

##For selection mesh##
#selection = cmds.ls(selection = True)
#meshDescendents = [cmds.listRelatives(mesh, parent = True, fullPath = True)[0] for mesh in cmds.listRelatives(allDescendents = True, fullPath = True, type = 'mesh')]
##Selected_Objects##

core_mat_001 = cmds.createNode('core_surface_shader')
core_mat_sg_001 = cmds.sets(renderable = True, noSurfaceShader = True, empty = True)
cmds.connectAttr('%s.outValue' % core_mat_001, '%s.miMaterialShader' % core_mat_sg_001)
cmds.connectAttr('%s.outValue' % core_mat_001, '%s.miShadowShader' % core_mat_sg_001)
cmds.setAttr('%s.colour' % core_mat_001, 0, 0, 0, type = 'double3')
cmds.setAttr('%s.output_override' % core_mat_001, 1)
cmds.sets(ZIP_GEO_001, edit = True, forceElement = core_mat_sg_001)


ZIP_Taxi_GEO_001 = ("r_taxi_letter_geo", "l_taxi_letter_geo")
core_mat_002 = cmds.createNode('core_surface_shader')
core_mat_sg_002 = cmds.sets(renderable = True, noSurfaceShader = True, empty = True)
cmds.connectAttr('%s.outValue' % core_mat_002, '%s.miMaterialShader' % core_mat_sg_002)
cmds.connectAttr('%s.outValue' % core_mat_002, '%s.miShadowShader' % core_mat_sg_002)
cmds.setAttr('%s.colour' % core_mat_002, 1, 1, 1, type = 'double3')
cmds.sets(ZIP_Taxi_GEO_001, edit = True, forceElement = core_mat_sg_002)



ZIP_GEO_002 = ("CHAR_Zip_hrc")
cmds.createRenderLayer(ZIP_GEO_002, name = "Taxi_sign_base_geo_LYR", noRecurse = True)
cmds.editRenderLayerGlobals(currentRenderLayer = "Taxi_sign_base_geo_LYR")


core_mat_003 = cmds.createNode('core_surface_shader')
core_mat_sg_003 = cmds.sets(renderable = True, noSurfaceShader = True, empty = True)
cmds.connectAttr('%s.outValue' % core_mat_003, '%s.miMaterialShader' % core_mat_sg_003)
cmds.connectAttr('%s.outValue' % core_mat_003, '%s.miShadowShader' % core_mat_sg_003)
cmds.setAttr('%s.colour' % core_mat_003, 0, 0, 0, type = 'double3')
cmds.setAttr('%s.output_override' % core_mat_003, 1)
cmds.sets(ZIP_GEO_002, edit = True, forceElement = core_mat_sg_003)


ZIP_Taxi_GEO_002 = ("taxi_sign_base_geo","r_taxi_letter_geo", "l_taxi_letter_geo")
#cmds.createRenderLayer(ZIP_Taxi_GEO, name = 'TAXI_LIGHT_SMALL', noRecurse = True)
#cmds.editRenderLayerGlobals(currentRenderLayer = 'TAXI_LIGHT_SMALL')
core_mat_004 = cmds.createNode('core_surface_shader')
core_mat_sg_004 = cmds.sets(renderable = True, noSurfaceShader = True, empty = True)
cmds.connectAttr('%s.outValue' % core_mat_004, '%s.miMaterialShader' % core_mat_sg_004)
cmds.connectAttr('%s.outValue' % core_mat_004, '%s.miShadowShader' % core_mat_sg_004)
cmds.setAttr('%s.colour' % core_mat_004, 1, 1, 1, type = 'double3')
cmds.sets(ZIP_Taxi_GEO_002, edit = True, forceElement = core_mat_sg_004)