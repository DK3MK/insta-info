import os
try:
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install colorama')
except:
    print('Done')

# this tool information account on instagram . . .
# بسم الله رب البدايات نبدأ
import requests, json
from colorama import Fore,Style
from user_agent import generate_user_agent
os.system('cls' if os.name == 'nt' else 'clear')

# colors :
b0 = Style.RESET_ALL
b1 = Fore.YELLOW
b4 = Fore.LIGHTCYAN_EX
b5 = Fore.LIGHTYELLOW_EX
b6 = Fore.RED
b7 = Fore.GREEN
b8 = Fore.MAGENTA
b9 = Fore.BLUE
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
        |__/|__/  |__/|_______/    \___/   \_______/ {b8}version 4
{b1}                    
{b6}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{b6}┃ {b5}Coded By {b8}dark man{b5} || Follow me for more.    {b6}┃
{b6}┃           {b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━{b0}━{b8}━            {b6}┃
{b6}┃   {b0}[{b1}+{b0}] {b7}InstaGram: {b4}aboud_coding                   {b6}┃
{b6}┃   {b0}[{b1}+{b0}] {b7}GitHub: {b4}DK3MK                             {b6}┃
{b6}┃   {b0}[{b1}+{b0}] {b7}TikTok: {b4}kmhp                              {b6}┃
{b6}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
print(logo)

target = input(f'{b0}[{b1}?{b0}] {b9}Enter username: {b6}')

head = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding':'gzip,deflate,br',
    'accept-language':'en-US,en;q=0.9,ar;q=0.8',
    'cookie':'mid=Y_uo7AALAAH37jDgISXeGrw-EYJz; ig_did=FCBB16B3-C36F-49C1-B3FC-0EDE85F66652; ig_nrcb=1; csrftoken=S4x1xplfnPwJqhHntm5R9FBv42k28dpD; ds_user_id=47675279829; sessionid=47675279829%3AQHMZZxVAh1twjN%3A2%3AAYdG38b-Bn14Ny_LuwvswLVfZvpDRyuS6pyWwj2qgg',
    'user-agent': generate_user_agent(),#'Instagram 9.4.0 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)',#generate_user_agent(),

    }

url = f'https://api-darkman-ffaction747.replit.app/insta?query={target}'

info = requests.get(url).json()
information = info['result']


id = (information['id'])
name = (information['full name'])
Bio = (information['bio'])
Followers = (information['follow'])
Following = (information['following'])
url = (information['bio link'])
private = (information['private'])
business = (information['business account'])
professional = (information['professional account'])
posts = str(information['posts'])
url_pic = (information['profile pic'])
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
{b0}[{b1}+{b0}] {b4}professional account {b5}:{b0} {professional}
{b0}[{b1}+{b0}] {b4}pic url :{b0} {url_pic}
""")
