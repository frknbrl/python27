from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
    kullaniciAdi = models.CharField(max_length=50)
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telefon = models.CharField(max_length=50, blank=True)
    eposta = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s , %s ,%s' % (self.adi, self.soyadi, self.eposta)
