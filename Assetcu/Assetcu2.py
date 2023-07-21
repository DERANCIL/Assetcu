import subprocess
import argparse
import os
import xml.etree.ElementTree as ET
from collections import defaultdict
import time
import sys

print(""""





                                                                                 ___   _____ _____ _____ _____ _____ _   _ 
                                                                                / _ \ /  ___/  ___|  ___|_   _/  __ \ | | |
                                                                                / /_\ \\ `--.\ `--.| |__   | | | /  \/ | | |
                                                                                |  _  | `--. \`--. \  __|  | | | |   | | | |
                                                                                | | | |/\__/ /\__/ / |___  | | | \__/\ |_| |
                                                                                \_| |_/\____/\____/\____/  \_/  \____/\___/ 
				                                        ⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
							⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
							⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
							⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
							⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
							⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
							⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
							⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
							⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
							⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
							⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
							⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
							⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
							⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
							⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋
		""""")

























print("For better results, please add your API keys (recommended) theHarvester/api-keys.yaml") 
print("For better results, please add your API keys (recommended) /root/.config/subfinder/provider-config.yaml")



time.sleep(5)


arguments = sys.argv[1:]
flag = False
domain=""
list_filename=""
if '-d' in arguments:
    print("Domain argümanı kullanıldı.")
    domain_index = arguments.index('-d')  # "-d" argümanının indeksini alıyoruz
    if domain_index + 1 < len(arguments):
        flag =True
        domain = arguments[domain_index + 1]
        print("Domain adı:", domain)
    else:
        sys.exit("Lütfen bir domain adı girin.")
elif '-l' in arguments:
    print("Liste argümanı kullanıldı.")
    list_index = arguments.index('-l')  # "-l" argümanının indeksini alıyoruz
    if list_index + 1 < len(arguments):
        list_filename = arguments[list_index + 1]
        print("Liste dosya adı:", list_filename)
    else:
        sys.exit("Lütfen bir liste dosya adı girin.")
else:
    sys.exit("Lütfen -d veya -l argümanlarından birini belirtin.")



   
