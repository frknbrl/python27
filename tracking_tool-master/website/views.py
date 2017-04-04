# -*- coding: utf-8 -*-

from django.http import HttpResponse
import datetime
import re, urllib
from lxml import html
import requests
import datetime
from django.http import *
from django.template import Template,Context

from django.shortcuts import render_to_response


def universite(request):
 universiteler = (
    ['Sakarya','Sakarya',13,70000,],
    ['Yıldız Teknik','İstanbul',10,30000],
    ['Anadolu','Eskişehir',17,22000],
 )
 baslik = "Üniversiteler Bilgilendirme"
 return render_to_response('universiteler2.html',locals())

# Sonra da datetime ile saat & tarih bilgilerini alarak HttpResponse'u döndürelim.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Saat ve tarihimizi, python modülü kullanarak yazdırdık: %s.</body></html>" % now
    return HttpResponse(html)

def ceyrekAltin(request):

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


    latestValueString = ceyrekAltinYuzdelikDegisim
    latestValueArray = latestValueString.partition("%")
    latestValueFloat = float(latestValueArray[0].replace(',', '.'))


    #print  " " + datetime.datetime.strftime(now, '%c') + "       " + ceyrekAltinSatisFiyati + "         " + ceyrekAltinAlisFiyati + "          " + ceyrekAltinYuzdelikDegisim

    now = datetime.datetime.now()


    status = "<html><body> %s     --     %s     --     %s     --     %s \n\n</body></html>" % (now, ceyrekAltinSatisFiyati, ceyrekAltinAlisFiyati, ceyrekAltinYuzdelikDegisim)

    anlikVeriler = [now, ceyrekAltinSatisFiyati, ceyrekAltinAlisFiyati, ceyrekAltinYuzdelikDegisim]

    baslik = "Ceyrek Altın Bilgilendirme"
    return render_to_response('finans.html', locals())

def gramAltin(request):

    pageGramAltin = requests.get('http://www.bigpara.com/altin/gram-altin-fiyati')
    treeGramAltin = html.fromstring(pageGramAltin.content)
    gramAltinSatis = treeGramAltin.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/span[2]/text()')
    gramAltinAlis = treeGramAltin.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[3]/span[2]/text()')
    gramAltinYuzdeDegisim = treeGramAltin.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[4]/span[3]/text()')

    j = 0
    gramAltinSatisFiyati = gramAltinSatis[j]

    i = 0
    gramAltinAlisFiyati = gramAltinAlis[i]

    k = 0
    gramAltinYuzdelikDegisim = gramAltinYuzdeDegisim[k]

    latestGramValueString = gramAltinYuzdelikDegisim
    latestGramValueArray = latestGramValueString.partition("%")
    latestGramValueFloat = float(latestGramValueArray[0].replace(',', '.'))

    def writeGram():
        now = datetime.datetime.now()

        print  " " + datetime.datetime.strftime(now, '%c') + "       " + gramAltinSatisFiyati + "         " + gramAltinAlisFiyati + "          " + gramAltinYuzdelikDegisim

    anlikVeriler = [now, gramAltinSatisFiyati, gramAltinAlisFiyati, gramAltinYuzdelikDegisim]

    baslik = "Gram Altın Bilgilendirme"
    return render_to_response('finans.html', locals())

