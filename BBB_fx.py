__author__ = 'bbb_jiunhao'
## Main_Python_FX_001

import maya.cmds as cmds
import maya.mel as mel
import os
from pymel.all import *
import sys
sys.path.append('//192.168.5.253/BBB_main/bbb/t/bubblebathbay_APPDIR/bbb_jiunhao/2013.5-x64/scripts')
import FX_Shortcut_Tools
reload(FX_Shortcut_Tools)

## Toggle
def toggleDynamicsVisibility(mPanel = 'modelPanel4'):
	currState = cmds.modelEditor(mPanel, q = True, dynamics = True)
	cmds.modelEditor(mPanel, edit = True, dynamics = not currState)

def toggleNurbsCurvesVisibility(mPanel_01 = 'modelPanel4'):
	currState_01 = cmds.modelEditor(mPanel_01, q = True, nurbsCurves = True)
	cmds.modelEditor(mPanel_01, edit = True, nurbsCurves = not currState_01)

def toggleManipulatorsVisibility(mPanel_02 = 'modelPanel4'):
	currState_02 = cmds.modelEditor(mPanel_02, q = True, manipulators = True)
	cmds.modelEditor(mPanel_02, edit = True, manipulators = not currState_02)


def toggleUnusedmodelPanelVisibility(mPanel_03 = 'modelPanel4'):
	currState_03 = cmds.modelEditor(mPanel_03, q = True, locators = True)
	currState_04 = cmds.modelEditor(mPanel_03, q = True, nurbsSurfaces = True)
	currState_05 = cmds.modelEditor(mPanel_03, q = True, fluids = True)
	currState_06 = cmds.modelEditor(mPanel_03, q = True, dimensions = True)
	currState_07 = cmds.modelEditor(mPanel_03, q = True, deformers = True)
	cmds.modelEditor(mPanel_03, edit = True, locators = not currState_03)
	cmds.modelEditor(mPanel_03, edit = True, nurbsSurfaces = not currState_04)
	cmds.modelEditor(mPanel_03, edit = True, fluids = not currState_05)
	cmds.modelEditor(mPanel_03, edit = True, dimensions = not currState_06)
	cmds.modelEditor(mPanel_03, edit = True, deformers = not currState_07)



## Playblast
def defaultButtonPush(*args):
	sceneName = cmds.file(query=True,sceneName=True).split('"')[-1].split(".")[0]
	sceneName = '%s.mov' % sceneName.split('/')[-5]
	userDesktopPath = '%s/Desktop/BBB_Playblast' % os.environ['USERPROFILE']
	os.makedirs(userDesktopPath) if not os.path.exists(userDesktopPath) else None
	cmds.playblast(format = 'qt', filename = '%s/%s' % (userDesktopPath, sceneName), forceOverwrite = True, sequenceTime = 0, clearCache = 1, viewer = 1, showOrnaments = 1, offScreen = True, fp = 4, percent = 100, compression = "Animation", quality = 100, widthHeight = [1280, 720])

## Clean Cache B4 Publish

def defaultButtonPush01(*args):
	cmds.select('global_dynamicAnim')
	result = cmds.promptDialog(
		title='Clean',
		message=' -Global Dynamic Value',
		text='Insert Number',
		button=['OK', 'Cancel'],
		defaultButton='OK',
		cancelButton='Cancel',
		dismissString='Cancel')
	if result == 'OK':
		number = cmds.promptDialog(query=True, text=True)
		cmds.setAttr("global_dynamicAnim.foamStartFrame",int(number))
		cmds.setAttr("global_dynamicAnim.wakeStartFrame",int(number))
		cmds.setAttr("global_dynamicAnim.startFrame",int(number))
		cmds.playbackOptions (animationStartTime=number)
		cmds.playbackOptions (minTime=number)

		cmds.select('oceanWakeFoamTexture','oceanWakeTexture')
		mel.eval ('fluidDeleteCache')
		mel.eval ('ClearInitialState')
		currentTime (int(number))
		currentTime (1)
		currentTime (int(number))

def defaultButtonPush02(*args):
	cmds.file('I:/bubblebathbay/fx/kelana_ballsplash_v003.ma' ,i = True)

