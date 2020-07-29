#!/bin/env python
#-*- coding: utf-8 -*-

import os,sys
from PIL import Image

IOS_APP_ICON_OUT_PUT = [
	["20@2x", 40],
	["20@2x-ipad", 40],
	["20@3x", 60],
	["20-ipad", 20],
	["29", 29],
	["29@2x", 58],
	["29@2x-ipad", 58],
	["29@3x-ipad", 87],
	["29-ipad", 29],
	["40", 40],
	["40@2x", 80],
	["40@3x", 120],
	["60@2x", 120],
	["60@3x", 180],
	["76", 76],
	["76@2x", 152],
	["83.5@2x", 167],
	["1024", 1024],
]
def output_ios_AppIcon():
	filePath = "./src/app_icon.png"
	im = Image.open(filePath)

	outPutDir = "./output/IOS_AppIcon"
	if not os.path.exists(outPutDir):
		os.makedirs(outPutDir)

	for c in IOS_APP_ICON_OUT_PUT:
		out = im.resize((c[1], c[1]), Image.ANTIALIAS)
		outPath = outPutDir + "/icon-" + c[0] + "." + im.format.lower()
		out.save(outPath, im.format)

	im.close()


IOS_APP_BG_OUT_PUT = [
	["LaunchImage", ],
]
def output_ios_AppBg():
	filePath = "./src/bg.png"
	im = Image.open(filePath)
	print("do nothing")

	# outPutDir = "./output/IOS_AppBg"
	# if not os.path.exists(outPutDir):
	# 	os.makedirs(outPutDir)

	# for c in IOS_APP_ICON_OUT_PUT:
	# 	out = im.resize((c[1], c[1]), Image.ANTIALIAS)
	# 	outPath = outPutDir + "/icon-" + c[0] + "." + im.format.lower()
	# 	out.save(outPath, im.format)

#宣传图
IOS_APP_IMAGE_OUT = [
	["65", 1242, 2688],
	["55", 1242, 2208],
	["129", 2048, 2732],
]
def output_ios_XCIcon():
	dirPath = "./src/xc"
	file_lists = os.listdir(dirPath)
	for fileName in file_lists:
		filePath = dirPath + "/" + fileName
		if not os.path.isdir(filePath):
			im = Image.open(filePath)

			for c in IOS_APP_IMAGE_OUT:
				out = im.resize((c[1], c[2]), Image.ANTIALIAS)

				outPutDir = "./output/IOS_AppXC/" + c[0]
				if not os.path.exists(outPutDir):
					os.makedirs(outPutDir)

				# fileName = os.path.basename(filePath)
				outPath = outPutDir + "/" + fileName + "." + im.format.lower()
				out.save(outPath, im.format)

			im.close()


#宣传图
ANDROID_APP_ICON = [
	["ldpi", 240, 320],
	["mdpi", 320, 480],
	["hdpi", 480, 800],
	["xhdpi", 720, 1280],
	["xxhdpi", 1090, 1920],
	["xxxhdpi", 3840, 2160],
]
def output_andriod_AppIcon():
	filePath = "./src/app_icon.png"
	fileName = os.path.basename(filePath)
	im = Image.open(filePath)

	for c in ANDROID_APP_ICON:
		outPutDir = "./output/ANDROID_AppIcon/mipmap-" + c[0]
		if not os.path.exists(outPutDir):
			os.makedirs(outPutDir)

		out = im.resize((c[1], c[2]), Image.ANTIALIAS)
		outPath = outPutDir + "/" + fileName + "." + im.format.lower()
		out.save(outPath, im.format)

	im.close()

def output_andriod_BgIcon():
	filePath = "./src/bg.png"
	im = Image.open(filePath)

	for c in ANDROID_APP_ICON:
		outPutDir = "./output/ANDROID_AppIcon/mipmap-" + c[0]
		if not os.path.exists(outPutDir):
			os.makedirs(outPutDir)

		out = im.resize((c[1], c[2]), Image.ANTIALIAS)
		fileName = os.path.basename(filePath)
		outPath = outPutDir + "/" + fileName + "." + im.format.lower()
		out.save(outPath, im.format)

	im.close()

#命令列表
COMMANDS = {
	"ios":{
		"app_icon":output_ios_AppIcon,
		"app_bg":output_ios_AppBg,
		"app_xc":output_ios_XCIcon,
	},

	"android":{
		"app_icon":output_andriod_AppIcon,
		"app_bg":output_andriod_BgIcon,
	}
}

def showHelpMsg():
	print("-help")

def main():
	if len(sys.argv) < 3:
		showHelpMsg()
		return

	f = COMMANDS[sys.argv[1]][sys.argv[2]]
	if f:
		f()
	else:
		showHelpMsg()

if __name__ == '__main__':
	main()
