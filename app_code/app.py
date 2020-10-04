from flask import Flask, render_template, request, session, redirect
import requests, json, os, re
import csv, json, sys
import pandas as pd
from pandas.io.json import json_normalize
import simplejson as json2
import subprocess
import psycopg2
from flask_bootstrap import Bootstrap
import random
import math
from datetime import date


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'super secret key'

app.config["IMAGE_UPLOADS"] = os.getcwd() + "/static/athlete_images"
app.config["ALLOWED_IMAGE_EXTENSİONS"] = ["PNG","JPG"]

def allowed_image(filename):
	if not "." in filename:
		return False
	ext = filename.rsplit(".",1)[1]

	if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSİONS"]:
		return True
	else:
		return False

#connecting to database
con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")

fileName =""
tableName =""
tableHeader = list()
tableHeaderCode = list()
tableData = list()
donatData = list()
columnNames = list()
diseaseDataList = list()
diseaseDataCodeList = list()

connectionList = list()


@app.route('/', methods=["GET","POST"])
def index():

	return render_template('main_page.html')

@app.route('/bulk', methods=["GET","POST"])
def index2():

	tableData = list()
	tableHeader = list()
	donatData = list()
	donatDataVal = list()
	colors = list()

	if request.method == 'POST':

		cur = con.cursor()

		fileName = str(request.form["file1"])
		tableName = str(request.form["table1"])

		columns = list()

		if tableName == "disease":
			columns = ["icd_code","disease_name"]
		elif tableName == "city":
			columns = ["stateid","cityid","city_name"]
		elif tableName == "disease_catcrit":
			columns = ["icd_code","health_catid","health_catcritid"]
		elif tableName == "district":
			columns = ["stateid","cityid","districtid","district_name"]
		elif tableName == "health_category":
			pcolumns = ["health_catid","health_catname"]
		elif tableName == "health_category_criteria":
			columns = ["health_catid","health_catcritid","health_catcritname"]
		elif tableName == "neighborhood":
			columns = ["nid","districtid","stateid","cityid","nname","zipcode"]
		elif tableName == "occupation":
			columns = ["occupationid","occupationname","sectorid"]
		elif tableName == "occupation_healthcatcrit":
			columns = ["occupationid","health_catid","health_catcritid"]
		elif tableName == "sector":
			columns = ["sectorid","sectorname"]
		elif tableName == "state":
			columns = ["stateid","statename"]
		elif tableName == "":
			print("not assigned")

		with open(fileName) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=",")
			next(csv_reader)
			for row in csv_reader:
				if tableName == "disease":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1]+")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ")"+";"
				elif tableName == "state":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1]+")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ")"+";"
				elif tableName == "city":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1] +","+columns[2] +")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ","+ "\'" +row[2]+ "\'"+ ")"+";"
				elif tableName == "district":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1] +","+columns[2] +","+columns[3] +")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ","+ "\'" +row[2]+ "\'"+","+ "\'" +row[3]+ "\'"+ ")"+";"
				elif tableName == "neighborhood":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1] +","+columns[2] +","+columns[3] +","+columns[4] +","+columns[5] +")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ","+ "\'" +row[2]+ "\'"+","+ "\'" +row[3]+ "\'"+ "," +"\'" +row[4]+ "\'"+ "," + "\'" +row[5]+ "\'" + ")"+";"
				elif tableName == "disease_catcrit":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1] +","+columns[2] +")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ","+ "\'" +row[2]+ "\'"+ ")"+";"
				elif tableName == "health_category":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1]+")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ")"+";"
				elif tableName == "health_category_criteria":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1] +","+columns[2] +")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ","+ "\'" +row[2]+ "\'"+ ")"+";"
				elif tableName == "occupation":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1] +","+columns[2] +")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ","+ "\'" +row[2]+ "\'"+ ")"+";"
				elif tableName == "occupation_healthcatcrit":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1] +","+columns[2] +")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ","+ "\'" +row[2]+ "\'"+ ")"+";"
				elif tableName == "sector":
					sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1]+")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ")"+";"

				cur.execute(sql_insert)

		con.commit()
		cur.close()


		cur = con.cursor()

		tableName = str(request.form["table1"])

		sql_insert = "SELECT * FROM " + tableName

		cur.execute(sql_insert)
		tableData = cur.fetchall()

		for i in cur.description:
			tableHeader.append(i[0])

		cur.close()



	return render_template('bulk.html',table=tableData,tableHeader=tableHeader,donatData=donatData,donatDataVal=donatDataVal,colors=colors)


