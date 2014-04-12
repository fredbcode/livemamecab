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
		self.test = "simple test"
		self.queue = Queue.Queue()
		tk.Tk.__init__(self)
		self.tree = ET.parse("lang.xml")
		self.root = self.tree.getroot()
		self.lang = loc[0]
		if self.lang == None:
			self.lang = "en_GB"
		for lang in self.root.findall(".//*[@code='"+self.lang+"']"):
			self.titleStr = lang.find("title").text
			self.tabNewStr = lang.find("tabNew").text
			self.tabEditStr = lang.find("tabEdit").text
			self.tabAboutStr = lang.find("tabAbout").text
			self.convertLabelStr = lang.find("convertLabel").text
			self.convertButtonStr = lang.find("convertButton").text
			self.createLabelStr = lang.find("createLabel").text
			self.createButtonStr = lang.find("createButton").text
			self.listSelectLabelStr = lang.find("listSelectLabel").text
			self.listEditButtonStr = lang.find("editButton").text
			self.listDeleteButtonStr = lang.find("deleteButton").text
			self.emuEditLabelStr = lang.find("emuEditLabel").text
			self.aboutLabelStr = lang.find("aboutLabel").text
			self.versionLabelStr = lang.find("versionLabel").text
			self.translationLabelStr = lang.find("translationLabel").text
		self.path = expanduser('~') + '/.cabrio/'
		self.title(self.titleStr)
		self.notebook = ttk.Notebook(self)
		self.notebook.grid(column=0, row=0)
		self.create = ttk.Frame(self.notebook)
		self.edit = ttk.Frame(self.notebook)
		self.about = ttk.Frame(self.notebook)
		self.notebook.add(self.create, text=self.tabNewStr)
		self.notebook.add(self.edit, text=self.tabEditStr)
		self.notebook.add(self.about, text=self.tabAboutStr)

		self.convertLabel = ttk.Label(self.create, text=self.convertLabelStr)
		self.convertLabel.grid(column=0, row=0, sticky="W")
		self.convertButton = ttk.Button(self.create, text=self.convertButtonStr, command=lambda: self.convertList())
		self.convertButton.grid(column=1, row=0, sticky="W")
		self.createLabel = ttk.Label(self.create, text=self.createLabelStr)
		self.createLabel.grid(column=0, row=1, sticky="W")
		self.createButton = ttk.Button(self.create, text=self.createButtonStr, command=lambda: self.createList())
		self.createButton.grid(column=1, row=1, sticky="W")
		
		self.gameLists = []
		self.xmlFiles = []
		self.genres = []
		self.files = os.listdir(self.path)
		for file in self.files:
			if os.path.isfile(self.path+"/"+file):
				if file.endswith("xml"):
					tree = ET.parse(self.path+"/"+file)
					for item in tree.findall(".//game-list"):
						name = item.find("name")
						try:
							self.gameLists.append(name.text)
							self.xmlFiles.append(tree)
							for category in item.findall(".//category"):
								genre = category.find("value").text
								try:
									self.genres.index(genre)
								except:
									self.genres.append(genre)
						except:
							pass
		self.genres.sort()
		self.gamesList = []
		self.scrollbar = ttk.Scrollbar(self.edit)
		self.scrollbar.grid(column=5, row=1, sticky="NS")
		self.gamesListbox = tk.Listbox(self.edit, yscrollcommand = self.scrollbar.set, width=50, selectmode="single")
		self.gamesListbox.grid(column=0, row=1, columnspan=4, sticky="NESW")
		self.gamesListbox.bind("<Double-Button-1>", self.editGame)
		self.scrollbar.config(command=self.gamesListbox.yview)
		self.emuEditLabel = ttk.Label(self.edit, text=self.emuEditLabelStr)
		self.emuEditLabel.grid(column=0, row=2, columnspan=4)
		self.listSelectLabel = ttk.Label(self.edit, text=self.listSelectLabelStr)
		self.listSelectLabel.grid(column=0, row=0)
		self.listSelectCombo = ttk.Combobox(self.edit, width=10, values=self.gameLists, state="readonly")
		self.listSelectCombo.bind("<<ComboboxSelected>>", self.getGames)
		self.listSelectCombo.grid(column=1, row=0)
		self.listEditButton = ttk.Button(self.edit, text=self.listEditButtonStr)
		self.listEditButton.grid(column=2, row=0)
		self.listDeleteButton = ttk.Button(self.edit, text=self.listDeleteButtonStr)
		self.listDeleteButton.grid(column=3, row=0)

		self.logoFile = tk.PhotoImage(file="cabrio_logo.gif")
		self.logo = ttk.Label(self.about, image=self.logoFile)
		self.logo.grid(column=0, row=1, columnspan=3)
		self.aboutLabel = ttk.Label(self.about, text=self.aboutLabelStr)
		self.aboutLabel.grid(column=0, row=2, columnspan=3)
		self.versionLabel = ttk.Label(self.about, text=self.versionLabelStr)
		self.versionLabel.grid(column=0, row=3, columnspan=3)
		self.translationLabel = ttk.Label(self.about, text=self.translationLabelStr)
		self.translationLabel.grid(column=0, row=4, columnspan=3)
		self.treeConfig = ET.parse(self.path + 'config.xml')
	def editGame(self, option =None):
		self.name = tk.StringVar()
		self.name.set(self.gamesListbox.get("active"))
		self.romFile = tk.StringVar()
		self.genre = tk.StringVar()
		for lang in self.root.findall(".//*[@code='"+self.lang+"']"):
			self.editGameTitleStr = lang.find("editGameTitle").text
			self.nameLabelStr = lang.find("nameLabel").text
			self.romLabelStr = lang.find("romLabel").text
			self.genreLabelStr = lang.find("genreLabel").text
			self.browseButtonStr = lang.find("browseButton").text
			self.cancelButtonStr = lang.find("cancelButton").text
			self.deleteButtonStr = lang.find("deleteButton").text
			self.saveButtonStr = lang.find("saveButton").text
		for item in self.treeGames.findall(".//game"):
			game = item.find("name")
			if game.text == self.name.get():
				self.element = item
				self.platform = item.find("platform").text
				self.romFile.set(item.find("rom-image").text)
				try:
					category = item.find("categories/category")
					self.genre.set(category.find("value").text)
				except:
					self.genre.set("")
		self.toplevel = tk.Toplevel(self.edit)
		self.toplevel.title(self.editGameTitleStr)
		self.frame = ttk.Frame(self.toplevel)
		self.frame.grid()
		self.nameLabel = ttk.Label(self.frame, text=self.nameLabelStr)
		self.nameLabel.grid(column=0, row=0, sticky="W")
		self.nameEntry = ttk.Entry(self.frame, text=self.name)
		self.nameEntry.grid(column=1, row=0, sticky="W")
		self.romLabel = ttk.Label(self.frame, text=self.romLabelStr)
		self.romLabel.grid(column=0, row=1, sticky="W")
		self.browseRomsPath = ttk.Label(self.frame, text=self.romFile.get())
		self.browseRomsPath.grid(column=1, row=1, sticky="W")
		self.browseButton = ttk.Button(self.frame, text=self.browseButtonStr, command=lambda: self.getRomFile())
		self.browseButton.grid(column=2,row=1)
		self.genreLabel = ttk.Label(self.frame, text=self.genreLabelStr)
		self.genreLabel.grid(column=0, row=2, sticky="W")
		self.genreCombo = ttk.Combobox(self.frame, textvariable=self.genre, values=self.genres)
		self.genreCombo.grid(column=1, row=2, sticky="W")
		self.saveButton = ttk.Button(self.frame, text=self.saveButtonStr, command=lambda: self.saveChanges())
		self.saveButton.grid(column=0, row=3, sticky="E")
		self.deleteButton = ttk.Button(self.frame, text=self.deleteButtonStr, command=lambda: self.askConfirmationGame())
		self.deleteButton.grid(column=1, row=3)
		self.cancelButton = ttk.Button(self.frame, text=self.cancelButtonStr, command=lambda: self.toplevel.destroy())
		self.cancelButton.grid(column=2, row=3, sticky="W")
	def saveChanges(self):
		self.element.find("name").text = self.name.get()
		self.element.find("rom-image").text = self.romFile.get()
		if self.genre.get() != "":
			try:
				category = self.element.find("categories/category")
				category.find("value").text = self.genre.get()
			except:
				categories = ET.SubElement(self.element, "categories")
				category = ET.SubElement(categories, "category")
				name = ET.SubElement(category, "name")
				value = ET.SubElement(category, "value")
				name.text = "Genre"
				value.text = self.genre.get()
		for item in self.treeGames.findall(".//game-list"):
			file = item.find("name").text
		self.treeGames.write(self.path+"Gamelist-"+file+".xml")
		self.toplevel.destroy()
	def askConfirmationGame(self):
		self.toplevel.destroy()
		for lang in self.root.findall(".//*[@code='"+self.lang+"']"):
			self.deleteConfirmLabelStr = lang.find("deleteConfirmLabel").text
			self.deleteFileCheckStr = lang.find("deleteFileCheck").text
			self.okButtonStr = lang.find("okButton").text
			self.cancelButtonStr = lang.find("cancelButton").text
		self.checkVar = tk.IntVar()
		self.checkVar.set(0)
		self.toplevel = tk.Toplevel(self.edit)
		self.toplevel.title(self.name.get())
		self.frame = ttk.Frame(self.toplevel)
		self.frame.grid()
		self.warningLabel = ttk.Label(self.frame, text=self.deleteConfirmLabelStr)
		self.warningLabel.grid(column=0, row=0, columnspan=2)
		self.deleteFile = ttk.Checkbutton(self.frame, variable=self.checkVar, text=self.deleteFileCheckStr)
		self.deleteFile.grid(column=0, row=1, columnspan=2)
		self.okButton = ttk.Button(self.frame, text=self.okButtonStr, command=lambda: self.deleteGame())
		self.okButton.grid(column=0, row=2)
		self.dontButton = ttk.Button(self.frame, text=self.cancelButtonStr, command=lambda: self.toplevel.destroy())
		self.dontButton.grid(column=1, row=2)
	def deleteGame(self):
		items = self.gamesListbox.curselection()
		pos = 0
		self.toplevel.destroy()
		rootGames = self.treeGames.getroot()
		for item in self.treeGames.findall(".//game-list"):
			file = item.find("name").text
		for games in self.treeGames.findall(".//games"):
			for game in games.findall(".//game"):
				name = game.find("name").text
				if name == self.name.get():
					for i in items:
						idx = int(i) - pos
						self.gamesListbox.delete(idx, idx)
						pos = pos + 1
					games.remove(game)
					self.treeGames.write(self.path+"Gamelist-"+file+".xml")
		if self.checkVar.get() == 1:
			os.remove(self.romFile.get())
	def getGames(self, option=None):
		self.gamesListbox.delete(0, "end")
		self.idx = self.listSelectCombo.current()
		self.treeGames = self.xmlFiles[self.idx]
		for item in self.treeGames.findall(".//game"):
			name = item.find("name")
			self.gamesListbox.insert("end", name.text)
	def getRomPath(self):
		path = tkFileDialog.askdirectory(title="Prout")
		self.romPath.set(path)
	def getRomFile(self):
		temp = self.romFile.get()
		position = temp.rindex(".")
		length = temp.__len__()
		extension = temp[position:length]
		rom = tkFileDialog.askopenfilename(title="Machin", defaultextension=extension, filetypes=[(extension+" files", extension),("All files", "*.*")])
		self.romFile.set(rom)
		self.browseRomsPath["text"] = rom
	def getHSXML(self):
		xml = tkFileDialog.askopenfilename(title="Machin", defaultextension=".zip", filetypes=[("XML files", ".xml"),("All files", "*.*")])
		self.HSXmlFile.set(xml)
		count = 0
		tree = ET.parse(xml)
		for item in tree.findall(".//game"):
			count = count + 1
		self.max.set(count)
	def checkConvertFields(self):
		name = self.listNameEntry.get()
		platform = self.platformEntry.get()
		xml = self.HSXmlFile.get()
		roms = self.romPath.get()
		extension = self.extensionEntry.get()
		if name == "":
			self.status.set(self.errorNoListStr)
		elif platform == "":
			self.status.set(self.errorNoPlatformStr)
		elif xml == "":
			self.status.set(self.errorNoXMLStr)
		elif extension == "":
			self.status.set(self.errorNoExtensionStr)
		elif roms == "":
			self.status.set(self.errorNoRomsStr)
		else:
			self.convertThread(name, platform, xml, roms, extension)
	def checkCreateFields(self):
		name = self.listNameEntry.get()
		platform = self.platformEntry.get()
		roms = self.romPath.get()
		extension = self.extensionEntry.get()
		if name == "":
			self.status.set(self.errorNoListStr)
		elif platform == "":
			self.status.set(self.errorNoPlatformStr)
		elif extension == "":
			self.status.set(self.errorNoExtensionStr)
		elif roms == "":
			self.status.set(self.errorNoRomsStr)
		else:
			self.createThread(name, platform, roms, extension)
	def activateButtons(self):
		self.startButton.config(state="enabled")
		self.convertButton.config(state="enabled")
		self.createButton.config(state="enabled")
		self.toplevel.destroy()
	def convertList(self):
		self.convertButton.config(state="disabled")
		self.createButton.config(state="disabled")
		for lang in self.root.findall(".//*[@code='"+self.lang+"']"):
			self.convertTitleStr = lang.find("convertTitle").text
			self.browseButtonStr = lang.find("browseButton").text
			self.selectEmuLabelStr = lang.find("selectEmuLabel").text
			self.listNameLabelStr = lang.find("listNameLabel").text
			self.platformLabelStr = lang.find("platformLabel").text
			self.browseHSXMLLabelStr = lang.find("browseHSXMLLabel").text
			self.browseRomsLabelStr = lang.find("browseRomsLabel").text
			self.extensionLabelStr = lang.find("extensionLabel").text
			self.startButtonStr = lang.find("startButton").text
			self.errorNoEmulatorStr = lang.find("errorNoEmulator").text
			self.errorNoListStr = lang.find("errorNoList").text
			self.errorNoPlatformStr = lang.find("errorNoPlatform").text
			self.errorNoXMLStr = lang.find("errorNoXML").text
			self.errorNoRomsStr = lang.find("errorNoRoms").text
			self.errorNoExtensionStr = lang.find("errorNoExtension").text
		self.max = tk.IntVar()
		self.max.set(100)
		self.status = tk.StringVar()
		self.status.set("")
		self.HSXmlFile = tk.StringVar()
		self.HSXmlFile.set("")
		self.romPath = tk.StringVar()
		self.romPath.set("")
		self.toplevel = tk.Toplevel(self.create)
		self.toplevel.protocol("WM_DELETE_WINDOW", self.activateButtons)
		self.frame = ttk.Frame(self.toplevel)
		self.frame.grid()
		self.toplevel.title(self.convertTitleStr)
		self.listNameLabel = ttk.Label(self.frame, text=self.listNameLabelStr)
		self.listNameLabel.grid(column=0, row=1, sticky="W")
		self.listNameEntry = ttk.Entry(self.frame)
		self.listNameEntry.grid(column=1, row=1, sticky="W")
		self.platformLabel = ttk.Label(self.frame, text=self.platformLabelStr)
		self.platformLabel.grid(column=0, row=2, sticky="W")
		self.platformEntry = ttk.Entry(self.frame)
		self.platformEntry.grid(column=1, row=2, sticky="W")
		self.browseHSXMLLabel = ttk.Label(self.frame, text=self.browseHSXMLLabelStr)
		self.browseHSXMLLabel.grid(column=0, row=3, sticky="W")
		self.browseHSXMLButton = ttk.Button(self.frame, text=self.browseButtonStr, command=lambda: self.getHSXML())
		self.browseHSXMLButton.grid(column=1, row=3, sticky="W")
		self.browseHSXMLPath = ttk.Label(self.frame, textvariable=self.HSXmlFile)
		self.browseHSXMLPath.grid(column=0, row=4, columnspan=4, sticky="W")
		self.extensionLabel = ttk.Label(self.frame, text=self.extensionLabelStr)
		self.extensionLabel.grid(column=0, row=5, sticky="W")
		self.extensionEntry = ttk.Entry(self.frame)
		self.extensionEntry.grid(column=1, row=5, sticky="W")
		self.browseRomsLabel = ttk.Label(self.frame, text=self.browseRomsLabelStr)
		self.browseRomsLabel.grid(column=0, row=6, sticky="W")
		self.browseRomsButton = ttk.Button(self.frame, text=self.browseButtonStr, command=lambda: self.getRomPath())
		self.browseRomsButton.grid(column=1,row=6, sticky="W")
		self.browseRomsPath = ttk.Label(self.frame, textvariable=self.romPath)
		self.browseRomsPath.grid(column=0, row=7, columnspan=4, sticky="W")
		self.startButton = ttk.Button(self.frame, text=self.startButtonStr, command=lambda: self.checkConvertFields())
		self.startButton.grid(column=0, row=8, columnspan=2)
		self.progressBar = ttk.Progressbar(self.frame, orient="horizontal", mode="determinate", maximum=self.max.get(), length=500)
		self.progressBar.grid(column=0, row=9, columnspan=4, sticky="W")
		self.separator = ttk.Separator(self.frame, orient="horizontal")
		self.separator.grid(column=0, row=10, columnspan=4, sticky="EW")
		self.statusLabel = ttk.Label(self.frame, textvariable=self.status)
		self.statusLabel.grid(column=0, row=11, columnspan=4, sticky="W")
	def convertThread(self, name, platform, xml, roms, extension):
		self.startButton.config(state="disabled")
		self.thread = convertEngine(self.queue)
		self.thread.start()
		self.periodicCall()
	def periodicCall(self):
		self.checkQueue()
		if self.thread.is_alive():
			self.after(100, self.periodicCall)
	def checkQueue(self):
		while self.queue.qsize():
			try:
				msg = self.queue.get()
				if type(msg) is str:
					self.status.set(msg)
				elif type(msg) is int:
					self.progressBar["value"] = msg
				elif type(msg) is bool:
					self.startButton.config(state="enabled")
					self.convertButton.config(state="enabled")
					self.createButton.config(state="enabled")
					self.toplevel.destroy()
				else:
					self.status.set(msg)
			except Queue.Empty:
				pass
	def setMax(self):
		count = self.queue.get(1)
		self.max.set(count)
	def createList(self):
		for lang in self.root.findall(".//*[@code='"+self.lang+"']"):
			self.createTitleStr = lang.find("convertTitle").text
			self.browseButtonStr = lang.find("browseButton").text
			self.listNameLabelStr = lang.find("listNameLabel").text
			self.platformLabelStr = lang.find("platformLabel").text
			self.browseRomsLabelStr = lang.find("browseRomsLabel").text
			self.extensionLabelStr = lang.find("extensionLabel").text
			self.startButtonStr = lang.find("startButton").text
			self.errorNoEmulatorStr = lang.find("errorNoEmulator").text
			self.errorNoListStr = lang.find("errorNoList").text
			self.errorNoPlatformStr = lang.find("errorNoPlatform").text
			self.errorNoXMLStr = lang.find("errorNoXML").text
			self.errorNoRomsStr = lang.find("errorNoRoms").text
			self.errorNoExtensionStr = lang.find("errorNoExtension").text
		self.max = tk.IntVar()
		self.max.set(100)
		self.status = tk.StringVar()
		self.status.set("")
		self.romPath = tk.StringVar()
		self.romPath.set("")
		self.toplevel = tk.Toplevel(self.create)
		self.frame = ttk.Frame(self.toplevel)
		self.frame.grid()
		self.toplevel.title(self.createTitleStr)
		self.listNameLabel = ttk.Label(self.frame, text=self.listNameLabelStr)
		self.listNameLabel.grid(column=0, row=1, sticky="W")
		self.listNameEntry = ttk.Entry(self.frame)
		self.listNameEntry.grid(column=1, row=1, sticky="W")
		self.platformLabel = ttk.Label(self.frame, text=self.platformLabelStr)
		self.platformLabel.grid(column=0, row=2, sticky="W")
		self.platformEntry = ttk.Entry(self.frame)
		self.platformEntry.grid(column=1, row=2, sticky="W")
		self.extensionLabel = ttk.Label(self.frame, text=self.extensionLabelStr)
		self.extensionLabel.grid(column=0, row=3, sticky="W")
		self.extensionEntry = ttk.Entry(self.frame)
		self.extensionEntry.grid(column=1, row=3, sticky="W")
		self.browseRomsLabel = ttk.Label(self.frame, text=self.browseRomsLabelStr)
		self.browseRomsLabel.grid(column=0, row=4, sticky="W")
		self.browseRomsButton = ttk.Button(self.frame, text=self.browseButtonStr, command=lambda: self.getRomPath())
		self.browseRomsButton.grid(column=1,row=4, sticky="W")
		self.browseRomsPath = ttk.Label(self.frame, textvariable=self.romPath)
		self.browseRomsPath.grid(column=0, row=5, columnspan=4, sticky="W")
		self.startButton = ttk.Button(self.frame, text=self.startButtonStr, command=lambda: self.checkCreateFields())
		self.startButton.grid(column=0, row=6, columnspan=2)
		self.progressBar = ttk.Progressbar(self.frame, orient="horizontal", mode="determinate", maximum=self.max.get(), length=500)
		self.progressBar.grid(column=0, row=7, columnspan=4, sticky="W")
		self.separator = ttk.Separator(self.frame, orient="horizontal")
		self.separator.grid(column=0, row=8, columnspan=4, sticky="EW")
		self.statusLabel = ttk.Label(self.frame, textvariable=self.status)
		self.statusLabel.grid(column=0, row=9, columnspan=4, sticky="W")
	def createThread(self, name, platform, roms, extension):
		self.startButton.config(state="disabled")
		self.queue.put(name)
		self.queue.put(platform)
		self.queue.put(roms)
		self.queue.put(extension)
		self.thread = createEngine(self.queue)
		self.thread.start()
		self.periodicCall()

