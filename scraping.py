from bs4 import BeautifulSoup
import requests
import csv

#import website and create lists for information to be scraped
page = requests.get("https://sunrisehouse.com/stop-drinking-alcohol/percentage-contents/#Alcohol-Percentage-in-Drinks")
soup = BeautifulSoup(page.content, 'html.parser')
alclist=list()
averagelist = list()

#specifies data that is needed from websit
content = soup.find_all('li', style='text-align: left;')
for i in range(len(content)):
    split = content[i].get_text().split('|')
    alc = split[0][:-1]
    alclist.append(alc)
    percent = split[1][6:-1]
    if '-' in percent:
        percent = percent.split('-')
        average=(int(percent[0])+int(percent[1]))/2
        averagelist.append(average)
    else:
        averagelist.append(int(percent))
        
#writes scraped data into csv        
with open('scrapedcsv.csv', mode='w', newline = '') as scrapedcsv_file:
        scrapedcsv_writer = csv.writer(scrapedcsv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        scrapedcsv_writer.writerow(alclist)
        scrapedcsv_writer.writerow(averagelist)