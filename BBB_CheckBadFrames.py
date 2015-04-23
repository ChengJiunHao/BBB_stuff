import sys, os

max = 342
path = 'K:/bubblebathbay/episodes/ep135/ep135_sh035/RenderLayers/R001/masterLayer'

max = range(1, max + 1)
shot_image = {}
[ shot_image.setdefault( i.split('.')[0], [] ) for i in os.listdir(path) if i.endswith('.exr') ]
[ shot_image[i.split('.')[0]].append( int(i.split('.')[-2]) ) for i in os.listdir(path) if i.endswith('.exr') ]

missing_frames = []
for val in shot_image.itervalues():
	for i in max:
		if i not in val:
			missing_frames.append(i)
			
if missing_frames:
	missing_frames = [str(i) for i in missing_frames]
	print ', '.join(missing_frames)
else:
	print 'Eveything good!'
