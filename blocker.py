import time
from datetime import datetime as dt

ipLocalMachine = "127.0.0.1"
blockedUrl = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]
startTime = "09:00:00"
endTime = "18:00:00"

hostsPath ="c:\Windows\System32\drivers\etc\hosts"

now = dt.now()
currTime = now.strftime("%H:%M:%S")

while True:
    if(startTime<=currTime and currTime<=endTime):
        print("Working Hours")
        with open(hostsPath,"r+") as file:
            content= file.read()
            for url in blockedUrl:
                if url in content:
                    pass
                else:
                    file.write("\n"+ipLocalMachine+" "+url+"\n")

    else: #AA_COMMAND_REMOVE_HOSTS
        print("Non Working Hours")
        with open(hostsPath,"r+") as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                if not any(url in line for url in blockedUrl):
                    file.write(line)
                file.truncate()
    time.sleep(10)

    