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
from datetime import date, timedelta


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'super secret key'

app.config["IMAGE_UPLOADS"] = os.getcwd() + "/static/athlete_images"
app.config["ALLOWED_IMAGE_EXTENSİONS"] = ["PNG","JPG","JPEG"]

def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".",1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSİONS"]:
        return True
    else:
        return False

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


        con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
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
        con.close()

        con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
        cur = con.cursor()

        tableName = str(request.form["table1"])

        sql_insert = "SELECT * FROM " + tableName

        cur.execute(sql_insert)
        tableData = cur.fetchall()

        for i in cur.description:
            tableHeader.append(i[0])

        cur.close()
        con.close()


    return render_template('bulk.html',table=tableData,tableHeader=tableHeader,donatData=donatData,donatDataVal=donatDataVal,colors=colors)


@app.route('/sporcu', methods=["GET","POST"])
def index3():

    if request.method == 'POST':

        infoList = request.form.getlist("SporcuInf")
        infoList2 = request.form.getlist("SporcuInf2")
        print(infoList)
        row = []
        for i in range(0,len(infoList)):
            row.append(infoList[i])
        for i in range(0,len(infoList2)):
            row.append(infoList2[i])

        con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
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

        row[1] = row[1].strip()

        row[2] = row[2].strip()


        sql_insert = "INSERT INTO sporcular " + "("+ columns[0] +","+columns[1] +","+columns[2] +","+columns[3] +","+columns[4] +","+columns[5] +","+columns[6] +","+columns[7] +","+columns[8] +","+columns[9] +","+columns[10] +","+columns[11]+","+columns[12] +","+columns[13] +")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ","+ "\'" +row[2]+ "\'"+","+ "\'" +row[3]+ "\'"+ "," +"\'" +row[4]+ "\'"+ "," + "\'" +row[5]+ "\'" + ","+ "\'" +row[6]+ "\'" + ","+ "\'" +row[7]+ "\'" + ","+ "\'" +row[8]+ "\'" + ","+ "\'" +row[9]+ "\'" + ","+ "\'" +row[10]+ "\'" + ","+ "\'" +row[13]+ "\'" + ","+ "\'" +row[11]+ "\'" + ","+ "\'" +row[12]+ "\'" + ")"+";"

        print(sql_insert)
        cur.execute(sql_insert)
        con.commit()
        cur.close()
        con.close()

        row[1] = row[1].strip().replace(" ","_")

        row[2] = row[2].strip().replace(" ","_")

        key = str(row[0]) + "_" + str(row[1]) + "_" + str(row[2]) + ".json"

        print(key)

        data = {}
        data['specs'] = [{},{},{},{},{},{},{}]

        with open('static/athlete_jsons/'+ key, 'w') as outfile:
            json.dump(data, outfile)


    return render_template('sporcu.html')

