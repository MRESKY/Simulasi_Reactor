'''Modul untuk mendefinisikan kelas reaktor kimia'''

class Reactor():
    '''Kelas untuk reaktor kimia'''
    def __init__(self, volume: float, temperatur: float, tekanan: float, konsentrasi_reaktan: float) -> None:
        '''Inisialisasi dengan volume, temperatur, tekanan, dan konsentrasi reaktan'''
        self.volume = volume
        self.temperatur = temperatur
        self.tekanan = tekanan
        self.konsentrasi_reaktan = konsentrasi_reaktan

    def get_status(self) -> None:
        '''Tampilkan status reaktor saat ini'''
        print(f'volume reaktor saat ini {self.volume}, \n suhu reaktor saat ini {self.temperatur}, \n tekanan reaktor saat ini {self.tekanan}, \n konsentrasi reaktan saat ini {self.konsentrasi_reaktan}')

    def update_status(self, volume_baru: float, temperatur_baru: float, tekanan_baru: float, konsentrasi_baru: float) -> None:
        '''Perbarui status reaktor dengan nilai baru'''
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