import os
import sys
import time
import cv2
import screenlapsehelper as helper

args = helper.validateargs(sys.argv)

out = None
counter = 0

if not args["-d"] == None:
	endtime = time.time() + args["-d"]
	infinite = False
else:
	endtime = 0
	infinite = True

print(infinite)
print(endtime)

if infinite:
	print("no duration specified, recording till stopped")
else:
	print("recording till: " + time.ctime(endtime))

print("press ctrl + c to stop recording")

try:
	while time.time() < endtime or infinite:
		os.system("screencapture -x -t jpg " + args["-l"] + "/" + str(counter) + ".jpg")

		img = cv2.imread(args["-l"] + "/" + str(counter) + ".jpg")
		if out == None:
			height, width, layers = img.shape
			size = (width,height)
			out = cv2.VideoWriter(args["-l"] + "/screenlapse" + args["-t"], cv2.VideoWriter_fourcc(*helper.videotypes[args["-t"]]), args["-fps"], size)
		out.write(img)

		os.remove(args["-l"] + "/" + str(counter) + ".jpg")

		counter = counter + 1
		time.sleep(args["-i"])
except KeyboardInterrupt:
	print("screenlapse: finished screenlapse with a total of " + str(counter + 1) + " frames.")
	print("saved to: " + str(args["-l"]) + "/screenlapse" + args["-t"])
	out.release()
