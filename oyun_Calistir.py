
import class_Oyuncu
import class_Oyun_motoru
#""" ---Tur bilgisi alma--- """
while True:
    try:
        kac_tur= int(input("Kaç tur oynamak istersiniz. -Rakam olarak giriniz.- \n"))
        break
    except:
        print("Lütfen sadece rakamsal değer giriniz. \n")
        
#""" ---Oyuncu sayısı --- """
while True:
    try:
        kac_kisilik_oyun = int(input("Kaç kişi oynayacaksınız. -Rakam olarak giriniz.- \n"))
        break
    except:
        print("Lütfen sadece rakamsal değer giriniz. \n")
        
#""" ---Bazı sabit değişkenler --- """    
sag_kalan=kac_kisilik_oyun
oyun_bittimi= False

#""" ---Oyuncuların nesnelerini oluşturup referanslarını kaydetme--- """
oyuncular=[]
for i in range (kac_kisilik_oyun):
    oyuncu_ad= str(input("Oyuncu adı giriniz. \n")).lower()
    oyuncular.append(class_Oyuncu.class_Oyuncu(oyuncu_ad,100))

#""" ---Oyun dinamiklerini barındıran nesnenin oluşturup tur döngüsüne girmek--- """
oyun1= class_Oyun_motoru.class_oyun_motoru()
for i in range(kac_tur):
    
    #""" ---Oyuncu sayısı ve kazanan kontrolü--- """
    if (sag_kalan <=1):
            for adlar in oyuncular:
                if adlar.oyuncu_bilgileri_getir()[1] >= 0:
                    print(f" {(adlar.oyuncu_bilgileri_getir()[0].upper())} adlı oyuncu oyunu kazandı. \n")
                    oyun_bittimi = True
                    break
    if (oyun_bittimi == True):
        break
    
    #""" ---Her bi turdaki kişi sayısı kadar oynatmak için döngü--- """
    for j in range(kac_kisilik_oyun):
        if(oyuncular[j].oyuncu_bilgileri_getir()[1] <= 0):
            continue
        else:
            print(f" => Şuan: {(oyuncular[j].oyuncu_bilgileri_getir()[0]).upper()} adlı oyunucun sırası.")
            
        hangi_oyuncu = str(input("Saldırmak istediğiniz oyuncunun adını giriniz. \n")).lower()
        oyuncu_index = 0
        oyuncu_bulundu=False
        
        #""" ---Basit bir hatayı önlemek için sonsuz döngüde saldırılacak oyuncunun adının istenmesi--- """
        while True:
            
            for adlar in oyuncular:
                if adlar.oyuncu_bilgileri_getir()[0] == hangi_oyuncu:
                    oyuncu_bulundu = True
                    break
                oyuncu_index += 1
                if (oyuncu_index >= len(oyuncular)):
                    print ("HATA! Oyuncu bulunamadı!")
                    break
                
            if oyuncu_bulundu == True:
                break
            else :
                hangi_oyuncu = str(input("Saldırmak istediğiniz oyuncunun adını tekrar giriniz. \n")).lower()
                oyuncu_index = 0
        
        #""" ---Oyun dinamiklerindeki basit rastlantısal saldırma fonksiyonunu çalıştırma--- """
        hasar=0
        while True:
            hasar = oyun1.calistir()
            if(hasar [1] == True):
                break
        
        #""" ---Dinamiklerden elde edilen hasar değerini oyunucun canından düşürme--- """
        if (oyuncular[oyuncu_index].oyuncu_bilgileri_getir()[1] >=0):
            oyuncular[oyuncu_index].hasar_al(hasar[0])
            
        if(oyuncular[oyuncu_index].oyuncu_bilgileri_getir()[1] <= 0):
            print(f"{oyuncular[oyuncu_index].oyuncu_bilgileri_getir()[0]} adlı oyuncu oyunu KAYBETTİ :(")
            sag_kalan -=1
            
            
        #""" ---Oyuncu tur sonu durum bilgilendirmeleri--- """
        print("*-*-*-*-*-*-*-*-*-*-* \n")
        print(f" => {hangi_oyuncu.upper()} adlı oyuncuya, {hasar[0]} hasar verdiniz. \n")
        print(f"{(oyuncular[oyuncu_index].oyuncu_bilgileri_getir()[0]).upper()} adlı oyunucunun son can durumu: {oyuncular[oyuncu_index].oyuncu_bilgileri_getir()[1]} \n")
        print("*-*-*-*-*-*-*-*-*-*-* \n")
        

