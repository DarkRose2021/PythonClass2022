from importlib.resources import contents
from bs4 import BeautifulSoup
from requests import get

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_video_games'

response = get(url)
# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

tables = soup.find_all('table')
# print(len(tables))
# print(tables[2])

gameTable = soup.find('table', {'class': {'wikitable'}})
# print(gameTable)

gameBody = gameTable.find('tbody')
gameTrs = gameBody.find_all('tr')

game_list = []
for tr in gameTrs:
    gameTds = tr.find_all('td')
    
    td_list = []
    for td in gameTds:
        if td.find('sup'):
            the_sups = td.find_all('sup')
            for sups in the_sups:
                sups.decompose()
        
        if td.find('a'):
            contents = td.find('a').contents[0]
            if td.find('a').find('i'):
                contents = td.find('a').find('i').contents[0]
        elif td.find('span'):
            contents = td.find('span').contents[0]
        else:
            contents = td.contents[0]
            
        contents = str(contents)
        contents = contents.replace('\n', '')
        
        if contents != '':
            td_list.append(contents)
    if td_list != []:
        game_list.append(td_list)
    
print(game_list)