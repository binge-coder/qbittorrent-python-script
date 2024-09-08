import sys
import Linux_notif
import Windows_notif

def osSpecific(arg):
    os_name = sys.platform
    if (os_name == 'linux'):
        Linux_notif.start(arg)
       
    elif (os_name == 'win32'):
        Windows_notif.start(arg)
    elif (os_name == 'darwin'):
        print("You have Mac system... code was not made for apple machines")
        exit()
    else:
        print("can't determine os")
        exit()

if __name__ == '__main__':
    osSpecific(arg=None)


