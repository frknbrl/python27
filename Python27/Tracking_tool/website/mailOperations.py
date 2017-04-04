# -*- coding:utf-8 -*-

#Libraries

import smtplib
import datetime
import time

import webOperations


def baglan():

    sunucu = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    sunucu.login("furkanbiroll@gmail.com","48586745366_f")
    return sunucu

def mailgonder():
    global latestValueString, latestValueArray, latestValueFloat
    latestValueString = webOperations.ceyrekAltinYuzdeSonDurum()
    latestValueArray = latestValueString.partition("%")
    latestValueFloat = float(latestValueArray[0].replace(',', '.'))

    global now

    now  = datetime.datetime.now()

    global ceyrekAltinSatisFiyati, ceyrekAltinAlisFiyati, ceyrekAltinYuzdelikDegisim
    ceyrekAltinSatisFiyati = webOperations.ceyrekAltinSatisFiyati
    ceyrekAltinAlisFiyati = webOperations.ceyrekAltinAlisFiyati
    ceyrekAltinYuzdelikDegisim = webOperations.ceyrekAltinYuzdelikDegisim

    sunucu = baglan()

    gonderici = "furkanbiroll@gmail.com"
    alici = "furkanbirol1905@gmail.com"
    konu = "\n\nALIM VEYA SATIM FIRSATI OLABİLİR!!!\n"
    icerik = "\n\nÇeyrek Altın için son yüzdelik değişim  " + latestValueString + "  oldu!" + "\n\nAlim firsati olabilir. \n\nSon durum asagidaki gibidir:\n\n" + "Tarih                   : " + datetime.datetime.strftime(now, '%c') + "\n" + "Satis Fiyati          : " + ceyrekAltinSatisFiyati + "\n" + "Alis Fiyati            : " + ceyrekAltinAlisFiyati + "\n" + "Degisim Orani(%) : " + ceyrekAltinYuzdelikDegisim + "\n"

    mail = """
            Gönderen:   %s
            Konu:       %s
            Mesaj:      %s
    """ % (gonderici,konu,icerik)

    try:

        #maili gönderiyoruz. Aldığı parametreler gonderenin mail adresi, alıcının mail adresi, ve mail içeriği
        sunucu.sendmail(gonderici,alici,mail)
        print "Mail basarili bir sekilde gonderildi."

    except EOFError:

        print "Mail gonderilirken hata olustu."

    sunucu.quit()

#mail gönder fonksiyonunu çağırdık
#mailgonder()


