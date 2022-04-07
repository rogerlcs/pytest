import threading
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()




def checkstatus(host, proxy):
    result = open("result.txt","at")
    proxies = {"http" : "http://%s:80" % (proxy),
               "https" : "http://%s:80" % (proxy)}
    try:
        r = requests.get("http://"+host, proxies = proxies, timeout = 3)
        if r.status_code == 200:
            print(Fore.GREEN + "%s,%s - %s\n" % (host,proxy,r.status_code))
            result.write("%s,%s - 200OK\n" % (host,proxy))
        else:
            print(Fore.RED + "%s,%s - %s\n" % (host,proxy,r.status_code))
        result.close()
    except:
        print(Fore.RED + "%s,%s - 400\n" % (host,proxy))
        result.close()
    


def main():
    proxyarq = str(input("Arquivo proxy:"))
    hostarq = str(input("Arquivo host:"))
    with open(proxyarq,'rt') as file:
        line = file.readline()
        while line:
            proxy = line.strip('\n')
            with open(hostarq,'rt') as file2:
                line2 = file2.readline()
                while line2:
                    host = line2.strip('\n')
                    if len(threading.enumerate()) < 10:
                        t = threading.Thread(target = checkstatus, args = (host,proxy))
                        t.start()
                        line2 = file2.readline()
            line = file.readline()

main() 