@app.route('/individual', methods=["GET","POST"])
def index4():

	tableData = list()
	tableHeader = list()
	donatData = list()
	donatDataVal = list()
	colors = list()
	actName = False


	if request.method == 'POST':

		con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
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
		con.close()

		columns = donatData
		row = "not assigned"

		actName = request.form.get("submits", False)
		con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
		cur = con.cursor()

		print(tableName)
		print(columns)

		if actName == "ADD ITEM":

			row = request.form.getlist("datas")

			if tableName == "sporcular":
				sql_insert = "INSERT INTO sporcular " + "("+ columns[0] +","+columns[1] +","+columns[2] +","+columns[3] +","+columns[4] +","+columns[5] +","+columns[6] +","+columns[7] +","+columns[8] +","+columns[9] +","+columns[10] +","+columns[11]+","+columns[12] +","+columns[13] +")"+" VALUES (" +"\'"+row[0]+"\'"+ ","+ "\'" +row[1]+ "\'"+ ","+ "\'" +row[2]+ "\'"+","+ "\'" +row[3]+ "\'"+ "," +"\'" +row[4]+ "\'"+ "," + "\'" +row[5]+ "\'" + ","+ "\'" +row[6]+ "\'" + ","+ "\'" +row[7]+ "\'" + ","+ "\'" +row[8]+ "\'" + ","+ "\'" +row[9]+ "\'" + ","+ "\'" +row[10]+ "\'" + ","+ "\'" +row[11]+ "\'" + ","+ "\'" +row[12]+ "\'" + ","+ "\'" +row[13]+ "\'" + ")"+";"


			cur.execute(sql_insert)
		elif actName == "DELETE ITEM":

			row = request.form.getlist("datas2")

			row[0] = row[0].strip()

			row[1] = row[1].strip()

			row[2] = row[2].strip()

			if tableName == "sporcular":
				sql_insert = "DELETE FROM " + tableName + " WHERE (" + columns[0] + " = " + "'" +row[0]+ "' AND " + columns[1] + " = " + "'" +row[1]+ "' AND " + columns[2] + " = " + "'" +row[2]+ "\'" + ");"

				deletekey = str(row[0]) + "_" + str(row[1]).strip().replace(" ","_") + "_" + str(row[2]).strip().replace(" ","_") + ".json"
				try:
					os.remove("static/athlete_jsons/"+deletekey)
				except:
					print("no json file")
			cur.execute(sql_insert)

		elif actName == "UPDATE ITEM":

			row = request.form.getlist("datas3")

			if tableName == "sporcular":
				print(columns)
				print(row)
				sql_insert = "UPDATE " + tableName + " SET " + columns[1] + " = "  + "'" + row[1] + "'" + "," + columns[2] + " = "  + "'" + row[2] + "'" + "," + columns[3] + " = "  + "'" + row[3] + "'" + "," + columns[4] + " = "  + "'" + row[4] + "'" + "," + columns[5] + " = "  + "'" + row[5] + "'" + "," + columns[6] + " = "  + "'" + row[6] + "'" + "," + columns[7] + " = "  + "'" + row[7] + "'" + "," + columns[8] + " = "  + "'" + row[8] + "'" + "," + columns[9] + " = "  + "'" + row[9] + "'" + "," + columns[10] + " = "  + "'" + row[10] + "'" + "," + columns[11] + " = "  + "'" + row[11] + "'" + "," + columns[12] + " = "  + "'" + row[12] + "'" + "," + columns[13] + " = "  + "'" + row[13] + "'" + " WHERE " + columns[0] + " = " + "'" +row[0]+ "'" + ";"

			cur.execute(sql_insert)


		print(sql_insert)


		sql_insert = "SELECT * FROM " + tableName

		cur.execute(sql_insert)
		tableData = cur.fetchall()
		tableData.sort()

		con.commit()
		cur.close()
		con.close()

	return render_template('individual.html',table=tableData,tableHeader=tableHeader,donatData=donatData)