@app.route('/sporcu', methods=["GET","POST"])
def index11():

	if request.method == 'POST':

		infoList = request.form.getlist("SporcuInf")
		infoList2 = request.form.getlist("SporcuInf2")
		print(infoList)
		row = []
		for i in range(0,len(infoList)):
			row.append(infoList[i])
		for i in range(0,len(infoList2)):
			row.append(infoList2[i])

		cur = con.cursor()

		columns = ["id", "sname", "sirname", "mass", "height","mevki", "health_up_body", "health_down_body", "body_size", "phone", "sporcu_foto", "notes","sex","age"]

		print(len(columns), columns)
		print(len(row), row)

		if request.files:
			image = request.files["item_image"]

			if image.filename == "":
				return redirect(request.url)

			if not allowed_image(image.filename):
				return redirect(request.url)

			image.save(os.path.join( app.config["IMAGE_UPLOADS"], image.filename))
			print("image saved")


		sql_insert = "INSERT INTO sporcular " + "("+ columns[0] +","+columns[1] +","+columns[2] +","+columns[3] +","+columns[4] +","+columns[5] +","+columns[6] +","+columns[7] +","+columns[8] +","+columns[9] +","+columns[10] +","+columns[11]+","+columns[12] +","+columns[13] +")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ","+ "\'" +row[2]+ "\'"+","+ "\'" +row[3]+ "\'"+ "," +"\'" +row[4]+ "\'"+ "," + "\'" +row[5]+ "\'" + ","+ "\'" +row[6]+ "\'" + ","+ "\'" +row[7]+ "\'" + ","+ "\'" +row[8]+ "\'" + ","+ "\'" +row[9]+ "\'" + ","+ "\'" +row[10]+ "\'" + ","+ "\'" +row[11]+ "\'" + ","+ "\'" +row[12]+ "\'" + ","+ "\'" +row[13]+ "\'" + ")"+";"

		print(sql_insert)
		cur.execute(sql_insert)
		con.commit()
		cur.close()

		key = str(row[0]) + "_" + str(row[1]) + "_" + str(row[2]) + ".json"

		print(key)

		data = {}
		data['specs'] = [{},{},{},{},{}]

		with open('static/athlete_jsons/'+ key, 'w') as outfile:
			json.dump(data, outfile)


	return render_template('sporcu.html')

@app.route('/individual', methods=["GET","POST"])
def index3():

	tableData = list()
	tableHeader = list()
	donatData = list()
	donatDataVal = list()
	colors = list()
	actName = False


	if request.method == 'POST':

		cur = con.cursor()

		tableName = str(request.form["table1"])

		if request.form.get("submits", False) != "ADD ITEM":
			session["table"] = tableName


		sql_insert = "SELECT * FROM " + tableName

		cur.execute(sql_insert)
		tableData = cur.fetchall()
		tableData.sort()

		for i in cur.description:
			tableHeader.append(i[0])

		for i in cur.description:
			donatData.append(i[0])


		cur.close()

		columns = donatData
		row = "not assigned"

		actName = request.form.get("submits", False)

		cur = con.cursor()

		print(tableName)
		print(columns)

		if actName == "ADD ITEM":

			row = request.form.getlist("datas")

			if tableName == "sporcular":
				sql_insert = "INSERT INTO " + tableName + "("+ columns[0] +","+columns[1]+")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ")"+";"


			#cur.execute(sql_insert)
		elif actName == "DELETE ITEM":

			row = request.form.getlist("datas2")


			if tableName == "sporcular":
				sql_insert = "DELETE FROM " + tableName + " WHERE (" + columns[0] + " = " + "'" +row[0]+ "' AND " + columns[1] + " = " + "'" +row[1]+ "' AND " + columns[2] + " = " + "'" +row[2]+ "\'" + ");"

				deletekey = str(row[0]) + "_" + str(row[1]) + "_" + str(row[2]) + ".json"
				try:
					os.remove("static/athlete_jsons/"+deletekey)
				except:
					print("no json file")
			cur.execute(sql_insert)

		elif actName == "UPDATE ITEM":

			row = request.form.getlist("datas3")

			if tableName == "disease" or tableName == "disease_catcrit":
				sql_insert = "UPDATE " + tableName + " SET " + columns[1] + " = "  + "'" + row[1] + "'" + " WHERE " + columns[0] + " = " + "'" +row[0]+ "'" + ";"
			else:
				sql_insert = "UPDATE " + tableName + " SET " + columns[1] + " = "  + "'" + row[1] + "'" + " WHERE " + columns[0] + " = " + row[0] + ";"
			#cur.execute(sql_insert)


		print(sql_insert)


		sql_insert = "SELECT * FROM " + tableName

		cur.execute(sql_insert)
		tableData = cur.fetchall()
		tableData.sort()


		con.commit()
		cur.close()








	return render_template('individual.html',table=tableData,tableHeader=tableHeader,donatData=donatData)


