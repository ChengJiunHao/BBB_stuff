from maya import cmds

cmds.progressWindow(isInterruptable = 1)

while True:
	WindowCheck = cmds.window(title = 'SHUTDOWN YOUR PC??? MUAHAHAHAHHAHAHA', widthHeight = (400, 500))
	cmds.paneLayout()
	cmds.scrollField(wordWrap=True, text='SHUTDOWN YOUR PC??? MUAHAHAHAHHAHAHA')
	cmds.showWindow(WindowCheck)
	cmds.showSelectionInTitle(WindowCheck)
	cmds.deleteUI(WindowCheck)
	
	if cmds.progressWindow(query = 1, isCancelled = 1):
		cmds.progressWindow(endProgress = 1)
		break
		
	cmds.refresh()

    testing