def defaultButtonPush03(*args):
	cmds.file('I:/bubblebathbay/fx/genericSplash.mb' ,i = True)

def SelectionError(*args):
	WindowCheck = cmds.window(title = 'ERROR', widthHeight = (400, 100))
	CHECK = cmds.ls( selection=True )
	if len(CHECK) == 0:
		#cmds.error( "###     Please Select CHAR_HULL_BASE     ###" )
		cmds.paneLayout()
		cmds.scrollField(wordWrap=True, text='       ###     Please Select CHAR_HULL_GEO     ###')
		cmds.showWindow(WindowCheck)
		cmds.showSelectionInTitle(WindowCheck)

def defaultButtonPush04(*args):
	charSelection = cmds.ls(sl=True)
	SelectionError()

	charName = charSelection[0]
	objectSplit = charName.split(':')
	FinalCharName = objectSplit[0]
	CharGeo_Duplicate01 = cmds.duplicate(charName)
	cmds.parent(world=True)
	mainGroup = cmds.group(n = "%s_wake_foam" % FinalCharName)

	groupPolygon = []
	for x in cmds.listRelatives(mainGroup, children = True, fullPath = True):
		for f in ['hull_geo', 'body_geo', 'geo','HubcapOld_geo']:
			if f in x:
				groupPolygon.append(x)

	cmds.select(groupPolygon, replace = True)
	EmitterObject = cmds.fluidEmitter(type='surface', der=1, her=2, fer=3, fdr=1.5, r=100.0, cye='none', cyi=1, mxd=0, mnd=0 )
	cmds.connectDynamic("oceanWakeTextureShape", em = EmitterObject[1])
	cmds.connectDynamic("oceanWakeFoamTextureShape", em = EmitterObject[1])
	cmds.setAttr('%s.maxDistance' % EmitterObject[1], 1)
	cmds.setAttr('%s.densityMethod' % EmitterObject[1], 2)
	cmds.setAttr('%s.fluidDensityEmission' % EmitterObject[1], 100)
	cmds.setAttr('%s.heatMethod' % EmitterObject[1], 2)
	cmds.setAttr('%s.fluidHeatEmission' % EmitterObject[1], 500)
	cmds.setAttr('%s.fluidFuelEmission' % EmitterObject[1], 1)
	cmds.setAttr('%s.fluidDropoff' % EmitterObject[1], 4.5)
	cmds.setAttr('%s.motionStreak' % EmitterObject[1], 1)
	cmds.setAttr('%s.fluidJitter' % EmitterObject[1], 0)
	cmds.setAttr('%s.turbulenceSpeed' % EmitterObject[1], 0)
	cmds.setAttr('%s.turbulenceFrequencyX' % EmitterObject[1], 0)
	cmds.setAttr('%s.turbulenceFrequencyY' % EmitterObject[1], 0)
	cmds.setAttr('%s.turbulenceFrequencyZ' % EmitterObject[1], 0)

	print "%s:cog_ctrl" % FinalCharName

	cmds.parentConstraint( "%s:cog_ctrl" % FinalCharName, mainGroup, maintainOffset = True )

def defaultButtonPush05(*args):
	cmds.progressWindow(isInterruptable = 1)

	while True:
		WindowCheck = cmds.window(title = '"Press Esc"', widthHeight = (800, 800))
		cmds.paneLayout()
		cmds.scrollField(wordWrap=True, text='"Press Esc"')
		cmds.showWindow(WindowCheck)
		cmds.showSelectionInTitle(WindowCheck)
		cmds.deleteUI(WindowCheck)

		if cmds.progressWindow(query = 1, isCancelled = 1):
			cmds.progressWindow(endProgress = 1)
			break

			cmds.refresh()


def LookThruCamera01(*args):
	for x in cmds.listRelatives('*CAM_hrc*', children = True, fullPath = True):

		cmds.lookThru(x)

		cmds.camera(x, e=True, displayResolution = True, displayGateMask = True, displayFilmGate = False, overscan=1.3 )




