
'''
refresh file size and check difference . if difference == 200 mb (200,000,000 Bytes)
'''


from decouple import config     #to get login details from .env 
import qbittorrentapi
import notify2

total_download_limit_MB =  500
total_download_limit_BYTES = total_download_limit_MB * (1024) * (1024)
total_downloaded_in_session = 0

def notify():
    notify2.init("qbittorrentapi reached the set dl limit")
    n_shutdown = notify2.Notification(f"Used up {total_download_limit_MB} MB in qbit",message = "shutting down qbittorrent")
    n_shutdown.set_urgency(notify2.URGENCY_NORMAL)
    n_shutdown.show()

def shutdown_procedure():

    notify()
    qbt_client.torrents.pause.all()
    qbt_client.application.shutdown()
    qbittorrentapi.auth_log_out()




qbt_client = qbittorrentapi.Client(host = "localhost:8080", username = config('USER'), password = config('PASSWORD'))

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)


# for torrent in qbt_client.torrents_info():
#     print(f'{torrent.hash[-6:]}: {torrent.name} ({torrent.state})({torrent.downloaded})')

for x in qbt_client.torrents_info():
    print(f"{x}\n")

# for torrent in qbt_client.torrents_info():
#     if(torrent.state == 'downloading'):
#         total_downloaded_in_session = total_downloaded_in_session + torrent.downloaded_session

# if(total_downloaded_in_session > total_download_limit_BYTES):

#     shutdown_procedure()



'''
#to pause all torrents
qbt_client.torrents.pause.all()
'''



# logging out
# qbittorrentapi.auth_log_out()

"""
# shutdown the computer
if shutdown == True: #made if condition so that i dont shut it down by mistake
    os.system("shutdown /s /d[u:]  /t 60 ") #this may not work or may malfunction
"""


