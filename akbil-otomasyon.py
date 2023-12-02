bakiye = 15.70
duraklar = {
        "Zincirlikuyu": 9.90,
        "Avcılar": 15.90,
        "Uzunçayır": 5.90,
        "Altunizade": 7.90,
        "Çağlayan": 12.90,
    }

def menu():
    print("Akbil-Metrobüs işlemine hoşgeldiniz! ")
    print(f"Güncel bakiyeniz: {bakiye}")
    print("1) Akbil Bakiye Yükleme \n2) Yolculuk \n3) Çıkış")
      
def bakiye_yukleme():
    global bakiye
    print(f"Güncel bakiyeniz {bakiye} olarak gözüküyor.")
    yukleme = int(input("Ne kadar yükleme yapmak istersiniz? "))
    bakiye += yukleme
    print(f"Yükleme başarılı! Bakiyeniz: {bakiye} olarak tanımlanmıştır!")
    
def yolculuk():
    global bakiye
    print("Duraklar ve Ücretleri")
    print(duraklar)
    hedef_durak = str(input("Hangi durağa gitmek istersiniz? "))
    if hedef_durak in duraklar:
        ucret = duraklar[hedef_durak]
        if ucret <= bakiye:
            bakiye -= ucret
            print(f"İyi yolculuklar! Kalan bakiyeniz: {bakiye} ")

        else:
            print("Bakiyeniz yetersizdir.")
            cevap = str(input("Bakiye yüklemek ister misiniz? (E/H): "))
            if cevap == "E":
                bakiye_yukleme()
            if cevap == "H":
                print("İyi günler dileriz.")                
while True:
    menu()
    secim = str(input("Lütfen seçiminizi yapınız:  "))   
    if secim == "1":
        bakiye_yukleme()
    if secim == "2":
        yolculuk()
    if secim == "3":
        print("İyi günler dileriz!")
        break 