@app.route('/olcum', methods=["GET","POST"])
def index4():

	tableHeader = list()
	tableData = None
	tableData2 = list()

	cur = con.cursor()

	sql_insert = "SELECT * FROM " + "sporcular"

	cur.execute(sql_insert)
	tableData = cur.fetchall()
	tableData.sort()

	for i in tableData:
		tableData2.append((i[0],i[1],i[2]))

	for i in cur.description[:3]:
		tableHeader.append(i[0])

	con.commit()
	cur.close()


	if request.method == 'POST':

		actName = request.form.get("submits", False)

		sporcuInfo = request.form.get("rowDataInput")[1:-1].strip().split(",")

		sporcuID = sporcuInfo[0]

		sporcuName = sporcuInfo[1][2:-1]

		sporcuSirName = sporcuInfo[2][2:-1]

		print(sporcuID)

		print(sporcuName)

		print(sporcuSirName)

		sporcuInfo = sporcuID + "_" + sporcuName + "_" + sporcuSirName + ".json"

		with open("static/athlete_jsons/"+sporcuInfo) as json_file:
		    sporcuData = json.load(json_file)


		print(sporcuData["specs"])

		today = date.today()

		olcumDate = today.strftime("%Y/%m/%d")


		if actName == "maximalTest":
			dataList = request.form.getlist("maximalTest")

			selectedDate = request.form.get("dateMaximal")

			if selectedDate != "":
				olcumDate = selectedDate.replace("-","/")

			print("tarih:",olcumDate)

			sporcuData["specs"][0][olcumDate] = dict()

			sporcuData["specs"][0][olcumDate]["squat"] = str(dataList[0])
			sporcuData["specs"][0][olcumDate]["bench_press"] = str(dataList[1])
			sporcuData["specs"][0][olcumDate]["row"] = str(dataList[2])
			sporcuData["specs"][0][olcumDate]["shoulder_press"] = str(dataList[3])
			sporcuData["specs"][0][olcumDate]["dead_lift"] = str(dataList[4])
			sporcuData["specs"][0][olcumDate]["hip_trust"] = str(dataList[5])

			sorted(sporcuData["specs"][0].items(),reverse=False)

			with open("static/athlete_jsons/"+sporcuInfo, 'w') as outfile:
			    json.dump(sporcuData, outfile)

		elif actName == "fmsTest":
			dataList = request.form.getlist("fmsTest")

			selectedDate = request.form.get("dateFMS")

			if selectedDate != "":
				olcumDate = selectedDate.replace("-","/")

			print("tarih:",olcumDate)

			sporcuData["specs"][1][olcumDate] = dict()

			sporcuData["specs"][1][olcumDate]["deep_squat"] = [str(dataList[0]),str(dataList[1]),str(dataList[2])]
			sporcuData["specs"][1][olcumDate]["hurdle_step"] = [str(dataList[3]),str(dataList[4]),str(dataList[5]),str(dataList[6])]
			sporcuData["specs"][1][olcumDate]["inline_lunge"] = [str(dataList[7]),str(dataList[8]),str(dataList[9]),str(dataList[10])]
			sporcuData["specs"][1][olcumDate]["shoulder_mobility"] = [str(dataList[11]),str(dataList[12]),str(dataList[13]),str(dataList[14])]
			sporcuData["specs"][1][olcumDate]["impingement_clearing"] = [str(dataList[15]),str(dataList[16]),str(dataList[17]),str(dataList[18])]
			sporcuData["specs"][1][olcumDate]["act_str_leg_raise"] = [str(dataList[19]),str(dataList[20]),str(dataList[21]),str(dataList[22])]
			sporcuData["specs"][1][olcumDate]["trunk_stability_push_up"] = [str(dataList[23]),str(dataList[24]),str(dataList[25])]
			sporcuData["specs"][1][olcumDate]["press_up_clearing"] = [str(dataList[26]),str(dataList[27]),str(dataList[28])]
			sporcuData["specs"][1][olcumDate]["rotary_stability"] = [str(dataList[29]),str(dataList[30]),str(dataList[31]),str(dataList[32])]
			sporcuData["specs"][1][olcumDate]["posterior_rocking_clearing"] = [str(dataList[33]),str(dataList[34]),str(dataList[35])]
			sporcuData["specs"][1][olcumDate]["total"] = str(dataList[36])

			sorted(sporcuData["specs"][1].items(),reverse=False)

			with open("static/athlete_jsons/"+sporcuInfo, 'w') as outfile:
			    json.dump(sporcuData, outfile)


		elif actName == "ybalanceTest":
			dataList = request.form.getlist("ybalanceTest")

			selectedDate = request.form.get("dateY")

			if selectedDate != "":
				olcumDate = selectedDate.replace("-","/")

			print("tarih:",olcumDate)

			sporcuData["specs"][2][olcumDate] = dict()

			sporcuData["specs"][2][olcumDate]["limb_length"] = str(dataList[0])
			sporcuData["specs"][2][olcumDate]["dominant_leg"] = str(dataList[1])
			sporcuData["specs"][2][olcumDate]["anterior"] = [str(dataList[2]),str(dataList[3]),str(dataList[4]),str(dataList[5]),str(dataList[6]),str(dataList[7]),str(dataList[8])]
			sporcuData["specs"][2][olcumDate]["posteromedial"] = [str(dataList[9]),str(dataList[10]),str(dataList[11]),str(dataList[12]),str(dataList[13]),str(dataList[14]),str(dataList[15])]
			sporcuData["specs"][2][olcumDate]["posterolateral"] = [str(dataList[16]),str(dataList[17]),str(dataList[18]),str(dataList[19]),str(dataList[20]),str(dataList[21]),str(dataList[22])]
			sporcuData["specs"][2][olcumDate]["total"] = [str(dataList[23]),str(dataList[24])]

			sorted(sporcuData["specs"][2].items(),reverse=False)

			with open("static/athlete_jsons/"+sporcuInfo, 'w') as outfile:
			    json.dump(sporcuData, outfile)

		elif actName == "jumpTest":
			dataList = request.form.getlist("jumpTest")

			selectedDate = request.form.get("dateJUMP")

			if selectedDate != "":
				olcumDate = selectedDate.replace("-","/")

			print("tarih:",olcumDate)

			sporcuData["specs"][3][olcumDate] = dict()

			sporcuData["specs"][3][olcumDate]["time"] = str(dataList[0])
			sporcuData["specs"][3][olcumDate]["location"] = str(dataList[1])
			sporcuData["specs"][3][olcumDate]["position"] = str(dataList[2])
			sporcuData["specs"][3][olcumDate]["jumps"] = [str(dataList[3]),str(dataList[4]),str(dataList[5])]


			sorted(sporcuData["specs"][3].items(),reverse=False)

			with open("static/athlete_jsons/"+sporcuInfo, 'w') as outfile:
			    json.dump(sporcuData, outfile)

		elif actName == "vertTest":
			dataList = request.form.getlist("vertTest")

			selectedDate = request.form.get("dateVERT")

			if selectedDate != "":
				olcumDate = selectedDate.replace("-","/")

			print("tarih:",olcumDate)

			maxJump = 0
			ortJump = 0

			for elem in dataList:
				if float(elem) > maxJump:
					maxJump = float(elem)

			for elem in dataList:
				ortJump = float(elem) + ortJump

			ortJump = ortJump / len(dataList)

			sporcuData["specs"][4][olcumDate] = dict()

			sporcuData["specs"][4][olcumDate]["max"] = maxJump
			sporcuData["specs"][4][olcumDate]["ort"] = ortJump

			sorted(sporcuData["specs"][4].items(),reverse=False)

			with open("static/athlete_jsons/"+sporcuInfo, 'w') as outfile:
			    json.dump(sporcuData, outfile)

	return render_template('olcum.html',table=tableData2,tableHeader=tableHeader)



