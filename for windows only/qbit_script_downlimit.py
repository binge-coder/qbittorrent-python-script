# from decouple import config     #to get login details from .env 
import qbittorrentapi
import time
import os
from win10toast import ToastNotifier

total_download_limit_MB =  500
shutdown_on_limit_reach = False
shutdown_on_speed_decrease = False


ans1 = input(f"Q1- download limit is set to {total_download_limit_MB} MB. Want to change? (y/N): ")
if (ans1 == 'y'):
    new = int(input("specify the new download limit(in MB): ")) 
    total_download_limit_MB = new
ans2 = input("Q2- want script to shutdown os after all torrents are paused (when it reaches download limit) ? (y/N): ")
if (ans2 == 'y'):
    shutdown_on_limit_reach = True
ans3 = input("Q3- do you want script to shutdown os when internet speed is decreased (before reaching download limit) (y/N) ? : ")
if (ans3 == 'y'):
    shutdown_on_speed_decrease = True

total_download_limit_BYTES = total_download_limit_MB * (1024) * (1024) # this needs to be below the setting custom download limit prompt.
def OS_Shutdown():
    n_os_shutdown = ToastNotifier()
    n_os_shutdown.show_toast(
        "shutting down pc",
        "pc will be shut down in a minute (qbit_script_downlimit.py)",
        duration = 20,
        threaded = True,
    )
    os.system("shutdown /s /d[u:]0:0  /t 60 ") #windows specific command

def notify_shutdown():
    n_shutdown = ToastNotifier()
    n_shutdown.show_toast(
        f"Used up {total_download_limit_MB} MB in qbit",
        "paused all torrents",
        duration = 20,
        threaded = True,
    )

def shutdown_procedure():
    notify_shutdown()
    qbt_client.torrents.pause.all()
    # qbt_client.app_shutdown() #it does not actually shutdown but instead minimises to system tray
    if (shutdown_on_limit_reach == True): 
        OS_Shutdown()
    qbt_client.auth_log_out()


def notify_data_finish():
    n_data_finish = ToastNotifier()
    n_data_finish.show_toast(
        f"download speed is now {speed}",
        "mobile data seems to be exhausted, use another phone",
        duration = 20,
        threaded = True,
        )
    if (shutdown_on_speed_decrease == True):
        OS_Shutdown()

print("authorising...")
# qbt_client = qbittorrentapi.Client(host = "localhost:8080", username = config('USER'), password = config('PASSWORD'))
qbt_client = qbittorrentapi.Client(host = "localhost:8080", username = "admin", password = "kkthegreat")
# go to qbittorrent settings, under web ui, add username and password from env file

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)
else:
    print("authorisation successful")


""" loop for continuous checking of torrent info """
while(True):
    total_downloaded_in_session = 0
    for torrent in qbt_client.torrents_info():
        if(torrent.state == 'downloading'):
            total_downloaded_in_session = total_downloaded_in_session + torrent.downloaded_session
            if(torrent.dlspeed < 10000): # 10KiB/s
                speed = torrent.dlspeed
                # os_specific_notification
                notify_data_finish()

    # print(f"Current total session download is: {total_downloaded_in_session / (1024 * 1024)} MB")

    if(total_downloaded_in_session > total_download_limit_BYTES):
        # os_specific_notification
        shutdown_procedure()
        quit()

    time.sleep(5)    # argument is in seconds
    


"""
# shutdown the computer
if shutdown == True: #made if condition so that i dont shut it down by mistake
    os.system("shutdown /s /d[u:]  /t 60 ") #this may not work or may malfunction
"""


