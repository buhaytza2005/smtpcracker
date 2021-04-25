# Smtpcracker
## Info
A very basic python3 tool for bruteforce password in smtp server.
## Usage
The first argument is the **txt file with passwords**.                                                                                                                   
The second argument is the **username** or **email** of the target.                                                                                                   
The third is the **smtp server** you want to attack.                    
The last is the **smtp port** you want to attack.                                                
Example: ``python3 smtpcrack.py wordlist.txt crackme@gmail.com smtp.gmail.com 465``
## Requirements
Python version: **3.0**                                                                                                                                                                     
Libraries: smtplib, sys, threading, colorama, pyfiglet (**all available in python3**).
## Warning
This script has been created for **ethical hacking** and **penetration-testing purposes**.                                                                  
Do **NOT use** it **without permission** of the target.                                                                                             
**I am not responsible for what can be done with this script.**
## Common Problems
### Gmail
Nowadays you **cant crack gmail password** with this method, the reason is that you need to turn on *acces to insecure apps*(**disabled by default**).
### Password List
You can find a lot of **password lists** on the **internet** only by searching them but they **arent efficient**.                                                                 
Best option is to **create a custom list** with **cupp** or **similar tools**.
### Problems with libraries
You cant install them with ``pip3 install libraryname``
### Other
If you have any other problem with this script you can report the issue [here](https://github.com/Kik449/smtpcracker/issues)!
