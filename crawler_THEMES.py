import lxml.etree as ET

file = ET.parse('temas.xml')
root = file.getroot()

for elem in root.findall('.//Pair[@key="icon"]'):
    print(elem)
    check = elem.find('.//String')
    print(check.text)
    check.text = check.text.replace(str(check.text),'/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/menu/temas.png')





file.write('temas_final.xml')