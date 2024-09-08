# from win10toast import ToastNotifier
import os
from qbit_script_downlimit import speed 
from qbit_script_downlimit import qbt_client
from qbit_script_downlimit import total_download_limit_MB
from qbit_script_downlimit import shutdown_on_finish
from qbit_script_downlimit import shutdown_on_speed_decrease

try:
    from win10toast import ToastNotifier
except ModuleNotFoundError:
    pass


# toast.show_toast(
#     "Notification",
#     "Notification body",
#     duration = 20,
#     icon_path = "icon.ico",
#     threaded = True,
# )


def OS_Shutdown():
    n_os_shutdown = ToastNotifier()
    n_os_shutdown.show_toast(
        "shutting down pc",
        "pc will be shut down in a minute (qbit_script_downlimit.py)",
        duration = 20,
        threaded = True,
    )
    os.system("shutdown /s /d[u:]  /t 60 ") #windows specific command

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
    if (shutdown_on_finish == True): 
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



def start(arg):
    if(arg == "notify_data_finish"):
        notify_data_finish()
    elif(arg == "shutdown_procedure"):
        shutdown_procedure()