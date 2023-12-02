ahmet = 20000
ayse = 1500
fatma = 3000

    
print("Bankamıza hoş geldiniz! Lütfen yapmak istediğiniz işlemi yazınız.")
print("Ahmet,Ayşe,Fatma")
hesapAdi = str(input("Lütfen Hesap Adınızı Seçiniz."))
print(f"Hoş geldiniz Sayın {hesapAdi} ")

def bakiye():
    if hesapAdi == "ahmet":
        print(f"Güncel bakiyeniz: {ahmet}")
    elif hesapAdi == "ayşe":
        print(f"Güncel bakiyeniz: {ayse}")
    elif hesapAdi == "fatma":
        print(f"Güncel bakiyeniz: {fatma}")
    else:
        print("Hatalı seçim!")
bakiye()

islem = str(input("Para çekmek için: 1, para göndermek için: 2, para yatırmak için: 3, çıkış yapmak için: 4 tuşlayınız! "))

if hesapAdi == "Ahmet" and islem == "1":
    tutar = int(input("Çekmek istediğiniz tutarı giriniz: "))
    if tutar <= ahmet:
        ahmet -= tutar
        print(f"Güncel bakiyeniz {ahmet} olarak güncellenmiştir.")
    else:
        print("Bakiyeniz yetersizdir.")
if hesapAdi == "Ayşe" and islem == "1":
    tutar = int(input("Çekmek istediğiniz tutarı giriniz: "))
    if tutar <= ayse:
        ayse -= tutar
        print(f"Güncel bakiyeniz {ayse} olarak güncellenmiştir.")
    else:
        print("Bakiyeniz yetersizdir.")        
if hesapAdi == "Fatma" and islem == "1":
    fatmatutar = int(input("Çekmek istediğiniz tutarı giriniz: "))
    if tutar <= fatma:
        fatma -= tutar
        print(f"Güncel bakiyeniz {fatma} olarak güncellenmiştir.")
    else:
        print("Bakiyeniz yetersizdir.")      


if hesapAdi == "Ahmet" and islem == "2":
    arkadas = str(input("Lütfen para göndermek istediğiniz kişiyi seçin. Ayşe,Fatma  "))
    miktar = int(input("Ne kadar göndermek istiyorsunuz?"))
    if miktar <= ahmet:
        ahmet -= miktar
        if arkadas == "Ayşe":
            print(f"{miktar} tutarında bakiye gönderilmiştir.")
            print(f"Güncel bakiyeniz {ahmet} olarak güncellenmiştir.")
            ayse += miktar
            print(ayse)
        elif arkadas == "Fatma":
            print(f"{miktar} tutarında bakiye gönderilmiştir.")
            print(f"Güncel bakiyeniz {ahmet} olarak güncellenmiştir.")
            fatma += miktar
            print(fatma)
            
if hesapAdi == "Ayşe" and islem == "2":
    arkadas = str(input("Lütfen para göndermek istediğiniz kişiyi seçin. Ahmet,Fatma  "))
    miktar = int(input("Ne kadar göndermek istiyorsunuz?"))
    if miktar <= ayse:
        ayse -= miktar
        if arkadas == "Ahmet":
            print(f"{miktar} tutarında bakiye gönderilmiştir.")
            print(f"Güncel bakiyeniz {ayse} olarak güncellenmiştir.")
            ahmet += miktar
        elif arkadas == "Fatma":
            print(f"{miktar} tutarında bakiye gönderilmiştir.")
            print(f"Güncel bakiyeniz {ayse} olarak güncellenmiştir.")
            fatma += miktar       
if hesapAdi == "Fatma" and islem == "2":
    arkadas = str(input("Lütfen para göndermek istediğiniz kişiyi seçin. Ahmet,Ayşe  "))
    miktar = int(input("Ne kadar göndermek istiyorsunuz?"))
    if miktar <= fatma:
        fatma -= miktar
        if arkadas == "Ahmet":
            print(f"{miktar} tutarında bakiye gönderilmiştir.")
            print(f"Güncel bakiyeniz {fatma} olarak güncellenmiştir.")
            ahmet += miktar
        elif arkadas == "Ayşe":
            print(f"{miktar} tutarında bakiye gönderilmiştir.")
            print(f"Güncel bakiyeniz {fatma} olarak güncellenmiştir.")
            ayse += miktar                       
if hesapAdi == "Ahmet" and islem == "3":
    yatirma = int(input("Ne kadar yatırmak istiyorsunuz?"))
    ahmet += yatirma
    print(f"Güncel bakiyeniz {ahmet} olarak güncellenmiştir.")
if hesapAdi == "Ayşe" and islem == "3":
    yatirma = int(input("Ne kadar yatırmak istiyorsunuz?"))
    ayse += yatirma
    print(f"Güncel bakiyeniz {ayse} olarak güncellenmiştir.")
if hesapAdi == "Fatma" and islem == "3":
    yatirma = int(input("Ne kadar yatırmak istiyorsunuz?"))
    fatma += yatirma
    print(f"Güncel bakiyeniz {fatma} olarak güncellenmiştir.")
    
if islem== "4":
    print("İyi Günler Dileriz.")
