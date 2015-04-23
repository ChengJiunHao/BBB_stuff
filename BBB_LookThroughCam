import maya.cmds as cmds


	CamGroup = []
	for x in cmds.listRelatives('*BAKE_CAM_hrc*', children = True, fullPath = True):
		for y in x:
			CamGroup.append(x)

			cmds.select( CamGroup, replace = True )

			CamSelection = cmds.ls( selection = True)

			cmds.lookThru( CamSelection)

			cmds.camera( CamSelection, e=True, displayResolution = True, displayGateMask = True, displayFilmGate = False, overscan=1.3 )
