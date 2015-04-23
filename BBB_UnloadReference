import maya.cmds as cmds

refDict = {}
for x in cmds.ls(sl = True, long = True):
    if cmds.referenceQuery(x, isNodeReferenced = True):
        if cmds.referenceQuery(x, isLoaded = True):
            refPath = cmds.referenceQuery(x, filename = True)
            refDict.setdefault(refPath)
    
for each in refDict.iterkeys():
    cmds.file(each, unloadReference = True)
