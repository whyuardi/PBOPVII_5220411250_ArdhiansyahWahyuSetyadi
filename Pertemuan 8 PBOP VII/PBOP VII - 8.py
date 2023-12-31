class PerpusItem():
    def __init__(self, judul, subjek):
        self.judul = judul
        self.subjek = subjek

    def LokasiPenyimpanan(self):
        return "Tidak ada"

    def info(self):
        return f"Item: {self.judul}, Subject: {self.subjek}"


class Katalog():
    def __init__(self):
        self.items = []

    def tambah_item(self, item):
        self.items.append(item)

    def cari(self, search_function):
        results = [item for item in self.items if search_function(item)]
        return results


class Buku(PerpusItem):
    def __init__(self, judul, subjek, ISBN, pengarang, jmlHal, ukuran):
        super().__init__(judul, subjek)
        self.ISBN = ISBN
        self.pengarang = pengarang
        self.jmlHal = jmlHal
        self.ukuran = ukuran

    def LokasiPenyimpanan(self):
        return f"The book '{self.judul}' ada di rak A."

    def info(self):
        return f"Buku: {self.judul}, Pengarang: {self.pengarang}, ISBN: {self.ISBN}, Jumlah Halaman: {self.jmlHal}, Ukuran: {self.ukuran}"


class Majalah(PerpusItem):
    def __init__(self, judul, subjek, volume, issue):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issue = issue

    def LokasiPenyimpanan(self):
        return f"The magazine '{self.judul}' ada di rak B."

    def info(self):
        return f"Majalah: {self.judul}, Volume: {self.volume}, Issue: {self.issue}"


class Pengarang:
    def __init__(self, nama):
        self.nama = nama

    def info(self):
        return self.nama

    def cari(self, search_query):
        return search_query.lower() in self.nama.lower()



pengarang1 = Pengarang("Yono")
buku1 = Buku("Yono & Yanto", "Dongeng Anak", "123456789", pengarang1.info(), 300, "A4")

majalah1 = Majalah("Adit Maling Timun", "Politik", "Vol 42", "Issue 3")


katalog = Katalog()


katalog.tambah_item(buku1)
katalog.tambah_item(majalah1)


search_query = input("Masukkan Judul: ")


def search_by_title(item, query):
    return query.lower() in item.judul.lower()


search_results = katalog.cari(lambda item: search_by_title(item, search_query))
for result in search_results:
    print(result.info())
    print(result.LokasiPenyimpanan())
