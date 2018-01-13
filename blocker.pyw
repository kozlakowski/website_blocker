import time
from datetime import datetime as dt # Wszędzie gdzie stosuje "dt" chodzi o datetime(zwykły skrót usprawniający pracę)

hosts_temp = r"C:\Users\kozla\Desktop\blocker\hosts" # Ścieżka do kopii pliku "hosts" znajdującego sie w folderze z programem python
hosts_path = r"C:\Windows\System32\drivers\etc\hosts" # Ścieżka do prawdziwego pliku "hosts"
redirect= "127.0.0.1"
website_list=["www.facebook.com","facebook.com"] # Witryny które będą blokowane (pamietać aby wpisać witrynę z "www" oraz bez tego)


while True: # while True sprawia że pętla będzie ciągle działać
    if dt(dt.now().year, dt.now().month, dt.now().day,00) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,10): # Pomiędzy jakimi godzinami program ma blokowaćdostęp do stron
        print("Working hours...")
        with open(hosts_path,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass # Jeżeli już się tam znajduje to nie robimy nic
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)

# PRZEMYŚLEĆ DOKŁADNE DZIAŁANIE KODY(GDZIE ZNAJDUJE SIĘ WSKAŹNIK, POBAWIĆ SIĘ GODZINAMI) !!!!!!!!!
