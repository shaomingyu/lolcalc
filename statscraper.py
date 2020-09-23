import requests
import bs4

#get request to stats dump page
res = requests.get('https://leagueoflegends.fandom.com/wiki/Module:ChampionData/data?action=edit')

#html parsing
soup = bs4.BeautifulSoup(res.text, 'lxml')

#converts useful information to string 
data = str(soup.textarea)

#trimming
data = data[data.find("return"):data.find("-- &lt")]