# -*- coding: utf-8 -*-

#Libraries

import re, urllib
from lxml import html
import requests
import datetime


pageCeyrekAltin = requests.get('http://www.bigpara.com/altin/ceyrek-altin-fiyati')
treeCeyrekAltin = html.fromstring(pageCeyrekAltin.content)
ceyrekAltinSatis = treeCeyrekAltin.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/span[2]/text()')
ceyrekAltinAlis = treeCeyrekAltin.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[3]/span[2]/text()')
ceyrekAltinYuzdeDegisim = treeCeyrekAltin.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[4]/span[3]/text()')

j = 0
ceyrekAltinSatisFiyati = ceyrekAltinSatis[j]

i = 0
ceyrekAltinAlisFiyati = ceyrekAltinAlis[i]

k = 0
ceyrekAltinYuzdelikDegisim = ceyrekAltinYuzdeDegisim[k]


def ceyrekAltinSatisSonDurum():
    j = 0
    ceyrekAltinSatisFiyati = ceyrekAltinSatis[j]
    return ceyrekAltinSatisFiyati


def ceyrekAltinAlisSonDurum():
    i = 0
    ceyrekAltinAlisFiyati = ceyrekAltinAlis[i]
    return ceyrekAltinAlisFiyati


def ceyrekAltinYuzdeSonDurum():
    k = 0
    ceyrekAltinYuzdelikDegisim = ceyrekAltinYuzdeDegisim[k]
    return ceyrekAltinYuzdelikDegisim

latestValueString = ceyrekAltinYuzdelikDegisim
latestValueArray = latestValueString.partition("%")
latestValueFloat = float(latestValueArray[0].replace(',', '.'))

def write():

    now  = datetime.datetime.now()

    print  " " + datetime.datetime.strftime(now, '%c') + "       " + ceyrekAltinSatisFiyati + "         " + ceyrekAltinAlisFiyati + "          " + ceyrekAltinYuzdelikDegisim

