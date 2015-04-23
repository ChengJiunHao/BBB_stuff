import os

import maya.cmds as cmds


Maximum = cmds.promptDialog(
				title = "Maximum shots of Episode",
				message = "(Total shot of Episode) Inser_number:",
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
				print(Episode+"sh%.3d" %int(Num))
		else:
			print(Episode+"sh%.3d is not Required" %int(Num))
