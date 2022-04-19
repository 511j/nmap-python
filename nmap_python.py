'''
# Codeing by lord4tb , [ @ilord4tb ]
# github : 511j
# Free src in >> https://github.com/511j/nmap-python
'''
import os
import time
from colorama import Fore
port_scann = f"""
    access security                                                                                                      
    access: PERMISSION DENIED.
    > access security grid
    access: PERMISSION DENIED.
    > access main security grid
    access: PERMISSION DENIED....and...
    {Fore.RED}YOU DIDN'T SAY THE MAGIC WORD!
    YOU DIDN'T SAY THE MAGIC WORD!
    YOU DIDN'T SAY THE MAGIC WORD!
    YOU DIDN'T SAY THE MAGIC WORD!{Fore.WHITE}
"""
print(port_scann)
os.system("sudo apt-get install nmap")
os.system("clear")
print(port_scann)
usersys = f"nmap {Fore.RED}~{Fore.WHITE}# "
print(f"Enter the target {Fore.RED}:{Fore.WHITE}")
target = input(usersys + Fore.RED)
print(f"{Fore.WHITE}The target is => {target}\n")
time.sleep(0.7)
print("Prosseing..")
time.sleep(1.3)
os.system("clear")
print(port_scann)
print(f"The target {Fore.RED}>{Fore.WHITE} {target}\n")
print("""[ 1 ] Scan all ports [ -p- ]
[ 2 ] Scan using TCP connect [ -sT ]
[ 3 ] Scan UDP ports [ -sU -p ]
""")
portt = input(usersys + Fore.RED)
if portt =='1':
    os.system("clear")
    print(Fore.WHITE + port_scann)
    os.system(f"nmap -p- {target}")
elif portt =='2':
    os.system("clear")
    print(Fore.WHITE + port_scann)
    os.system(f"nmap -sT  {target}")
elif portt =='3':
    os.system("clear")
    print(Fore.WHITE + port_scann)
    os.system(f"nmap  -sU -p  {target}")
else:
    print(f"{Fore.WHITE}[ {Fore.RED}-{Fore.WHITE} ] Error inputting")