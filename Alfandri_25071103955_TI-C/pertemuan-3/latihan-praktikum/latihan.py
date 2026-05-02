class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis

    def sound():
        return 'suara' 

class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, __harga):
        super().__init__(self, jenis, merk, tahun_rilis)
        self.harga = __harga

    def get_harga(self):
        return self.harga

    def set_harga(self, harga):
        self.harga = harga

class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, __cc):
        super().__init__(self, jenis, merk, tahun_rilis)
        self.cc = __cc

    def get_cc(self):
        return self.cc

    def set_cc(self, __cc):
        self.cc = __cc

sepeda = Vehicle("sepeda gunung", "polygon", 2022,)
motor = Motor("matic", "honda", 2021, 15000000)
mobil = Mobil("manual", "toyota", 2015, 5000)

print(mobil.get_cc())
print(motor.get_harga())