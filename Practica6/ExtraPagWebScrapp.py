import requests
from bs4 import BeautifulSoup
 
URL=(input(str("Ingresa una pagina web a extraer sus sub paginas \nEjemplo http://www.fcfm.uanl.mx/ \nR:")))

grab=requests.get(URL)
soup=BeautifulSoup(grab.text, 'html.parser')
 
chale = open("subPaginas.txt", "w")
for paginas in soup.find_all("a"):
   dat=str(paginas.get('href'))
   chale.write(dat)
   chale.write("\n")
 
chale.close()