#!/usr/bin/python
# -*- coding: utf-8 -*-

#Парсер геоданных Адресного Реестра Москвы.
#Скачайте json c http://data.mos.ru/opendata/7705031674-adresniy-reestr-zdaniy-i-soorujeniy-v-gorode-moskve
#Положите его под именем "Адресный реестр зданий и сооружений в городе Москве.json" в папку со скриптом
#python parcer.py
#Сгенерируется csv, который можно открыть в QGIS.


import ijson,urllib
import sys


from shapely.geometry import Polygon, MultiPolygon

import csv



#temp=sys.stdout
#sys.stdout=buff


values={}

fs = open('address_reestr_moscow.csv','w')
fs.write("Адрес,Административный Район,Номер дома,Номер корпуса,Номер строения,Признак владения,Признак сооружения,wkt_geom\n")
fs.close()

f = open('Адресный реестр зданий и сооружений в городе Москве.json','r')
parser = ijson.parse(f)
for prefix, event, value in parser:



    print prefix, event, value
    if  (prefix, event) == ('item', 'start_map'):
        values={}
        values['addrFull']=''
        values['admArea']=''
        values['nomerDoma']=''
        values['nomerKorpusa']=''
        values['nomerStroenia']=''
        values['priznakVladenia']=''
        values['priznakSooruzenia']=''
    elif (prefix, event) == ('item.Cells.ADRES', 'string'):
        full_addr=value
        values['addrFull']=value.encode('utf-8')
        #stream.write('<%s>' % value)

    elif (prefix, event) == ('item.Cells.DMT', 'string'):
        values['nomerDoma']=value.encode('utf-8')
    elif (prefix, event) == ('item.Cells.AdmArea.item', 'string'):
        values['AdmArea']=value.encode('utf-8')
    elif (prefix, event) == ('item.Cells.KRT', 'string'):
        values['nomerKorpusa']=value.encode('utf-8')
    elif (prefix, event) == ('item.Cells.STRT', 'string'):
        values['nomerStroenia']=value.encode('utf-8')
    elif (prefix, event) == ('item.Cells.VLD', 'string'):
        values['priznakVladenia']=value.encode('utf-8')
    elif (prefix, event) == ('item.Cells.SOOR', 'string'):
        values['priznakSooruzenia']=value.encode('utf-8')

    elif (prefix, event) == ('item.Cells.geoData.type', 'string'):
        #geomStarted=True
        geomType=value
        coords_array=[]
    elif (prefix, event) == ('item.Cells.geoData.coordinates.item.item.item','number'): #тип геометрии - polygon
        #добавляем одну координату в массив
        coords_array.append(value)
        #print '#='+str(value)
    elif (prefix, event) == ('item.Cells.geoData.coordinates.item.item.item.item','number'): #тип геометрии - multipolygon
        #добавляем одну координату в массив
        coords_array.append(value)


    elif (prefix, event) == ('item.Cells.geoData.coordinates.item', 'end_array'):
        #geom_started=False   #Кончился их список координат
        #print coords_array
        #print len(coords_array)
        coordsForShapely=[]
        for i in xrange(0,len(coords_array),2):
            coordsForShapely.append((coords_array[i],coords_array[i+1]))
        #print coords_array
        
        #Поскольку сейчас в исходном файле дырок в мультиполигонах не найдено, то все геометрии делаются полигонами.
        '''if geomType == 'Polygon':
            geom = Polygon(coordsForShapely)
        if geomType == 'MultiPolygon':
            geom = MultiPolygon(coordsForShapely)
        '''
        geom = Polygon(coordsForShapely)

        #print geom.wkt

        #модуль csv не работает с файлами открытыми на дозапись, поэтому генерирую строку csv вручную
        #export_values=(values['Полный адрес'].encode('utf-8'),values['Номер дома'].encode('utf-8'))
        export_string=''
        #for name, valueq in values:
        export_string += '"'+values['addrFull']+'",'
        export_string += '"'+values['admArea']+'",'
        export_string += '"'+values['nomerDoma']+'",'
        export_string += '"'+values['nomerKorpusa']+'",'
        export_string += '"'+values['nomerStroenia']+'",'
        export_string += '"'+values['priznakVladenia']+'",'
        export_string += '"'+values['priznakSooruzenia']+'",'


        print export_string

        fs = open('address_reestr_moscow.csv','a')
        fs.write(export_string+'"'+geom.wkt+'"'+"\n")
        fs.close()
        print '=================================='