def LookThruCamera02(*args):
	for x in cmds.listRelatives('*BAKE_CAM_hrc*', children = True, fullPath = True):

		cmds.lookThru(x)

		cmds.camera(x, e=True, displayResolution = True, displayGateMask = True, displayFilmGate = False, overscan=1.3 )




def defaultButtonPush08(*args):
	cmds.progressWindow(isInterruptable = 1)

	while True:
		WindowCheck = cmds.window(title = '"Press Esc"', widthHeight = (400, 200))
		cmds.paneLayout()
		cmds.scrollField(wordWrap=True, text='"Press Esc"')
		cmds.showWindow(WindowCheck)
		cmds.showSelectionInTitle(WindowCheck)
		cmds.deleteUI(WindowCheck)

		if cmds.progressWindow(query = 1, isCancelled = 1):
			cmds.progressWindow(endProgress = 1)
			break

		cmds.refresh()



def defaultButtonPush09(*args):
	Maximum = cmds.promptDialog(
					title = "Maximum shots of Episode",
					message = "(Total shot of Episode) Insert_number:",
					button = ["OK", "Cancel"],
					defaultButton = "OK",
					cancelButton = "Cancel",
					dismissString = "Cancel")
	if Maximum == "OK":
		text001 = cmds.promptDialog(query = True, text = True)
		Num = 0
	EPI = cmds.promptDialog(
					title = "Episode",
					message = "ep + insert number:",
					button = ["OK", "Cancel"],
					defaultButton = "OK",
					cancelButton = "Cancel",
					dismissString = "Cancel")
	if EPI == "OK":
		Episode = cmds.promptDialog(query = True, text = True)

		for x in range(1, int(text001)+1):
			Num = Num+1
			AnimCachePath = "I:/bubblebathbay/episodes/%s/%s_sh%.3d/FX/publish/fx/" %(Episode,Episode,int(Num))
			if os.path.exists(AnimCachePath):
				if len(os.listdir(AnimCachePath)) != 0:
					VersionFolder = [i for i in os.listdir(AnimCachePath) if i.startswith("v") and not i.endswith("-copy")]
					LatestVersion = reduce(lambda a,b: a if int(a.strip("v")) > int(b.strip("v")) else b ,VersionFolder)
					if len(os.listdir(AnimCachePath+LatestVersion))== 0:
						print(Episode+"sh%.3d" %int(Num))
				else:
					print(Episode+"sh%.3d Empty or not Required" %int(Num))
			else:
				print(Episode+"sh%.3d Empty or not Required" %int(Num))







## Window On/Off
if cmds.window('JiunHaoFX_window',exists=True):
	cmds.deleteUI('JiunHaoFX_window')

Fx_Tools = cmds.window('JiunHaoFX_window', title = 'Fx_Shortcut_Tools', rtf = True, s = False, width = 250)
mainColumnLayout = cmds.columnLayout(rowSpacing = 1.5, columnWidth = 250, parent = Fx_Tools, adjustableColumn=True )
mainFrameLayout = cmds.frameLayout(label = 'FX', borderStyle = 'in', collapsable = True, collapse = False, parent = mainColumnLayout, width = 250)
mainLyt = cmds.columnLayout(rowSpacing = 1.5, columnWidth = 250, parent = mainFrameLayout, adjustableColumn = True)
cmds.separator(width = 180, height = 1, style = "out", parent = mainLyt)

