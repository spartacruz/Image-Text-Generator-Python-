from PIL import Image, ImageFont, ImageDraw
import ctypes

f = open("C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\1. Logo Model Number\\_text\\modelNumber.txt", 'r+', encoding='utf-8')
modelNumber = [line for line in f.read().splitlines()]
f.close()

f = open("C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\1. Logo Model Number\\_text\\nameFileSource.txt", 'r+', encoding='utf-8')
nameFileSource = [line for line in f.read().splitlines()]
f.close()

f = open("C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\1. Logo Model Number\\_text\\nameFileSaveSimpen.txt", 'r+', encoding='utf-8')
nameFileSave = [line for line in f.read().splitlines()]
f.close()

totalExport = 0
errorExport = 0

if len(nameFileSource) == len(modelNumber) & len(nameFileSource) == len(nameFileSave):
	hitung = range(len(nameFileSource))
	for i in hitung:
		dirLoad = "C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\1. Logo Model Number\\_image\\before\\"
		
		try:
			img = Image.open(dirLoad + nameFileSource[i])
		except (FileNotFoundError):
			errorExport = errorExport + 1
			break
		textToWrite = modelNumber[i]

		fontSize = 85 #20/85 rasio font, 1pt = 4.25
		if len(textToWrite) <= 20: fontSize = 85
		elif len(textToWrite) <= 26: fontSize = 72
		elif len(textToWrite) <= 32: fontSize = 60
		else: fontSize = 45 #51

		lebar, tinggi = img.size
		draw = ImageDraw.Draw(img)

		font = ImageFont.truetype("calibri.ttf", fontSize)

		lebarBaru, tinggiBaru = draw.textsize(textToWrite, font=font)

		draw.text(((lebar - lebarBaru)/2, 875), textToWrite, fill=000000 ,font=font, align="center")

		dirSave = "C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\1. Logo Model Number\\_image\\after\\"
		img.save(dirSave + nameFileSave[i])
		totalExport = totalExport + 1
else:
	textFileSource = "nameFileSource: " + str(len(nameFileSource))
	textModelNumber = "modelNumber: " + str(len(modelNumber))
	textFileSave = "nameFileSaveSimpen: " + str(len(nameFileSave))
 
	textConcatenate = "Jumlah Text : " + "\n" + textFileSource + "\n" + textModelNumber + "\n" + textFileSave
	ctypes.windll.user32.MessageBoxW(0, "Jumlah List Text Tidak Sama.\nTolong Check Lagi Ya\n\n" + textConcatenate, "Error", 0)

exportSukses = "Done!\nTotal export = " + str(totalExport)

if errorExport >= 1:
	exportGagal = "Total yang GAGAL = " + str(errorExport)
	exportSukses = exportSukses + "\n" + exportGagal

ctypes.windll.user32.MessageBoxW(0, exportSukses, "Exported", 0)
