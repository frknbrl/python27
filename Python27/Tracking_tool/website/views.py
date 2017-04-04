# -*- coding: utf-8 -*-

from django.http import HttpResponse
import datetime
import re, urllib

from django.utils.timezone import now
from lxml import html
import requests
import datetime
from django.http import *
from django.template import Template,Context

from django.shortcuts import render_to_response, render

from django.shortcuts import render # sayfa gösterim
from django.contrib.auth.forms import * # formlar
from django.contrib.auth import * #Login - Logout
from django.contrib.auth.decorators import * #görünüm gizlenme
from django.http import * # Http komutları
from django.contrib.auth.models import User



# Create your views here.
def kayit(request):
    kullanici = User.objects.create_user('Furkan','fbirol@gmail.com','fbirol')
    kullanici.first_name = Furkan
    kullanici.last_name = Birol
    kullanici.save()
    return render(request,'index.html',locals())

def giris(request):

    #Giriş yapan bidaha giremesin
    oku = request.user.id
    if(oku):
        return HttpResponseRedirect('/bilgi/')
    # formu çağırdık.
    form = AuthenticationForm
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        giris_kontrol = AuthenticationForm(data=request.POST)
        if(giris_kontrol.is_valid()):
            kullanici = authenticate(username=username,password=password)
            login(request,kullanici)
            #Yönlendir
            return HttpResponseRedirect('/bilgi/')
    return render(request,'giris.html',locals())

def bilgi(request):

    oku = request.user.id
    if(not oku):
        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/index/')

    return render(request, 'bilgi.html', locals())

# Sonra da datetime ile saat & tarih bilgilerini alarak HttpResponse'u döndürelim.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Saat ve tarihimizi, python modülü kullanarak yazdırdık: %s.</body></html>" % now
    return HttpResponse(html)

def finans(request):

#Çeyrek Altın Durum Bölümü

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

    # print  " " + datetime.datetime.strftime(now, '%c') + "       " + ceyrekAltinSatisFiyati + "         " + ceyrekAltinAlisFiyati + "          " + ceyrekAltinYuzdelikDegisim

    now = datetime.datetime.now()

    status = "<html><body> %s     --     %s     --     %s     --     %s \n\n</body></html>" % (
    now, ceyrekAltinSatisFiyati, ceyrekAltinAlisFiyati, ceyrekAltinYuzdelikDegisim)

    anlikVeriler = [now, ceyrekAltinSatisFiyati, ceyrekAltinAlisFiyati, ceyrekAltinYuzdelikDegisim]

    baslik = "Ceyrek Altın Bilgilendirme"

#Gram Altın Durum Bölümü

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

    anlikVeriler = [now, gramAltinSatisFiyati, gramAltinAlisFiyati, gramAltinYuzdelikDegisim]

    baslik = "Gram Altın Bilgilendirme"

#Dolar Durum Bölümü

    pageDolar = requests.get('http://www.bigpara.com/doviz/dolar/')
    treeDolar = html.fromstring(pageDolar.content)
    dolarSatis = treeDolar.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/span[2]/text()')
    dolarAlis = treeDolar.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[3]/span[2]/text()')
    dolarYuzdeDegisim = treeDolar.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[4]/span[3]/text()')

    j = 0
    dolarSatisFiyati = dolarSatis[j]

    i = 0
    dolarAlisFiyati = dolarAlis[i]

    k = 0
    dolarYuzdelikDegisim = dolarYuzdeDegisim[k]

    latestDolarValueString = dolarYuzdelikDegisim
    latestDolarValueArray = latestDolarValueString.partition("%")
    latestDolarValueFloat = float(latestDolarValueArray[0].replace(',', '.'))

    anlikVeriler = [now, dolarSatisFiyati, dolarAlisFiyati, dolarYuzdelikDegisim]

    baslik = "Dolar Bilgilendirme"

#Euro Durum Bölümü

    pageEuro = requests.get('http://www.bigpara.com/doviz/euro/')
    treeEuro = html.fromstring(pageEuro.content)
    euroSatis = treeEuro.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/span[2]/text()')
    euroAlis = treeEuro.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[3]/span[2]/text()')
    euroYuzdeDegisim = treeEuro.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div[4]/span[3]/text()')

    j = 0
    euroSatisFiyati = euroSatis[j]

    i = 0
    euroAlisFiyati = euroAlis[i]

    k = 0
    euroYuzdelikDegisim = euroYuzdeDegisim[k]

    latestEuroValueString = euroYuzdelikDegisim
    latestEuroValueArray = latestEuroValueString.partition("%")
    latestEuroValueFloat = float(latestEuroValueArray[0].replace(',', '.'))

    anlikVeriler = [now, euroSatisFiyati, euroAlisFiyati, euroYuzdelikDegisim]

    baslik = "Euro Bilgilendirme"

    return render_to_response('finans.html', locals())

def cikis_yap(request):
    oku = request.user.id
    if(not oku):
        return HttpResponseRedirect('/')
    logout(request)

    # Yönlendir
    return HttpResponseRedirect('/')

    return HttpResponse('Çıkış Yapıldı!, Lütfen Sayfayı Yenileyin!')


