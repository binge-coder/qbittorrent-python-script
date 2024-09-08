
# from logging import shutdown
from decouple import config     #to get login details from .env 
import qbittorrentapi
import notify2
import time
import os


def OS_Shutdown():
        # os.system("shutdown /s /d[u:]  /t 60 ") #this may not work or may malfunction. its windows specific i think
        os.system("shutdown -P") #for linux

def notify():
    notify2.init("qbittorrentapi reached the set dl limit")
    n_shutdown = notify2.Notification(f"qbittorrent will shutdown pc after 1 min",message = "download speed has dipped")
    n_shutdown.set_urgency(notify2.URGENCY_CRITICAL)
    n_shutdown.show()

def shutdown_procedure():
    notify()
    qbt_client.torrents.pause.all()
    qbt_client.app_shutdown() #it does not actually shutdown but instead minimises to system tray
    OS_Shutdown()
    qbt_client.auth_log_out()
    quit()

print("authorising...")
qbt_client = qbittorrentapi.Client(host = "localhost:8080", username = config('USER'), password = config('PASSWORD'))

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)
else:
    print("authorisation successful")


""" loop for continuous checking of torrent info """
time.sleep(60) # initially the dl speed is slow so check after some time
while(True):
    total_downloaded_in_session = 0
    for torrent in qbt_client.torrents_info():
        if(torrent.state == 'downloading'):
            if(torrent.dlspeed < 10000): # 10KiB/s
                shutdown_procedure()
    time.sleep(5)    # argument is in seconds

# 'dlspeed' # 1 mbps = 1,042,735


    


"""
# shutdown the computer
if shutdown == True: #made if condition so that i dont shut it down by mistake
    os.system("shutdown /s /d[u:]  /t 60 ") #this may not work or may malfunction
"""


