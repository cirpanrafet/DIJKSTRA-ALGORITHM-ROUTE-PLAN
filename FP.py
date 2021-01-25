# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 22:25:46 2021

3@author: cirpan
"""
#DIJKSTRA ALGORITHM, ROUTE PLANING IN TURKEY

import numpy as np
import pandas as pd
import json
from geographiclib.geodesic import Geodesic
from geojson import MultiLineString

cityinf=[
  {
    "id": 1,
    "name": "Adana",
    "latitude": 37.0000,
    "longitude": 35.3213,
    "population": 2183167,
    
  },
  {
    "id": 2,
    "name": "Adıyaman",
    "latitude": 37.7648,
    "longitude": 38.2786,
    "population": 602774,
    "region": "Güneydoğu Anadolu"
  },
  {
    "id": 3,
    "name": "Afyonkarahisar",
    "latitude": 38.7507,
    "longitude": 30.5567,
    "population": 709015,
    "region": "Ege"
  },
  {
    "id": 4,
    "name": "Ağrı",
    "latitude": 39.7191,
    "longitude": 43.0503,
    "population": 547210,
    "region": "Doğu Anadolu"
  },
  {
    "id": 5,
    "name": "Amasya",
    "latitude": 40.6499,
    "longitude": 35.8353,
    "population": 322167,
    "region": "Karadeniz"
  },
  {
    "id": 6,
    "name": "Ankara",
    "latitude": 39.9208,
    "longitude": 32.8541,
    "population": 5270575,
    "region": "İç Anadolu"
  },
  {
    "id": 7,
    "name": "Antalya",
    "latitude": 36.8841,
    "longitude": 30.7056,
    "population": 2288456,
    "region": "Akdeniz"
  },
  {
    "id": 8,
    "name": "Artvin",
    "latitude": 41.1828,
    "longitude": 41.8183,
    "population": 168370,
    "region": "Karadeniz"
  },
  {
    "id": 9,
    "name": "Aydın",
    "latitude": 37.8560,
    "longitude": 27.8416,
    "population": 1053506,
    "region": "Ege"
  },
  {
    "id": 10,
    "name": "Balıkesir",
    "latitude": 39.6484,
    "longitude": 27.8826,
    "population": 1186688,
    "region": "Ege"
  },
  {
    "id": 11,
    "name": "Bilecik",
    "latitude": 40.0567,
    "longitude": 30.0665,
    "population": 212361,
    "region": "Marmara"
  },
  {
    "id": 12,
    "name": "Bingöl",
    "latitude": 39.0626,
    "longitude": 40.7696,
    "population": 267184,
    "region": "Doğu Anadolu"
  },
  {
    "id": 13,
    "name": "Bitlis",
    "latitude": 38.3938,
    "longitude": 42.1232,
    "population": 267184,
    "region": "Doğu Anadolu"
  },
  {
    "id": 14,
    "name": "Bolu",
    "latitude": 40.5760,
    "longitude": 31.5788,
    "population": 291095,
    "region": "Karadeniz"
  },
  {
    "id": 15,
    "name": "Burdur",
    "latitude": 37.4613,
    "longitude": 30.0665,
    "population": 258339,
    "region": "Akdeniz"
  },
  {
    "id": 16,
    "name": "Bursa",
    "latitude": 40.2669,
    "longitude": 29.0634,
    "population": 2842547,
    "region": "Marmara"
  },
  {
    "id": 17,
    "name": "Çanakkale",
    "latitude": 40.1553,
    "longitude": 26.4142,
    "population": 513341,
    "region": "Marmara"
  },
  {
    "id": 18,
    "name": "Çankırı",
    "latitude": 40.6013,
    "longitude": 33.6134,
    "population": 180945,
    "region": "İç Anadolu"
  },
  {
    "id": 19,
    "name": "Çorum",
    "latitude": 40.5506,
    "longitude": 34.9556,
    "population": 525180,
    "region": "Karadeniz"
  },
  {
    "id": 20,
    "name": "Denizli",
    "latitude": 37.7765,
    "longitude": 29.0864,
    "population": 993442,
    "region": "Ege"
  },
  {
    "id": 21,
    "name": "Diyarbakır",
    "latitude": 37.9144,
    "longitude": 40.2306,
    "population": 1654196,
    "region": "Güneydoğu Anadolu"
  },
  {
    "id": 22,
    "name": "Edirne",
    "latitude": 41.6818,
    "longitude": 26.5623,
    "population": 402537,
    "region": "Marmara"
  },
  {
    "id": 23,
    "name": "Elâzığ",
    "latitude": 38.6810,
    "longitude": 39.2264,
    "population": 574304,
    "region": "Doğu Anadolu"
  },
  {
    "id": 24,
    "name": "Erzincan",
    "latitude": 39.7500,
    "longitude": 39.5000,
    "population": 222918,
    "region": "Doğu Anadolu"
  },
  {
    "id": 25,
    "name": "Erzurum",
    "latitude": 39.9000,
    "longitude": 41.2700,
    "population": 762321,
    "region": "Doğu Anadolu"
  },
  {
    "id": 26,
    "name": "Eskişehir",
    "latitude": 39.7767,
    "longitude": 30.5206,
    "population": 826716,
    "region": "İç Anadolu"
  },
  {
    "id": 27,
    "name": "Gaziantep",
    "latitude": 37.0662,
    "longitude": 37.3833,
    "population": 1931836,
    "region": "Güneydoğu Anadolu"
  },
  {
    "id": 28,
    "name": "Giresun",
    "latitude": 40.9128,
    "longitude": 38.3895,
    "population": 426686,
    "region": "Karadeniz"
  },
  {
    "id": 29,
    "name": "Gümüşhane",
    "latitude": 40.4386,
    "longitude": 39.5086,
    "population": 151449,
    "region": "Karadeniz"
  },
  {
    "id": 30,
    "name": "Hakkâri",
    "latitude": 37.5833,
    "longitude": 43.7333,
    "population": 278775,
    "region": "Doğu Anadolu"
  },
  {
    "id": 31,
    "name": "Hatay",
    "latitude": 36.4018,
    "longitude": 36.3498,
    "population": 1533507,
    "region": "Akdeniz"
  },
  {
    "id": 32,
    "name": "Isparta",
    "latitude": 37.7648,
    "longitude": 30.5566,
    "population": 421766,
    "region": "Akdeniz"
  },
  {
    "id": 33,
    "name": "Mersin",
    "latitude": 36.8000,
    "longitude": 34.6333,
    "population": 1745221,
    "region": "Akdeniz"
  },
  {
    "id": 34,
    "name": "İstanbul",
    "latitude": 41.0053,
    "longitude": 28.9770,
    "population": 14657434,
    "region": "Marmara"
  },
  {
    "id": 35,
    "name": "İzmir",
    "latitude": 38.4189,
    "longitude": 27.1287,
    "population": 4168415,
    "region": "Ege"
  },
  {
    "id": 36,
    "name": "Kars",
    "latitude": 40.6167,
    "longitude": 43.1000,
    "population": 292660,
    "region": "Doğu Anadolu"
  },
  {
    "id": 37,
    "name": "Kastamonu",
    "latitude": 41.3887,
    "longitude": 33.7827,
    "population": 372633,
    "region": "Karadeniz"
  },
  {
    "id": 38,
    "name": "Kayseri",
    "latitude": 38.7312,
    "longitude": 35.4787,
    "population": 1341056,
    "region": "İç Anadolu"
  },
  {
    "id": 39,
    "name": "Kırklareli",
    "latitude": 41.7333,
    "longitude": 27.2167,
    "population": 346973,
    "region": "Marmara"
  },
  {
    "id": 40,
    "name": "Kırşehir",
    "latitude": 39.1425,
    "longitude": 34.1709,
    "population": 225562,
    "region": "İç Anadolu"
  },
  {
    "id": 41,
    "name": "Kocaeli",
    "latitude": 40.8533,
    "longitude": 29.8815,
    "population": 1780055,
    "region": "Marmara"
  },
  {
    "id": 42,
    "name": "Konya",
    "latitude": 37.8667,
    "longitude": 32.4833,
    "population": 2130544,
    "region": "İç Anadolu"
  },
  {
    "id": 43,
    "name": "Kütahya",
    "latitude": 39.4167,
    "longitude": 29.9833,
    "population": 571463,
    "region": "Ege"
  },
  {
    "id": 44,
    "name": "Malatya",
    "latitude": 38.3552,
    "longitude": 38.3095,
    "population": 772904,
    "region": "Doğu Anadolu"
  },
  {
    "id": 45,
    "name": "Manisa",
    "latitude": 38.6191,
    "longitude": 27.4289,
    "population": 1380366,
    "region": "Ege"
  },
  {
    "id": 46,
    "name": "Kahramanmaraş",
    "latitude": 37.5858,
    "longitude": 36.9371,
    "population": 1096610,
    "region": "Akdeniz"
  },
  {
    "id": 47,
    "name": "Mardin",
    "latitude": 37.3212,
    "longitude": 40.7245,
    "population": 796591,
    "region": "Güneydoğu Anadolu"
  },
  {
    "id": 48,
    "name": "Muğla",
    "latitude": 37.2153,
    "longitude": 28.3636,
    "population": 908877,
    "region": "Ege"
  },
  {
    "id": 49,
    "name": "Muş",
    "latitude": 38.9462,
    "longitude": 41.7539,
    "population": 408728,
    "region": "Doğu Anadolu"
  },
  {
    "id": 50,
    "name": "Nevşehir",
    "latitude": 38.6939,
    "longitude": 34.6857,
    "population": 286767,
    "region": "İç Anadolu"
  },
  {
    "id": 51,
    "name": "Niğde",
    "latitude": 37.9667,
    "longitude": 34.6833,
    "population": 346114,
    "region": "İç Anadolu"
  },
  {
    "id": 52,
    "name": "Ordu",
    "latitude": 40.9839,
    "longitude": 37.8764,
    "population": 728949,
    "region": "Karadeniz"
  },
  {
    "id": 53,
    "name": "Rize",
    "latitude": 41.0201,
    "longitude": 40.5234,
    "population": 328979,
    "region": "Karadeniz"
  },
  {
    "id": 54,
    "name": "Sakarya",
    "latitude": 40.6940,
    "longitude": 30.4358,
    "population": 953181,
    "region": "Marmara"
  },
  {
    "id": 55,
    "name": "Samsun",
    "latitude": 41.2928,
    "longitude": 36.3313,
    "population": 1279884,
    "region": "Karadeniz"
  },
  {
    "id": 56,
    "name": "Siirt",
    "latitude": 37.9333,
    "longitude": 41.9500,
    "population": 320351,
    "region": "Güneydoğu Anadolu"
  },
  {
    "id": 57,
    "name": "Sinop",
    "latitude": 42.0231,
    "longitude": 35.1531,
    "population": 204133,
    "region": "Karadeniz"
  },
  {
    "id": 58,
    "name": "Sivas",
    "latitude": 39.7477,
    "longitude": 37.0179,
    "population": 618617,
    "region": "İç Anadolu"
  },
  {
    "id": 59,
    "name": "Tekirdağ",
    "latitude": 40.9833,
    "longitude": 27.5167,
    "population": 937910,
    "region": "Marmara"
  },
  {
    "id": 60,
    "name": "Tokat",
    "latitude": 40.3167,
    "longitude": 36.5500,
    "population": 593990,
    "region": "Karadeniz"
  },
  {
    "id": 61,
    "name": "Trabzon",
    "latitude": 41.0015,
    "longitude": 39.7178,
    "population": 768417,
    "region": "Karadeniz"
  },
  {
    "id": 62,
    "name": "Tunceli",
    "latitude": 39.3074,
    "longitude": 39.4388,
    "population": 86076,
    "region": "Doğu Anadolu"
  },
  {
    "id": 63,
    "name": "Şanlıurfa",
    "latitude": 37.1591,
    "longitude": 38.7969,
    "population": 1892320,
    "region": "Güneydoğu Anadolu"
  },
  {
    "id": 64,
    "name": "Uşak",
    "latitude": 38.6823,
    "longitude": 29.4082,
    "population": 353048,
    "region": "Ege"
  },
  {
    "id": 65,
    "name": "Van",
    "latitude": 38.4891,
    "longitude": 43.4089,
    "population": 1096397,
    "region": "Doğu Anadolu"
  },
  {
    "id": 66,
    "name": "Yozgat",
    "latitude": 39.8181,
    "longitude": 34.8147,
    "population": 419440,
    "region": "İç Anadolu"
  },
  {
    "id": 67,
    "name": "Zonguldak",
    "latitude": 41.4564,
    "longitude": 31.7987,
    "population": 595907,
    "region": "Karadeniz"
  },
  {
    "id": 68,
    "name": "Aksaray",
    "latitude": 38.3687,
    "longitude": 34.0370,
    "population": 386514,
    "region": "İç Anadolu"
  },
  {
    "id": 69,
    "name": "Bayburt",
    "latitude": 40.2552,
    "longitude": 40.2249,
    "population": 78550,
    "region": "Karadeniz"
  },
  {
    "id": 70,
    "name": "Karaman",
    "latitude": 37.1759,
    "longitude": 33.2287,
    "population": 242196,
    "region": "İç Anadolu"
  },
  {
    "id": 71,
    "name": "Kırıkkale",
    "latitude": 39.8468,
    "longitude": 33.5153,
    "population": 270271,
    "region": "İç Anadolu"
  },
  {
    "id": 72,
    "name": "Batman",
    "latitude": 37.8812,
    "longitude": 41.1351,
    "population": 566633,
    "region": "Güneydoğu Anadolu"
  },
  {
    "id": 73,
    "name": "Şırnak",
    "latitude": 37.4187,
    "longitude": 42.4918,
    "population": 490184,
    "region": "Güneydoğu Anadolu"
  },
  {
    "id": 74,
    "name": "Bartın",
    "latitude": 41.5811,
    "longitude": 32.4610,
    "population": 190708,
    "region": "Karadeniz"
  },
  {
    "id": 75,
    "name": "Ardahan",
    "latitude": 41.1105,
    "longitude": 42.7022,
    "population": 99265,
    "region": "Doğu Anadolu"
  },
  {
    "id": 76,
    "name": "Iğdır",
    "latitude": 39.8880,
    "longitude": 44.0048,
    "population": 192435,
    "region": "Doğu Anadolu"
  },
  {
    "id": 77,
    "name": "Yalova",
    "latitude": 40.6500,
    "longitude": 29.2667,
    "population": 233009,
    "region": "Marmara"
  },
  {
    "id": 78,
    "name": "Karabük",
    "latitude": 41.2061,
    "longitude": 32.6204,
    "population": 236978,
    "region": "Karadeniz"
  },
  {
    "id": 79,
    "name": "Kilis",
    "latitude": 36.7184,
    "longitude": 37.1212,
    "population": 130655,
    "region": "Güneydoğu Anadolu"
  },
  {
    "id": 80,
    "name": "Osmaniye",
    "latitude": 37.2130,
    "longitude": 36.1763,
    "population": 512873,
    "region": "Akdeniz"
  },
  {
    "id": 81,
    "name": "Düzce",
    "latitude": 40.8438,
    "longitude": 31.1565,
    "population": 360388,
    "region": "Karadeniz"
  }
]
  
graph={#türkiye şehir haritası şehir komşulukları

'1' : {'31':193,'80':98,'46':196,'38':304,'51':181,'33':86},
  '2' : {'63':112,'21':205,'44':106,'46':162,'27':152},
  '3' : {'32':165,'42':227,'26':132,'43':96,'64':111,'20':218,'15':165},
  '4' : {'65':228,'76':145,'36':180,'25':184,'49':244,'13':234},
  '5' : {'66':175,'60':114,'55':124,'19':92},
  '6' : {'42':262,'68':229,'40':179,'71':79,'18':132,'14':187,'26':234}, 
  '7' : {'33':485,'70':327,'42':303,'32':127,'15':31,'48':269},
  '8' : {'53':149,'25':195,'75':115},
  '9' : {'48':98,'20':125,'45':137,'35':112},
  '10': {'35':202,'45':151,'43':227,'16':148,'17':193},
  '11': {'43':112,'26':88,'14':215,'54':107,'16':96,'41':141},
  '12': {'21':142,'49':115,'25':180,'24':234,'62':130,'23':142},
  '13': {'56':95,'65':160,'4':234,'49':84,'72':134},
  '14': {'26':217,'6':187,'18':208,'67':158,'81':51,'54':3,'11':215},
  '15': {'48':238,'7':31,'32':32,'3':165,'20':140}, 
  '16': {'10':148,'43':182,'11':96,'54':184,'41':132,'77':68},
  '17': {'10':193,'59':195,'22':223},
  '18': {'6':132,'71':107,'19':156,'37':107,'67':262,'14':208,'78':161},
  '19': {'66':107,'5':92,'55':168,'57':264,'37':204,'18':156,'71':165},
  '20': {'48':141,'15':140,'3':218,'64':155,'45':203,'9':125},
  '21': {'63':179,'47':93,'72':98,'49':209,'12':142,'23':154,'44':229,'2':205},
  '22': {'17':223,'59':143,'39':65}, 
  '23': {'21':154,'12':142,'62':78,'24':216,'44':99},
  '24': {'23':216,'62':127,'12':234,'25':188,'69':122,'29':129,'28':287,'58':246,'44':301},
  '25': {'12':180,'49':204,'4':184,'36':206,'75':227,'8':195,'53':252,'69':125,'24':188,'61':262},
  '26': {'3':132,'42':333,'6':234,'14':217,'11':88,'43':79},
  '27': {'79':56,'63':150,'2':152,'46':78,'80':135,'31':180},
  '28': {'29':160,'61':130,'24':287,'58':287,'52':48},
  '29': {'24':129,'69':106,'61':103,'28':160},
  '30': {'65':197,'73':195},
  '31': {'79':120,'27':180,'80':127,'1':193},
  '32': {'7':127,'42':240,'3':165,'15':32},
  '33': {'1':86,'51':193,'42':357,'70':296,'7':485},
  '34': {'41':104,'59':146,'39':213},
  '35': {'9':112,'45':39,'10':202}, 
  '36': {'4':180,'76':136,'75':90,'25':206},
  '37': {'19':204,'57':183,'18':107,'74':182,'78':112}, 
  '38': {'1':304,'46':275,'58':197,'66':176,'50':85,'51':131},
  '39': {'22':65,'59':117,'34':213},
  '40': {'50':94,'66':115,'71':111,'6':179,'68':94},
  '41': {'77':72,'34':104,'16':132,'11':141,'54':67},
  '42' : {'3':227,'6':262,'7':303,'26':333,'32':240,'70':110,'33':357,'51':225,'68':151},
  '43' : {'26':79,'11':112,'45':314,'64':142,'3':96,'16':182,'10':227},
  '44' : {'23':99,'58':239,'24':301,'46':217,'21':229,'2':106},
  '45' : {'10':151,'43':314,'64':194,'20':203,'9':137,'35':39},
  '46' : {'2':162,'27':78,'79':149,'1':196,'80':107,'38':275,'58':324,'44':217,'79':149},
  '47' : {'73':190,'56':227,'72':144,'21':93,'63':189},
  '48' : {'7':269,'15':238,'20':141,'9':98},
  '49' : {'25':204,'4':244,'13':84,'72':181,'21':209,'12':115},
  '50' : {'38':85,'66':162,'40':94,'68':77,'51':81},
  '51' : {'50':81,'68':119,'42':225,'33':193,'1':181,'38':131},
  '52' : {'28':48,'55':148,'60':191,'58':298},
  '53' : {'25':252,'8':149,'61':80,'69':149},
  '54' : {'41':67,'81':85,'14':3,'11':107,'16':184},
  '55' : {'57':158,'19':168,'5':124,'60':227,'52':148},
  '56' : {'65':255,'73':95,'47':227,'72':87,'13':95},
  '57' : {'55':158,'19':264,'37':183},
  '58' : {'52':298,'28':287,'24':246,'44':239,'46':324,'38':197,'66':224,'60':107},
  '59' : {'22':143,'39':117,'34':146,'17':195},
  '60' : {'52':191,'55':227,'5':114,'66':210,'58':107},
  '61' : {'53':80,'69':138,'29':103,'28':130,'25':262},
  '62' : {'24':127,'12':130,'23':78},
  '63' : {'47':189,'21':179,'2':112,'27':150},
  '64' : {'43':142,'3':111,'20':155,'45':194},
  '65' : {'30':197,'73':363,'56':255,'13':160,'4':228},
  '66' : {'60':210,'58':224,'38':176,'50':162,'40':115,'71':140,'19':107,'5':175},
  '67' : {'78':101,'74':88,'14':158,'81':114,'18':262},
  '68' : {'6':229,'42':151,'40':94,'50':77,'51':119},
  '69' : {'25':125,'53':149,'61':138,'29':106,'24':122},
  '70' : {'42':110,'33':296,'7':327},
  '71' : {'19':165,'66':140,'40':111,'6':79,'18':107},
  '72' : {'56':87,'13':134,'49':181,'21':98,'47':144},
  '73' : {'56':95,'65':363,'30':198,'47':190},
  '74' : {'78':89,'37':182,'67':88},
  '75' : {'25':227,'36':90,'8':115},
  '76' : {'4':145,'36':136},
  '77' : {'41':72,'16':68},
  '78' : {'74':89,'37':112,'18':161,'67':101},
  '79' : {'27':56,'31':120,'46':149},
  '80' : {'27':135,'46':107,'1':98,'31':127},
  '81' : {'67':114,'14':51,'54':85}
}


def dijkstra(graph, baslangıç, bitiş, visited=[], distances={}, predecessors={}):

  if baslangıç == bitiş:
    # En kısa yolu oluşturur ve görüntüleriz
    rota = []
    pred = bitiş
    while pred != None:
      rota.append(pred)
      
      pred = predecessors.get(pred, None)  # ata dizisinde fınısh varmı varsa değerini döndür yoksa none

    #yolu güzel bir şekilde görüntülemek için diziyi tersine çevirir.
    readable = rota[0]
    for index in range(1, len(rota)):  # tersten yazdırarak sonucu elde ederiz
      readable = rota[index] + '----->' + readable

    print("ROUTE: " + readable)
   
  else:
    # ilk çalıştırma ise maliyeti başlatır.
    if not visited:  # sadece basta girer
      distances[baslangıç] = 0

    # komsuları gez
    for neighbor in graph[baslangıç]:
      if neighbor not in visited:
        new_distance = distances[baslangıç] + graph[baslangıç][neighbor]
        if new_distance < distances.get(neighbor, float('inf')):
          distances[neighbor] = new_distance

          predecessors[neighbor] = baslangıç
        
    # ziyaret edildi olarak işaretle
    visited.append(baslangıç)  # visited uğranmamış komşulara uğruyor
    
    # şimdi tüm komşular ziyaret edildi: tekrar
    # 'x' mesafeli en az ziyaret edilen düğümü seçin
    # Dijskstra'yı src = 'x' ile çalıştırın
    unvisited = {}
    for k in graph:

      if k not in visited:
       
        unvisited[k] = distances.get(k, float('inf'))
       
    x = min(unvisited, key=unvisited.get)
   
    dijkstra(graph, x, bitiş, visited, distances, predecessors)
   

print('------WE CREATE THE SHORTEST ROUTE FOR YOUR TRAVEL------')
print("CHECK THE PLATE INFORMATION OF THE CITIES YOU WANT TO GO BY THE SHORT WAY")

say1=input("ENTER THE PLATE INFORMATION OF YOUR POINT OF MOVEMENT:")
start_lat = cityinf[int(say1)-1]["latitude"]
start_lon = cityinf[int(say1)-1]["longitude"]

say2=input("ENTER THE PLATE INFORMATION OF THE DESTINATION:")
cities = pd.DataFrame(data={
   'City': [cityinf[int(say2)-1]["name"]],
   'Lat' : [cityinf[int(say2)-1]["latitude"]],
   'Lon' : [cityinf[int(say2)-1]["longitude"]]
})

def haversine_distance(lat1, lon1, lat2, lon2):
   r = 6371
   phi1 = np.radians(lat1)
   phi2 = np.radians(lat2)
   delta_phi = np.radians(lat2 - lat1)
   delta_lambda = np.radians(lon2 - lon1)
   a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
   res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
   return np.round(res, 2)

distances_km = []
for row in cities.itertuples(index=False):
   distances_km.append(
       haversine_distance(start_lat, start_lon, row.Lat, row.Lon)
   )
   
cities['DistanceFrom'] = distances_km

start_name = cityinf[int(say1)-1]["name"]
finish_name = cityinf[int(say2)-1]["name"]

print('')
print('POINT OF MOVEMENT:',(say1),'-',start_name)
print('POINT OF DESTINATION:',(say2),'-',finish_name)
print('')
dijkstra(graph, say1, say2)
print('')
print('DISTANCE BETWEEN',start_name,'-',finish_name,list(cities['DistanceFrom'])[0],"KM")


def geodesic(lat1, lon1, lat2, lon2, steps):
    inverse = Geodesic.WGS84.Inverse(lat1, lon1, lat2, lon2)
    linestrings = []
    coordinates = []

    for i in range(0, steps + 1):
        direct = Geodesic.WGS84.Direct(inverse['lat1'], inverse['lon1'], inverse['azi1'], (i / float(steps)) * inverse['s12'])
        if len(coordinates) > 0:
            if (coordinates[-1][0] < -90 and direct['lon2'] > 90) or (coordinates[-1][0] > 90 and direct['lon2'] < -90):
                linestrings.append(coordinates)
                coordinates = []
        coordinates.append((direct['lon2'], direct['lat2']))

    linestrings.append(coordinates)
    geojson = MultiLineString(linestrings)
    return geojson

linestrings = []

for linestring in geodesic(start_lat, start_lon, row.Lat, row.Lon, 100)['coordinates']:
    linestrings.append(linestring)

with open("GMT203PROJECT_file.json", "w") as write_file:
    json.dump(MultiLineString(linestrings), write_file)


