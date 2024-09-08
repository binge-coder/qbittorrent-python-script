from decouple import config     #to get login details from .env 
import qbittorrentapi
import time
import os_specific_notification as myOs


total_download_limit_MB =  2
shutdown_on_finish = False
shutdown_on_speed_decrease = False


ans1 = input(f"download limit is set to {total_download_limit_MB} MB. Want to change? (y/n): ")
if (ans1 == 'y'):
    new = int(input("specify the new download limit(in MB): ")) 
    total_download_limit_MB = new
ans2 = input("want script to shutdown os after all torrents are paused (when it reaches download limit) ? (y/n): ")
if (ans2 == 'y'):
    shutdown_on_finish = True
ans3 = input("do you want script to shutdown os when internet speed is decreased (before reaching download limit) ? ")
if (ans3 == 'y'):
    shutdown_on_speed_decrease = True

total_download_limit_BYTES = total_download_limit_MB * (1024) * (1024) # this needs to be below the setting custom download limit prompt.

# done
# def OS_Shutdown():
#     if shutdown == True: #made if condition so that i dont shut it down by mistake
#         # os.system("shutdown /s /d[u:]  /t 60 ") #this may not work or may malfunction. its windows specific i think
#         notify2.init("qbit_script_downlimit.py is shutting down pc")
#         n_os_shutdown = notify2.Notification("shutting down pc", message = "pc will be shutdown in a minute")
#         n_os_shutdown.set_urgency(notify2.URGENCY_CRITICAL)
#         n_os_shutdown.show()
#         os.system("shutdown -P") #for linux

# done
# def notify_shutdown():
#     notify2.init("qbittorrentapi reached the set dl limit")
#     n_shutdown = notify2.Notification(f"Used up {total_download_limit_MB} MB in qbit",message = "paused all torrents")
#     n_shutdown.set_urgency(notify2.URGENCY_CRITICAL)
#     n_shutdown.show()

# done
# def notify_data_finish():
#     notify2.init("downloads are not paused but speed is seems slow")
#     n_data_finish = notify2.Notification(f"download speed is now {speed}", message = "mobile data seems to be exhausted, use another phone")

# done
# def shutdown_procedure():

#     notify_shutdown()
#     qbt_client.torrents.pause.all()
#     # qbt_client.app_shutdown() #it does not actually shutdown but instead minimises to system tray
#     OS_Shutdown()
#     qbt_client.auth_log_out()

print("authorising...")
qbt_client = qbittorrentapi.Client(host = "localhost:8080", username = config('USER'), password = config('PASSWORD'))
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
                myOs.osSpecific("notify_data_finish")

    print(f"Current total session download is: {total_downloaded_in_session / (1024 * 1024)} MB")

    if(total_downloaded_in_session > total_download_limit_BYTES):
        # os_specific_notification
        myOs.osSpecific("shutdown_procedure")
        quit()

    time.sleep(5)    # argument is in seconds
    


"""
# shutdown the computer
if shutdown == True: #made if condition so that i dont shut it down by mistake
    os.system("shutdown /s /d[u:]  /t 60 ") #this may not work or may malfunction
"""


