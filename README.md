# Torrent-Email
this python script will email you the magnet url of the latest TV show once you have fed it the list. 
this would be a python script which would send you an email with the magnet url of the shows that you have in a.txt file in the same directory

for instance in my case I am going to be running this script on pyhtonanywhere.com and have scheduked i to run everyday at 9 AM IST.
this script will only send you the magnet of the latest epoisode of the TV series that you have addded in the .txt file

#Present Features
This script will take the name of the movies in the given text file, scrap rarbg.to and store the magnet links related to each movie in seperate json files

#Requirements
* Python3
* beautifulsoup4
* requests

#Basic usage
`python3 torrent-scrapper.py shows.txt`

#File with Show/Movie search names
Please make sure that the text file that has the names of the TV shows/Movies is in the format like the following

*1=Show+1+name
*2=Show+2+name

this is important or the json file that is generated wont have the magnet url of the torrent
