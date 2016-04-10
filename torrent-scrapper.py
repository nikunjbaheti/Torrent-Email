#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
import json
import sys

target_site = "https://rarbg.to"

if not len(sys.argv)==2:
    print("Usage: "+sys.argv[0]+" <file name>")
    exit()

keywords_table=[]

with open(sys.argv[1],'r') as search_list:
    for line in search_list.readlines():
        keyword = line.split("=")
        if len(keyword) == 2:
            keywords_table.append(keyword[1].strip())

for keyword in keywords_table:
    search_string = target_site+"/torrents.php?search="+keyword
    html_response = requests.get(search_string)
    text_data = html_response.text

    soup = BeautifulSoup(text_data)

    torrent_links = {}
    for link in soup.find_all('a'):
        if re.search(r'^\/torrent\/\w+$',str(link.get('href'))):
            torrent_links[str(link.get('title'))] = target_site+str(link.get('href'))

    magnet_table = {}
    for key in torrent_links.keys():
        magnet_page = requests.get(torrent_links[key])
        magnet_text = magnet_page.text
        magnet_soup = BeautifulSoup(magnet_text)

        for link in magnet_soup.find_all('a'):
            if re.search(r'^magnet',str(link.get('href'))):
                magnet_table[key] = str(link.get('href'))

    with open(keyword.replace('+','-')+'-rarbg-magnet-data.json','w') as fp:
        json.dump(magnet_table,fp)
