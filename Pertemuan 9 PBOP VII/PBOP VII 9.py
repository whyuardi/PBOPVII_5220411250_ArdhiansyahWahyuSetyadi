class Animal:
    def __init__(self, nama, sifat, ukuran, jumlah_kaki):
        self.nama = nama
        self.sifat = sifat
        self.ukuran = ukuran
        self.jumlah_kaki = jumlah_kaki

    def display_info(self):
        print(f"\nNama : {self.nama}, Sifat : {self.sifat}, Ukuran : {self.ukuran}, Jumlah Kaki : {self.jumlah_kaki}")

class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_jalan, jenis_mamalia):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_jalan = bisa_jalan
        self.jenis_mamalia = jenis_mamalia

    def display_info(self):
        super().display_info()
        print(f"\nBisa Jalan : {self.bisa_jalan}, Jenis Mamalia : {self.jenis_mamalia}")

class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_terbang = bisa_terbang
        self.jenis_aves = jenis_aves

    def display_info(self):
        super().display_info()
        print(f"\nBisa Terbang : {self.bisa_terbang}, Jenis Aves : {self.jenis_aves}")

class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, jenis_ayam, bisa_diadu):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, True, "Peternakan")
        self.jenis_ayam = jenis_ayam
        self.bisa_diadu = bisa_diadu

    def display_info(self):
        super().display_info()
        print(f"\nJenis Ayam : {self.jenis_ayam}, Bisa Diadu : {self.bisa_diadu}")

class Merpati(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, True, "Peliharaan")

merpati = Merpati("Pidgeon", "Ramah", "Kecil", 2)
merpati.display_info()

ayam = Ayam("Ayam", "Berani", "Sedang", 2, "Kampung", True)
ayam.display_info()
