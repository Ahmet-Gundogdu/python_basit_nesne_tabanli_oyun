class class_Oyuncu():
    def __init__(self,ad="none",can=0) :
        #""" ---Oyuncu nesnesini tanımlama--- """
        self.nesnenin_adi=ad
        self.nesnenin_cani=can
    
    
    #""" ---Oyuncu bilgi alma--- """
    def karakter_info(self):
        print("Karakter Bilgileri Adı: {}, Canı: {}.".format(self.nesnenin_adi, self.nesnenin_cani))
        
    #""" ---Oyuncu hasar alma--- """
    def hasar_al(self,hasar_miktari):
        self.nesnenin_cani -= hasar_miktari
    
        
    def oyuncu_bilgileri_getir(self):
        bilgiler = [self.nesnenin_adi, self.nesnenin_cani]
        return bilgiler
    