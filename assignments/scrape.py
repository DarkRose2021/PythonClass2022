from calendar import month
from importlib.resources import contents
from urllib import response
from requests import get
from pip import main
from bs4 import BeautifulSoup
from datetime import date

def scrape():
    url = 'http://neumont.smartcatalogiq.com/2021-2022/Catalog/Academic-Calendar'
    events = []
    titles = []  
    dates = []
    today = date.today().strftime('%b-%d-%Y')
    month, day, year = today.split('-')
    
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    

    main_div = soup.find('div', {'class':{'combinedChild'}})
    all_tables = main_div.find_all('table')

    all_captions = soup.find_all('caption')
    for caption in all_captions:
        contents = caption.contents[0]
        titles.append(contents)
        
        for table in all_tables:
            tempList = []
            for row in table.find('tbody').find_all('tr'):
                contents = row.find_all('td')[0].contents[0]
                contents = contents.replace('\xa0', '')
                tempList.append((contents, row.find_all('td')[1].contents[0]))
        if tempList != []:        
            events.append(tempList)
            
    quarterEvents = ''
    for title in titles:
        for event in events:
            for quarter in event:
                temp = ' '.join(str(x) for x in quarter)
                quarterEvents += str(title)+': \n     ' + temp +'\n'
                contents = title +' '+ quarter[0]
                dates.append(contents)            

    return quarterEvents

def saveEvents():
    file = open('Events.txt', 'w')
    file.write(scrape())
    file.close
    

if __name__ == '__main__':
    scrape()