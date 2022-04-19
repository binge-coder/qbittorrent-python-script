'''

to do :
. set limit to 200 mb
. read files and check size

procedure:
. read file size in the beginning 
. refresh file size and check difference . if difference == 200 mb (200,000,000 Bytes)

'''

from decouple import config     #to get login details from .env 
import qbittorrentapi
import os # to get the file size

shutdown = 0
qbt_client = qbittorrentapi.Client(host = "localhost:8080", username = config('USER'), password = config('PASSWORD'))

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)

'''
for torrent in qbt_client.torrents_info():
    print(f'{torrent.hash[-6:]}: {torrent.name} ({torrent.state})')
'''

'''
#pause all torrents
qbt_client.torrents.pause.all()

'''
def getsize():
    """ this function will be used to get the directory size """




# logging out
qbittorrentapi.auth_log_out()

# shutdown the computer
if shutdown == 1:
    os.system("shutdown /s /d[u:]  /t 60 ") #this may not work or may malfunction