class convertEngine(threading.Thread):
	"""docstring for convertEngine"""
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue
	def run(self, ):
		self.path = expanduser('~') + '/.cabrio/'
		name = app.listNameEntry.get()
		platform = app.platformEntry.get()
		xml = app.browseHSXMLPath.cget("text")
		romsPath = app.browseRomsPath.cget("text")
		romsPath = romsPath + "/"
		extension = app.extensionEntry.get()
		extension = "." + extension
		count = 0
		tree = ET.parse(xml)
		R = ET.Element("cabrio-config")
		GL = ET.SubElement(R, "game-list")
		N = ET.SubElement(GL, "name")
		N.text = name
		G = ET.SubElement(GL, "games") 
		for item in tree.findall(".//game"):
			count = count + 1
			self.queue.put(count)
			if os.path.exists(romsPath + item.get("name") + extension):
				game = ET.SubElement(G, "game")	
				name = ET.SubElement(game, "name")
				name.text = item.find("description").text
				self.queue.put(name.text)
				pf = ET.SubElement(game, "platform")
				pf.text = platform
				rom = ET.SubElement(game, "rom-image")
				rom.text = romsPath + item.get("name") + ".zip"
				"""images = ET.SubElement(game, "images")
				imageL = ET.SubElement(images, "image")
				typeL = ET.SubElement(imageL, "type")
				typeL.text = "logo"
				imageFileL = ET.SubElement(imageL, "image-file")
				imageFileL.text = "/path/to/logo"
				imageSS = ET.SubElement(images, "image")
				typeSS = ET.SubElement(imageSS, "type")
				typeSS.text = "screenshot"
				imageFileSS = ET.SubElement(imageSS, "image-file")
				imageFileSS.text = "path/to/screenshot"""
				categories = ET.SubElement(game, "categories")
				category = ET.SubElement(categories, "category")
				categoryName = ET.SubElement(category, "name")
				categoryName.text = "Genre"
				value = ET.SubElement(category, "value")
				value.text = item.find("genre").text
		status = "Complete"
		self.queue.put(status)
		T = ET.ElementTree(R)
		self.indent(R)
		T.write(self.path+"Gamelist-"+N.text+".xml")
		self.queue.put(True)
		
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

