##CHAR_Hull_Emmiter##TestEp130sh156##

#####################################

###############start#################

#####################################
import maya.cmds as cmds

charSelection = cmds.ls(sl=True)
def SelectionError():
    CHECK = cmds.ls( selection=True )
    if len(CHECK) == 0:
        cmds.error( "###     Please Select CHAR_BASE_HULL     ###" )
SelectionError()

charName = charSelection[0]
objectSplit = charName.split(':')
FinalCharName = objectSplit[0]
CharGeo_Duplicate01 = cmds.duplicate(charName)
cmds.parent(world=True)
mainGroup = cmds.group(n = "%s_wake_foam" % FinalCharName)

groupPolygon = []
for x in cmds.listRelatives(mainGroup, children = True, fullPath = True):
    for f in ['hull_geo', 'body_geo', 'geo']:
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
cmds.setAttr('%s.fluidHeatEmission' % EmitterObject[1], 1000)
cmds.setAttr('%s.fluidFuelEmission' % EmitterObject[1], 1)
cmds.setAttr('%s.fluidDropoff' % EmitterObject[1], 4.5)
cmds.setAttr('%s.motionStreak' % EmitterObject[1], 1)
cmds.setAttr('%s.fluidJitter' % EmitterObject[1], 0)
cmds.setAttr('%s.turbulenceSpeed' % EmitterObject[1], 0)
cmds.setAttr('%s.turbulenceFrequencyX' % EmitterObject[1], 0)
cmds.setAttr('%s.turbulenceFrequencyY' % EmitterObject[1], 0)
cmds.setAttr('%s.turbulenceFrequencyZ' % EmitterObject[1], 0)
cmds.parentConstraint( "%s:cog_ctrl" % FinalCharName, mainGroup, maintainOffset = True )


##FIN##
