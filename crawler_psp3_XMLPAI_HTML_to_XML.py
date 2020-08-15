
import  os
import pathlib
import sqlite3
from bs4 import BeautifulSoup


#variavies iniciais
dados = open('ps3.php', 'r', encoding="utf-8").read()
dados= BeautifulSoup(dados, 'html5lib')
key_titulo = dados.find_all('p', {'class':'textoJogoPS3'})
key_imagem = dados.find_all('img')



titulos = []
for titulo in key_titulo:
    titulo = str(titulo).split("<br/>")[0].split("Jogo: ")[1]
    titulos.append(titulo)
    #print(titulo)

imagens = []
for imagem in key_imagem:
    try:
        if str(imagem).split('ps3/')[1].split('" width')[0][-1] == '>':
            pass
        else:
            imagem = str(imagem).split('ps3/')[1].split('" width')[0]
            imagens.append(imagem)
            #print(imagem)
    except:
        pass

print(len(titulos), len(imagens))





dicionario_jogos = list(zip(list(titulos), list(imagens)))#--





with open('ps3.xml','a') as arquivo:
    texto0 = """<XMBML version="1.0">
    <View id="tcxs_items">
        <Attributes>"""
    arquivo.write(texto0)

    for i in  range(len(dicionario_jogos)):
        titulo = dicionario_jogos[i][0]
        imagem = dicionario_jogos[i][1]
        print(imagem, titulo)
        texto1 = f"""
            <!-- id:{i} | PlayStation PS3 | TCXS PROJECT 2020 | {titulo.upper()} -->
            <Table key="tcxs_{i}">
                <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/ps3/{imagem}</String></Pair>
                <Pair key="title"><String>Jogo: {titulo}</String></Pair>
                <Pair key="info"><String>Idioma do Jogo: INGLES | DUBLADO/LEGENDADO </String></Pair>
            </Table>"""
        arquivo.write(texto1)

    texto2 = """
        </Attributes>
        <Items>"""
    arquivo.write(texto2)

    for i in range(len(dicionario_jogos)):
        titulo = dicionario_jogos[i][0]
        imagem = dicionario_jogos[i][1]
        texto3 = f"""
                <Query class="type:x-xmb/folder-pixmap" key="tcxs_{i}" attr="tcxs_{i}" 
src="xmb://localhost/dev_hdd0/game/HENBSTORE/USRDIR/XMLS/ps3/{imagem[0:-4].replace(' ','')}.xml#tcxs_items" />"""
        arquivo.write(texto3)

    texto4 = """
		</Items>
	</View>
</XMBML>"""
    arquivo.write(texto4)

arquivo.close()