class createEngine(threading.Thread):
	"""docstring for createtEngine"""
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue
	def run(self, ):
		self.path = expanduser('~') + '/.cabrio/'
		name = self.queue.get(1)
		platform = self.queue.get(1)
		romsPath = self.queue.get(1)
		romsPath = romsPath + "/"
		extension = self.queue.get(1)
		extension = "." + extension
		files = os.listdir(romsPath)
		count = 0
		for file in files:
			if os.path.isfile(romsPath+file):
				if file.endswith(extension):
					count = count + 1
		R = ET.Element("cabrio-config")
		GL = ET.SubElement(R, "game-list")
		N = ET.SubElement(GL, "name")
		N.text = name
		G = ET.SubElement(GL, "games") 
		for file in files:
			if os.path.isfile(romsPath+file):
				if file.endswith(extension):
					position = file.index(extension)
					rom = file[:position]
					game = ET.SubElement(G, "game")	
					name = ET.SubElement(game, "name")
					name.text = rom
					self.queue.put(name.text)
					pf = ET.SubElement(game, "platform")
					pf.text = platform
					rom = ET.SubElement(game, "rom-image")
					rom.text = romsPath+file
					"""images = ET.SubElement(game, "images")
					imageL = ET.SubElement(images, "image")
					typeL = ET.SubElement(imageL, "type")
					typeL.text = "logo"
					imageFileL = ET.SubElement(imageL, "image-file")
					imageFileL.text = "/path/to/logo"
					imageSS = ET.SubElement(images, "image")
					typeSS = ET.SubElement(imageSS, "type")
					typeSS.text = "screenshot"
					imageFileSS = ET.SubElement(imageSS, "image-file")
					imageFileSS.text = "path/to/screenshot"""
		status = "Complete"
		self.queue.put(status)
		T = ET.ElementTree(R)
		self.indent(R)
		T.write(self.path+"Gamelist-"+N.text+".xml")
		self.queue.put(True)
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