@app.route('/olcum', methods=["GET","POST"])
def index5():

    tableHeader = list()
    tableData = None
    tableData2 = list()

    con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
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
    con.close()

    if request.method == 'POST':

        actName = request.form.get("submits", False)

        sporcuInfo = request.form.get("rowDataInput")[1:-1].strip().split(",")

        sporcuID = sporcuInfo[0]

        sporcuName = sporcuInfo[1][2:-1]

        sporcuSirName = sporcuInfo[2][2:-1]

        print(sporcuID)

        print(sporcuName)

        print(sporcuSirName)

        sporcuInfo = sporcuID + "_" + sporcuName.strip().replace(" ","_") + "_" + sporcuSirName.strip().replace(" ","_") + ".json"

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
            totalJump = 0
            ortJump = 0

            try:
                maxJump = dataList[0]
                ortJump = dataList[1]
                totalJump = dataList[2]
            except:
                maxJump = 0
                ortJump = 0
                totalJump = 0

            sporcuData["specs"][4][olcumDate] = dict()

            sporcuData["specs"][4][olcumDate]["max"] = maxJump
            sporcuData["specs"][4][olcumDate]["ort"] = ortJump
            sporcuData["specs"][4][olcumDate]["total"] = totalJump


            sorted(sporcuData["specs"][4].items(),reverse=False)

            with open("static/athlete_jsons/"+sporcuInfo, 'w') as outfile:
                json.dump(sporcuData, outfile)

        elif actName == "polarTest":
            dataList = request.form.getlist("polarTest")

            selectedDate = request.form.get("datePolar")

            if selectedDate != "":
                olcumDate = selectedDate.replace("-","/")

            print("tarih:",olcumDate)

            maxJump = 0
            totalJump = 0
            ortJump = 0

            try:
                maxJump = dataList[0]
                ortJump = dataList[1]
                totalJump = dataList[2]
            except:
                maxJump = 0
                ortJump = 0
                totalJump = 0
            sporcuData["specs"][5][olcumDate] = dict()
            sporcuData["specs"][5][olcumDate]["max"] = maxJump
            sporcuData["specs"][5][olcumDate]["ort"] = ortJump
            sporcuData["specs"][5][olcumDate]["total"] = totalJump

            sorted(sporcuData["specs"][5].items(),reverse=False)

            with open("static/athlete_jsons/"+sporcuInfo, 'w') as outfile:
                json.dump(sporcuData, outfile)


        elif actName == "servisTest":
            dataList = request.form.getlist("servisTest")

            selectedDate = request.form.get("dateServis")

            if selectedDate != "":
                olcumDate = selectedDate.replace("-","/")

            print("tarih:",olcumDate)

            maxJump = 0
            totalJump = 0
            ortJump = 0

            try:
                maxJump = dataList[0]
                ortJump = dataList[1]
                totalJump = dataList[2]
            except:
                maxJump = 0
                ortJump = 0
                totalJump = 0
            sporcuData["specs"][6][olcumDate] = dict()
            sporcuData["specs"][6][olcumDate]["max"] = maxJump
            sporcuData["specs"][6][olcumDate]["ort"] = ortJump
            sporcuData["specs"][6][olcumDate]["total"] = totalJump

            sorted(sporcuData["specs"][6].items(),reverse=False)

            with open("static/athlete_jsons/"+sporcuInfo, 'w') as outfile:
                json.dump(sporcuData, outfile)


    return render_template('olcum.html',table=tableData2,tableHeader=tableHeader)



