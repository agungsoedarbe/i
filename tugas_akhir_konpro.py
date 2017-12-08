class travel(object):
    kode    = str
    jumlah_peserta  = 0
    ket  = str
    ket2    = 0
    ket3 = 0


    def _init_ (self,kode,jumlah_peserta,ket,ket2):
        self.kode           = kode
        self.jumlah_peserta = jumlah_peserta
        self.ket            = ket
        self.ket2           = ket2

    def get_ket(self):
        if self.kode == "yog":
            ket = "Yogyakarta"
        elif self.kode == "jkt":
            ket = "Jakarta"
        elif self.kode=="sb":
            ket = "Sawarna Banten"
        else:
            ket = "Error"
        return ket

    def get_ket2(self):
        if self.kode =="yog" and self.jumlah_peserta >= 100:
            ket2 = 555000
        elif self.kode =="yog" and self.jumlah_peserta <=100:
            ket2 = self.jumlah_peserta*((15*555000)/100)
        elif self.kode =="jkt" and self.jumlah_peserta>= 85:
            ket2 = 325000
        elif self.kode =="jkt" and self.jumlah_peserta <= 85:
            ket2 = self.jumlah_peserta*((15*325000)/100)
        elif self.kode =="sb" and self.jumlah_peserta >= 70:
            ket2 = 300000
        else:
            ket2 = self.jumlah_peserta*((15*300000)/100)
        return ket2

    def get_ket3(self):
        if self.kode == "yog":
            ket = 555000
        elif self.kode == "jkt":
            ket = 325000
        elif self.kode=="sb":
            ket = 300000
        else:
            ket = "Error"
        return ket

    def menghitung_total(self):
        total = self.jumlah_peserta*self.get_ket3()
        return total



def main():
    a = travel()

    a.kode = raw_input("Masukan Kode Tujuan : ")
    a.jumlah_peserta    = int(raw_input("Masukan Jumlah Peserta : "))


    print "Program Travel"
    print "Author By : Frika Da Cintia"
    print "Teknik Informatika"
    print "========================================="
    print " Tujuan          : ",a.get_ket()
    print " Jumlah Peserta  : ",a.jumlah_peserta
    print " Biaya / Peserta : ",a.get_ket2()
    print " Total Harga     : ",a.menghitung_total()


if __name__ == '__main__':
    main()