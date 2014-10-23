from SimpleCV import Camera, Image
import copy

cam = Camera()

last = []

while True:
	last.append( cam.getImage() )
	last = last[-20:]
	img = last[0].copy()
	for i in xrange(1,len(last)):
		img = img + (last[i] / len(last))
	
	img = last[-1] - img
	img.show()