@app.route('/gecmis', methods=["GET","POST"])
def index6():

    tupleList = list()
    dateKey = ""
    dataDict = dict()
    sporcuFullName = ""
    testType = -1
    imageSource = "static/athlete_images/default.png"

    tableHeader = list()
    tableData = None
    tableData2 = list()

    con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
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
    con.close()

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

        con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
        cur = con.cursor()

        sql_insert = "SELECT * FROM sporcular WHERE  ( id = '"+ sporcuID +"' AND sname = '"+ sporcuName +"' AND sirname = '"+  sporcuSirName  +"');";

        cur.execute(sql_insert)

        sporcuIndData = cur.fetchall()

        imageSource = "static/athlete_images/"+sporcuIndData[0][10]
        print(imageSource)

        cur.close()
        con.close()

        sporcuInfo = sporcuID + "_" + sporcuName.strip().replace(" ","_") + "_" + sporcuSirName.strip().replace(" ","_") + ".json"

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
def index7():

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

	#vert test section

    vertTestsWeekLab = []

    vertTestMax = []
    vertTestOrt = []
    vertTestTotal = []

    vertTestTakimOrt = []

    jsonProfilDict = {}

    tempProfileDict = {}
    tempProfileDict["photo"] = "static/athlete_images/default.png"

    con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
    cur = con.cursor()

    tableName = "sporcular"

    sql_insert = "SELECT * FROM " + tableName

    cur.execute(sql_insert)
    tableData = cur.fetchall()

    for i in tableData:
        print( i[0] ,i[1], i[2])
        jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]] = {}
        jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["json"] = str(i[0]) + "_" + i[1].replace(" ","_") + "_" + i[2].replace(" ","_") +".json"
        jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["id"] = str(i[0])
        jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["sname"] = str(i[1])
        jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["sirname"] = str(i[2])



    print(jsonProfilDict)

    cur.close()
    con.close()

    if request.method == 'POST':

        con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
        cur = con.cursor()

        jsonName = jsonProfilDict[request.form.get("tableChosen")]["json"]

        tempId = jsonProfilDict[request.form.get("tableChosen")]["id"]

        tempName = jsonProfilDict[request.form.get("tableChosen")]["sname"]

        tempSir = jsonProfilDict[request.form.get("tableChosen")]["sirname"]

        sql_insert = "SELECT * FROM " + tableName + " WHERE (" + "id" + " = " + "'" +tempId+ "' AND " + "sname" + " = " + "'" +tempName+ "' AND " + "sirname" + " = " + "'" +tempSir+ "\'" + ");"

        print(sql_insert)

        cur.execute(sql_insert)

        dataInn = cur.fetchall()

        print(dataInn)

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

        try:
            fmsTestInjuryPercent = abs( ( float(sporcuData["specs"][1][fmsTestsWeekLab[-1]]["total"]) / 18 ) * 100 - 100 )
        except:
            fmsTestInjuryPercent = "not given"

        yTestsWeekLab =  list(sporcuData["specs"][2].keys())[-52:]


        try:
            yTestsLimbLength = sporcuData["specs"][2][yTestsWeekLab[-1]]["limb_length"]
        except:
            fmsTestInjuryPercent = "not given"

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


        vertTestsWeekLab = list(sporcuData["specs"][4].keys())[-52:]

        for i in vertTestsWeekLab:
            vertTestMax.append(sporcuData["specs"][4][i]["max"])
            vertTestOrt.append(sporcuData["specs"][4][i]["ort"])
            vertTestTotal.append(sporcuData["specs"][4][i]["total"])
            tempCount = 0
            tempSum = 0
            for filename in os.listdir(os.getcwd() + "/static/athlete_jsons"):

                with open("static/athlete_jsons/"+filename) as json_file:
                    sporcuDataTemp = json.load(json_file)
                    print(filename)
                    try:
                        print(sporcuDataTemp["specs"][4][i]["ort"])
                        tempSum = tempSum + float(sporcuDataTemp["specs"][4][i]["ort"])
                        tempCount = tempCount + 1
                    except:
                        print("no key")

            try:
                vertTestTakimOrt.append(tempSum / tempCount)
            except:
                vertTestTakimOrt.append(-1)
        cur.close()
        con.close()

    return render_template('profiller.html', jsonProfilDict=jsonProfilDict, tempProfileDict=tempProfileDict,powerTestsWeekLab=powerTestsWeekLab,
	 powerTestsWeekSquatVal=powerTestsWeekSquatVal,powerTestsWeekBenchVal=powerTestsWeekBenchVal,powerTestsWeekRowVal=powerTestsWeekRowVal,powerTestsWeekShoulderVal=powerTestsWeekShoulderVal,
	 powerTestsWeekDeadVal=powerTestsWeekDeadVal,powerTestsWeekHipVal=powerTestsWeekHipVal,fmsTestsWeekLab=fmsTestsWeekLab,fmsTestsWeekDeepVal=fmsTestsWeekDeepVal,
	 fmsTestsWeekHurdleVal=fmsTestsWeekHurdleVal,fmsTestsWeekInlineVal=fmsTestsWeekInlineVal,fmsTestsWeekShoulderVal=fmsTestsWeekShoulderVal,fmsTestsWeekImpigeVal=fmsTestsWeekImpigeVal,
	 fmsTestsWeekActiveStrVal=fmsTestsWeekActiveStrVal,fmsTestsWeekTrunkVal=fmsTestsWeekTrunkVal,fmsTestsWeekPressVal=fmsTestsWeekPressVal,fmsTestsWeekRotaryVal=fmsTestsWeekRotaryVal,
	 fmsTestsWeekPosteriVal=fmsTestsWeekPosteriVal,fmsTestsWeekTotalVal=fmsTestsWeekTotalVal,yTestsWeekLab=yTestsWeekLab,yTestsWeekLeftVal=yTestsWeekLeftVal,
	 yTestsWeekRightVal=yTestsWeekRightVal,yTestsAnteriorDef=yTestsAnteriorDef,yTestsPosteromedialDef=yTestsPosteromedialDef,yTestsPosterolateralDef=yTestsPosterolateralDef
	 ,yTestsLimbLength=yTestsLimbLength,jumpTestsWeekLab=jumpTestsWeekLab,jumpTestsJ1=jumpTestsJ1,jumpTestsJ2=jumpTestsJ2,jumpTestsJ3=jumpTestsJ3,jumpTestsOrt=jumpTestsOrt,
	 fmsTestInjuryPercent=fmsTestInjuryPercent,vertTestsWeekLab = vertTestsWeekLab, vertTestMax=vertTestMax, vertTestOrt=vertTestOrt, vertTestTotal=vertTestTotal, vertTestTakimOrt=vertTestTakimOrt)