@app.route('/gecmis', methods=["GET","POST"])
def index21():

	tupleList = list()
	dateKey = ""
	dataDict = dict()
	sporcuFullName = ""
	testType = 0
	imageSource = "static/athlete_images/default.png"

	tableHeader = list()
	tableData = None
	tableData2 = list()

	cur = con.cursor()

	sql_insert = "SELECT * FROM " + "sporcular"

	cur.execute(sql_insert)
	tableData = cur.fetchall()
	tableData.sort()

	for i in tableData:
		tableData2.append((i[0],i[1],i[2]))

	for i in cur.description[:3]:
		tableHeader.append(i[0])

	con.commit()
	cur.close()

	if request.method == 'POST':


		dateKey = request.form.get("dateInputText")

		if len(dateKey) == 3 or len(dateKey) == 10:
			if "/" not in dateKey:
				dateKey = dateKey.upper()
				if dateKey != "SON":
					redirect(request.url)
		else:
			redirect(request.url)


		result=list(reversed(dateKey.split("/")))
		dateKey = ""
		for i in result:
			dateKey = dateKey + i + "/"
		dateKey = dateKey[:-1]

		testType = int(request.form.get("testType"))

		sporcuInfo = request.form.get("rowDataInput")[1:-1].strip().split(",")

		sporcuID = sporcuInfo[0]

		sporcuName = sporcuInfo[1][2:-1]

		sporcuSirName = sporcuInfo[2][2:-1]

		cur = con.cursor()

		sql_insert = "SELECT * FROM sporcular WHERE  ( id = '"+ sporcuID +"' AND sname = '"+ sporcuName +"' AND sirname = '"+  sporcuSirName  +"');";

		cur.execute(sql_insert)

		sporcuIndData = cur.fetchall()

		imageSource = "static/athlete_images/"+sporcuIndData[0][10]
		print(imageSource)

		cur.close()


		sporcuInfo = sporcuID + "_" + sporcuName + "_" + sporcuSirName + ".json"

		sporcuFullName = sporcuName + " " + sporcuSirName

		with open("static/athlete_jsons/"+sporcuInfo) as json_file:
		    sporcuData = json.load(json_file)


		if dateKey in sporcuData["specs"][testType]:
			print(dateKey)
			dataDict = sporcuData["specs"][testType][dateKey]



		elif dateKey == "SON":
			dateKey = list(sporcuData["specs"][testType].keys())[-1]
			dataDict = sporcuData["specs"][testType][dateKey]

		result=list(reversed(dateKey.split("/")))
		dateKey = ""
		for i in result:
			dateKey = dateKey + i + "/"
		dateKey = dateKey[:-1]



	return render_template('gecmis.html',table=tableData2,dateKey=dateKey,sporcuFullName=sporcuFullName,tableHeader=tableHeader,dataDict=dataDict,tupleList=tupleList,testType=testType,imageSource=imageSource)