def domain_check(domain_value):
        # Subfinder komutunu çalıştırma
    subfinder_cmd = f'subfinder -d {domain_value}  -silent -o subfind1.txt'
    subprocess.call(subfinder_cmd, shell=True)
    
    theharvester_cmd = f'cd theHarvester && python3 theHarvester.py -d {domain_value} -b all -f dot'
    subprocess.call(theharvester_cmd, shell=True)
    
    # dot.json dosyasını bir üst dizine taşıma
    os.rename('theHarvester/dot.xml', 'dot.xml')
    
    # dot.xml dosyasını silme
    os.remove('theHarvester/dot.json')
    
    
    print("Taramalar Başlıyor.")
    
    
    # Dosya adı ve yolu
    dosya_adi = "dot.xml"
    
    # Domainleri tutacak liste
    domainler = []
    
    # XML dosyasını ağaç olarak yükle
    tree = ET.parse(dosya_adi)
    root = tree.getroot()
    
    # Domainleri bul
    for host_etiketi in root.iter("host"):
        domain = host_etiketi.text
        if domain is not None:
            domain = domain.strip()
            domainler.append(domain)
    
    # Domainleri "liste.txt" dosyasına yazdır
    with open("liste.txt", "w") as dosya:
        for domain in domainler:
            dosya.write(domain + "\n")
    print("AMASS Başlyıor")
    
    amass_cmd = f'amass enum -passive -d {domain_value} -o amass1.txt'
    subprocess.call(amass_cmd, shell=True)
    
    amass2_cmd = f'amass enum -brute -w Subbrute.txt -d {domain_value} -o amass2.txt'
    subprocess.call(amass2_cmd, shell=True)
    
    
    
    os.remove('dot.xml')
    print("DOSYALAMA BAŞLIYOR")
    
    
    dosya_listesi = ['subfind1.txt', 'amass1.txt', 'liste.txt', 'amass2.txt']
    
    # Tüm dosyaların içeriğini birleştir ve yinelenen satırları elime
    birlesik_satirlar = set()
    
    for dosya_adi in dosya_listesi:
        dosya_yolu = os.path.join(os.getcwd(), dosya_adi)
        if os.path.isfile(dosya_yolu):
            with open(dosya_yolu, 'r') as dosya:
                satirlar = dosya.readlines()
                birlesik_satirlar.update(satirlar)
    
    # Yeni dosya adını ve yolu belirle
    yeni_dosya_adi = f"{domain_value}sub.txt"
    yeni_dosya_yolu = os.path.join(os.path.dirname(dosya_yolu), yeni_dosya_adi)
    
    # Dosyayı oluştur ve birleştirilmiş satırları yaz
    with open(yeni_dosya_yolu, 'w') as yeni_dosya:
        yeni_dosya.writelines(birlesik_satirlar)
    
    print("Dosya birleştirme işlemi tamamlandı.")
    print(f"Çıktı dosyası: {yeni_dosya_yolu}")
    
    # Dosyaları sil
    for dosya_adi in dosya_listesi:
        dosya_yolu = os.path.join(os.getcwd(), dosya_adi)
        if os.path.isfile(dosya_yolu):
            os.remove(dosya_yolu)
    
    
    
    
    
    print("Sonraki aşamaya geçiliyor.")
    
    
    dnsx_cmd = f'dnsx -l {domain_value}sub.txt  -a -resp -o {domain_value}subIP_OUT.txt'
    subprocess.call(dnsx_cmd, shell=True)
    
    # Dosyayı okuyarak domain ve IP adreslerini eşleştirme
    domain_ip_map = defaultdict(list)
    
    with open(f"{domain_value}subIP_OUT.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                domain, ip = line.split(" ")
                domain_ip_map[domain].append(ip)
    
    # Tekrar eden domainleri tespit etme ve "??????" ile işaretlenme
    for domain, ip_list in domain_ip_map.items():
        if len(ip_list) > 1:
            for i in range(len(ip_list)):
                ip_list[i] = "??????"
    
    # Dosyayı temizleme ve güncel verileri yazdırma
    with open(f"{domain_value}subIP_OUT.txt", "w") as file:
        for domain, ip_list in domain_ip_map.items():
            for ip in ip_list:
                file.write(f"{domain} {ip}\n")
    lines_seen = set()
    
    with open(f"{domain_value}subIP_OUT.txt", "r") as file:
        lines = file.readlines()
    
    with open(f"{domain_value}subIP_OUT.txt", "w") as file:
        for line in lines:
            if line not in lines_seen:
                file.write(line)
                lines_seen.add(line)
    
    
    try:
        dosya = open(f"{domain_value}subIP_OUT.txt", "r")  # IP adreslerini içeren dosyayı okuyoruz
        icerik = dosya.readlines()  # Dosyanın içeriğini satır satır okuyoruz
        dosya.close()  # Dosyayı kapatıyoruz
    
        ip_listesi = []
        for satir in icerik:
            if "[" in satir and "]" in satir:  # IP adreslerini içeren satırları kontrol ediyoruz
                ip = satir[satir.index("[") + 1: satir.index("]")]
                ip_listesi.append(ip)
    
        subdomain_dosya = open(f"{domain_value}sub.txt", "r")  # Subdomain listesini içeren dosyayı okuyoruz
        subdomain_icerik = subdomain_dosya.read()  # Subdomain dosyasının içeriğini okuyoruz
        subdomain_dosya.close()  # Subdomain dosyasını kapatıyoruz
    
        yeni_dosya = open(f"{domain_value}PreNaabuscan.txt", "w")  # Yeni dosyayı yazmak için "w" modunda açıyoruz
        for ip in ip_listesi:
            yeni_dosya.write(ip + "\n")  # IP adresini yeni dosyaya yazıyoruz
    
        yeni_dosya.write(subdomain_icerik)  # Subdomain içeriğini yeni dosyaya yazıyoruz
        yeni_dosya.close()  # Yeni dosyayı kapatıyoruz
    
        print("Port Taramasına geçiliyor.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        
        
    Naabu_cmd = f'naabu -list {domain_value}PreNaabuscan.txt -o {domain_value}PORT.txt'
    subprocess.call(Naabu_cmd, shell=True)
    
    httpx_cmd = f'httpx -list {domain_value}PORT.txt -o {domain_value}Url.txt'
    subprocess.call(httpx_cmd, shell=True)
    
    dir_cmd = f'mkdir OUTPUT/{domain_value}inf '
    subprocess.call(dir_cmd, shell=True)
    dir2_cmd = f'mv {domain_value}PORT.txt OUTPUT &mv {domain_value}PreNaabuscan.txt OUTPUT&mv {domain_value}Url.txt  OUTPUT&&mv {domain_value}subIP_OUT.txt OUTPUT&&mv {domain_value}sub.txt OUTPUT'
    subprocess.call(dir2_cmd, shell=True)
    
    dir3_cmd = f'cd OUTPUT &&mv {domain_value}sub.txt {domain_value}inf && mv {domain_value}subIP_OUT.txt {domain_value}inf && mv {domain_value}Url.txt  {domain_value}inf && mv {domain_value}PORT.txt {domain_value}inf && mv {domain_value}PreNaabuscan.txt {domain_value}inf'
    subprocess.call(dir3_cmd, shell=True)




if flag == True:
    domain_check(domain)
else:
    with open(list_filename, "r") as dosya:
        satirlar = dosya.readlines()

    for satir in satirlar:
        domain_check(satir.strip())

        
