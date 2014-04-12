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
		self.style = ttk.Style()
		self.style.theme_use("clam")
		self.tree = ET.parse("cabrio-config.xml")
		self.root = self.tree.getroot()
		self.lang = loc[0]
		if self.lang == None:
			self.lang = "en_GB"
		if self.root.findall(".//*[@code='"+self.lang+"']") == []:
			self.lang = "en_GB"
		for lang in self.root.findall(".//*[@code='"+self.lang+"']"):
			self.titleStr = lang.find("title").text
			self.setButtonStr =lang.find("setButton").text
			self.displayTabStr = lang.find("displayTab").text
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

		self.path = expanduser("~") + "/.cabrio/"
		self.configTree = ET.parse(self.path + "config.xml")
		self.configRoot = self.configTree.getroot()
		self.fullscreenVar = tk.IntVar()
		self.fullscreen = self.getNode("full-screen")
		if self.fullscreen.text == "true":
			self.fullscreenVar.set(1)
		elif self.fullscreen == "false":
			self.fullscreenVar.set(0)
		self.framerate = self.getNode("frame-rate")
		self.framerateVar = tk.StringVar()
		self.framerateVar.set(self.framerate.text)
		self.videoLoop = self.getNode("video-loop")
		self.videoLoopVar = tk.IntVar()
		if self.videoLoop.text == "true":
			self.videoLoopVar.set(1)
		elif self.videoLoop.text == "false":
			self.videoLoopVar.set(0)
		self.themesList = self.getFolders("/usr/share/cabrio/themes/")
		self.theme = self.getNode("theme")
		self.themeVar = tk.StringVar()
		self.themeVar.set(self.theme.text)
		self.width = self.getNode("width")
		self.widthVar = tk.StringVar()
		self.widthVar.set(self.width.text)
		self.height = self.getNode("height")
		self.heightVar = tk.StringVar()
		self.heightVar.set(self.height.text)
		self.rotation = self.getNode("rotation")
		self.rotationVar = tk.StringVar()
		self.rotationVar.set(self.rotation.text)
		self.flipHorizontal = self.getNode("flip-horizontal")
		self.flipHorizontalVar = tk.StringVar()
		self.flipHorizontalVar.set(self.flipHorizontal.text)
		self.flipVertical = self.getNode("flip-vertical")
		self.flipVerticalVar = tk.StringVar()
		self.flipVerticalVar.set(self.flipVertical.text)
		self.quality = self.getNode("quality")
		self.qualityVar = tk.StringVar()
		self.qualityVar.set(self.quality.text)
		self.maxImageWidth = self.getNode("max-image-width")
		self.maxImageWidthVar = tk.StringVar()
		self.maxImageWidthVar.set(self.maxImageWidth.text)
		self.maxImageHeight = self.getNode("max-image-height")
		self.maxImageHeightVar = tk.StringVar()
		self.maxImageHeightVar.set(self.maxImageHeight.text)
		self.emulatorBinary = tk.StringVar()
		self.emulatorBinary.set("")
		self.emulatorsList = []
		
		self.title(self.titleStr)
		self.notebook = ttk.Notebook(self)
		self.notebook.grid(column=0, row=0)
		self.displayTab = ttk.Frame(self.notebook)
		self.controlsTab = ttk.Frame(self.notebook)
		self.emulatorsTab = ttk.Frame(self.notebook)
		self.aboutTab = ttk.Frame(self.notebook)
		self.notebook.add(self.displayTab, text=self.displayTabStr)
		self.notebook.add(self.controlsTab, text=self.controlsTabStr)
		self.notebook.add(self.emulatorsTab, text=self.emulatorsTabStr)
		self.notebook.add(self.aboutTab, text=self.aboutTabStr)
		self.displayPanedWindow = ttk.Panedwindow(self.displayTab, orient="vertical")
		self.displayPanedWindow.grid()
		self.interfaceLabelFrame = ttk.Labelframe(self.displayTab, text=self.interfaceLabelFrameStr)
		self.displayPanedWindow.add(self.interfaceLabelFrame)
		self.fsCheckButton = ttk.Checkbutton(self.interfaceLabelFrame, variable=self.fullscreenVar, text=self.fullscreenStr, command=lambda a=self.fullscreen, b=self.fullscreenVar: self.writeBool(a, b))
		self.fsCheckButton.grid(column=0, row=0, sticky="W")
		self.framerateLabel = ttk.Label(self.interfaceLabelFrame, text=self.framerateStr)
		self.framerateLabel.grid(column=0, row=1, sticky="W")
		self.framerateEntry = ttk.Entry(self.interfaceLabelFrame, text=self.framerateVar)
		self.framerateEntry.grid(column=1, row=1, sticky="W")
		self.setFramerateButton = ttk.Button(self.interfaceLabelFrame, text=self.setButtonStr, command=lambda a=self.framerate, b= self.framerateVar: self.writeString(a, b))
		self.setFramerateButton.grid(column=2, row=1)
		self.videoLoopCheckButton = ttk.Checkbutton(self.interfaceLabelFrame, variable=self.videoLoopVar, text=self.videoLoopStr, command=lambda a=self.videoLoop, b=self.videoLoopVar: self.writeBool(a, b))
		self.videoLoopCheckButton.grid(column=0, row=2, columnspan=2, sticky="W")
		self.themeLabel = ttk.Label(self.interfaceLabelFrame, text=self.themeStr)
		self.themeLabel.grid(column=0, row=3, sticky="W")
		self.themesCombobox = ttk.Combobox(self.interfaceLabelFrame, values=self.themesList, textvariable=self.themeVar, state="readonly")
		self.themesCombobox.bind("<<ComboboxSelected>>", self.writeTheme)
		self.themesCombobox.grid(column=1, row=3, sticky="W")
		
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
		
	def editEmulator(self, option=None):
		self.displayName = tk.StringVar()
		self.displayName.set(self.emulatorsListbox.get("active"))
		for lang in self.root.findall(".//*[@code='"+self.lang+"']"):
			self.newEmulatorTitleStr = lang.find("newEmulatorTitle").text
			self.browseEmulatorLabelStr = lang.find("browseEmulatorLabel").text
			self.browseButtonStr = lang.find("browseButton").text
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
			self.confirmDeleteLabelStr = lang.find("confirmDeleteLabel").text#
			self.okButtonStr = lang.find("okButton").text
		self.toplevel = tk.Toplevel(self.emulatorsTab)
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
		self.emulatorExecButton = ttk.Button(self.frame, text=self.browseButtonStr)
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
		self.saveButton = ttk.Button(self.frame, text=self.saveButtonStr, command=lambda: self.checkChanges())
		self.saveButton.grid(column=0, row=99, columnspan=1)
		if option != "new":
			self.deleteButton = ttk.Button(self.frame, text=self.deleteButtonStr, command=lambda: self.confirmDelete())
			self.deleteButton.grid(column=1, row=99, columnspan=1)
		self.cancelButton = ttk.Button(self.frame, text=self.cancelButtonStr, command=lambda: self.toplevel.destroy())
		self.cancelButton.grid(column=2, row=99, columnspan=2)
		self.separator = ttk.Separator(self.frame, orient="horizontal")
		self.separator.grid(column=0, row=100, columnspan=4, sticky="EW")
		self.statusLabel = ttk.Label(self.frame, textvariable=self.statusVar)
		self.statusLabel.grid(column=0, row=101, columnspan=4, sticky="W")
	def confirmDelete(self):
		self.toplevel.destroy()
		self.toplevel = tk.Toplevel(self.emulatorsTab)
		self.frame = ttk.Frame(self.toplevel, borderwidth=10)
		self.frame.grid()
		self.confirmDeleteLabel = ttk.Label(self.frame, text=self.confirmDeleteLabelStr)
		self.confirmDeleteLabel.grid(column=0, row=0, columnspan=2)
		self.confirmButton = ttk.Button(self.frame, text=self.okButtonStr, command=lambda: self.deleteEmulator())
		self.confirmButton.grid(column=0, row=1)
		self.cancelButton = ttk.Button(self.frame, text=self.cancelButtonStr, command=lambda: self.toplevel.destroy())
		self.cancelButton.grid(column=1, row=1)
	def deleteEmulator(self):
		self.toplevel.destroy()
		name = self.emulatorsListbox.get("active")
		emulators = self.configRoot.find(".//emulators")
		for item in emulators.findall(".//emulator"):
			displayName = item.find("display-name")
			if name == displayName.text:
				emulators.remove(item)
				self.emulatorsListbox.delete("active")
				self.emulatorsList.remove(name)
				self.configTree.write(self.path + "config.xml")
	def checkChanges(self):
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
							self.saveChanges()
			else:
				self.saveChanges()
	def saveChanges(self):
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
	def writeBool(self, node, var):
		if var.get() == 1:
			node.text = "true"
		elif var.get() == 0:
			node.text = "false"
		self.configTree.write(self.path + 'config.xml')
	def writeString(self, node1, var1, node2=None, var2=None):
		node1.text = var1.get()
		if node2 != None:
			node2.text = var2.get()
		self.configTree.write(self.path + 'config.xml')
	def writeTheme(self, event):
		current = self.themesCombobox.current()
		selected = self.themesList[current]
		self.theme.text = selected
		self.configTree.write(self.path + 'config.xml')
	def getNode(self, name):
		for node in self.configRoot.findall(".//"+name):
			return node
	def getFolders(self, dir):
		return [name for name in os.listdir(dir)]
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