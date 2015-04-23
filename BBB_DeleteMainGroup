import maya.cmds as cmds


 
		
def push001():
	cmds.select("ABC_ANIM_CACHES_hrc")
	ABC_ANIM_CACHE = cmds.ls(selection = True)
	cmds.select("ABC_ANIM_CACHES_hrc")

	groupPolygon = []
	for x in cmds.listRelatives(ABC_ANIM_CACHE, allDescendents = True, fullPath = True):
		if not cmds.getAttr('%s.visibility' % x):
				groupPolygon.append(x)

	cmds.select(groupPolygon, replace = True)
	cmds.delete(groupPolygon)



def push002():
	cmds.deleteUI('comfirmy')

cmds.window( 'comfirmy', title='Selected Hidden OBJ', widthHeight=(220, 200), bgc = (1, 1, 1 ), sizeable = False, minimizeButton = False, maximizeButton = False, titleBarMenu= False )
cmds.rowLayout( numberOfColumns=2 )
cmds.iconTextButton( command = 'push001();', style='iconAndTextVertical', image1='T:/bubblebathbay_APPDIR/bbb_leonloong/2013.5-x64/prefs/icons/yes.jpg', label='Delete', w=100)
cmds.iconTextButton( command = 'push002()', style='iconAndTextVertical', image1='T:/bubblebathbay_APPDIR/bbb_leonloong/2013.5-x64/prefs/icons/no.jpg', label='No', w=100)
cmds.showWindow( 'comfirmy' )
