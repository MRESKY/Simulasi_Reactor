
class Reactor():
    def __init__(self, volume, temperatur, tekanan, konsentrasi_reaktan):
        self.volume = volume
        self.temperatur = temperatur
        self.tekanan = tekanan
        self.konsentrasi_reaktan = konsentrasi_reaktan
    
    def get_status(self):
        print(f'volume reaktor saat ini {self.volume}, \n suhu reaktor saat ini {self.temperatur}, \n tekanan reaktor saat ini {self.tekanan}, \n konsentrasi reaktan saat ini {self.konsentrasi_reaktan}')

    def update_status(self, volume_baru, temperatur_baru, tekanan_baru, konsentrasi_baru):
        self.volume = volume_baru
        self.temperatur = temperatur_baru
        self.tekanan = tekanan_baru
        self.konsentrasi_reaktan = konsentrasi_baru
        print('status reaktor berhasil diupdate')


if __name__ == "__main__":
    # reactor = Reactor(100, 350, 1.5, 2.0)
    # model = kineticModel(reactor, 0.1, 1)
    # model.calculate_rate()
    # model.calculate_heat_balance()
    pass