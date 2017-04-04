# -*- coding: utf-8 -*-

#Libraries

import re, urllib
import smtplib
import os
import time
import math
import datetime
from lxml import html
import requests
import sqlite3
import smtplib

import databaseOperations
import webOperations
import mailOperations

#Codes

an = datetime.datetime.now()

print "\n" + "SQLite Database Version : " + (sqlite3.version) + "\n"

print "\n         ###Ceyrek Altin Durum Izleme Programi###\n\n             ###Designed by Furkan Birol###\n\n"
print "\n" + "************************ " + datetime.datetime.strftime(an, '%c') + " ************************" + "\n"


databaseOperations.__init__()
databaseOperations.create()

print "       " + "Tarih" + "      " + "    " + "Satis Fiyati" + "   " + "Alis Fiyati" + "   " + "Degisim Orani(%)" + "\n"
print "-------------------" + "   " + "------------" + "   " + "-----------" + "   " + "----------------" + "\n"

global latestValueString, latestValueArray, latestValueFloat
latestValueString = webOperations.ceyrekAltinYuzdeSonDurum()
latestValueArray = latestValueString.partition("%")
latestValueFloat = float(latestValueArray[0].replace(',', '.'))

sendMail = 0
x = 0

while x < 3:

    global now

    databaseOperations.insert()

    now  = datetime.datetime.now()

    webOperations.write()

    if (sendMail == 0):

        if ((latestValueFloat < (-4.50)) or (latestValueFloat > (4.50))):

            # mail gönder fonksiyonunu çağırdık
            mailOperations.mailgonder()
            sendMail = 1
            #pass

        else:

            pass

    else:

        pass

    x = x + 1

    time.sleep(5)