@app.route('/rm', methods=["GET","POST"])
def index8():

	return render_template('rm.html')

@app.route('/vert', methods=["GET","POST"])
def index9():

	nameChosen = ""

	dateChosen = ""

	#vert tests by team

	vertTestMaxLab = []
	vertTestMaxValue = []

	vertTestOrtLab = []
	vertTestOrtValue = []

	vertTestTotalLab = []
	vertTestTotalValue = []

	#vert test section

	vertTestsWeekLab = []

	vertTestMax = []
	vertTestOrt = []
	vertTestTotal = []

	jsonProfilDict = {}


	con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
	cur = con.cursor()

	tableName = "sporcular"

	sql_insert = "SELECT * FROM " + tableName

	cur.execute(sql_insert)
	tableData = cur.fetchall()

	for i in tableData:
		print( i[0] ,i[1], i[2])
		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]] = str(i[0]) + "_" + i[1].strip().replace(" ","_")+ "_" + i[2].strip().replace(" ","_") +".json"

	print(jsonProfilDict)

	cur.close()
	con.close()


	if request.method == 'POST':

		dateChosen = request.form.get("dateChosen").replace("-","/")

		print(dateChosen)

		jsonName = jsonProfilDict[request.form.get("tableChosen")]

		nameChosen = request.form.get("tableChosen")[2:]

		with open("static/athlete_jsons/"+jsonName) as json_file:
			sporcuData = json.load(json_file)


		vertTestsWeekLab = list(sporcuData["specs"][4].keys())[-52:]

		for i in vertTestsWeekLab:
			vertTestMax.append(sporcuData["specs"][4][i]["max"])
			vertTestOrt.append(sporcuData["specs"][4][i]["ort"])
			vertTestTotal.append(sporcuData["specs"][4][i]["total"])

		for filename in os.listdir(os.getcwd() + "/static/athlete_jsons"):

			with open("static/athlete_jsons/"+filename) as json_file:
				sporcuDataTemp = json.load(json_file)

				vertTestMaxLab.append(filename.replace("_"," ")[2:-5])
				vertTestOrtLab.append(filename.replace("_"," ")[2:-5])
				vertTestTotalLab.append(filename.replace("_"," ")[2:-5])
				try:
					vertTestMaxValue.append(sporcuDataTemp["specs"][4][dateChosen]["max"])
					vertTestOrtValue.append(sporcuDataTemp["specs"][4][dateChosen]["ort"])
					vertTestTotalValue.append(sporcuDataTemp["specs"][4][dateChosen]["total"])
				except:
					vertTestMaxValue.append("-1")
					vertTestOrtValue.append(-1)
					vertTestTotalValue.append("-1")

		print(vertTestMaxLab)
		print(vertTestMaxValue)
		print(vertTestOrtValue)
		print(vertTestTotalValue)


	return render_template('vert.html',nameChosen=nameChosen,jsonProfilDict=jsonProfilDict,vertTestsWeekLab=vertTestsWeekLab,vertTestMax=vertTestMax,vertTestOrt=vertTestOrt,vertTestTotal=vertTestTotal,
		vertTestMaxLab=vertTestMaxLab,vertTestOrtLab=vertTestOrtLab,vertTestTotalLab=vertTestTotalLab,vertTestMaxValue=vertTestMaxValue,
		vertTestOrtValue=vertTestOrtValue,vertTestTotalValue=vertTestTotalValue)