@app.route('/profiller', methods=["GET","POST"])
def index69():

	sporcuData = {}


	#power test section
	powerTestsWeekLab = []

	powerTestsWeekSquatVal = []
	powerTestsWeekBenchVal = []
	powerTestsWeekRowVal = []
	powerTestsWeekShoulderVal = []
	powerTestsWeekDeadVal = []
	powerTestsWeekHipVal = []


	#fms test section
	fmsTestsWeekLab = []

	fmsTestsWeekDeepVal = []
	fmsTestsWeekHurdleVal = []
	fmsTestsWeekInlineVal = []
	fmsTestsWeekShoulderVal = []
	fmsTestsWeekImpigeVal = []
	fmsTestsWeekActiveStrVal = []
	fmsTestsWeekTrunkVal = []
	fmsTestsWeekPressVal = []
	fmsTestsWeekRotaryVal = []
	fmsTestsWeekPosteriVal = []
	fmsTestsWeekTotalVal = []

	fmsTestInjuryPercent = 0

	#y balance test section
	yTestsWeekLab = []

	yTestsWeekLeftVal  = []
	yTestsWeekRightVal = []
	yTestsAnteriorDef = []
	yTestsPosteromedialDef = []
	yTestsPosterolateralDef = []
	yTestsLimbLength = 0

	#jump test section

	jumpTestsWeekLab = []

	jumpTestsJ1 = []
	jumpTestsJ2 = []
	jumpTestsJ3 = []
	jumpTestsOrt = []


	jsonProfilDict = {}

	tempProfileDict = {}

	cur = con.cursor()

	tableName = "sporcular"

	sql_insert = "SELECT * FROM " + tableName

	cur.execute(sql_insert)
	tableData = cur.fetchall()

	for i in tableData:
		print( i[0] ,i[1], i[2])
		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]] = str(i[0]) + "_" + i[1]+ "_" + i[2] +".json"

	print(jsonProfilDict)

	cur.close()

	if request.method == 'POST':

		cur = con.cursor()

		jsonName = jsonProfilDict[request.form.get("tableChosen")]

		tempId = jsonName.split("_")[0]

		tempName = jsonName.split("_")[1]

		tempSir = jsonName.split("_")[2][:jsonName.split("_")[2].find(".")]

		sql_insert = "SELECT * FROM " + tableName + " WHERE (" + "id" + " = " + "'" +tempId+ "' AND " + "sname" + " = " + "'" +tempName+ "' AND " + "sirname" + " = " + "'" +tempSir+ "\'" + ");"

		cur.execute(sql_insert)

		dataInn = cur.fetchall()

		tempProfileDict["id"] = dataInn[0][0]#

		tempProfileDict["name"] = dataInn[0][1]#

		tempProfileDict["sirname"] = dataInn[0][2]#

		tempProfileDict["mass"] = dataInn[0][3]#

		tempProfileDict["height"] = dataInn[0][4]#

		tempProfileDict["mevki"] = dataInn[0][5]

		tempProfileDict["ust_saglik"] = dataInn[0][6]

		tempProfileDict["alt_saglik"] = dataInn[0][7]

		tempProfileDict["beden"] = dataInn[0][8]

		tempProfileDict["phone"] = dataInn[0][9]

		tempProfileDict["photo"] = "static/athlete_images/" + dataInn[0][10]

		tempProfileDict["notes"] = dataInn[0][11]

		tempProfileDict["sex"] = dataInn[0][12]#

		tempProfileDict["age"] = dataInn[0][13]#

		with open("static/athlete_jsons/"+jsonName) as json_file:
			sporcuData = json.load(json_file)

		powerTestsWeekLab =  list(sporcuData["specs"][0].keys())[-52:]

		for i in powerTestsWeekLab:
			powerTestsWeekSquatVal.append(sporcuData["specs"][0][i]["squat"])
			powerTestsWeekBenchVal.append(sporcuData["specs"][0][i]["bench_press"])
			powerTestsWeekRowVal.append(sporcuData["specs"][0][i]["row"])
			powerTestsWeekShoulderVal.append(sporcuData["specs"][0][i]["shoulder_press"])
			powerTestsWeekDeadVal.append(sporcuData["specs"][0][i]["dead_lift"])
			powerTestsWeekHipVal.append(sporcuData["specs"][0][i]["hip_trust"])

		fmsTestsWeekLab =  list(sporcuData["specs"][1].keys())[-52:]

		for i in fmsTestsWeekLab:
			fmsTestsWeekDeepVal.append(sporcuData["specs"][1][i]["deep_squat"][-2])
			fmsTestsWeekHurdleVal.append(sporcuData["specs"][1][i]["hurdle_step"][-2])
			fmsTestsWeekInlineVal.append(sporcuData["specs"][1][i]["inline_lunge"][-2])
			fmsTestsWeekShoulderVal.append(sporcuData["specs"][1][i]["shoulder_mobility"][-2])
			fmsTestsWeekImpigeVal.append(sporcuData["specs"][1][i]["impingement_clearing"][-2])
			fmsTestsWeekActiveStrVal.append(sporcuData["specs"][1][i]["act_str_leg_raise"][-2])
			fmsTestsWeekTrunkVal.append(sporcuData["specs"][1][i]["trunk_stability_push_up"][-2])
			fmsTestsWeekPressVal.append(sporcuData["specs"][1][i]["press_up_clearing"][-2])
			fmsTestsWeekRotaryVal.append(sporcuData["specs"][1][i]["rotary_stability"][-2])
			fmsTestsWeekPosteriVal.append(sporcuData["specs"][1][i]["posterior_rocking_clearing"][-2])
			fmsTestsWeekTotalVal.append(sporcuData["specs"][1][i]["total"])

		fmsTestInjuryPercent = abs( ( float(sporcuData["specs"][1][fmsTestsWeekLab[-1]]["total"]) / 18 ) * 100 - 100 )

		yTestsWeekLab =  list(sporcuData["specs"][2].keys())[-52:]

		yTestsLimbLength = sporcuData["specs"][2][yTestsWeekLab[-1]]["limb_length"]

		for i in yTestsWeekLab:
			yTestsWeekLeftVal.append(sporcuData["specs"][2][i]["total"][0])
			yTestsWeekRightVal.append(sporcuData["specs"][2][i]["total"][1])
			yTestsAnteriorDef.append(sporcuData["specs"][2][i]["anterior"][-1])
			yTestsPosteromedialDef.append(sporcuData["specs"][2][i]["posteromedial"][-1])
			yTestsPosterolateralDef.append(sporcuData["specs"][2][i]["posterolateral"][-1])

		print(yTestsWeekLeftVal)
		print(yTestsWeekRightVal)

		jumpTestsWeekLab = list(sporcuData["specs"][3].keys())[-52:]

		for i in jumpTestsWeekLab:
			jumpTestsJ1.append(sporcuData["specs"][3][i]["jumps"][0])
			jumpTestsJ2.append(sporcuData["specs"][3][i]["jumps"][1])
			jumpTestsJ3.append(sporcuData["specs"][3][i]["jumps"][2])
			jumpTestsOrt.append(  (  float(sporcuData["specs"][3][i]["jumps"][0]) + float(sporcuData["specs"][3][i]["jumps"][1]) + float(sporcuData["specs"][3][i]["jumps"][2])  ) / 3 )

	return render_template('profiller.html', jsonProfilDict=jsonProfilDict, tempProfileDict=tempProfileDict,powerTestsWeekLab=powerTestsWeekLab,
	 powerTestsWeekSquatVal=powerTestsWeekSquatVal,powerTestsWeekBenchVal=powerTestsWeekBenchVal,powerTestsWeekRowVal=powerTestsWeekRowVal,powerTestsWeekShoulderVal=powerTestsWeekShoulderVal,
	 powerTestsWeekDeadVal=powerTestsWeekDeadVal,powerTestsWeekHipVal=powerTestsWeekHipVal,fmsTestsWeekLab=fmsTestsWeekLab,fmsTestsWeekDeepVal=fmsTestsWeekDeepVal,
	 fmsTestsWeekHurdleVal=fmsTestsWeekHurdleVal,fmsTestsWeekInlineVal=fmsTestsWeekInlineVal,fmsTestsWeekShoulderVal=fmsTestsWeekShoulderVal,fmsTestsWeekImpigeVal=fmsTestsWeekImpigeVal,
	 fmsTestsWeekActiveStrVal=fmsTestsWeekActiveStrVal,fmsTestsWeekTrunkVal=fmsTestsWeekTrunkVal,fmsTestsWeekPressVal=fmsTestsWeekPressVal,fmsTestsWeekRotaryVal=fmsTestsWeekRotaryVal,
	 fmsTestsWeekPosteriVal=fmsTestsWeekPosteriVal,fmsTestsWeekTotalVal=fmsTestsWeekTotalVal,yTestsWeekLab=yTestsWeekLab,yTestsWeekLeftVal=yTestsWeekLeftVal,
	 yTestsWeekRightVal=yTestsWeekRightVal,yTestsAnteriorDef=yTestsAnteriorDef,yTestsPosteromedialDef=yTestsPosteromedialDef,yTestsPosterolateralDef=yTestsPosterolateralDef
	 ,yTestsLimbLength=yTestsLimbLength,jumpTestsWeekLab=jumpTestsWeekLab,jumpTestsJ1=jumpTestsJ1,jumpTestsJ2=jumpTestsJ2,jumpTestsJ3=jumpTestsJ3,jumpTestsOrt=jumpTestsOrt,
	 fmsTestInjuryPercent=fmsTestInjuryPercent)


"""
if __name__ == "__main__":
	app.run(debug=True,port=8000)
"""

