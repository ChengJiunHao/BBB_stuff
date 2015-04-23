from maya import cmds


## More readable ##
geometry = cmds.ls(geometry=True)

transforms = cmds.listRelatives(geometry, p=True, path=True)

cmds.select(transforms, r=True)

## Work in 1 line  ##

cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)



import maya.cmds as cmds

refDict = {}
for x in cmds.ls(sl = True, long = True):
    if cmds.referenceQuery(x, isNodeReferenced = True):
        if cmds.referenceQuery(x, isLoaded = True):
            refPath = cmds.referenceQuery(x, filename = True)
            refDict.setdefault(refPath)
    
for each in refDict.iterkeys():
    cmds.file(each, unloadReference = True)
