import os
import sys

def osSpecific():
    os_name = sys.platform
    if (os_name == 'linux'):
        os.system("pip3 install notify2")
    elif (os_name == 'win32'):
    #     # os.system("pip install notify2") notify2 not for windows (first hand experience)
        os.system("pip3 install win10toast")

    elif (os_name == 'darwin'):
        print("You have Mac system... code was not made for apple machines")
        exit()
    else:
        print("can't determine os")
        exit()


def start():
    osSpecific()
    print("\ninstalling qbittorrent-api using pip\n")
    os.system("pip install qbittorrent-api")
    print("\ninstalling python-decouple\n")
    os.system("pip install python-decouple")
    



if __name__ == "__main__":
    start()