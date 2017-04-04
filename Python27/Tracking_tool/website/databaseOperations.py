# -*- coding: utf-8 -*-

#Libraries

import sqlite3
import datetime
import time

import webOperations

global ceyrekAltinSatisFiyati, ceyrekAltinAlisFiyati, ceyrekAltinYuzdelikDegisim

ceyrekAltinSatisFiyati = webOperations.ceyrekAltinSatisFiyati
ceyrekAltinAlisFiyati = webOperations.ceyrekAltinAlisFiyati
ceyrekAltinYuzdelikDegisim = webOperations.ceyrekAltinYuzdelikDegisim

def __init__():
    db_name = "database.db"
    global im, connection

    with sqlite3.connect('database.db') as connection:
        print "Connection of the Database successfully. \n"

    im = connection.cursor()

    return im, connection

def create():
    create_table = ("""
    CREATE TABLE IF NOT exists ceyrekAltin(
    Kayit_No INTEGER PRIMARY KEY,
    Tarih INTEGER NOT NULL ,
    Satis_Fiyati INTEGER NOT NULL ,
    Alis_Fiyati INTEGER NOT NULL ,
    Yuzde_Degisim INTEGER NOT NULL)
    """)

    im.execute(create_table)
    connection.commit()

def insert():

    global datetime
    global now

    now  = datetime.datetime.now()

    insert_table = ('''
            INSERT INTO ceyrekAltin (
            Kayit_No, Tarih, Satis_Fiyati,
            Alis_Fiyati, Yuzde_Degisim)
            VALUES (?, ?, ?, ?, ?)
            ''')

    im.executemany('''INSERT INTO ceyrekAltin(Tarih, Satis_Fiyati, Alis_Fiyati, Yuzde_Degisim) VALUES(?,?,?,?)''',
                   [(datetime.datetime.strftime(now, '%c'), ceyrekAltinSatisFiyati, ceyrekAltinAlisFiyati,
                    ceyrekAltinYuzdelikDegisim)])

    connection.commit()

def delete():

    pass

def update():

    pass

def list():
    read_table = ("""SELECT * FROM ceyrekAltin""")

    veriler = im.execute(read_table)

    print "       " + "Tarih" + "      " + "    " + "Satis Fiyati" + "   " + "Alis Fiyati" + "   " + "Degisim Orani(%)" + "\n"
    print "-------------------" + "   " + "------------" + "   " + "-----------" + "   " + "----------------" + "\n"

    for row in veriler:
       print " ", row[1] , "     " + row[2] , "       " , row[3] , "        " , row[4]

    print "\nPrice of the gold values collected and saved successfully..."

    connection.commit()

#choose = database()
#choose.create()

#print ("1-Ekle\n2-Sil\n3-Guncelle\n4-Listele\n0-Cikis")
#islem = input("Seciminiz : ")
#if (islem == 1):
#    choose.insert()
#elif (islem == 2):
#    choose.delete()
#elif (islem == 3):
#    choose.update()
#elif (islem == 4):
#    choose.list()