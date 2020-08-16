import  os
import pathlib
import sqlite3
from bs4 import BeautifulSoup







#############################################
#
# OBS ESTA INCOMPLETO POIS NAO BATIA AS IMAGENS COM OS XMLS




#variavies iniciais
dados = open('xml_pai/ps2.xml', 'r', encoding="utf-8").read()
dados_xml = BeautifulSoup(dados, "xml")
key_icon = dados_xml.find_all('Pair', {'key':'icon'},'String')
key_nome_xml = dados_xml.find_all('Query')

#le todos nomes de xml no xml pai---------------->
xmls = []
for xml in key_nome_xml:
    try:
        xml = str(xml).split('#')[0].split('PS2/')[1]  #pega o nome de todos arquivos xml no xml pai
        #print(xml)
        if str(xml) == 'battlestadium.xml' or str(xml) == 'tonyskater4.xml':
            pass
        else:
            xmls.append(xml)
    except:
        pass
nome_xml = sorted(xmls) #sorted poe em ordem alfabetica
#print(nome_xml)

#le o nome de todos icones no xml pai---------------->
icones = []
for icone in key_icon:
    #print(icone)
    if '<Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/IMAGES/PS2/tonyskater4.png</String></Pair>'  in str(icone) or   '<Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/IMAGES/PS2/sotc.jpg</String></Pair>'  in str(icone) or '<Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/IMAGES/PS2/gta3.jpg</String></Pair>'  in str(icone) or '<Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/IMAGES/PS2/animefighters.jpg</String></Pair>'  in str(icone) or '<Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/IMAGES/PS1/aviso.png</String></Pair>'  in str(icone) or '<Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/IMAGES/PS1/inf.png</String></Pair>' in str(icone) or '<Pair key="icon"><String>/dev_hdd0/game/TCXSPROJECT/USRDIR/IMAGES/PS1/inf.png</String></Pair>' in str(icone):
        #print('.')
        pass
    else:
        #print(icone)
        icone = str(icone).split('PS2/')[1].split('<')[0]
        if icone == 'aviso.png' or icone == 'inf.png':
            pass
        else:
            icones.append(icone)
nome_icone = sorted(icones)  # sorted poe em ordem alfabetica
print(nome_icone)
print(nome_xml)

dicionario_jogos = dict(zip(list(nome_icone), list(nome_xml)))  # --
#print(dicionario_jogos)
