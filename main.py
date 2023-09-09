from colorama import  Fore, Style
import requests

text = """
----------------------------------------------------------------------
 _   _             _ _           _____ _               _             
| | | |           (_) |         /  __ \ |             | |            
| | | | __ _ _ __  _| |_ _   _  | /  \/ |__   ___  ___| | _____ _ __ 
| | | |/ _` | '_ \| | __| | | | | |   | '_ \ / _ \/ __| |/ / _ \ '__|
\ \_/ / (_| | | | | | |_| |_| | | \__/\ | | |  __/ (__|   <  __/ |   
 \___/ \__,_|_| |_|_|\__|\__, |  \____/_| |_|\___|\___|_|\_\___|_|   
                          __/ |                                      
                         |___/                                       
----------------------------------------------------------------------

"""


print(text)
print(Style.DIM + Fore.GREEN + "[+] " + Fore.WHITE + "Created by Vexxly")

def main():
  vanity = input(Style.NORMAL + Fore.GREEN + "[+] "+Fore.WHITE + "Enter Vanity To Check: ")
  check = requests.get(f"https://discord.com/api/v9/invites/{vanity}")
  if check.status_code ==404:
    print(Fore.GREEN + "[+] " + Fore.WHITE + f"{vanity} is Claimable!")
  else:
    print(Fore.RED + "[-] " + Fore.WHITE + f"{vanity} is Taken!")
  x = input(Fore.GREEN + "[+] "+Fore.WHITE + "Want to check another? ").lower()
  if x == "yes":
    main()

main()
