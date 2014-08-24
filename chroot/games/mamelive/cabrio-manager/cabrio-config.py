# -*- coding: utf-8 -*-
try:
	import Tkinter as tk
	import ttk
except ImportError:
	import tkinter as tk
	import tkinter.ttk as ttk
import tkFileDialog
import locale
import Queue
import threading
import subprocess
import xml.etree.ElementTree as ET
import sys
import os
from os.path import expanduser
loc = locale.getdefaultlocale()
class App(tk.Tk):
	"""docstring for App"""
	def __init__(self):
		tk.Tk.__init__(self)
		# For test purpose only:
		# self.SDLout = "up: joystick0 axis SDL_KEYCODE = -1 \ndown: joystick0 axis SDL_KEYCODE = 1 \nleft: joystick0 axis SDL_KEYCODE = -1 \nright: joystick0 axis SDL_KEYCODE = 1 \nselect: joystick0 button SDL_KEYCODE = 0 \nback: joystick0 button SDL_KEYCODE = 2\nquit: joystick0 button SDL_KEYCODE = 1"
		# self.SDLout = "up: joystick0 axis SDL_KEYCODE = -1 typeaxis = 1 \ndown: joystick0 axis SDL_KEYCODE = 1 typeaxis = 1 \nleft: joystick0 axis SDL_KEYCODE = -1 typeaxis = 0 \nright: joystick0 axis SDL_KEYCODE = 1 typeaxis = 0 \nselect: joystick0 button SDL_KEYCODE = 1 typeaxis = 0 \nback: joystick0 button SDL_KEYCODE = 3 typeaxis = 0 \nquit: joystick0 button SDL_KEYCODE = 2 typeaxis = 0"
		self.SDLkeys = [
			"backspace",
			"tab",
			"return",
			"escape",
			"space",
			"exclaim",
			"quotedbl",
			"hash",
			"dollar",
			"percent",
			"ampersand",
			"quote",
			"leftparen",
			"rightparen",
			"asterisk",
			"plus",
			"comma",
			"minus",
			"period",
			"slash",
			"0",
			"1",
			"2",
			"3",
			"4",
			"5",
			"6",
			"7",
			"8",
			"9",
			"colon",
			"semicolon",
			"less",
			"equals",
			"greater",
			"question",
			"at",
			"leftbracket",
			"backslash",
			"rightbracket",
			"caret",
			"underscore",
			"backquote",
			"a",
			"b",
			"c",
			"d",
			"e",
			"f",
			"g",
			"h",
			"i",
			"j",
			"k",
			"l",
			"m",
			"n",
			"o",
			"p",
			"q",
			"r",
			"s",
			"t",
			"u",
			"v",
			"w",
			"x",
			"y",
			"z",
			"delete",
			"capslock",
			"F1",
			"F2",
			"F3",
			"F4",
			"F5",
			"F6",
			"F7",
			"F8",
			"F9",
			"F10",
			"F11",
			"F12",
			"printscreen",
			"scrolllock",
			"pause",
			"insert",
			"home",
			"pageup",
			"end",
			"pagedown",
			"right",
			"left",
			"down",
			"up",
			"NUMLOCKCLEAR",
			"KP_DIVIDE",
			"KP_MULTIPLY",
			"KP_MINUS",
			"KP_PLUS",
			"KP_ENTER",
			"KP_1",
			"KP_2",
			"KP_3",
			"KP_4",
			"KP_5",
			"KP_6",
			"KP_7",
			"KP_8",
			"KP_9",
			"KP_0",
			"KP_PERIOD",
			"APPLICATION",
			"POWER",
			"KP_EQUALS",
			"F13",
			"F14",
			"F15",
			"F16",
			"F17",
			"F18",
			"F19",
			"F20",
			"F21",
			"F22",
			"F23",
			"F24",
			"EXECUTE",
			"HELP",
			"MENU",
			"SELECT",
			"STOP",
			"AGAIN",
			"UNDO",
			"CUT",
			"COPY",
			"PASTE",
			"FIND",
			"MUTE",
			"VOLUMEUP",
			"VOLUMEDOWN",
			"KP_COMMA",
			"KP_EQUALSAS400",
			"ALTERASE",
			"SYSREQ",
			"CANCEL",
			"CLEAR",
			"PRIOR",
			"RETURN2",
			"SEPARATOR",
			"OUT",
			"OPER",
			"CLEARAGAIN",
			"CRSEL",
			"EXSEL",
			"KP_00",
			"KP_000",
			"thousandsseparator",
			"decimalseparator",
			"currencyunit",
			"currencysubunit",
			"KP_LEFTPAREN",
			"KP_RIGHTPAREN",
			"KP_LEFTBRACE",
			"KP_RIGHTBRACE",
			"KP_TAB",
			"KP_BACKSPACE",
			"KP_A",
			"KP_B",
			"KP_C",
			"KP_D",
			"KP_E",
			"KP_F",
			"KP_XOR",
			"KP_POWER",
			"KP_PERCENT",
			"KP_LESS",
			"KP_GREATER",
			"KP_AMPERSAND",
			"KP_DBLAMPERSAND",
			"KP_VERTICALBAR",
			"KP_DBLVERTICALBAR",
			"KP_COLON",
			"KP_HASH",
			"KP_SPACE",
			"KP_AT",
			"KP_EXCLAM",
			"KP_MEMSTORE",
			"KP_MEMRECALL",
			"KP_MEMCLEAR",
			"KP_MEMADD",
			"KP_MEMSUBTRACT",
			"KP_MEMMULTIPLY",
			"KP_MEMDIVIDE",
			"KP_PLUSMINUS",
			"KP_CLEAR",
			"KP_CLEARENTRY",
			"KP_BINARY",
			"KP_OCTAL",
			"KP_DECIMAL",
			"KP_HEXADECIMAL",
			"LCTRL",
			"LSHIFT",
			"LALT",
			"LGUI",
			"RCTRL",
			"RSHIFT",
			"RALT",
			"RGUI",
			"MODE",
			"AUDIONEXT",
			"AUDIOPREV",
			"AUDIOSTOP",
			"AUDIOPLAY",
			"AUDIOMUTE",
			"MEDIASELECT",
			"WWW",
			"MAIL",
			"CALCULATOR",
			"COMPUTER",
			"AC_SEARCH",
			"AC_HOME",
			"AC_BACK",
			"AC_FORWARD",
			"AC_STOP",
			"AC_REFRESH",
			"AC_BOOKMARKS",
			"BRIGHTNESSDOWN",
			"BRIGHTNESSUP",
			"DISPLAYSWITCH",
			"KBDILLUMTOGGLE",
			"KBDILLUMDOWN",
			"KBDILLUMUP",
			"EJECT",
			"SLEEP"]
		self.SDLcardinals = ["up", "down", "left", "right"]
		self.SDLpolarity = ["minus", "plus"]
		self.SDLbuttons = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
		self.joyTypes = ["axis", "ball", "button", "hat"]
		self.kbTypes = ["Default"]
		self.mouseTypes = ["axis", "button"]
		self.style = ttk.Style()
		self.style.theme_use("clam")
		try:
			self.tree = ET.parse("cabrio-config.xml")
		except:
			sys.exit("Error: cabrio-config.xml not found, it should be in the same folder that this script.")
		self.root = self.tree.getroot()
		self.lang = loc[0]
		if self.lang == None:
			self.lang = "en_GB"
		if self.root.findall(".//*[@code='"+self.lang+"']") == []:
			self.lang = "en_GB"
		for lang in self.root.findall(".//*[@code='"+self.lang+"']"):
			self.browseButtonStr = lang.find("browseButton").text
			self.titleStr = lang.find("title").text
			self.setButtonStr =lang.find("setButton").text
			self.displayTabStr = lang.find("displayTab").text
			self.pathTabStr = lang.find("pathTab").text
			self.controlsTabStr = lang.find("controlsTab").text
			self.emulatorsTabStr = lang.find("emulatorsTab").text
			self.aboutTabStr = lang.find("aboutTab").text
			self.interfaceLabelFrameStr = lang.find("interfaceLabelFrame").text
			self.fullscreenStr = lang.find("fullscreen").text
			self.framerateStr = lang.find("framerate").text
			self.videoLoopStr = lang.find("videoLoop").text
			self.themeStr = lang.find("theme").text
			self.screenLabelFrameStr = lang.find("screenLabelFrame").text
			self.widthStr = lang.find("width").text
			self.heightStr = lang.find("height").text
			self.rotationStr = lang.find("rotation").text
			self.flipHorizontalStr = lang.find("flipHorizontal").text
			self.flipVerticalStr = lang.find("flipVertical").text
			self.graphicsLabelFrameStr = lang.find("graphicsLabelFrame").text
			self.qualityLabelStr = lang.find("qualityLabel").text
			self.qualityLowStr = lang.find("qualityLow").text
			self.qualityMediumStr = lang.find("qualityMedium").text
			self.qualityHighStr = lang.find("qualityHigh").text
			self.maxImageWidthLabelStr = lang.find("maxImageWidth").text
			self.maxImageHeightLabelStr = lang.find("maxImageHeight").text
			self.newEmulatorLabelStr = lang.find("newEmulatorLabel").text
			self.addButtonStr = lang.find("addButton").text
			self.editEmulatorLabelStr = lang.find("editEmulatorLabel").text
			self.aboutLabelStr = lang.find("aboutLabel").text
			self.versionLabelStr = lang.find("versionLabel").text
			self.translationLabelStr = lang.find("translationLabel").text
			self.authorLabelStr = lang.find("authorLabel").text
			self.themesPathLabelStr = lang.find("themesPathLabel").text
			self.backgroundPathLabelStr = lang.find("backgroundPathLabel").text
			self.logoPathLabelStr = lang.find("logoPathLabel").text
			self.videoPathLabelStr = lang.find("videoPathLabel").text
			self.screenshotPathLabelStr = lang.find("screenshotPathLabel").text
			self.upLabelStr = lang.find("upLabel").text
			self.downLabelStr = lang.find("downLabel").text
			self.leftLabelStr = lang.find("leftLabel").text
			self.rightLabelStr = lang.find("rightLabel").text
			self.selectLabelStr = lang.find("selectLabel").text
			self.backLabelStr = lang.find("backLabel").text
			self.quitLabelStr = lang.find("quitLabel").text
			self.list1LabelStr = lang.find("list1Label").text
			self.list2LabelStr = lang.find("list2Label").text
			self.list3LabelStr = lang.find("list3Label").text
			self.list4LabelStr = lang.find("list4Label").text
			self.list5LabelStr = lang.find("list5Label").text
			self.keyboardStr = lang.find("keyboard").text
			self.mouseStr = lang.find("mouse").text
			self.joystickStr = lang.find("joystick").text
			self.deviceStr = lang.find("device").text
			self.idStr = lang.find("id").text
			self.typeStr = lang.find("type").text
			self.valueStr = lang.find("value").text
			self.setAllKeysStr = lang.find("setAllKeys").text
			self.audioLabelFrameStr = lang.find("audio").text
			self.themeSoundsStr = lang.find("themeSounds").text
			self.videoSoundStr = lang.find("videoSound").text
			self.musicVolumeStr = lang.find("musicVolume").text
			self.hideButtonsStr = lang.find("hideButtons").text
			self.themeTabStr = lang.find("themeTab").text
		self.path = expanduser("~") + "/.cabrio/"
		try:
			self.configTree = ET.parse(self.path + "config.xml")
		except:
			sys.exit("Error: unable to find Cabrio config file, please start Cabrio to create it.")
		self.configRoot = self.configTree.getroot()
		self.fullscreen = self.getNode("full-screen", "interface", "false")
		self.fullscreenVar = self.setVar(self.fullscreen, bool)
		self.framerate = self.getNode("frame-rate", "interface", "60")
		self.framerateVar = tk.StringVar()
		self.framerateVar.set(self.framerate.text)
		self.videoLoop = self.getNode("video-loop", "interface", "true")
		self.videoLoopVar = self.setVar(self.videoLoop, bool)
		self.hideButtons = self.getNode("hide-buttons", "interface", "false")
		self.hideButtonsVar = self.setVar(self.hideButtons, bool)
		self.musicVolume = self.getNode("music-volume", "interface", "128")
		self.musicVolumeVar = self.setVar(self.musicVolume, float)
		self.videoSound = self.getNode("video-sound", "interface", "true")
		self.videoSoundVar = self.setVar(self.videoSound, bool)
		self.themeSounds = self.getNode("theme-sound", "interface", "true")
		self.themeSoundsVar = self.setVar(self.themeSounds, bool)
		try:
			self.themesList = self.getFolders("/usr/share/cabrio/themes/")
		except:
			print "test"
			sys.exit("Error: No themes found, please check your Cabrio installation.")
		self.theme = self.getNode("theme", "interface", "carousel")
		self.themeVar = tk.StringVar()
		self.themeVar.set(self.theme.text)
		self.width = self.getNode("width", "interface/screen", "1024")
		self.widthVar = self.setVar(self.width, str)
		self.height = self.getNode("height", "interface/screen", "768")
		self.heightVar = self.setVar(self.height, str)
		self.rotation = self.getNode("rotation", "interface/screen", "0")
		self.rotationVar = self.setVar(self.rotation, str)
		self.flipHorizontal = self.getNode("flip-horizontal", "interface/screen", "0")
		self.flipHorizontalVar = self.setVar(self.flipHorizontal, str)
		self.flipVertical = self.getNode("flip-vertical", "interface/screen", "0")
		self.flipVerticalVar = self.setVar(self.flipVertical, str)
		self.quality = self.getNode("quality", "interface/graphics", "high")
		self.qualityVar = self.setVar(self.quality, str)
		self.maxImageWidth = self.getNode("max-image-width", "interface/graphics", "512")
		self.maxImageWidthVar = self.setVar(self.maxImageWidth, str)
		self.maxImageHeight = self.getNode("max-image-height", "interface/graphics", "512")
		self.maxImageHeightVar = self.setVar(self.maxImageHeight, str)
		
		self.upValue = self.getNode("value", "", "up", "up")
		self.upValueVar = self.setVar(self.upValue, str)
		self.upDeviceType = self.getNode("type", "device", "keyboard", "up")
		self.upDeviceTypeVar = self.setVar(self.upDeviceType, str)
		self.upDeviceId  = self.getNode("id", "device", "0", "up")
		self.upDeviceIdVar = self.setVar(self.upDeviceId, int)
		self.upControlType = self.getNode("type", "control", "Default", "up")
		self.upControlTypeVar = self.setVar(self.upControlType, str)
		self.upControlId = self.getNode("id", "control", "0", "up")
		self.upControlIdVar = self.setVar(self.upControlId, int)
		self.upControlList = self.setControlList(self.upDeviceTypeVar)
		self.upValueList = self.setValueList(self.upDeviceTypeVar.get(), self.upControlTypeVar.get())

		self.downValue = self.getNode("value", "", "down", "down")
		self.downValueVar = self.setVar(self.downValue, str)
		self.downDeviceType = self.getNode("type", "device", "keyboard", "down")
		self.downDeviceTypeVar = self.setVar(self.downDeviceType, str)
		self.downDeviceId  = self.getNode("id", "device", "0", "down")
		self.downDeviceIdVar = self.setVar(self.downDeviceId, int)
		self.downControlType = self.getNode("type", "control", "Default", "down")
		self.downControlTypeVar = self.setVar(self.downControlType, str)
		self.downControlId = self.getNode("id", "control", "0", "down")
		self.downControlIdVar = self.setVar(self.downControlId, int)
		self.downControlList = self.setControlList(self.downDeviceTypeVar)
		self.downValueList = self.setValueList(self.downDeviceTypeVar.get(), self.downControlTypeVar.get())

		self.leftValue = self.getNode("value", "", "left", "left")
		self.leftValueVar = self.setVar(self.leftValue, str)
		self.leftDeviceType = self.getNode("type", "device", "keyboard", "left")
		self.leftDeviceTypeVar = self.setVar(self.leftDeviceType, str)
		self.leftDeviceId  = self.getNode("id", "device", "0", "left")
		self.leftDeviceIdVar = self.setVar(self.leftDeviceId, int)
		self.leftControlType = self.getNode("type", "control", "Default", "left")
		self.leftControlTypeVar = self.setVar(self.leftControlType, str)
		self.leftControlId = self.getNode("id", "control", "0", "left")
		self.leftControlIdVar = self.setVar(self.leftControlId, int)
		self.leftControlList = self.setControlList(self.leftDeviceTypeVar)
		self.leftValueList = self.setValueList(self.leftDeviceTypeVar.get(), self.leftControlTypeVar.get())

		self.rightValue = self.getNode("value", "", "right", "right")
		self.rightValueVar = self.setVar(self.rightValue, str)
		self.rightDeviceType = self.getNode("type", "device", "keyboard", "right")
		self.rightDeviceTypeVar = self.setVar(self.rightDeviceType, str)
		self.rightDeviceId  = self.getNode("id", "device", "0", "right")
		self.rightDeviceIdVar = self.setVar(self.rightDeviceId, int)
		self.rightControlType = self.getNode("type", "control", "Default", "right")
		self.rightControlTypeVar = self.setVar(self.rightControlType, str)
		self.rightControlId = self.getNode("id", "control", "0", "right")
		self.rightControlIdVar = self.setVar(self.rightControlId, int)
		self.rightControlList = self.setControlList(self.rightDeviceTypeVar)
		self.rightValueList = self.setValueList(self.rightDeviceTypeVar.get(), self.rightControlTypeVar.get())

		self.selectValue = self.getNode("value", "", "return", "select")
		self.selectValueVar = self.setVar(self.selectValue, str)
		self.selectDeviceType = self.getNode("type", "device", "keyboard", "select")
		self.selectDeviceTypeVar = self.setVar(self.selectDeviceType, str)
		self.selectDeviceId  = self.getNode("id", "device", "0", "select")
		self.selectDeviceIdVar = self.setVar(self.selectDeviceId, int)
		self.selectControlType = self.getNode("type", "control", "Default", "select")
		self.selectControlTypeVar = self.setVar(self.selectControlType, str)
		self.selectControlId = self.getNode("id", "control", "0", "select")
		self.selectControlIdVar = self.setVar(self.selectControlId, int)
		self.selectControlList = self.setControlList(self.selectDeviceTypeVar)
		self.selectValueList = self.setValueList(self.selectDeviceTypeVar.get(), self.selectControlTypeVar.get())

		self.backValue = self.getNode("value", "", "backspace", "back")
		self.backValueVar = self.setVar(self.backValue, str)
		self.backDeviceType = self.getNode("type", "device", "keyboard", "back")
		self.backDeviceTypeVar = self.setVar(self.backDeviceType, str)
		self.backDeviceId  = self.getNode("id", "device", "0", "back")
		self.backDeviceIdVar = self.setVar(self.backDeviceId, int)
		self.backControlType = self.getNode("type", "control", "Default", "back")
		self.backControlTypeVar = self.setVar(self.backControlType, str)
		self.backControlId = self.getNode("id", "control", "0", "back")
		self.backControlIdVar = self.setVar(self.backControlId, int)
		self.backControlList = self.setControlList(self.backDeviceTypeVar)
		self.backValueList = self.setValueList(self.backDeviceTypeVar.get(), self.backControlTypeVar.get())

		self.quitValue = self.getNode("value", "", "escape", "quit")
		self.quitValueVar = self.setVar(self.quitValue, str)
		self.quitDeviceType = self.getNode("type", "device", "keyboard", "quit")
		self.quitDeviceTypeVar = self.setVar(self.quitDeviceType, str)
		self.quitDeviceId  = self.getNode("id", "device", "0", "quit")
		self.quitDeviceIdVar = self.setVar(self.quitDeviceId, int)
		self.quitControlType = self.getNode("type", "control", "Default", "quit")
		self.quitControlTypeVar = self.setVar(self.quitControlType, str)
		self.quitControlId = self.getNode("id", "control", "0", "quit")
		self.quitControlIdVar = self.setVar(self.quitControlId, int)
		self.quitControlList = self.setControlList(self.quitDeviceTypeVar)
		self.quitValueList = self.setValueList(self.quitDeviceTypeVar.get(), self.quitControlTypeVar.get())

		self.list1Value = self.getNode("value", "", "LSHIFT", "list1")
		self.list1ValueVar = self.setVar(self.list1Value, str)
		self.list1DeviceType = self.getNode("type", "device", "keyboard", "list1")
		self.list1DeviceTypeVar = self.setVar(self.list1DeviceType, str)
		self.list1DeviceId  = self.getNode("id", "device", "0", "list1")
		self.list1DeviceIdVar = self.setVar(self.list1DeviceId, int)
		self.list1ControlType = self.getNode("type", "control", "Default", "list1")
		self.list1ControlTypeVar = self.setVar(self.list1ControlType, str)
		self.list1ControlId = self.getNode("id", "control", "0", "list1")
		self.list1ControlIdVar = self.setVar(self.list1ControlId, int)
		self.list1ControlList = self.setControlList(self.list1DeviceTypeVar)
		self.list1ValueList = self.setValueList(self.list1DeviceTypeVar.get(), self.list1ControlTypeVar.get())

		self.list2Value = self.getNode("value", "", "LCTRL", "list2")
		self.list2ValueVar = self.setVar(self.list2Value, str)
		self.list2DeviceType = self.getNode("type", "device", "keyboard", "list2")
		self.list2DeviceTypeVar = self.setVar(self.list2DeviceType, str)
		self.list2DeviceId  = self.getNode("id", "device", "0", "list2")
		self.list2DeviceIdVar = self.setVar(self.list2DeviceId, int)
		self.list2ControlType = self.getNode("type", "control", "Default", "list2")
		self.list2ControlTypeVar = self.setVar(self.list2ControlType, str)
		self.list2ControlId = self.getNode("id", "control", "0", "list2")
		self.list2ControlIdVar = self.setVar(self.list2ControlId, int)
		self.list2ControlList = self.setControlList(self.list2DeviceTypeVar)
		self.list2ValueList = self.setValueList(self.list2DeviceTypeVar.get(), self.list2ControlTypeVar.get())

		self.list3Value = self.getNode("value", "", "LALT", "list3")
		self.list3ValueVar = self.setVar(self.list3Value, str)
		self.list3DeviceType = self.getNode("type", "device", "keyboard", "list3")
		self.list3DeviceTypeVar = self.setVar(self.list3DeviceType, str)
		self.list3DeviceId  = self.getNode("id", "device", "0", "list3")
		self.list3DeviceIdVar = self.setVar(self.list3DeviceId, int)
		self.list3ControlType = self.getNode("type", "control", "Default", "list3")
		self.list3ControlTypeVar = self.setVar(self.list3ControlType, str)
		self.list3ControlId = self.getNode("id", "control", "0", "list3")
		self.list3ControlIdVar = self.setVar(self.list3ControlId, int)
		self.list3ControlList = self.setControlList(self.list3DeviceTypeVar)
		self.list3ValueList = self.setValueList(self.list3DeviceTypeVar.get(), self.list3ControlTypeVar.get())

		self.list4Value = self.getNode("value", "", "space", "list4")
		self.list4ValueVar = self.setVar(self.list4Value, str)
		self.list4DeviceType = self.getNode("type", "device", "keyboard", "list4")
		self.list4DeviceTypeVar = self.setVar(self.list4DeviceType, str)
		self.list4DeviceId  = self.getNode("id", "device", "0", "list4")
		self.list4DeviceIdVar = self.setVar(self.list4DeviceId, int)
		self.list4ControlType = self.getNode("type", "control", "Default", "list4")
		self.list4ControlTypeVar = self.setVar(self.list4ControlType, str)
		self.list4ControlId = self.getNode("id", "control", "0", "list4")
		self.list4ControlIdVar = self.setVar(self.list4ControlId, int)
		self.list4ControlList = self.setControlList(self.list4DeviceTypeVar)
		self.list4ValueList = self.setValueList(self.list4DeviceTypeVar.get(), self.list4ControlTypeVar.get())

		self.list5Value = self.getNode("value", "", "RALT", "list5")
		self.list5ValueVar = self.setVar(self.list5Value, str)
		self.list5DeviceType = self.getNode("type", "device", "keyboard", "list5")
		self.list5DeviceTypeVar = self.setVar(self.list5DeviceType, str)
		self.list5DeviceId  = self.getNode("id", "device", "0", "list5")
		self.list5DeviceIdVar = self.setVar(self.list5DeviceId, int)
		self.list5ControlType = self.getNode("type", "control", "Default", "list5")
		self.list5ControlTypeVar = self.setVar(self.list5ControlType, str)
		self.list5ControlId = self.getNode("id", "control", "0", "list5")
		self.list5ControlIdVar = self.setVar(self.list5ControlId, int)
		self.list5ControlList = self.setControlList(self.list5DeviceTypeVar)
		self.list5ValueList = self.setValueList(self.list5DeviceTypeVar.get(), self.list5ControlTypeVar.get())

		self.emulatorBinary = tk.StringVar()
		self.emulatorBinary.set("")
		self.emulatorsList = []
		self.devicesList = ["keyboard", "mouse", "joystick"]
		self.joyControlList = ["axis", "ball", "button", "hat"]
		self.mouseControlList = ["axis", "Button"]
		self.keyboardControlList = ["Default"]
		
		# Widgets declaration starts here.
		self.title(self.titleStr)
		self.notebook = ttk.Notebook(self)
		self.notebook.grid(column=0, row=0)
		self.displayTab = ttk.Frame(self.notebook)
		# self.pathTab = ttk.Frame(self.notebook)
		self.controlsTab = ttk.Frame(self.notebook)
		self.emulatorsTab = ttk.Frame(self.notebook)
		self.themeTab = ttk.Frame(self.notebook)
		self.aboutTab = ttk.Frame(self.notebook)
		self.notebook.add(self.displayTab, text=self.displayTabStr)
		# self.notebook.add(self.pathTab, text=self.pathTabStr)
		self.notebook.add(self.controlsTab, text=self.controlsTabStr)
		self.notebook.add(self.emulatorsTab, text=self.emulatorsTabStr)
		self.notebook.add(self.themeTab, text=self.themeTabStr)
		self.notebook.add(self.aboutTab, text=self.aboutTabStr)
		# Theme label frame widgets declaration starts here.
		self.themeLabel = ttk.Label(self.themeTab, text=self.themeStr)
		self.themeLabel.grid(column=0, row=0, sticky="W")
		self.themesCombobox = ttk.Combobox(self.themeTab, values=self.themesList, textvariable=self.themeVar, state="readonly")
		self.themesCombobox.bind("<<ComboboxSelected>>", self.writeTheme)
		self.themesCombobox.grid(column=1, row=0, sticky="W")
		# Display tab widgets declaration starts here.
		self.displayPanedWindow = ttk.Panedwindow(self.displayTab, orient="vertical")
		self.displayPanedWindow.grid()
		self.interfaceLabelFrame = ttk.Labelframe(self.displayTab, text=self.interfaceLabelFrameStr)
		self.displayPanedWindow.add(self.interfaceLabelFrame)
		# Interface label frame widgets declaration starts here.
		self.fsCheckButton = ttk.Checkbutton(self.interfaceLabelFrame, variable=self.fullscreenVar, text=self.fullscreenStr, command=lambda a=self.fullscreen, b=self.fullscreenVar: self.writeBool(a, b))
		self.fsCheckButton.grid(column=0, row=0, sticky="W")
		self.hideButtonsCheckButton = ttk.Checkbutton(self.interfaceLabelFrame, variable=self.hideButtonsVar, text=self.hideButtonsStr, command=lambda a=self.hideButtons, b=self.hideButtonsVar: self.writeBool(a, b))
		self.hideButtonsCheckButton.grid(column=1, row=0, sticky="W")
		self.videoLoopCheckButton = ttk.Checkbutton(self.interfaceLabelFrame, variable=self.videoLoopVar, text=self.videoLoopStr, command=lambda a=self.videoLoop, b=self.videoLoopVar: self.writeBool(a, b))
		self.videoLoopCheckButton.grid(column=0, row=1, columnspan=2, sticky="W")
		self.framerateLabel = ttk.Label(self.interfaceLabelFrame, text=self.framerateStr)
		self.framerateLabel.grid(column=0, row=2, sticky="W")
		self.framerateEntry = ttk.Entry(self.interfaceLabelFrame, text=self.framerateVar)
		self.framerateEntry.grid(column=1, row=2, sticky="W")
		self.setFramerateButton = ttk.Button(self.interfaceLabelFrame, text=self.setButtonStr, command=lambda a=self.framerate, b= self.framerateVar: self.writeString(a, b))
		self.setFramerateButton.grid(column=2, row=2)
		# Screen label frame widgets declaration starts here.
		self.screenLabelFrame = ttk.Labelframe(self.displayTab, text=self.screenLabelFrameStr)
		self.displayPanedWindow.add(self.screenLabelFrame)
		self.widthLabel = ttk.Label(self.screenLabelFrame, text=self.widthStr)
		self.widthLabel.grid(column=0, row=0, sticky="W")
		self.widthEntry = ttk.Entry(self.screenLabelFrame, text=self.widthVar, width=7)
		self.widthEntry.grid(column=1, row=0, sticky="W")
		self.heightLabel = ttk.Label(self.screenLabelFrame, text=self.heightStr)
		self.heightLabel.grid(column=2, row=0, sticky="W")
		self.heightEntry = ttk.Entry(self.screenLabelFrame, text=self.heightVar, width=7)
		self.heightEntry.grid(column=3, row=0, sticky="W")
		self.resolutionButton = ttk.Button(self.screenLabelFrame, text=self.setButtonStr, command=lambda a=self.width, b=self.widthVar, c=self.height, d=self.heightVar: self.writeString(a, b, c, d))
		self.resolutionButton.grid(column=4, row=0, sticky="W")
		self.rotationLabel = ttk.Label(self.screenLabelFrame, text=self.rotationStr)
		self.rotationLabel.grid(column=0, row=1, sticky="W")
		self.rotationRadio0 = ttk.Radiobutton(self.screenLabelFrame, text="0°", variable=self.rotationVar, value="0", command=lambda a=self.rotation, b=self.rotationVar: self.writeString(a, b))
		self.rotationRadio0.grid(column=1, row=1)
		self.rotationRadio90 = ttk.Radiobutton(self.screenLabelFrame, text="90°", variable=self.rotationVar, value="90", command=lambda a=self.rotation, b=self.rotationVar: self.writeString(a, b))
		self.rotationRadio90.grid(column=2, row=1)
		self.rotationRadio180 = ttk.Radiobutton(self.screenLabelFrame, text="180°", variable=self.rotationVar, value="180", command=lambda a=self.rotation, b=self.rotationVar: self.writeString(a, b))
		self.rotationRadio180.grid(column=3, row=1)
		self.rotationRadio270 = ttk.Radiobutton(self.screenLabelFrame, text="270°", variable=self.rotationVar, value="270", command=lambda a=self.rotation, b=self.rotationVar: self.writeString(a, b))
		self.rotationRadio270.grid(column=4, row=1)
		self.flipHorizontalCheckbutton = ttk.Checkbutton(self.screenLabelFrame, variable=self.flipHorizontalVar, text=self.flipHorizontalStr, command=lambda a=self.flipHorizontal, b=self.flipHorizontalVar: self.writeInt(a, b))
		self.flipHorizontalCheckbutton.grid(column=0, row=2, columnspan=3)
		self.flipVerticalCheckbutton = ttk.Checkbutton(self.screenLabelFrame, variable=self.flipVerticalVar, text=self.flipVerticalStr, command=lambda a=self.flipVertical, b=self.flipVerticalVar: self.writeInt(a, b))
		self.flipVerticalCheckbutton.grid(column=3, row=2, columnspan=3)
		# Graphics label frame widget declaration starts here.
		self.graphicsLabelFrame = ttk.Labelframe(self.displayTab, text=self.graphicsLabelFrameStr)
		self.displayPanedWindow.add(self.graphicsLabelFrame)
		self.qualityLabel = ttk.Label(self.graphicsLabelFrame, text=self.qualityLabelStr)
		self.qualityLabel.grid(column=0, row=0)
		self.qualityRadioLow = ttk.Radiobutton(self.graphicsLabelFrame, text=self.qualityLowStr, variable=self.qualityVar, value="low", command=lambda a=self.quality, b=self.qualityVar: self.writeString(a, b))
		self.qualityRadioLow.grid(column=1, row=0)
		self.qualityRadioMedium = ttk.Radiobutton(self.graphicsLabelFrame, text=self.qualityMediumStr, variable=self.qualityVar, value="medium", command=lambda a=self.quality, b=self.qualityVar: self.writeString(a, b))
		self.qualityRadioMedium.grid(column=2, row=0)
		self.qualityRadioHigh = ttk.Radiobutton(self.graphicsLabelFrame, text=self.qualityHighStr, variable=self.qualityVar, value="high", command=lambda a=self.quality, b=self.qualityVar: self.writeString(a, b))
		self.qualityRadioHigh.grid(column=3, row=0)
		self.maxImageWidthLabel = ttk.Label(self.graphicsLabelFrame, text=self.maxImageWidthLabelStr)
		self.maxImageWidthLabel.grid(column=0, row=1, sticky="W")
		self.maxImageWidthEntry = ttk.Entry(self.graphicsLabelFrame, text=self.maxImageWidthVar, width=5)
		self.maxImageWidthEntry.grid(column=1, row=1, columnspan=2)
		self.maxImageHeigthLabel = ttk.Label(self.graphicsLabelFrame, text=self.maxImageHeightLabelStr)
		self.maxImageHeigthLabel.grid(column=0, row=2, sticky="W")
		self.maxImageHeightEntry = ttk.Entry(self.graphicsLabelFrame, text=self.maxImageHeightVar, width=5)
		self.maxImageHeightEntry.grid(column=1, row=2, columnspan=2)
		self.maxSetButton = ttk.Button(self.graphicsLabelFrame, text=self.setButtonStr, command=lambda a=self.maxImageWidth, b=self.maxImageWidthVar, c=self.maxImageHeight, d=self.maxImageHeightVar: self.writeString(a, b, c, d))
		self.maxSetButton.grid(column=5, row=1, rowspan=2)
		# Audio label frame widgets declaration starts here.
		self.audioLabelFrame = ttk.Labelframe(self.displayTab, text=self.audioLabelFrameStr)
		self.displayPanedWindow.add(self.audioLabelFrame)
		self.videoSoundCheckButton = ttk.Checkbutton(self.audioLabelFrame, variable=self.videoSoundVar, text=self.videoSoundStr, command=lambda a=self.videoSound, b=self.videoSoundVar: self.writeBool(a, b))
		self.videoSoundCheckButton.grid(column=0, row=0, sticky="W")
		self.themeSoundsCheckButton = ttk.Checkbutton(self.audioLabelFrame, variable=self.themeSoundsVar, text=self.themeSoundsStr, command=lambda a=self.themeSounds, b=self.themeSoundsVar: self.writeBool(a, b))
		self.themeSoundsCheckButton.grid(column=0, row=1, sticky="W")
		self.musicVolumeLabel = ttk.Label(self.audioLabelFrame, text=self.musicVolumeStr)
		self.musicVolumeLabel.grid(column=0, row=2)
		self.musicVolumeScale = ttk.Scale(self.audioLabelFrame, length=250, orient="horizontal", from_=1.0, to=128.0, variable=self.musicVolumeVar)
		self.musicVolumeScale.bind("<ButtonRelease-1>", lambda a=None, b=self.musicVolume, c=self.musicVolumeScale: self.writeFloat(a, b, c))
		self.musicVolumeScale.grid(column=1, row=2)
		# self.musicVolumeSpinbox = tk.Spinbox(self.audioLabelFrame, from_=1.0, to=128.0, textvariable=self.musicVolumeVar, width=3)
		# self.musicVolumeSpinbox.grid(column=1, row=2)
		# self.setmusicVolumeButton = ttk.Button(self.audioLabelFrame, text=self.setButtonStr, command=lambda a=self.musicVolume, b= self.musicVolumeVar: self.writeString(a, b))
		# self.setmusicVolumeButton.grid(column=2, row=2)
		# Locations tab starts here
		# self.themesPathLabel = ttk.Label(self.pathTab, text=self.themesPathLabelStr)
		# self.themesPathLabel.grid(column=0, row=0, sticky="W")
		# self.themesPathEntry = ttk.Entry(self.pathTab)
		# self.themesPathEntry.grid(column=1, row=0)
		# self.themesPathBrowse = ttk.Button(self.pathTab, text=self.browseButtonStr)
		# self.themesPathBrowse.grid(column=2, row=0)
		# self.backgroundPathLabel = ttk.Label(self.pathTab, text=self.backgroundPathLabelStr)
		# self.backgroundPathLabel.grid(column=0, row=1, sticky="W")
		# self.backgroundPathEntry = ttk.Entry(self.pathTab)
		# self.backgroundPathEntry.grid(column=1, row=1)
		# self.backgroundPathBrowse = ttk.Button(self.pathTab, text=self.browseButtonStr)
		# self.backgroundPathBrowse.grid(column=2, row=1)
		# self.logoPathLabel = ttk.Label(self.pathTab, text=self.logoPathLabelStr)
		# self.logoPathLabel.grid(column=0, row=2, sticky="W")
		# self.logoPathEntry = ttk.Entry(self.pathTab)
		# self.logoPathEntry.grid(column=1, row=2)
		# self.logoPathBrowse = ttk.Button(self.pathTab, text=self.browseButtonStr)
		# self.logoPathBrowse.grid(column=2, row=2)
		# self.videoPathLabel = ttk.Label(self.pathTab, text=self.videoPathLabelStr)
		# self.videoPathLabel.grid(column=0, row=3, sticky="W")
		# self.videoPathEntry = ttk.Entry(self.pathTab)
		# self.videoPathEntry.grid(column=1, row=3)
		# self.videoPathBrowse = ttk.Button(self.pathTab, text=self.browseButtonStr)
		# self.videoPathBrowse.grid(column=2, row=3)
		# self.screenshotPathLabel = ttk.Label(self.pathTab, text=self.screenshotPathLabelStr)
		# self.screenshotPathLabel.grid(column=0, row=4, sticky="W")
		# self.screenshotPathEntry = ttk.Entry(self.pathTab)
		# self.screenshotPathEntry.grid(column=1, row=4)
		# self.screenshotPathBrowse = ttk.Button(self.pathTab, text=self.browseButtonStr)
		# self.screenshotPathBrowse.grid(column=2, row=4)
		# Controls tab starts here
		self.mapAllButton = ttk.Button(self.controlsTab, text=self.setAllKeysStr, command=lambda: self.getControls())
		self.mapAllButton.grid(column=0, row=0, columnspan=8)
		self.deviceLabel = ttk.Label(self.controlsTab, text=self.deviceStr)
		self.deviceLabel.grid(column=1, row=1, sticky="W")
		self.deviceIdLabel = ttk.Label(self.controlsTab, text=self.idStr)
		self.deviceIdLabel.grid(column=2, row=1, sticky="W")
		self.deviceSeparator = ttk.Separator(self.controlsTab, orient="vertical")
		self.deviceSeparator.grid(column=3, row=1, sticky="NS", rowspan=8)
		self.typeLabel = ttk.Label(self.controlsTab, text=self.typeStr)
		self.typeLabel.grid(column=4, row=1, sticky="W")
		self.typeIdLabel = ttk.Label(self.controlsTab, text=self.idStr)
		self.typeIdLabel.grid(column=5, row=1, sticky="W")
		self.typeSeparator = ttk.Separator(self.controlsTab, orient="vertical")
		self.typeSeparator.grid(column=6, row=1, sticky="NS", rowspan=8)
		self.valueLabel = ttk.Label(self.controlsTab, text=self.valueStr)
		self.valueLabel.grid(column=7, row=1, sticky="W")
		# Up widgets declaration
		self.upLabel = ttk.Label(self.controlsTab, text=self.upLabelStr)
		self.upLabel.grid(column=0, row=2, sticky="W")
		self.upDeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.upDeviceTypeVar, state="readonly", width=7)
		self.upDeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="up", c="device": self.updateWidget(a, b, c))
		self.upDeviceTypeCombobox.grid(column=1, row=2)
		self.upDeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.upDeviceIdVar, width=2)
		self.upDeviceIdSpinbox.grid(column=2, row=2)
		self.upControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.upControlList, textvariable=self.upControlTypeVar, state="readonly", width=7)
		self.upControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="up", c="control": self.updateWidget(a, b, c))
		self.upControlTypeCombobox.grid(column=4, row=2)
		self.upControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.upControlIdVar, width=2)
		self.upControlIdSpinbox.grid(column=5, row=2, sticky="W")
		self.upValueCombobox = ttk.Combobox(self.controlsTab, values=self.upValueList, textvariable=self.upValueVar, state="readonly", width=17)
		self.upValueCombobox.grid(column=7, row=2, sticky="W")
		# Down widgets declaration
		self.downLabel = ttk.Label(self.controlsTab, text=self.downLabelStr)
		self.downLabel.grid(column=0, row=3, sticky="W")
		self.downDeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.downDeviceTypeVar, state="readonly", width=7)
		self.downDeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="down", c="device": self.updateWidget(a, b, c))
		self.downDeviceTypeCombobox.grid(column=1, row=3)
		self.downDeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.downDeviceIdVar, width=2)
		self.downDeviceIdSpinbox.grid(column=2, row=3)
		self.downControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.downControlList, textvariable=self.downControlTypeVar, state="readonly", width=7)
		self.downControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="down", c="control": self.updateWidget(a, b, c))
		self.downControlTypeCombobox.grid(column=4, row=3)
		self.downControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.downControlIdVar, width=2)
		self.downControlIdSpinbox.grid(column=5, row=3, sticky="W")
		self.downValueCombobox = ttk.Combobox(self.controlsTab, values=self.downValueList, textvariable=self.downValueVar, state="readonly", width=17)
		self.downValueCombobox.grid(column=7, row=3, sticky="W")
		# Left widgets declaration
		self.leftLabel = ttk.Label(self.controlsTab, text=self.leftLabelStr)
		self.leftLabel.grid(column=0, row=4, sticky="W")
		self.leftDeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.leftDeviceTypeVar, state="readonly", width=7)
		self.leftDeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="left", c="device": self.updateWidget(a, b, c))
		self.leftDeviceTypeCombobox.grid(column=1, row=4)
		self.leftDeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.leftDeviceIdVar, width=2)
		self.leftDeviceIdSpinbox.grid(column=2, row=4)
		self.leftControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.leftControlList, textvariable=self.leftControlTypeVar, state="readonly", width=7)
		self.leftControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="left", c="control": self.updateWidget(a, b, c))
		self.leftControlTypeCombobox.grid(column=4, row=4)
		self.leftControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.leftControlIdVar, width=2)
		self.leftControlIdSpinbox.grid(column=5, row=4, sticky="W")
		self.leftValueCombobox = ttk.Combobox(self.controlsTab, values=self.leftValueList, textvariable=self.leftValueVar, state="readonly", width=17)
		self.leftValueCombobox.grid(column=7, row=4, sticky="W")
		# Right widgets declaration
		self.rightLabel = ttk.Label(self.controlsTab, text=self.rightLabelStr)
		self.rightLabel.grid(column=0, row=5, sticky="W")
		self.rightDeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.rightDeviceTypeVar, state="readonly", width=7)
		self.rightDeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="right", c="device": self.updateWidget(a, b, c))
		self.rightDeviceTypeCombobox.grid(column=1, row=5)
		self.rightDeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.rightDeviceIdVar, width=2)
		self.rightDeviceIdSpinbox.grid(column=2, row=5)
		self.rightControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.rightControlList, textvariable=self.rightControlTypeVar, state="readonly", width=7)
		self.rightControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="right", c="control": self.updateWidget(a, b, c))
		self.rightControlTypeCombobox.grid(column=4, row=5)
		self.rightControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.rightControlIdVar, width=2)
		self.rightControlIdSpinbox.grid(column=5, row=5, sticky="W")
		self.rightValueCombobox = ttk.Combobox(self.controlsTab, values=self.rightValueList, textvariable=self.rightValueVar, state="readonly", width=17)
		self.rightValueCombobox.grid(column=7, row=5, sticky="W")
		# Select widgets declaration
		self.selectLabel = ttk.Label(self.controlsTab, text=self.selectLabelStr)
		self.selectLabel.grid(column=0, row=6, sticky="W")
		self.selectDeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.selectDeviceTypeVar, state="readonly", width=7)
		self.selectDeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="select", c="device": self.updateWidget(a, b, c))
		self.selectDeviceTypeCombobox.grid(column=1, row=6)
		self.selectDeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.selectDeviceIdVar, width=2)
		self.selectDeviceIdSpinbox.grid(column=2, row=6)
		self.selectControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.selectControlList, textvariable=self.selectControlTypeVar, state="readonly", width=7)
		self.selectControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="select", c="control": self.updateWidget(a, b, c))
		self.selectControlTypeCombobox.grid(column=4, row=6)
		self.selectControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.selectControlIdVar, width=2)
		self.selectControlIdSpinbox.grid(column=5, row=6, sticky="W")
		self.selectValueCombobox = ttk.Combobox(self.controlsTab, values=self.selectValueList, textvariable=self.selectValueVar, state="readonly", width=17)
		self.selectValueCombobox.grid(column=7, row=6, sticky="W")
		# Back widgets declaration
		self.backLabel = ttk.Label(self.controlsTab, text=self.backLabelStr)
		self.backLabel.grid(column=0, row=7, sticky="W")
		self.backDeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.backDeviceTypeVar, state="readonly", width=7)
		self.backDeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="back", c="device": self.updateWidget(a, b, c))
		self.backDeviceTypeCombobox.grid(column=1, row=7)
		self.backDeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.backDeviceIdVar, width=2)
		self.backDeviceIdSpinbox.grid(column=2, row=7)
		self.backControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.backControlList, textvariable=self.backControlTypeVar, state="readonly", width=7)
		self.backControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="back", c="control": self.updateWidget(a, b, c))
		self.backControlTypeCombobox.grid(column=4, row=7)
		self.backControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.backControlIdVar, width=2)
		self.backControlIdSpinbox.grid(column=5, row=7, sticky="W")
		self.backValueCombobox = ttk.Combobox(self.controlsTab, values=self.backValueList, textvariable=self.backValueVar, state="readonly", width=17)
		self.backValueCombobox.grid(column=7, row=7, sticky="W")
		# Quit widgets declaration
		self.quitLabel = ttk.Label(self.controlsTab, text=self.quitLabelStr)
		self.quitLabel.grid(column=0, row=8, sticky="W")
		self.quitDeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.quitDeviceTypeVar, state="readonly", width=7)
		self.quitDeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="quit", c="device": self.updateWidget(a, b, c))
		self.quitDeviceTypeCombobox.grid(column=1, row=8)
		self.quitDeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.quitDeviceIdVar, width=2)
		self.quitDeviceIdSpinbox.grid(column=2, row=8)
		self.quitControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.quitControlList, textvariable=self.quitControlTypeVar, state="readonly", width=7)
		self.quitControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="quit", c="control": self.updateWidget(a, b, c))
		self.quitControlTypeCombobox.grid(column=4, row=8)
		self.quitControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.quitControlIdVar, width=2)
		self.quitControlIdSpinbox.grid(column=5, row=8, sticky="W")
		self.quitValueCombobox = ttk.Combobox(self.controlsTab, values=self.quitValueList, textvariable=self.quitValueVar, state="readonly", width=17)
		self.quitValueCombobox.grid(column=7, row=8, sticky="W")
		self.saveButton = ttk.Button(self.controlsTab, text="Save", command=lambda: self.saveControlsChange())
		# List 1 widgets declaration
		self.list1Label = ttk.Label(self.controlsTab, text=self.list1LabelStr)
		self.list1Label.grid(column=0, row=8, sticky="W")
		self.list1DeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.list1DeviceTypeVar, state="readonly", width=7)
		self.list1DeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="list1", c="device": self.updateWidget(a, b, c))
		self.list1DeviceTypeCombobox.grid(column=1, row=8)
		self.list1DeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.list1DeviceIdVar, width=2)
		self.list1DeviceIdSpinbox.grid(column=2, row=8)
		self.list1ControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.list1ControlList, textvariable=self.list1ControlTypeVar, state="readonly", width=7)
		self.list1ControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="list1", c="control": self.updateWidget(a, b, c))
		self.list1ControlTypeCombobox.grid(column=4, row=8)
		self.list1ControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.list1ControlIdVar, width=2)
		self.list1ControlIdSpinbox.grid(column=5, row=8, sticky="W")
		self.list1ValueCombobox = ttk.Combobox(self.controlsTab, values=self.list1ValueList, textvariable=self.list1ValueVar, state="readonly", width=17)
		self.list1ValueCombobox.grid(column=7, row=8, sticky="W")
		# List 2 widgets declaration
		self.list2Label = ttk.Label(self.controlsTab, text=self.list2LabelStr)
		self.list2Label.grid(column=0, row=9, sticky="W")
		self.list2DeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.list2DeviceTypeVar, state="readonly", width=7)
		self.list2DeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="list2", c="device": self.updateWidget(a, b, c))
		self.list2DeviceTypeCombobox.grid(column=1, row=9)
		self.list2DeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.list2DeviceIdVar, width=2)
		self.list2DeviceIdSpinbox.grid(column=2, row=9)
		self.list2ControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.list2ControlList, textvariable=self.list2ControlTypeVar, state="readonly", width=7)
		self.list2ControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="list2", c="control": self.updateWidget(a, b, c))
		self.list2ControlTypeCombobox.grid(column=4, row=9)
		self.list2ControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.list2ControlIdVar, width=2)
		self.list2ControlIdSpinbox.grid(column=5, row=9, sticky="W")
		self.list2ValueCombobox = ttk.Combobox(self.controlsTab, values=self.list2ValueList, textvariable=self.list2ValueVar, state="readonly", width=17)
		self.list2ValueCombobox.grid(column=7, row=9, sticky="W")
		# List 3 widgets declaration
		self.list3Label = ttk.Label(self.controlsTab, text=self.list3LabelStr)
		self.list3Label.grid(column=0, row=10, sticky="W")
		self.list3DeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.list3DeviceTypeVar, state="readonly", width=7)
		self.list3DeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="list3", c="device": self.updateWidget(a, b, c))
		self.list3DeviceTypeCombobox.grid(column=1, row=10)
		self.list3DeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.list3DeviceIdVar, width=2)
		self.list3DeviceIdSpinbox.grid(column=2, row=10)
		self.list3ControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.list3ControlList, textvariable=self.list3ControlTypeVar, state="readonly", width=7)
		self.list3ControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="list3", c="control": self.updateWidget(a, b, c))
		self.list3ControlTypeCombobox.grid(column=4, row=10)
		self.list3ControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.list3ControlIdVar, width=2)
		self.list3ControlIdSpinbox.grid(column=5, row=10, sticky="W")
		self.list3ValueCombobox = ttk.Combobox(self.controlsTab, values=self.list3ValueList, textvariable=self.list3ValueVar, state="readonly", width=17)
		self.list3ValueCombobox.grid(column=7, row=10, sticky="W")
		# List 4 widgets declaration
		self.list4Label = ttk.Label(self.controlsTab, text=self.list4LabelStr)
		self.list4Label.grid(column=0, row=11, sticky="W")
		self.list4DeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.list4DeviceTypeVar, state="readonly", width=7)
		self.list4DeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="list4", c="device": self.updateWidget(a, b, c))
		self.list4DeviceTypeCombobox.grid(column=1, row=11)
		self.list4DeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.list4DeviceIdVar, width=2)
		self.list4DeviceIdSpinbox.grid(column=2, row=11)
		self.list4ControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.list4ControlList, textvariable=self.list4ControlTypeVar, state="readonly", width=7)
		self.list4ControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="list4", c="control": self.updateWidget(a, b, c))
		self.list4ControlTypeCombobox.grid(column=4, row=11)
		self.list4ControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.list4ControlIdVar, width=2)
		self.list4ControlIdSpinbox.grid(column=5, row=11, sticky="W")
		self.list4ValueCombobox = ttk.Combobox(self.controlsTab, values=self.list4ValueList, textvariable=self.list4ValueVar, state="readonly", width=17)
		self.list4ValueCombobox.grid(column=7, row=11, sticky="W")
		# List 5 widgets declaration
		self.list5Label = ttk.Label(self.controlsTab, text=self.list5LabelStr)
		self.list5Label.grid(column=0, row=12, sticky="W")
		self.list5DeviceTypeCombobox = ttk.Combobox(self.controlsTab, values=self.devicesList, textvariable=self.list5DeviceTypeVar, state="readonly", width=7)
		self.list5DeviceTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="list5", c="device": self.updateWidget(a, b, c))
		self.list5DeviceTypeCombobox.grid(column=1, row=12)
		self.list5DeviceIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99.0, textvariable=self.list5DeviceIdVar, width=2)
		self.list5DeviceIdSpinbox.grid(column=2, row=12)
		self.list5ControlTypeCombobox = ttk.Combobox(self.controlsTab, values=self.list5ControlList, textvariable=self.list5ControlTypeVar, state="readonly", width=7)
		self.list5ControlTypeCombobox.bind("<<ComboboxSelected>>", lambda a=None, b="list5", c="control": self.updateWidget(a, b, c))
		self.list5ControlTypeCombobox.grid(column=4, row=12)
		self.list5ControlIdSpinbox = tk.Spinbox(self.controlsTab, from_=0.0, to=99, textvariable=self.list5ControlIdVar, width=2)
		self.list5ControlIdSpinbox.grid(column=5, row=12, sticky="W")
		self.list5ValueCombobox = ttk.Combobox(self.controlsTab, values=self.list5ValueList, textvariable=self.list5ValueVar, state="readonly", width=17)
		self.list5ValueCombobox.grid(column=7, row=12, sticky="W")
		# save button
		self.saveButton = ttk.Button(self.controlsTab, text="Save", command=lambda: self.saveControlsChange())
		self.saveButton.grid(column=0, row=13, columnspan=8)
		# Emulator tab widgets declaration starts here.
		self.newEmulatorLabel = ttk.Label(self.emulatorsTab, text=self.newEmulatorLabelStr)
		self.newEmulatorLabel.grid(column=0, row=0, sticky="W")
		self.addEmulatorButton = ttk.Button(self.emulatorsTab, text=self.addButtonStr, command=lambda a="new": self.editEmulator(a))
		self.addEmulatorButton.grid(column=1, row=0, sticky="W")
		self.scrollbar = ttk.Scrollbar(self.emulatorsTab)
		self.scrollbar.grid(column=5, row=1, sticky="NS")
		self.emulatorsListbox = tk.Listbox(self.emulatorsTab, yscrollcommand = self.scrollbar.set, width=40, selectmode="single")
		for item in self.configRoot.findall(".//emulator"):
			displayName = item.find("display-name")
			self.emulatorsListbox.insert("end", displayName.text)
			self.emulatorsList.append(displayName.text)
		self.emulatorsListbox.grid(column=0, row=1, columnspan=4, sticky="NESW")
		self.emulatorsListbox.bind("<Double-Button-1>", self.editEmulator)
		self.scrollbar.config(command=self.emulatorsListbox.yview)
		self.editEmulatorLabel = ttk.Label(self.emulatorsTab, text=self.editEmulatorLabelStr)
		self.editEmulatorLabel.grid(column=0, row=2, sticky="W")
		# About tab widgets starts here.
		self.logoFile = tk.PhotoImage(file="cabrio-config.gif")
		self.logo = ttk.Label(self.aboutTab, image=self.logoFile)
		self.logo.grid(column=0, row=1, columnspan=3)
		self.aboutLabel = ttk.Label(self.aboutTab, text=self.aboutLabelStr)
		self.aboutLabel.grid(column=0, row=2, columnspan=3)
		self.versionLabel = ttk.Label(self.aboutTab, text=self.versionLabelStr)
		self.versionLabel.grid(column=0, row=3, columnspan=3)
		self.translationLabel = ttk.Label(self.aboutTab, text=self.translationLabelStr)
		self.translationLabel.grid(column=0, row=4, columnspan=3)
		self.authorLabel = ttk.Label(self.aboutTab, text=self.authorLabelStr)
		self.authorLabel.grid(column=0, row=5, columnspan=3)
		# Adjust the states
		self.updateWidget(None, "up", "device")
		self.updateWidget(None, "up", "control")
		self.updateWidget(None, "down", "device")
		self.updateWidget(None, "down", "control")
		self.updateWidget(None, "left", "device")
		self.updateWidget(None, "left", "control")
		self.updateWidget(None, "right", "device")
		self.updateWidget(None, "right", "control")
		self.updateWidget(None, "select", "device")
		self.updateWidget(None, "select", "control")
		self.updateWidget(None, "back", "device")
		self.updateWidget(None, "back", "control")
		self.updateWidget(None, "quit", "device")
		self.updateWidget(None, "quit", "control")
		self.updateWidget(None, "list1", "device")
		self.updateWidget(None, "list1", "control")
		self.updateWidget(None, "list2", "device")
		self.updateWidget(None, "list2", "control")
		self.updateWidget(None, "list3", "device")
		self.updateWidget(None, "list3", "control")
		self.updateWidget(None, "list4", "device")
		self.updateWidget(None, "list4", "control")
		self.updateWidget(None, "list5", "device")
		self.updateWidget(None, "list5", "control")
	def updateWidget(self, event, control, target):
		if control == "up":
			x = self.upDeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.upValueCombobox["values"] = self.SDLkeys
					self.upControlTypeCombobox["values"] = self.kbTypes
					self.upControlTypeCombobox.state(["disabled"])
					self.upControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.upControlTypeCombobox.set("Default")
						self.upValueCombobox.set("up")
				elif x == "mouse":
					self.upValueCombobox["values"] = self.SDLcardinals
					self.upControlTypeCombobox["values"] = self.mouseTypes
					self.upControlTypeCombobox.state(["!disabled"])
					self.upControlIdSpinbox["state"] = "normal"
					if event != None:
						self.upControlTypeCombobox.set("axis")
						self.upValueCombobox.set("up")
				elif x == "joystick":
					self.upValueCombobox["values"] = self.SDLpolarity
					self.upControlTypeCombobox["values"] = self.joyTypes
					self.upControlTypeCombobox.state(["!disabled"])
					self.upControlIdSpinbox["state"] = "normal"
					if event != None:
						self.upControlTypeCombobox.set("axis")
						self.upValueCombobox.set("plus")
			elif target == "control":
				y = self.upControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.upValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.upValueCombobox.set("plus")
					elif x == "mouse":
						self.upValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.upValueCombobox.set("up")
				elif y == "button":
					self.upValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.upValueCombobox.set("1")
				elif y == "hat":
					self.upValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.upValueCombobox.set("up")
				elif y == "ball":
					self.upValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.upValueCombobox.set("up")
		elif control == "down":
			x = self.downDeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.downValueCombobox["values"] = self.SDLkeys
					self.downControlTypeCombobox["values"] = self.kbTypes
					self.downControlTypeCombobox.state(["disabled"])
					self.downControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.downControlTypeCombobox.set("Default")
						self.downValueCombobox.set("down")
				elif x == "mouse":
					self.downValueCombobox["values"] = self.SDLcardinals
					self.downControlTypeCombobox["values"] = self.mouseTypes
					self.downControlTypeCombobox.state(["!disabled"])
					self.downControlIdSpinbox["state"] = "normal"
					if event != None:
						self.downControlTypeCombobox.set("axis")
						self.downValueCombobox.set("down")
				elif x == "joystick":
					self.downValueCombobox["values"] = self.SDLpolarity
					self.downControlTypeCombobox["values"] = self.joyTypes
					self.downControlTypeCombobox.state(["!disabled"])
					self.downControlIdSpinbox["state"] = "normal"
					if event != None:
						self.downControlTypeCombobox.set("axis")
						self.downValueCombobox.set("minus")
			elif target == "control":
				y = self.downControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.downValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.downValueCombobox.set("minus")
					elif x == "mouse":
						self.downValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.downValueCombobox.set("down")
				elif y == "button":
					self.downValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.downValueCombobox.set("1}2")
				elif y == "hat":
					self.downValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.downValueCombobox.set("down")
				elif y == "ball":
					self.downValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.downValueCombobox.set("down")
		elif control == "left":
			x = self.leftDeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.leftValueCombobox["values"] = self.SDLkeys
					self.leftControlTypeCombobox["values"] = self.kbTypes
					self.leftControlTypeCombobox.state(["disabled"])
					self.leftControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.leftControlTypeCombobox.set("Default")
						self.leftValueCombobox.set("left")
				elif x == "mouse":
					self.leftValueCombobox["values"] = self.SDLcardinals
					self.leftControlTypeCombobox["values"] = self.mouseTypes
					self.leftControlTypeCombobox.state(["!disabled"])
					self.leftControlIdSpinbox["state"] = "normal"
					if event != None:
						self.leftControlTypeCombobox.set("axis")
						self.leftValueCombobox.set("left")
				elif x == "joystick":
					self.leftValueCombobox["values"] = self.SDLpolarity
					self.leftControlTypeCombobox["values"] = self.joyTypes
					self.leftControlTypeCombobox.state(["!disabled"])
					self.leftControlIdSpinbox["state"] = "normal"
					if event != None:
						self.leftControlTypeCombobox.set("axis")
						self.leftValueCombobox.set("plus")
			elif target == "control":
				y = self.leftControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.leftValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.leftValueCombobox.set("plus")
					elif x == "mouse":
						self.leftValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.leftValueCombobox.set("left")
				elif y == "button":
					self.leftValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.leftValueCombobox.set("3")
				elif y == "hat":
					self.leftValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.leftValueCombobox.set("left")
				elif y == "ball":
					self.leftValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.leftValueCombobox.set("left")
		elif control == "right":
			x = self.rightDeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.rightValueCombobox["values"] = self.SDLkeys
					self.rightControlTypeCombobox["values"] = self.kbTypes
					self.rightControlTypeCombobox.state(["disabled"])
					self.rightControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.rightControlTypeCombobox.set("Default")
						self.rightValueCombobox.set("right")
				elif x == "mouse":
					self.rightValueCombobox["values"] = self.SDLcardinals
					self.rightControlTypeCombobox["values"] = self.mouseTypes
					self.rightControlTypeCombobox.state(["!disabled"])
					self.rightControlIdSpinbox["state"] = "normal"
					if event != None:
						self.rightControlTypeCombobox.set("axis")
						self.rightValueCombobox.set("right")
				elif x == "joystick":
					self.rightValueCombobox["values"] = self.SDLpolarity
					self.rightControlTypeCombobox["values"] = self.joyTypes
					self.rightControlTypeCombobox.state(["!disabled"])
					self.rightControlIdSpinbox["state"] = "normal"
					if event != None:
						self.rightControlTypeCombobox.set("axis")
						self.rightValueCombobox.set("minus")
			elif target == "control":
				y = self.rightControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.rightValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.rightValueCombobox.set("minus")
					elif x == "mouse":
						self.rightValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.rightValueCombobox.set("right")
				elif y == "button":
					self.rightValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.rightValueCombobox.set("4")
				elif y == "hat":
					self.rightValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.rightValueCombobox.set("right")
				elif y == "ball":
					self.rightValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.rightValueCombobox.set("right")
		elif control == "select":
			x = self.selectDeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.selectValueCombobox["values"] = self.SDLkeys
					self.selectControlTypeCombobox["values"] = self.kbTypes
					self.selectControlTypeCombobox.state(["disabled"])
					self.selectControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.selectControlTypeCombobox.set("Default")
						self.selectValueCombobox.set("return")
				elif x == "mouse":
					self.selectValueCombobox["values"] = self.SDLcardinals
					self.selectControlTypeCombobox["values"] = self.mouseTypes
					self.selectControlTypeCombobox.state(["!disabled"])
					self.selectControlIdSpinbox["state"] = "normal"
					if event != None:
						self.selectControlTypeCombobox.set("button")
						self.selectValueCombobox.set("1")
				elif x == "joystick":
					self.selectValueCombobox["values"] = self.SDLpolarity
					self.selectControlTypeCombobox["values"] = self.joyTypes
					self.selectControlTypeCombobox.state(["!disabled"])
					self.selectControlIdSpinbox["state"] = "normal"
					if event != None:
						self.selectControlTypeCombobox.set("button")
						self.selectValueCombobox.set("1")
			elif target == "control":
				y = self.selectControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.selectValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.selectValueCombobox.set("plus")
					elif x == "mouse":
						self.selectValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.selectValueCombobox.set("up")
				elif y == "button":
					self.selectValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.selectValueCombobox.set("1")
				elif y == "hat":
					self.selectValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.selectValueCombobox.set("up")
				elif y == "ball":
					self.selectValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.selectValueCombobox.set("up")
		elif control == "back":
			x = self.backDeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.backValueCombobox["values"] = self.SDLkeys
					self.backControlTypeCombobox["values"] = self.kbTypes
					self.backControlTypeCombobox.state(["disabled"])
					self.backControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.backControlTypeCombobox.set("Default")
						self.backValueCombobox.set("backspace")
				elif x == "mouse":
					self.backValueCombobox["values"] = self.SDLcardinals
					self.backControlTypeCombobox["values"] = self.mouseTypes
					self.backControlTypeCombobox.state(["!disabled"])
					self.backControlIdSpinbox["state"] = "normal"
					if event != None:
						self.backControlTypeCombobox.set("button")
						self.backValueCombobox.set("2")
				elif x == "joystick":
					self.backValueCombobox["values"] = self.SDLpolarity
					self.backControlTypeCombobox["values"] = self.joyTypes
					self.backControlTypeCombobox.state(["!disabled"])
					self.backControlIdSpinbox["state"] = "normal"
					if event != None:
						self.backControlTypeCombobox.set("button")
						self.backValueCombobox.set("2")
			elif target == "control":
				y = self.backControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.backValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.backValueCombobox.set("plus")
					elif x == "mouse":
						self.backValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.backValueCombobox.set("left")
				elif y == "button":
					self.backValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.backValueCombobox.set("1")
				elif y == "hat":
					self.backValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.backValueCombobox.set("left")
				elif y == "ball":
					self.backValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.backValueCombobox.set("left")
		elif control == "quit":
			x = self.quitDeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.quitValueCombobox["values"] = self.SDLkeys
					self.quitControlTypeCombobox["values"] = self.kbTypes
					self.quitControlTypeCombobox.state(["disabled"])
					self.quitControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.quitControlTypeCombobox.set("Default")
						self.quitValueCombobox.set("escape")
				elif x == "mouse":
					self.quitValueCombobox["values"] = self.SDLcardinals
					self.quitControlTypeCombobox["values"] = self.mouseTypes
					self.quitControlTypeCombobox.state(["!disabled"])
					self.quitControlIdSpinbox["state"] = "normal"
					if event != None:
						self.quitControlTypeCombobox.set("button")
						self.quitValueCombobox.set("3")
				elif x == "joystick":
					self.quitValueCombobox["values"] = self.SDLpolarity
					self.quitControlTypeCombobox["values"] = self.joyTypes
					self.quitControlTypeCombobox.state(["!disabled"])
					self.quitControlIdSpinbox["state"] = "normal"
					if event != None:
						self.quitControlTypeCombobox.set("button")
						self.quitValueCombobox.set("3")
			elif target == "control":
				y = self.quitControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.quitValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.quitValueCombobox.set("plus")
					elif x == "mouse":
						self.quitValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.quitValueCombobox.set("right")
				elif y == "button":
					self.quitValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.quitValueCombobox.set("1")
				elif y == "hat":
					self.quitValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.quitValueCombobox.set("right")
				elif y == "ball":
					self.quitValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.quitValueCombobox.set("right")
		elif control == "list1":
			x = self.list1DeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.list1ValueCombobox["values"] = self.SDLkeys
					self.list1ControlTypeCombobox["values"] = self.kbTypes
					self.list1ControlTypeCombobox.state(["disabled"])
					self.list1ControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.list1ControlTypeCombobox.set("Default")
						self.list1ValueCombobox.set("LSHIFT")
				elif x == "mouse":
					self.list1ValueCombobox["values"] = self.SDLcardinals
					self.list1ControlTypeCombobox["values"] = self.mouseTypes
					self.list1ControlTypeCombobox.state(["!disabled"])
					self.list1ControlIdSpinbox["state"] = "normal"
					if event != None:
						self.list1ControlTypeCombobox.set("button")
						self.list1ValueCombobox.set("4")
				elif x == "joystick":
					self.list1ValueCombobox["values"] = self.SDLpolarity
					self.list1ControlTypeCombobox["values"] = self.joyTypes
					self.list1ControlTypeCombobox.state(["!disabled"])
					self.list1ControlIdSpinbox["state"] = "normal"
					if event != None:
						self.list1ControlTypeCombobox.set("button")
						self.list1ValueCombobox.set("4")
			elif target == "control":
				y = self.list1ControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.list1ValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.list1ValueCombobox.set("plus")
					elif x == "mouse":
						self.list1ValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.list1ValueCombobox.set("right")
				elif y == "button":
					self.list1ValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.list1ValueCombobox.set("4")
				elif y == "hat":
					self.list1ValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.list1ValueCombobox.set("right")
				elif y == "ball":
					self.list1ValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.list1ValueCombobox.set("right")
		elif control == "list2":
			x = self.list2DeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.list2ValueCombobox["values"] = self.SDLkeys
					self.list2ControlTypeCombobox["values"] = self.kbTypes
					self.list2ControlTypeCombobox.state(["disabled"])
					self.list2ControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.list2ControlTypeCombobox.set("Default")
						self.list2ValueCombobox.set("LCTRL")
				elif x == "mouse":
					self.list2ValueCombobox["values"] = self.SDLcardinals
					self.list2ControlTypeCombobox["values"] = self.mouseTypes
					self.list2ControlTypeCombobox.state(["!disabled"])
					self.list2ControlIdSpinbox["state"] = "normal"
					if event != None:
						self.list2ControlTypeCombobox.set("button")
						self.list2ValueCombobox.set("5")
				elif x == "joystick":
					self.list2ValueCombobox["values"] = self.SDLpolarity
					self.list2ControlTypeCombobox["values"] = self.joyTypes
					self.list2ControlTypeCombobox.state(["!disabled"])
					self.list2ControlIdSpinbox["state"] = "normal"
					if event != None:
						self.list2ControlTypeCombobox.set("button")
						self.list2ValueCombobox.set("5")
			elif target == "control":
				y = self.list2ControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.list2ValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.list2ValueCombobox.set("plus")
					elif x == "mouse":
						self.list2ValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.list2ValueCombobox.set("right")
				elif y == "button":
					self.list2ValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.list2ValueCombobox.set("5")
				elif y == "hat":
					self.list2ValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.list2ValueCombobox.set("right")
				elif y == "ball":
					self.list2ValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.list2ValueCombobox.set("right")
		elif control == "list3":
			x = self.list3DeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.list3ValueCombobox["values"] = self.SDLkeys
					self.list3ControlTypeCombobox["values"] = self.kbTypes
					self.list3ControlTypeCombobox.state(["disabled"])
					self.list3ControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.list3ControlTypeCombobox.set("Default")
						self.list3ValueCombobox.set("LALT")
				elif x == "mouse":
					self.list3ValueCombobox["values"] = self.SDLcardinals
					self.list3ControlTypeCombobox["values"] = self.mouseTypes
					self.list3ControlTypeCombobox.state(["!disabled"])
					self.list3ControlIdSpinbox["state"] = "normal"
					if event != None:
						self.list3ControlTypeCombobox.set("button")
						self.list3ValueCombobox.set("5")
				elif x == "joystick":
					self.list3ValueCombobox["values"] = self.SDLpolarity
					self.list3ControlTypeCombobox["values"] = self.joyTypes
					self.list3ControlTypeCombobox.state(["!disabled"])
					self.list3ControlIdSpinbox["state"] = "normal"
					if event != None:
						self.list3ControlTypeCombobox.set("button")
						self.list3ValueCombobox.set("5")
			elif target == "control":
				y = self.list3ControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.list3ValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.list3ValueCombobox.set("plus")
					elif x == "mouse":
						self.list3ValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.list3ValueCombobox.set("right")
				elif y == "button":
					self.list3ValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.list3ValueCombobox.set("5")
				elif y == "hat":
					self.list3ValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.list3ValueCombobox.set("right")
				elif y == "ball":
					self.list3ValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.list3ValueCombobox.set("right")
		elif control == "list4":
			x = self.list4DeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.list4ValueCombobox["values"] = self.SDLkeys
					self.list4ControlTypeCombobox["values"] = self.kbTypes
					self.list4ControlTypeCombobox.state(["disabled"])
					self.list4ControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.list4ControlTypeCombobox.set("Default")
						self.list4ValueCombobox.set("space")
				elif x == "mouse":
					self.list4ValueCombobox["values"] = self.SDLcardinals
					self.list4ControlTypeCombobox["values"] = self.mouseTypes
					self.list4ControlTypeCombobox.state(["!disabled"])
					self.list4ControlIdSpinbox["state"] = "normal"
					if event != None:
						self.list4ControlTypeCombobox.set("button")
						self.list4ValueCombobox.set("5")
				elif x == "joystick":
					self.list4ValueCombobox["values"] = self.SDLpolarity
					self.list4ControlTypeCombobox["values"] = self.joyTypes
					self.list4ControlTypeCombobox.state(["!disabled"])
					self.list4ControlIdSpinbox["state"] = "normal"
					if event != None:
						self.list4ControlTypeCombobox.set("button")
						self.list4ValueCombobox.set("5")
			elif target == "control":
				y = self.list4ControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.list4ValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.list4ValueCombobox.set("plus")
					elif x == "mouse":
						self.list4ValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.list4ValueCombobox.set("right")
				elif y == "button":
					self.list4ValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.list4ValueCombobox.set("5")
				elif y == "hat":
					self.list4ValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.list4ValueCombobox.set("right")
				elif y == "ball":
					self.list4ValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.list4ValueCombobox.set("right")
		elif control == "list5":
			x = self.list5DeviceTypeCombobox.get()
			if target == "device":
				if x == "keyboard":
					self.list5ValueCombobox["values"] = self.SDLkeys
					self.list5ControlTypeCombobox["values"] = self.kbTypes
					self.list5ControlTypeCombobox.state(["disabled"])
					self.list5ControlIdSpinbox["state"] = "disabled"
					if event != None:
						self.list5ControlTypeCombobox.set("Default")
						self.list5ValueCombobox.set("RALT")
				elif x == "mouse":
					self.list5ValueCombobox["values"] = self.SDLcardinals
					self.list5ControlTypeCombobox["values"] = self.mouseTypes
					self.list5ControlTypeCombobox.state(["!disabled"])
					self.list5ControlIdSpinbox["state"] = "normal"
					if event != None:
						self.list5ControlTypeCombobox.set("button")
						self.list5ValueCombobox.set("5")
				elif x == "joystick":
					self.list5ValueCombobox["values"] = self.SDLpolarity
					self.list5ControlTypeCombobox["values"] = self.joyTypes
					self.list5ControlTypeCombobox.state(["!disabled"])
					self.list5ControlIdSpinbox["state"] = "normal"
					if event != None:
						self.list5ControlTypeCombobox.set("button")
						self.list5ValueCombobox.set("5")
			elif target == "control":
				y = self.list5ControlTypeCombobox.get()
				if y == "axis":
					if x == "joystick":
						self.list5ValueCombobox["values"] = self.SDLpolarity
						if event != None:
							self.list5ValueCombobox.set("plus")
					elif x == "mouse":
						self.list5ValueCombobox["values"] = self.SDLcardinals
						if event != None:
							self.list5ValueCombobox.set("right")
				elif y == "button":
					self.list5ValueCombobox["values"] = self.SDLbuttons
					if event != None:
						self.list5ValueCombobox.set("5")
				elif y == "hat":
					self.list5ValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.list5ValueCombobox.set("right")
				elif y == "ball":
					self.list5ValueCombobox["values"] = self.SDLcardinals
					if event != None:
						self.list5ValueCombobox.set("right")
	def editEmulator(self, option=None):
		self.displayName = tk.StringVar()
		self.displayName.set(self.emulatorsListbox.get("active"))
		for lang in self.root.findall(".//*[@code='"+self.lang+"']"):
			self.newEmulatorTitleStr = lang.find("newEmulatorTitle").text
			self.browseEmulatorLabelStr = lang.find("browseEmulatorLabel").text
			# self.createScriptLabelStr = lang.find("createScriptLabel").text
			# self.createScriptButtonStr = lang.find("createScriptButton").text
			self.emulatorNameLabelStr = lang.find("emulatorNameLabel").text
			self.emulatorDisplayNameLabelStr = lang.find("emulatorDisplayNameLabel").text
			self.emulatorPlatformLabelStr = lang.find("emulatorPlatformLabel").text
			self.editTitleStr = lang.find("editTitle").text
			self.extraLabelStr = lang.find("extraLabel").text
			self.addParameterStr = lang.find("addParameter").text
			self.delParameterStr = lang.find("delParameter").text
			self.saveButtonStr = lang.find("saveButton").text
			self.cancelButtonStr = lang.find("cancelButton").text
			self.deleteButtonStr = lang.find("deleteButton").text
			self.errorNoDisplayNameStr = lang.find("errorNoDisplayName").text
			self.errorNoPlatformStr = lang.find("errorNoPlatform").text
			self.errorNoExecutableStr = lang.find("errorNoExecutable").text
			self.errorNoParameterStr = lang.find("errorNoParameter").text
			self.confirmDeleteLabelStr = lang.find("confirmDeleteLabel").text
			self.okButtonStr = lang.find("okButton").text
			self.browseExecLabelStr = lang.find("browseExecLabel").text
		self.toplevel = tk.Toplevel(self.emulatorsTab)
		self.wait_visibility(self.toplevel)
		self.toplevel.grab_set()
		self.frame = ttk.Frame(self.toplevel, borderwidth=10)
		self.frame.grid()
		self.emulatorNameLabel = ttk.Label(self.frame, text=self.emulatorNameLabelStr)
		self.emulatorNameLabel.grid(column=0, row=0, sticky="W")
		self.emulatorNameEntry = ttk.Entry(self.frame)
		self.emulatorNameEntry.grid(column=1, row=0, sticky="W", columnspan=3)
		self.emulatorDisplayNameLabel = ttk.Label(self.frame, text=self.emulatorDisplayNameLabelStr)
		self.emulatorDisplayNameLabel.grid(column=0, row=1, sticky="W")
		self.emulatorDisplayNameEntry = ttk.Entry(self.frame)
		self.emulatorDisplayNameEntry.grid(column=1, row=1, sticky="W", columnspan=3)
		self.emulatorPlatformLabel = ttk.Label(self.frame, text=self.emulatorPlatformLabelStr)
		self.emulatorPlatformLabel.grid(column=0, row=2, sticky="W")
		self.emulatorPlatformEntry = ttk.Entry(self.frame)
		self.emulatorPlatformEntry.grid(column=1, row=2, sticky="W", columnspan=3)
		self.browseEmulatorLabel = ttk.Label(self.frame, text=self.browseEmulatorLabelStr)
		self.browseEmulatorLabel.grid(column=0, row=3, columnspan=2, sticky="W")
		self.emulatorExecEntry = ttk.Entry(self.frame)
		self.emulatorExecEntry.grid(column=0, row=4, sticky="W")
		self.emulatorExecButton = ttk.Button(self.frame, text=self.browseButtonStr, command=lambda a=self.emulatorExecEntry: self.getFile(a))
		self.emulatorExecButton.grid(column=1, row=4, sticky="W", columnspan=3)
		# self.createScriptLabel = ttk.Label(self.frame, text=self.createScriptLabelStr)
		# self.createScriptLabel.grid(column=0, row=5, sticky="W")
		# self.createScriptButton = ttk.Button(self.frame, text=self.createScriptButtonStr)
		# self.createScriptButton.grid(column=1, row=5, sticky="W")
		self.parametersLabel = ttk.Label(self.frame, text=self.extraLabelStr)
		self.parametersLabel.grid(column=0, row=6, sticky="W")
		self.addParameter = ttk.Button(self.frame, text=self.addParameterStr, command=lambda: self.addParam())
		self.addParameter.grid(column=1, row=6, sticky="W", columnspan=3)
		self.index = None
		self.parameters = []
		self.deleteParameters = []
		self.parametersVar = []
		self.statusVar = tk.StringVar()
		self.statusVar.set("")
		if option != "new":
			self.toplevel.title(self.editTitleStr)
			self.index = -1
			for item in self.configRoot.findall(".//emulator"):
				displayName = item.find("display-name")
				if displayName.text == self.displayName.get():
					self.element = item
					name = item.find("name")
					executable = item.find("executable")
					self.emulatorNameEntry.insert(0, name.text)
					self.emulatorNameEntry.configure(state="disabled")
					self.emulatorDisplayNameEntry.insert(0, displayName.text)
					self.emulatorExecEntry.insert(0, executable.text)
					try:
						platform = item.find("platform")
					except:
						platform = None
					if platform != None:
						self.emulatorPlatformEntry.insert(0, platform.text)
					try:
						params = item.find("params")
					except:
						params = None
					if params != None:
						for param in params.findall("param/name"):
							self.index = self.index + 1
							tempText = tk.StringVar()
							tempText.set(param.text)
							self.parametersVar.append(tempText)

							tempEntry = ttk.Entry(self.frame)
							tempEntry.insert(0, tempText.get())
							tempEntry.grid(column=0, row=self.index + 7, sticky="W")
							self.parameters.append(tempEntry)
							tempDelete = ttk.Button(self.frame, text=self.delParameterStr, command=lambda a=self.index, b=option: self.removeParam(a, b))
							tempDelete.grid(column=1, row=self.index + 7, sticky="W", columnspan=3)
							self.deleteParameters.append(tempDelete)
		else:
			self.toplevel.title(self.newEmulatorTitleStr)
		self.saveButton = ttk.Button(self.frame, text=self.saveButtonStr, command=lambda: self.checkEmuChanges())
		self.saveButton.grid(column=0, row=99, columnspan=1)
		if option != "new":
			self.deleteButton = ttk.Button(self.frame, text=self.deleteButtonStr, command=lambda: self.confirmDelete())
			self.deleteButton.grid(column=1, row=99, columnspan=1)
		self.cancelButton = ttk.Button(self.frame, text=self.cancelButtonStr, command=lambda: self.closeWindow())
		self.cancelButton.grid(column=2, row=99, columnspan=2)
		self.separator = ttk.Separator(self.frame, orient="horizontal")
		self.separator.grid(column=0, row=100, columnspan=4, sticky="EW")
		self.statusLabel = ttk.Label(self.frame, textvariable=self.statusVar)
		self.statusLabel.grid(column=0, row=101, columnspan=4, sticky="W")
	def confirmDelete(self):
		self.closeWindow()
		self.toplevel = tk.Toplevel(self.emulatorsTab)
		self.wait_visibility(self.toplevel)
		self.toplevel.grab_set()
		self.frame = ttk.Frame(self.toplevel, borderwidth=10)
		self.frame.grid()
		self.confirmDeleteLabel = ttk.Label(self.frame, text=self.confirmDeleteLabelStr)
		self.confirmDeleteLabel.grid(column=0, row=0, columnspan=2)
		self.confirmButton = ttk.Button(self.frame, text=self.okButtonStr, command=lambda: self.deleteEmulator())
		self.confirmButton.grid(column=0, row=1)
		self.cancelButton = ttk.Button(self.frame, text=self.cancelButtonStr, command=lambda: self.closeWindow())
		self.cancelButton.grid(column=1, row=1)
	def deleteEmulator(self):
		self.closeWindow()
		name = self.emulatorsListbox.get("active")
		emulators = self.configRoot.find(".//emulators")
		for item in emulators.findall(".//emulator"):
			displayName = item.find("display-name")
			if name == displayName.text:
				emulators.remove(item)
				self.emulatorsListbox.delete("active")
				self.emulatorsList.remove(name)
				self.configTree.write(self.path + "config.xml")
	def checkEmuChanges(self):
		name = self.emulatorNameEntry.get()
		displayName = self.emulatorDisplayNameEntry.get()
		platform = self.emulatorPlatformEntry.get()
		executable = self.emulatorExecEntry.get()
		if name == "":
			self.statusVar.set(self.errorNoNameStr)
		elif displayName == "":
			self.statusVar.set(self.errorNoDisplayNameStr)
		elif platform == "":
			self.statusVar.set(self.errorNoPlatformStr)
		elif executable == "":
			self.statusVar.set(self.errorNoExecutableStr)
		else:
			if self.parameters != []:
				count = 0
				for parameter in self.parameters:
					count = count + 1
					if parameter.get() == "":
						self.statusVar.set(self.errorNoParameterStr)
					else:
						if len(self.parameters) == count:
							self.saveEmuChanges()
			else:
				self.saveEmuChanges()
	def saveEmuChanges(self):
		try:
			# Test if the element exists
			self.element
		except:
			# If the element doesn't exist, create it
			emulators = self.configTree.find(".//emulators")
			self.element = ET.SubElement(emulators, "emulator")
		if self.element.find("name") == None:
			name = ET.SubElement(self.element, "name")
		else:
			name = self.element.find("name")
		name.text = self.emulatorNameEntry.get()
		if self.element.find("display-name") == None:
			displayName = ET.SubElement(self.element, "display-name")
		else:
			displayName = self.element.find("display-name")
		displayName.text = self.emulatorDisplayNameEntry.get()
		if self.element.find("executable") == None:
			executable = ET.SubElement(self.element, "executable")
		else:
			executable = self.element.find("executable")
		executable.text = self.emulatorExecEntry.get()
		if self.element.find("platform") == None:
			platform = ET.SubElement(self.element, "platform")
		else:
			platform = self.element.find("platform")
		platform.text = self.emulatorPlatformEntry.get()
		if self.parameters != []:
			if self.emulatorNameEntry.instate(["disabled"]):
				for item in self.configRoot.findall(".//emulator"):
					emulator = item.find("name")
					if emulator.text == self.emulatorNameEntry.get():
						params = item.find("params")
						try:
							item.remove(params)
						except:
							pass
						params = ET.SubElement(item, "params")
						for p in self.parameters:
							param = ET.SubElement(params, "param")
							paramName = ET.SubElement(param, "name")
							paramName.text = p.get()
			else:
				params = ET.SubElement(self.element, "params")
				for p in self.parameters:
					param = ET.SubElement(params, "param")
					paramName = ET.SubElement(param, "name")
					paramName.text = p.get()
		else:
			for item in self.configRoot.findall(".//emulator"):
				emulator = item.find("name")
				if emulator.text == self.emulatorNameEntry.get():
					params = item.find("params")
					try:
						item.remove(params)
					except:
						pass
		self.indent(self.configRoot)
		self.configTree.write(self.path + "config.xml")
		if not displayName.text in self.emulatorsList:
			self.emulatorsListbox.insert("end", displayName.text)
		self.closeWindow()
	def saveControlsChange(self):
		self.upValue.text = self.upValueCombobox.get()
		self.upDeviceType.text = self.upDeviceTypeCombobox.get()
		self.upDeviceId.text = self.upDeviceIdSpinbox.get()
		self.upControlType.text = self.upControlTypeCombobox.get()
		self.upControlId.text = self.upControlIdSpinbox.get()
		self.downValue.text = self.downValueCombobox.get()
		self.downDeviceType.text = self.downDeviceTypeCombobox.get()
		self.downDeviceId.text = self.downDeviceIdSpinbox.get()
		self.downControlType.text = self.downControlTypeCombobox.get()
		self.downControlId.text = self.downControlIdSpinbox.get()
		self.leftValue.text = self.leftValueCombobox.get()
		self.leftDeviceType.text = self.leftDeviceTypeCombobox.get()
		self.leftDeviceId.text = self.leftDeviceIdSpinbox.get()
		self.leftControlType.text = self.leftControlTypeCombobox.get()
		self.leftControlId.text = self.leftControlIdSpinbox.get()
		self.rightValue.text = self.rightValueCombobox.get()
		self.rightDeviceType.text = self.rightDeviceTypeCombobox.get()
		self.rightDeviceId.text = self.rightDeviceIdSpinbox.get()
		self.rightControlType.text = self.rightControlTypeCombobox.get()
		self.rightControlId.text = self.rightControlIdSpinbox.get()
		self.selectValue.text = self.selectValueCombobox.get()
		self.selectDeviceType.text = self.selectDeviceTypeCombobox.get()
		self.selectDeviceId.text = self.selectDeviceIdSpinbox.get()
		self.selectControlType.text = self.selectControlTypeCombobox.get()
		self.selectControlId.text = self.selectControlIdSpinbox.get()
		self.backValue.text = self.backValueCombobox.get()
		self.backDeviceType.text = self.backDeviceTypeCombobox.get()
		self.backDeviceId.text = self.backDeviceIdSpinbox.get()
		self.backControlType.text = self.backControlTypeCombobox.get()
		self.backControlId.text = self.backControlIdSpinbox.get()
		self.quitValue.text = self.quitValueCombobox.get()
		self.quitDeviceType.text = self.quitDeviceTypeCombobox.get()
		self.quitDeviceId.text = self.quitDeviceIdSpinbox.get()
		self.quitControlType.text = self.quitControlTypeCombobox.get()
		self.quitControlId.text = self.quitControlIdSpinbox.get()
		self.list1Value.text = self.list1ValueCombobox.get()
		self.list1DeviceType.text = self.list1DeviceTypeCombobox.get()
		self.list1DeviceId.text = self.list1DeviceIdSpinbox.get()
		self.list1ControlType.text = self.list1ControlTypeCombobox.get()
		self.list1ControlId.text = self.list1ControlIdSpinbox.get()
		self.list2Value.text = self.list2ValueCombobox.get()
		self.list2DeviceType.text = self.list2DeviceTypeCombobox.get()
		self.list2DeviceId.text = self.list2DeviceIdSpinbox.get()
		self.list2ControlType.text = self.list2ControlTypeCombobox.get()
		self.list2ControlId.text = self.list2ControlIdSpinbox.get()
		self.list3Value.text = self.list3ValueCombobox.get()
		self.list3DeviceType.text = self.list3DeviceTypeCombobox.get()
		self.list3DeviceId.text = self.list3DeviceIdSpinbox.get()
		self.list3ControlType.text = self.list3ControlTypeCombobox.get()
		self.list3ControlId.text = self.list3ControlIdSpinbox.get()
		self.list4Value.text = self.list4ValueCombobox.get()
		self.list4DeviceType.text = self.list4DeviceTypeCombobox.get()
		self.list4DeviceId.text = self.list4DeviceIdSpinbox.get()
		self.list4ControlType.text = self.list4ControlTypeCombobox.get()
		self.list4ControlId.text = self.list4ControlIdSpinbox.get()
		self.list5Value.text = self.list5ValueCombobox.get()
		self.list5DeviceType.text = self.list5DeviceTypeCombobox.get()
		self.list5DeviceId.text = self.list5DeviceIdSpinbox.get()
		self.list5ControlType.text = self.list5ControlTypeCombobox.get()
		self.list5ControlId.text = self.list5ControlIdSpinbox.get()
		self.indent(self.configRoot)
		self.configTree.write(self.path + "config.xml")
	def closeWindow(self):
		self.toplevel.grab_release()
		self.toplevel.destroy()
	def addParam(self, option=None):
		if self.index == None:
			self.index = 0
		else:
			self.index = len(self.parameters)
		tempEntry = ttk.Entry(self.frame)
		tempEntry.grid(column=0, row=self.index + 8, sticky="W")
		self.parameters.append(tempEntry)
		tempDelete = ttk.Button(self.frame, text=self.delParameterStr, command=lambda a=self.index, b=option: self.removeParam(a, b))
		tempDelete.grid(column=1, row=self.index + 8, sticky="W")
		self.deleteParameters.append(tempDelete)
	def removeParam(self, index, option=None):
		self.parameters[index].destroy()
		self.parameters.pop(index)
		self.deleteParameters[index].destroy()
		self.deleteParameters.pop(index)
	def writeInt(self, node, var):
		node.text = str(var.get())
		self.configTree.write(self.path + 'config.xml')
	def writeFloat(self, event, node, var):
		node.text = str(int(var.get()))
		self.configTree.write(self.path + 'config.xml')
	def writeBool(self, node, var):
		if var.get() == 1:
			node.text = "true"
		elif var.get() == 0:
			node.text = "false"
		self.configTree.write(self.path + 'config.xml')
	def writeString(self, node1, var1, node2=None, var2=None):
		node1.text = var1.get()
		if node2 != None: # For resolution it is necessary to save 2 values.
			node2.text = var2.get()
		self.configTree.write(self.path + 'config.xml')
	def writeTheme(self, event):
		current = self.themesCombobox.current()
		selected = self.themesList[current]
		self.theme.text = selected
		self.configTree.write(self.path + 'config.xml')
	def setControlList(self, var):
		a = var.get()
		if a == "keyboard":
			b = self.kbTypes
		elif a == "joystick":
			b = self.joyTypes
		elif a == "mouse":
			b = self.mouseTypes
		return b
	def setValueList(self, a, b):
		if a == "keyboard":
			c = self.SDLkeys
		elif a == "joystick":
			if b == "hat":
				c = self.SDLcardinals
			elif b == "axis":
				c = self.SDLpolarity
			elif b == "button":
				c = self.SDLbuttons
			elif b == "ball":
				c = self.SDLcardinals
		elif a == "mouse":
			if b == "axis":
				c = self.SDLcardinals
			elif b == "button":
				c = self.SDLbuttons
		return c
	def setVar(self, node, sourceType):
		if sourceType == str:
			var = tk.StringVar()
			var.set(node.text)
		elif sourceType == bool:
			var = tk.IntVar()
			if node.text == "true":
				var.set(1)
			elif node.text == "false":
				var.set(0)
		elif sourceType == int:
			var = tk.IntVar()
			var.set(int(node.text))
		elif sourceType == float:
			var = tk.DoubleVar()
			var.set(float(node.text))
		return var
	def updateControl(self, control, valueWidget, deviceWidget, deviceIdVar, controlWidget, controlIdVar):
		# Get control
		t = control.find("E =") + 4 # Store the position of the value
		y = int(control[t:t+2]) # extract the value and convert it to number
		t = control.find("s =") + 4
		a = int(control[t:t+1])
		controlIdVar.set(a)
		t = control.find("joystick")
		if t > -1:
			i = t + 8 # Get the position of the ID in the string
			deviceWidget.set("joystick")
			u = control.find("hat")
			if u > -1:
				f = control.find("down:")
				if f > -1:
					fix = "down"
				else :
					f = control.find("right")
					if f > -1:
						fix = "right"
					else:
						fix = None
 				controlWidget.set("hat")
				z = self.translateValue(y, "joystick", "hat", fix)
				valueWidget.set(z)
			u = control.find(" axis")
			if u > -1:
				controlWidget.set("axis")
				z = self.translateValue(y, "joystick", "axis")
				valueWidget.set(z)
			u = control.find("button")
			if u > -1:
				controlWidget.set("button")
				z = self.translateValue(y, "joystick", "button")
				valueWidget.set(z)
			u = control.find("ball")
			if u > -1:
				controlWidget.set("ball")
				z = self.translateValue(y, "joystick", "ball")
				valueWidget.set(z)
		t = control.find("mouse")
		if t > -1:
			i = t + 5 # Get the position of the ID in the string
			deviceWidget.set("mouse")
			u = control.find(" axis")
			if u > -1:
				controlWidget.set("axis")
				z = self.translateValue(y, "mouse", "axis")
				valueWidget.set(z)
			u = control.find("button")
			if u > -1:
				controlWidget.set("button")
				z = self.translateValue(y, "mouse", "button")
				valueWidget.set(z)
		t = control.find("keyboard")
		if t > -1:
			i = t + 8 # Get the position of the ID in the string
			deviceWidget.set("keyboard")
			controlWidget.set("Default")
			z = self.translateValue(y, "keyboard")
			valueWidget.set(z)
		# Get id
		x = control[i]
		deviceIdVar.set(x)
	def translateValue(self, value, device, type=None, fix=None):
		if device == "joystick":
			if type == "hat":
				if value == 0:
					v = fix
				elif value == 1:
					v = "up"
				elif value == 2:
					v = "down"
				elif value == 3:
					v = "left"
				elif value == 4:
					v = "right"
			elif type == "axis":
				if value == 0:
					v = "error"
				elif value == 1:
					v = "plus"
				elif value == -1:
					v = "minus"
			elif type == "button":
				v = value
			elif type == "ball":
				if value == 0:
					v = "error"
				elif value == 1:
					v = "up"
				elif value == 2:
					v = "down"
				elif value == 3:
					v = "left"
				elif value == 4:
					v = "right"
		elif device == "mouse":
			if type == "axis":
				if value == 0:
					v = "error"
				elif value == 1:
					v = "up"
				elif value == 2:
					v = "down"
				elif value == 3:
					v = "left"
				elif value == 4:
					v = "right"
			elif type == "button":
				v = value
		elif device == "keyboard":
			if value == 0:
				v = "Unknown"
			elif value == 8:
				v = "backspace"
			elif value == 9:
				v = "tab"
			elif value == 13:
				v = "return"
			elif value == 27:
				v = "escape"
			elif value == 32:
				v = "space"
			elif value == 33:
				v = "exclaim"
			elif value == 34:
				v = "quotedbl"
			elif value == 35:
				v = "hash"
			elif value == 36:
				v = "dollar"
			elif value == 36:
				v = "dollar"
			elif value == 37:
				v = "percent"
			elif value == 38:
				v = "ampersand"
			elif value == 39:
				v = "quote"
			elif value == 40:
				v = "leftparen"
			elif value == 41:
				v = "rightparen"
			elif value == 42:
				v = "asterisk"
			elif value == 43:
				v = "plus"
			elif value == 44:
				v = "comma"
			elif value == 45:
				v = "minus"
			elif value == 46:
				v = "period"
			elif value == 47:
				v = "slash"
			elif value == 48:
				v = "0"
			elif value == 49:
				v = "1"
			elif value == 50:
				v = "2"
			elif value == 51:
				v = "3"
			elif value == 52:
				v = "4"
			elif value == 53:
				v = "5"
			elif value == 54:
				v = "6"
			elif value == 55:
				v = "7"
			elif value == 56:
				v = "8"
			elif value == 57:
				v = "9"
			elif value == 58:
				v = "colon"
			elif value == 59:
				v = "semicolon"
			elif value == 60:
				v = "less"
			elif value == 61:
				v = "equals"
			elif value == 62:
				v = "greater"
			elif value == 63:
				v = "question"
			elif value == 64:
				v = "at"
			elif value == 91:
				v = "leftbracket"
			elif value == 92:
				v = "backslash"
			elif value == 93:
				v = "rightbracket"
			elif value == 94:
				v = "caret"
			elif value == 95:
				v = "underscore"
			elif value == 96:
				v = "backquote"
			elif value == 97:
				v = "a"
			elif value == 98:
				v = "b"
			elif value == 99:
				v = "c"
			elif value == 100:
				v = "d"
			elif value == 101:
				v = "e"
			elif value == 102:
				v = "f"
			elif value == 103:
				v = "g"
			elif value == 104:
				v = "h"
			elif value == 105:
				v = "i"
			elif value == 106:
				v = "j"
			elif value == 107:
				v = "k"
			elif value == 108:
				v = "l"
			elif value == 109:
				v = "m"
			elif value == 110:
				v = "n"
			elif value == 111:
				v = "o"
			elif value == 112:
				v = "p"
			elif value == 113:
				v = "q"
			elif value == 114:
				v = "r"
			elif value == 115:
				v = "s"
			elif value == 116:
				v = "t"
			elif value == 117:
				v = "u"
			elif value == 118:
				v = "v"
			elif value == 119:
				v = "w"
			elif value == 120:
				v = "x"
			elif value == 121:
				v = "y"
			elif value == 122:
				v = "z"
			elif value == 127:
				v = "delete"
			elif value == 301:
				v = "capslock"
			elif value == 282:
				v = "F1"
			elif value == 283:
				v = "F2"
			elif value == 284:
				v = "F3"
			elif value == 285:
				v = "F4"
			elif value == 286:
				v = "F5"
			elif value == 287:
				v = "F6"
			elif value == 288:
				v = "F7"
			elif value == 289:
				v = "F8"
			elif value == 290:
				v = "F9"
			elif value == 291:
				v = "F10"
			elif value == 292:
				v = "F11"
			elif value == 293:
				v = "F12"
			elif value == 316:
				v = "printscreen"
			elif value == 317:
				v = "scrolllock"
			elif value == 318:
				v = "pause"
			elif value == 277:
				v = "insert"
			elif value == 278:
				v = "home"
			elif value == 280:
				v = "pageup"
			elif value == 279:
				v = "end"
			elif value == 281:
				v = "pagedown"
			elif value == 275:
				v = "right"
			elif value == 276:
				v = "left"
			elif value == 274:
				v = "down"
			elif value == 273:
				v = "up"
			elif value == 300:
				v = "NUMLOCKCLEAR"
			elif value == 267:
				v = "KP_DIVIDE"
			elif value == 268:
				v = "KP_MULTIPLY"
			elif value == 269:
				v = "KP_MINUS"
			elif value == 270:
				v = "KP_PLUS"
			elif value == 271:
				v = "KP_ENTER"
			elif value == 257:
				v = "KP_1"
			elif value == 258:
				v = "KP_2"
			elif value == 259:
				v = "KP_3"
			elif value == 260:
				v = "KP_4"
			elif value == 261:
				v = "KP_5"
			elif value == 262:
				v = "KP_6"
			elif value == 263:
				v = "KP_7"
			elif value == 264:
				v = "KP_8"
			elif value == 265:
				v = "KP_9"
			elif value == 256:
				v = "KP_0"
			elif value == 266:
				v = "KP_PERIOD"
			elif value == 320:
				v = "POWER"
			elif value == 272:
				v = "KP_EQUALS"
			elif value == 294:
				v = "F13"
			elif value == 295:
				v = "F14"
			elif value == 296:
				v = "F15"
			else:
				v = "Unknown"
		return v
	def getControls(self):
		# get data from the output of the console
		p = subprocess.Popen(["cabrio-config"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		raw, err = p.communicate()
		# raw = self.SDLout
		output = raw.split("\n")
		for n in output:
			t = n.find("up:")
			if t > -1:
				self.updateControl(n, self.upValueCombobox, self.upDeviceTypeCombobox, self.upDeviceIdVar, self.upControlTypeCombobox, self.upControlIdVar)
				self.updateWidget(None, "up", "device")
				self.updateWidget(None, "up", "control")
			t = n.find("down:")
			if t > -1:
				self.updateControl(n, self.downValueCombobox, self.downDeviceTypeCombobox, self.downDeviceIdVar, self.downControlTypeCombobox, self.downControlIdVar)
				self.updateWidget(None, "down", "device")
				self.updateWidget(None, "down", "control")
			t = n.find("left:")
			if t > -1:
				self.updateControl(n, self.leftValueCombobox, self.leftDeviceTypeCombobox, self.leftDeviceIdVar, self.leftControlTypeCombobox, self.leftControlIdVar)
				self.updateWidget(None, "left", "device")
				self.updateWidget(None, "left", "control")
			t = n.find("right:")
			if t > -1:
				self.updateControl(n, self.rightValueCombobox, self.rightDeviceTypeCombobox, self.rightDeviceIdVar, self.rightControlTypeCombobox, self.rightControlIdVar)
				self.updateWidget(None, "right", "device")
				self.updateWidget(None, "right", "control")
			t = n.find("select:")
			if t > -1:
				self.updateControl(n, self.selectValueCombobox, self.selectDeviceTypeCombobox, self.selectDeviceIdVar, self.selectControlTypeCombobox, self.selectControlIdVar)
				self.updateWidget(None, "select", "device")
				self.updateWidget(None, "select", "control")
			t = n.find("back:")
			if t > -1:
				self.updateControl(n, self.backValueCombobox, self.backDeviceTypeCombobox, self.backDeviceIdVar, self.backControlTypeCombobox, self.backControlIdVar)
				self.updateWidget(None, "back", "device")
				self.updateWidget(None, "back", "control")
			t = n.find("quit:")
			if t > -1:
				self.updateControl(n, self.quitValueCombobox, self.quitDeviceTypeCombobox, self.quitDeviceIdVar, self.quitControlTypeCombobox, self.quitControlIdVar)
				self.updateWidget(None, "quit", "device")
				self.updateWidget(None, "quit", "control")
			t = n.find("list1:")
			if t > -1:
				self.updateControl(n, self.list1ValueCombobox, self.list1DeviceTypeCombobox, self.list1DeviceIdVar, self.list1ControlTypeCombobox, self.list1ControlIdVar)
				self.updateWidget(None, "list1", "device")
				self.updateWidget(None, "list1", "control")
			t = n.find("list2:")
			if t > -1:
				self.updateControl(n, self.list2ValueCombobox, self.list2DeviceTypeCombobox, self.list2DeviceIdVar, self.list2ControlTypeCombobox, self.list2ControlIdVar)
				self.updateWidget(None, "list2", "device")
				self.updateWidget(None, "list2", "control")
			t = n.find("list3:")
			if t > -1:
				self.updateControl(n, self.list3ValueCombobox, self.list3DeviceTypeCombobox, self.list3DeviceIdVar, self.list3ControlTypeCombobox, self.list3ControlIdVar)
				self.updateWidget(None, "list3", "device")
				self.updateWidget(None, "list3", "control")
			t = n.find("list4:")
			if t > -1:
				self.updateControl(n, self.list4ValueCombobox, self.list4DeviceTypeCombobox, self.list4DeviceIdVar, self.list4ControlTypeCombobox, self.list4ControlIdVar)
				self.updateWidget(None, "list4", "device")
				self.updateWidget(None, "list4", "control")
			t = n.find("list5:")
			if t > -1:
				self.updateControl(n, self.list5ValueCombobox, self.list5DeviceTypeCombobox, self.list5DeviceIdVar, self.list5ControlTypeCombobox, self.list5ControlIdVar)
				self.updateWidget(None, "list5", "device")
				self.updateWidget(None, "list5", "control")
	def getNode(self, tag, parent, value, name=None):
		if name == None:
			node = self.configRoot.find(".//"+tag)
			if node == None:
				p = self.configRoot.find(parent)
				node = ET.SubElement(p, tag)
				if value == None:
					value = ""
				node.text = value
				self.indent(self.configRoot)
				self.configTree.write(self.path + "config.xml")
		else:
			trick = 0
			for p in self.configRoot.findall(".//event"):
				n = p.find("name")
				if n.text == name:
					trick = 1
					if parent == "":
						node = p.find(tag)
					else:
						node = p.find(parent+"/"+tag)
						if node == None:
							if p.find(parent) == None:
								p = ET.SubElement(p, parent)
							else:
								p = p.find(parent)
							t = ET.SubElement(p, tag)
							t.text = value
							self.indent(self.configRoot)
							self.configTree.write(self.path + "config.xml")
							node = t
			if trick == 0:
				p = self.configRoot.find(".//controls")
				e = ET.SubElement(p, "event")
				n = ET.SubElement(e, "name")
				n.text = name
				t = ET.SubElement(e, tag)
				t.text = value
				self.indent(self.configRoot)
				self.configTree.write(self.path + "config.xml")
				node = e
		return node
	def getFolders(self, dir):
		return [name for name in os.listdir(dir)]
	def getFile(self, var):
		target = tkFileDialog.askopenfilename(title=self.browseExecLabelStr)
		var.insert(0, target)
	def indent(self, elem, level=0):
		i = "\n" + level*"  "
		if len(elem):
			if not elem.text or not elem.text.strip():
				elem.text = i + "  "
			if not elem.tail or not elem.tail.strip():
				elem.tail = i
			for elem in elem:
				self.indent(elem, level+1)
			if not elem.tail or not elem.tail.strip():
				elem.tail = i
		else:
			if level and (not elem.tail or not elem.tail.strip()):
				elem.tail = i
app = App()
app.mainloop()