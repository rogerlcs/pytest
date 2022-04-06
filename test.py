from requests import Request, Session
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def checkstatus(host, proxy):
    proxies = {"http" : "http://%s:80" % (proxy),
               "https" : "http://%s:80" % (proxy)}
    try:
        s = Session()
        r = Request('CONNECT',"http://"+host)
        prepped = r.prepare()
        resp = s.send(prepped, proxies = proxies, timeout = 3) 
        return resp.status_code
    except OSError:
        return "400"
    else:
        return "erro"
    


def main():
    nomearq = str(input("Arquivo:"))
    with open(nomearq,'rt') as file:
        line = file.readline()
        while line:
            line = line.strip('\n')
            host,proxy = line.split(',')
            status = checkstatus(host, proxy)
            if status == 200:
                print(Fore.GREEN + "%s - %s" % (line,status))
            else:
                print(Fore.RED + "%s - %s" % (line,status))
            line = file.readline()

main() 