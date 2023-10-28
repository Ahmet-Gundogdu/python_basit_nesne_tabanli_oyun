class class_oyun_motoru():
    from random import random 
    
    verilecek_hasar=0
    atis_deneme_basarisi=False
    def calistir(self):

        ates_Bolge = str(input(" Ateş etmeyi deneyeceğiniz bölgeyi girin. \n Baş, Omuz, Kollar, Gövde, Ayaklar. \n")).lower()

        match ates_Bolge:
            case "baş":
                sayi = int(self.random()*100)
                atis_deneme_basarisi =True
                if( sayi >=85):
                    self.verilecek_hasar = 60
                    
                elif(sayi <85 and sayi >= 75):
                    self.verilecek_hasar = 50
                    
                elif(sayi <75 and sayi >= 65):
                    self.verilecek_hasar = 40
                    
                elif(sayi <65):
                    self.verilecek_hasar = 30
                    
            case "omuz":
                sayi = int(self.random()*50)
                atis_deneme_basarisi =True
                if( sayi >=30):
                    self.verilecek_hasar = 30
                    
                elif(sayi <30 and sayi >= 20):
                    self.verilecek_hasar = 25
                    
                elif(sayi <20 and sayi >= 10):
                    self.verilecek_hasar = 15
                    
                elif(sayi <10):
                    self.verilecek_hasar = 5
                    
            case "kollar":
                sayi = int(self.random()*50)
                atis_deneme_basarisi =True
                if( sayi >=30):
                    self.verilecek_hasar = 30
                    
                elif(sayi <30 and sayi >= 20):
                    self.verilecek_hasar = 20
                    
                elif(sayi <20 and sayi >= 10):
                    self.verilecek_hasar = 15
                    
                elif(sayi <10):
                    self.verilecek_hasar = 10
                    
            case "gövde":
                sayi = int(self.random()*50)
                atis_deneme_basarisi =True
                if( sayi >=45):
                    self.verilecek_hasar = 50
                    
                elif(sayi <45 and sayi >= 30):
                    self.verilecek_hasar = 30
                    
                elif(sayi <30 and sayi >= 20):
                    self.verilecek_hasar = 15
                    
                elif(sayi <15):
                    self.verilecek_hasar = 10
                    
            case "ayaklar":
                atis_deneme_basarisi =True
                self.verilecek_hasar = 15
                
            case _:
                atis_deneme_basarisi =False
                print("Geçersiz atış denemesi!")
        return self.verilecek_hasar, atis_deneme_basarisi