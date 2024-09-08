

import os
from qbit_script_downlimit import speed 
from qbit_script_downlimit import qbt_client
from qbit_script_downlimit import total_download_limit_MB
from qbit_script_downlimit import shutdown_on_finish
from qbit_script_downlimit import shutdown_on_speed_decrease

try:
    import notify2
except ModuleNotFoundError:
    pass

def OS_Shutdown():
    #made if condition so that i dont shut it down by mistake
    # os.system("shutdown /s /d[u:]  /t 60 ") #this may not work or may malfunction. its windows specific i think
    notify2.init("qbit_script_downlimit.py is shutting down pc")
    n_os_shutdown = notify2.Notification("shutting down pc", message = "pc will be shutdown in a minute")
    n_os_shutdown.set_urgency(notify2.URGENCY_CRITICAL)
    n_os_shutdown.show()
    os.system("shutdown -P") #for linux

def notify_data_finish():
    notify2.init("downloads are not paused but speed is seems slow")
    n_data_finish = notify2.Notification(f"download speed is now {speed}", message = "mobile data seems to be exhausted, use another phone")
    n_data_finish.set_urgency(notify2.URGENCY_CRITICAL)
    n_data_finish.show()
    if (shutdown_on_speed_decrease == True): 
        OS_Shutdown()

def notify_shutdown():
    notify2.init("qbittorrentapi reached the set dl limit")
    n_shutdown = notify2.Notification(f"Used up {total_download_limit_MB} MB in qbit",message = "paused all torrents")
    n_shutdown.set_urgency(notify2.URGENCY_CRITICAL)
    n_shutdown.show()

def shutdown_procedure():

    notify_shutdown()
    qbt_client.torrents.pause.all()
    # qbt_client.app_shutdown() #it does not actually shutdown but instead minimises to system tray
    if (shutdown_on_finish == True): 
        OS_Shutdown()
    qbt_client.auth_log_out()

def start(arg):
    if(arg == "notify_data_finish"):
        notify_data_finish()
    elif(arg == "shutdown_procedure"):
        shutdown_procedure()