cmds.button( label='Playblast', command = 'FX_Shortcut_Tools.defaultButtonPush()', backgroundColor = [0,.7,0])
cmds.button( label='Toggle Dynamic Visibility', command = 'FX_Shortcut_Tools.toggleDynamicsVisibility()', backgroundColor = [.5,.5,.5])
cmds.button( label='Toggle NurbsCurves Visibility', command = 'FX_Shortcut_Tools.toggleNurbsCurvesVisibility()', backgroundColor = [0.5,.5,.5])
cmds.button( label='Toggle Manipulators Visibility', command = 'FX_Shortcut_Tools.toggleManipulatorsVisibility()', backgroundColor = [0.5,.5,.5])
cmds.button( label='Toggle Unused modelPanel Visibility', command = 'FX_Shortcut_Tools.toggleUnusedmodelPanelVisibility()', backgroundColor = [0.5,.5,.5])
cmds.button( label='Splash Setup *kalana_ballsplash_v003*', command = 'FX_Shortcut_Tools.defaultButtonPush02()', backgroundColor = [.8,.8,.8])
cmds.button( label='Splash Setup *genericSplash_cleaned*', command = 'FX_Shortcut_Tools.defaultButtonPush03()', backgroundColor = [.2,.2,.2])
cmds.button( label='CLEAN', command = 'FX_Shortcut_Tools.defaultButtonPush01()', backgroundColor = [.75,.0,.0])
cmds.separator(width = 180, height = 3, style = "out", parent = mainLyt)
# cmds.text(label = "ExtraEmitter", align = "center", parent = mainLyt, backgroundColor = [0, 0, 0])
cmds.button( label='Check-FXCache(Server)', command = 'FX_Shortcut_Tools.defaultButtonPush09()', backgroundColor = [0,.0,.0])
cmds.separator(width = 180,height = 3, style = "out", parent = mainLyt)
# cmds.button( label='BAKE_CAM_VIEW', command = 'FX_Shortcut_Tools.defaultButtonPush06()', backgroundColor = [.1,.1,.1])
# cmds.button( label='BAKE_CAM_VIEW_for_light', command = 'FX_Shortcut_Tools.defaultButtonPush07()', backgroundColor = [.1,.1,.1])
CAMCAM = cmds.rowLayout(numberOfColumns = 3, columnWidth3 = (80, 50, 50), columnAlign = (1, "center"), parent = mainLyt)
cmds.button(label = "CAM_VIEW_FX", command = "FX_Shortcut_Tools.LookThruCamera01()", align = "center", width = 122, height = 20, parent = CAMCAM, backgroundColor = [0.5, 0.5, 0.5])
cmds.button(label = "CAM_VIEW_LIGHT", command = "FX_Shortcut_Tools.LookThruCamera02()", align = "center", width = 122, height = 20, parent = CAMCAM, backgroundColor = [0.5, 0.5, 0.5])
cmds.separator(width = 180,height = 3, style = "out", parent = mainLyt)

# cmds.separator(width = 180, height = 1, style = "out", parent = mainLyt)
# cmds.text(label = "ExtraEmitter", align = "center", parent = mainLyt, backgroundColor = [0, 0, 0])
# cmds.separator(width = 180,height = 1, style = "out", parent = mainLyt)

# renderStatsRowColumnLayout = cmds.rowColumnLayout(numberOfColumns = 3, width = 250, parent = mainLyt)

# cmds.button(label = " CHAR_HULL_EMIT ", align = "center", command = "FX_Shortcut_Tools.defaultButtonPush04()", backgroundColor = [1, 1, 0.5], width = 245)




##cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.showWindow()

frameLayout = cmds.frameLayout(label = 'ExtraEmitter', borderStyle = 'in', collapsable = True, collapse = True, parent = mainColumnLayout, width = 250)
frameChildColumnLayout = cmds.columnLayout(parent = frameLayout)

cmds.button(label = " CHAR_HULL_EMIT ", align = "center", command = "FX_Shortcut_Tools.defaultButtonPush04()", backgroundColor = [1, 1, 0.5], width = 245)
cmds.button(label = " TESTING ", align = "center", command = "FX_Shortcut_Tools.defaultButtonPush08()", backgroundColor = [.75, 0, 0], width = 245)
#cmds.button(label = " #NO . Don't Click ", align = "center", command = "FX_Shortcut_Tools.defaultButtonPush05()", backgroundColor = [0, 0, 0], width = 245)
# cmds.checkBox('bubbleBathBayStaticCB', label = '', width = 15, value = True)
# cmds.button(label = "Clean-up Statics!", width = 245, align = "center", command = "bbbLightTools.cleanupStatics()", backgroundColor = [1, 0.5, 0.5])
# cmds.button(label = "Import Static(s)", width = 245, align = "center", command = "bbbLightTools.importStaticEnv()", backgroundColor = [0.33, 1, 0.33])
cmds.showWindow()