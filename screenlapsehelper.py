import os

helpstr = """usage: screenlapse [-l -i -d -t -fps -h]
-d<seconds>\t duration of capture, requiered to run.
-l<path>\t output file path, default is current directory
-i<seconds>\t frame capture interval, default is 1 second
-t<format>\t video output format, default is mp4 (other options are avi & mkv)
-fps\t\t frames per second in video, default is 15 fps
-h\t\t display help message
"""

videotypes = {".mp4": "mp4v", ".avi": "DIVX", ".mkv": "X264"}

def validateargs(args):
	counter = 0
	formargs = {}

	for arg in args:
		if arg.lower() == "-d":
			try:
				formargs["-d"] = int(args[counter + 1])
			except:
				print("error: time needs to be in full seconds")
				exit()

		elif arg.lower() == "-l":
			if args[counter +1][-1] == "/":
				args[counter + 1] = args[counter + 1][:-1]

			if not os.path.isdir(args[counter + 1]):
				if not os.path.isfile(args[counter + 1]):
					print("creating directory: " + args[counter + 1])
					os.system("mkdir " + args[counter + 1])
				else:
					print("screenlapse: " + args[counter + 1] + ": is not a directory")
					exit()

			formargs["-l"] = args[counter + 1]

		elif arg.lower() == "-i":
			try:
				formargs["-i"] = int(args[counter + 1])
			except:
				print("error: time interval needs to be in full seconds")
				exit()

		elif arg.lower() == "-t":
			if not "." + args[counter + 1].lower() in videotypes:
				print("error unknown filetype")
				exit()
			else:
				formargs["-t"] = "." + args[counter + 1].lower()

		elif arg.lower() == "-fps":
			try:
				formargs["-fps"] = int(args[counter + 1])
			except:
				print("error: fps needs to be a full number")
				exit()

		elif arg.lower() == "-h" or arg.lower() == "--help":
			print(helpstr)
			exit()

		counter = counter + 1

	if not "-d" in formargs:
		formargs["-d"] = None
	if not "-l" in formargs:
		formargs["-l"] = os.getcwd()
	if not "-i" in formargs:
		formargs["-i"] = 1
	if not "-t" in formargs:
		formargs["-t"] = ".mp4"
	if not "-fps" in formargs:
		formargs["-fps"] = 15

	return formargs