from bs4 import BeautifulSoup
import sys
import  os
import pathlib
import sqlite3



"""
#current_file.close()
for path in pathlib.Path("PS1").iterdir():
    if path.is_file():
        current_file = open(path, "r").read()
        #le o xml
        dados_xml = BeautifulSoup(current_file, "xml")
        key_title = dados_xml.find('Pair', {'key':'title'},'String')
        #pega todas strings
        strings = dados_xml.find_all('String')
        string_titulo = str(strings[1])
        #pega a string do titulo limpa
        titulo_splitado = string_titulo.split()[2].split('<')[0]
        titulo = titulo_splitado
        print(titulo)
        
        
        
BASE INICIO:
        with open('1xtreme.xml', 'r') as f:
    data = f.read()
    #print(data)


#le o xml
dados_xml = BeautifulSoup(data, "xml")
print(dados_xml)
key_title = dados_xml.find('Pair', {'key':'title'},'String')
print(key_title)

#pega todas strings
strings = dados_xml.find_all('String')
string_titulo = str(strings[1])
#print(string_titulo)

#pega a string do titulo limpa
titulo_splitado = string_titulo.split()[2].split('<')[0]
titulo = titulo_splitado
print(titulo)

"""
#conn = sqlite3.connect('tcxsDB.db')
#cursor = conn.cursor()
#cursor.execute("""  CREATE TABLE IF NOT EXISTS playstation1  (int_id integer not null primary key autoincrement, icone varchar(5000), titulo varchar(5000), descricao varchar(5000), link varchar(500), data varchar(500));  """)
for path in pathlib.Path("xml_jogos/PS1").iterdir():
    if path.is_file():
        current_file = open(path, "r").read()
        dados_xml = BeautifulSoup(current_file, "xml")
        titulo = str(dados_xml.find('Pair', {'key':'title'},'String').find_all('String')).split()[2].split('<')[0]
        link = str(dados_xml.find('Pair', {'key':'module_action'},'String').find_all('String')[0])[8:-9]
        print(titulo,link)
        gravar = open('teste.txt','a')
        gravar.write(f'{titulo}\n')
print(len(titulo))
gravar.close()