@app.route('/cikti', methods=["GET","POST"])
def index10():

	sporcuData = {}
	#--------------------------
	squatList = []

	benchList = []

	rowList = []

	shoulderList = []

	deadliftList = []

	hiptrustList = []
	#--------------------------

	jsonProfilDict = {}

	tempProfileDict = {}

	def_img = "static/athlete_images/default.png"

	nameChosen = ""

	con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
	cur = con.cursor()

	tableName = "sporcular"

	sql_insert = "SELECT * FROM " + tableName

	cur.execute(sql_insert)
	tableData = cur.fetchall()

	for i in tableData:
		print( i[0] ,i[1], i[2])
		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]] = {}
		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["json"] = str(i[0]) + "_" + i[1].strip().replace(" ","_")+ "_" + i[2].strip().replace(" ","_") +".json"
		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["id"] = str(i[0])
		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["sname"] =  i[1]
		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["sirname"] =  i[2]

	print(jsonProfilDict)

	cur.close()

	if request.method == 'POST':

		jsonName = jsonProfilDict[request.form.get("tableChosen")]["json"]

		nameChosen = request.form.get("tableChosen")[2:]

		cur = con.cursor()

		jsonName = jsonProfilDict[request.form.get("tableChosen")]["json"]

		tempId = jsonProfilDict[request.form.get("tableChosen")]["id"]

		tempName = jsonProfilDict[request.form.get("tableChosen")]["sname"]

		tempSir = jsonProfilDict[request.form.get("tableChosen")]["sirname"]

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

		cur.close()

		def_img = tempProfileDict["photo"]

		with open("static/athlete_jsons/"+jsonName) as json_file:
			sporcuData = json.load(json_file)

		powerTestsWeekLab =  list(sporcuData["specs"][0].keys())[-52:]

		if len(powerTestsWeekLab) > 0:

			dataPercent = sporcuData["specs"][0][powerTestsWeekLab[-1]]

			print(dataPercent)

			squatList = [ int(dataPercent["squat"]) , int(dataPercent["squat"])*9/10, int(dataPercent["squat"])*85/100, int(dataPercent["squat"])* 80/100, int(dataPercent["squat"])*75/100, int(dataPercent["squat"])*70/100,int(dataPercent["squat"])*65/100,int(dataPercent["squat"])*6/10,int(dataPercent["squat"])*55/100, int(dataPercent["squat"])*5/10 ]

			benchList = [ int(dataPercent["bench_press"]) , int(dataPercent["bench_press"])*9/10, int(dataPercent["bench_press"])*85/100, int(dataPercent["bench_press"])* 80/100, int(dataPercent["bench_press"])*75/100, int(dataPercent["bench_press"])*70/100,int(dataPercent["bench_press"])*65/100,int(dataPercent["bench_press"])*6/10,int(dataPercent["bench_press"])*55/100, int(dataPercent["bench_press"])*5/10 ]

			rowList = [ int(dataPercent["row"]) , int(dataPercent["row"])*9/10, int(dataPercent["row"])*85/100, int(dataPercent["row"])* 80/100, int(dataPercent["row"])*75/100, int(dataPercent["row"])*70/100,int(dataPercent["row"])*65/100,int(dataPercent["row"])*6/10,int(dataPercent["row"])*55/100, int(dataPercent["row"])*5/10 ]

			shoulderList = [ int(dataPercent["shoulder_press"]) , int(dataPercent["shoulder_press"])*9/10, int(dataPercent["shoulder_press"])*85/100, int(dataPercent["shoulder_press"])* 80/100, int(dataPercent["shoulder_press"])*75/100, int(dataPercent["shoulder_press"])*70/100,int(dataPercent["shoulder_press"])*65/100,int(dataPercent["shoulder_press"])*6/10,int(dataPercent["shoulder_press"])*55/100, int(dataPercent["shoulder_press"])*5/10 ]

			deadliftList = [ int(dataPercent["dead_lift"]) , int(dataPercent["dead_lift"])*9/10, int(dataPercent["dead_lift"])*85/100, int(dataPercent["dead_lift"])* 80/100, int(dataPercent["dead_lift"])*75/100, int(dataPercent["dead_lift"])*70/100,int(dataPercent["dead_lift"])*65/100,int(dataPercent["dead_lift"])*6/10,int(dataPercent["dead_lift"])*55/100, int(dataPercent["dead_lift"])*5/10 ]

			hiptrustList = [ int(dataPercent["hip_trust"]) , int(dataPercent["hip_trust"])*9/10, int(dataPercent["hip_trust"])*85/100, int(dataPercent["hip_trust"])* 80/100, int(dataPercent["hip_trust"])*75/100, int(dataPercent["hip_trust"])*70/100,int(dataPercent["hip_trust"])*65/100,int(dataPercent["hip_trust"])*6/10,int(dataPercent["hip_trust"])*55/100, int(dataPercent["hip_trust"])*5/10 ]

	return render_template('cikti.html',nameChosen=nameChosen,jsonProfilDict=jsonProfilDict,def_img=def_img,tempProfileDict=tempProfileDict,squatList=squatList,
		benchList=benchList,rowList=rowList,shoulderList=shoulderList,deadliftList=deadliftList,hiptrustList=hiptrustList)

