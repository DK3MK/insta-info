import os
try:
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install colorama')
except:
    print('Done')

import requests
from user_agent import generate_user_agent
from colorama import Fore,Style

b0 = Style.RESET_ALL
b1 = Fore.YELLOW
b4 = Fore.LIGHTCYAN_EX
b5 = Fore.LIGHTYELLOW_EX
b6 = Fore.RED
b7 = Fore.GREEN
b8 = Fore.MAGENTA
b9 = Fore.BLUE
os.system('cls' if os.name == 'nt' else 'clear')
logo = f"""{b1}
   /$$                         /$$
  | $$                        | $$
 /$$$$$$    /$$$$$$   /$$$$$$ | $$
|_  $$_/   /$$__  $$ /$$__  $$| $$
  | $$    | $$  \ $$| $$  \ $$| $$
  | $$ /$$| $$  | $$| $$  | $$| $$
  |  $$$$/|  $$$$$$/|  $$$$$$/| $$
   \___/   \______/  \______/ |__/
         /$$                       /$$              
        |__/                      | $$              
         /$$ /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ 
        | $$| $$__  $$ /$$_____/|_  $$_/   |____  $$
        | $$| $$  \ $$|  $$$$$$   | $$      /$$$$$$$
        | $$| $$  | $$ \____  $$  | $$ /$$ /$$__  $$
        | $$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$
        |__/|__/  |__/|_______/    \___/   \_______/ {b8}version 3
{b1}                    
{b6}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{b6}┃ {b5}Coded By {b8}DARK MAN 747{b5} || Follow me for more.    {b6}┃
{b6}┃           {b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━            {b6}┃
{b6}┃   {b0}[{b1}+{b0}] {b7}InstaGram: {b4}aboud_coding                   {b6}┃
{b6}┃   {b0}[{b1}+{b0}] {b7}GitHub: {b4}Dark-Man747                       {b6}┃
{b6}┃   {b0}[{b1}+{b0}] {b7}TikTok: {b4}kmhp                              {b6}┃
{b6}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
print(logo)

target = input(f'{b0}[{b1}?{b0}] {b9}Enter username: {b6}')

url = f"https://www.instagram.com/{target}/?__a=1&__d=dis"
head = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding':'gzip,deflate,br',
    'accept-language':'en-US,en;q=0.9,ar;q=0.8',
    'cookie':'mid=Y_uo7AALAAH37jDgISXeGrw-EYJz; ig_did=FCBB16B3-C36F-49C1-B3FC-0EDE85F66652; ig_nrcb=1; csrftoken=S4x1xplfnPwJqhHntm5R9FBv42k28dpD; ds_user_id=47675279829; sessionid=47675279829%3AQHMZZxVAh1twjN%3A2%3AAYdG38b-Bn14Ny_LuwvswLVfZvpDRyuS6pyWwj2qgg',
    'user-agent': generate_user_agent(),#'Instagram 9.4.0 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)',#generate_user_agent(),

    }
information = requests.get(url,headers=head).json()

id = (information['graphql']['user']['id'])
name = (information['graphql']['user']['full_name'])
Bio = (information['graphql']['user']['biography'])
Followers = (information['graphql']['user']['edge_followed_by']['count'])
Following = (information['graphql']['user']['edge_follow']['count'])
url = (information['graphql']['user']['external_url'])
private = (information['graphql']['user']['is_private'])
business = (information['graphql']['user']['is_business_account'])
posts = str(information['graphql']['user']["edge_owner_to_timeline_media"]["count"])
re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}",headers=head)
ree = re.json()
dat = ree['date']

print(f"""
{b0}[{b1}+{b0}] {b4}Id {b1}:{b0} {id}
{b0}[{b1}+{b0}] {b4}Name {b1}:{b0} {name}
{b0}[{b1}+{b0}] {b4}Bio {b1}:{b0} {Bio}
{b0}[{b1}+{b0}] {b4}Followers {b1}:{b0} {Followers}
{b0}[{b1}+{b0}] {b4}Following {b1}:{b0} {Following}
{b0}[{b1}+{b0}] {b4}posts {b1}:{b0} {posts}
{b0}[{b1}+{b0}] {b4}date :{b0} {dat}
{b0}[{b1}+{b0}] {b4}Bio link {b1}:{b0} {url}
{b0}[{b1}+{b0}] {b4}Private {b1}:{b0} {private}
{b0}[{b1}+{b0}] {b4}Business Account {b5}:{b0} {business}
""")
