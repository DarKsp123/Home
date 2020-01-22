import platform
import sys

info = 'OS info is: \n {} \n\nPython version is: {} {}'.format(platform.uname(), sys.version, platform.architecture())
print(info)

with open('D:\OS_info.txt', 'w') as ff:
    ff.write(info)