# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:25:50 2019

@author: Manuel
"""
""" Este é un exemplo de manexo dun PDF
para logo realizar un histograma básico con el.
O codigo ten dúas partes:
na primeira, usamos PyPDF2 e unicode para:
    1) abrir o documento pdf e poder usalo
    2) as paxinas de dito documento estan en unicode; precisamos ASCII para que non haxa problemas cos diferntes caracters (tiles, que desapareceran)
    Asi que tamen o convertemos a ascii usando unidecode.
    3) na terceira parte facemos unha pequena transformacion do texto que conseguimos na parte1, que sae lixeiramente alterado.
    enton, para poder procesalo correctamente, eliminamos rengleiras baleiras, xuntamos palabras separados por guions, etc
    4) finalmente facemos un historigrama eliminando as palabras "ruido" (que, do, etc)
 """
import unidecode
import PyPDF2
#documento no que imos escribir o contido do pdf para logo procesalo
programa_BNG = open('procesamentoBNG.txt', 'w')
pdf_aberto = open('BNG19.pdf', 'rb')
pdfLector = PyPDF2.PdfFileReader(pdf_aberto)
numero_pax = pdfLector.numPages
for i in range(numero_pax):
    paxina = pdfLector.getPage(i)
    #print(paxina.extractText())
    # está en unicode, temos que pasalo a ascii
    pax= unidecode.unidecode(paxina.extractText())
    
   # ascii_page = page.extractText().encode('utf-8', 'replace')
    programa_BNG.write(pax)
    
pdf_aberto.close()
mas_frecuentes = dict()
palabro=''    
programa_BNG = open('procesamentoBNG.txt', 'r')
for linea in programa_BNG:
    linea=linea.strip()
    palabras=linea.split() 
    if not palabras or palabras[0]=='-': #comprobando se a liña está baleira ou é só un guión
        continue;
    if palabras[0][0]=='-': #nesta parte estou xuntando as palabras de duas liñas separados por un guion:
                            #Exemplo:
                            #casa 
                            #-mento
                            #palabras_sen_guion=casamento
        palabra_sen_guion= palabro + palabras[0][1:]
        palabras.append(palabra_sen_guion)
    
    palabro=palabras.pop(len(palabras)-1) # gardo a ultima palabra ('casa' por se hai guion na seguinte liña.
                                        #se o hai, concaténoa coa seguinte
                                        
    for palabra in palabras: #minusculas para que no haxa discordancias
        mas_frecuentes[palabra.lower()]=mas_frecuentes.get(palabra.lower(), 0) + 1
programa_BNG.close()
conx_prep_art= ['a', 'agas', 'ante', 'ate', 'baixo', 'cabo', 'canda', 'cara a', 'con', 'contra', 'de', 'deica', 'desde', 'en', 'entre', 
                           'para', 'perante', 'por', 'segundo', 'sen', 'so', 'sobre', 'tras',
                            'consonte', 'diante', 'durante', 'menos', 'onda', 'salvo', 'senón', 'tirante','tamen',
                            'mais', 'un', 'unha', 'o', 'e', 'que', 'da', 'do', 'dos', 'das','como','no','l', 'os', 'as', 'na', 'ao', 'se', '*']
histograma_ordeado = list()
for palabrexa, frecuencia in mas_frecuentes.items():
    if palabrexa in conx_prep_art:
        continue
    histograma_ordeado.append((frecuencia, palabrexa))
histograma_ordeado.sort(reverse=True)
print(histograma_ordeado[0:20])

casa = input()
programa_BNG = open('procesamentoBNGAbril.txt', 'w')
pdf_aberto = open(casa, 'rb')
pdfLector = PyPDF2.PdfFileReader(pdf_aberto)
numero_pax = pdfLector.numPages
for i in range(numero_pax):
    paxina = pdfLector.getPage(i)
    #print(paxina.extractText())
    # está en unicode, temos que pasalo a ascii
    pax= unidecode.unidecode(paxina.extractText())
    
   # ascii_page = page.extractText().encode('utf-8', 'replace')
    programa_BNG.write(pax)
    
pdf_aberto.close()
mas_frecuentes = dict()
palabro=''    
programa_BNG = open('procesamentoBNGAbril.txt', 'r')
for linea in programa_BNG:
    linea=linea.strip()
    palabras=linea.split() 
    if not palabras or palabras[0]=='-': #comprobando se a liña está baleira ou é só un guión
        continue;
    if palabras[0][0]=='-': #nesta parte estou xuntando as palabras de duas liñas separados por un guion:
                            #Exemplo:
                            #casa 
                            #-mento
                            #palabras_sen_guion=casamento
        palabra_sen_guion= palabro + palabras[0][1:]
        palabras.append(palabra_sen_guion)
    
    palabro=palabras.pop(len(palabras)-1) # gardo a ultima palabra ('casa' por se hai guion na seguinte liña.
                                        #se o hai, concaténoa coa seguinte
                                        
    for palabra in palabras: #minusculas para que no haxa discordancias
        mas_frecuentes[palabra.lower()]=mas_frecuentes.get(palabra.lower(), 0) + 1
programa_BNG.close()
conx_prep_art= ['a', 'agas', 'ante', 'ate', 'baixo', 'cabo', 'canda', 'cara a', 'con', 'contra', 'de', 'deica', 'desde', 'en', 'entre', 
                           'para', 'perante', 'por', 'segundo', 'sen', 'so', 'sobre', 'tras',
                            'consonte', 'diante', 'durante', 'menos', 'onda', 'salvo', 'senón', 'tirante','tamen',
                            'mais', 'un', 'unha', 'o', 'e', 'que', 'da', 'do', 'dos', 'das','como','no','l', 'os', 'as', 'na', 'ao', 'se', '*']
histograma_ordeado = list()
for palabrexa, frecuencia in mas_frecuentes.items():
    if palabrexa in conx_prep_art:
        continue
    histograma_ordeado.append((frecuencia, palabrexa))
histograma_ordeado.sort(reverse=True)
print(histograma_ordeado[0:5])