@app.route('/program', methods=["GET","POST"])
def index11():


	return render_template('program.html')

@app.route('/saha', methods=["GET","POST"])
def index12():


	return render_template('saha.html')

@app.route('/verttakim', methods=["GET","POST"])
def index13():

	outputJson = {}

	athletes = {}
	athleteNames = []
	jsonProfilDict = {}
	filterNames = []

	testType = ""
	sdate = ""
	edate = ""

	sdateHTML = ""
	edateHTML = ""

	pdfList = ""

	con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
	cur = con.cursor()

	tableName = "sporcular"

	sql_insert = "SELECT * FROM " + tableName

	cur.execute(sql_insert)
	tableData = cur.fetchall()

	cur.close()
	con.close()

	for i in tableData:
		print( i[0] ,i[1], i[2])
		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]] = {}
		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["json"] = str(i[0]) + "_" + i[1].strip().replace(" ","_")+ "_" + i[2].strip().replace(" ","_") +".json"

		con = psycopg2.connect( host="Carnagie-1760.postgres.pythonanywhere-services.com",port="11760",database="mahirdb",user="super",password="facethest0rm")
		cur = con.cursor()

		jsonName = str(i[0]) + "_" + i[1].strip().replace(" ","_")+ "_" + i[2].strip().replace(" ","_") +".json"

		tempId = str(i[0])

		tempName = i[1]

		tempSir = i[2]

		sql_insert = "SELECT * FROM " + tableName + " WHERE (" + "id" + " = " + "'" +tempId+ "' AND " + "sname" + " = " + "'" +tempName+ "' AND " + "sirname" + " = " + "'" +tempSir+ "\'" + ");"

		cur.execute(sql_insert)

		dataInn = cur.fetchall()

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["id"] = dataInn[0][0]#

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["name"] = dataInn[0][1]#

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["sirname"] = dataInn[0][2]#

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["mass"] = dataInn[0][3]#

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["height"] = dataInn[0][4]#

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["mevki"] = dataInn[0][5]

		if dataInn[0][5] not in filterNames:
			filterNames.append(dataInn[0][5])

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["ust_saglik"] = dataInn[0][6]

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["alt_saglik"] = dataInn[0][7]

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["beden"] = dataInn[0][8]

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["phone"] = dataInn[0][9]

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["photo"] = "static/athlete_images/" + dataInn[0][10]

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["notes"] = dataInn[0][11]

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["sex"] = dataInn[0][12]#

		jsonProfilDict[ str(i[0]) + " " + i[1]+ " " + i[2]]["age"] = dataInn[0][13]#

		cur.close()
		con.close()


	print("all",jsonProfilDict)

	if request.method == 'POST':

		testType = request.form.get("testType")
		if testType == None:
			return render_template('verttakim.html',jsonProfilDict=jsonProfilDict,filterNames=filterNames)

		testType = int(testType)

		sdate = request.form.get("startDate")
		edate = request.form.get("endDate")
		sdateHTML = sdate
		edateHTML = edate

		pdfList = request.form.getlist("pdfTo")
		print("len",len(pdfList))
		if len(pdfList) == 0:
			return render_template('verttakim.html',jsonProfilDict=jsonProfilDict,filterNames=filterNames)


		sdate = date(int(sdate.split("-")[0]), int(sdate.split("-")[1]), int(sdate.split("-")[2]))
		edate = date(int(edate.split("-")[0]), int(edate.split("-")[1]), int(edate.split("-")[2]))

		delta = edate - sdate


		for i in pdfList:

			tempName = i[:-5]

			outputJson[tempName] = {}

			outputJson[tempName]["name"] = tempName.replace("_"," ")

			outputJson[tempName]["max"] = {}
			outputJson[tempName]["max"]["label"] = []
			outputJson[tempName]["max"]["value"] = []

			outputJson[tempName]["ort"] = {}
			outputJson[tempName]["ort"]["label"] = []
			outputJson[tempName]["ort"]["value"] = []

			outputJson[tempName]["total"] = {}
			outputJson[tempName]["total"]["label"] = []
			outputJson[tempName]["total"]["value"] = []

			sporcuData = {}

			with open("static/athlete_jsons/"+i) as json_file:
				sporcuData = json.load(json_file)


			for j in range(delta.days + 1):
			    day = sdate + timedelta(days=j)
			    currentDate = str(day).replace("-","/")

			    vertTestsWeekLab = list(sporcuData["specs"][testType].keys())

			    if currentDate in vertTestsWeekLab:
			    	print(currentDate)
			    	outputJson[tempName]["max"]["label"].append(currentDate)
			    	outputJson[tempName]["ort"]["label"].append(currentDate)
			    	outputJson[tempName]["total"]["label"].append(currentDate)
			    	outputJson[tempName]["max"]["value"].append(sporcuData["specs"][testType][currentDate]["max"])
			    	outputJson[tempName]["ort"]["value"].append(sporcuData["specs"][testType][currentDate]["ort"])
			    	outputJson[tempName]["total"]["value"].append(sporcuData["specs"][testType][currentDate]["total"])

		print(outputJson)


	return render_template('verttakim.html',jsonProfilDict=jsonProfilDict,filterNames=filterNames,outputJson=outputJson, sdateHTML=sdateHTML, edateHTML=edateHTML)
@app.route('/takimprogram', methods=["GET","POST"])
def index14():

	return render_template('takimprogram.html')

if __name__ == "__main__":
    app.run(debug=True,port=8000)


