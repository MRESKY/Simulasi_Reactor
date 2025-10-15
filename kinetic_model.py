'''Modul untuk perhitungan kinetika reaksi kimia pada reaktor'''

class kineticModel():
    '''Kelas untuk model kinetika reaksi kimia'''
    def __init__(self, reaktor, konstanta_reaksi, orde_reaksi) -> None:
        '''Inisialisasi dengan objek reaktor, konstanta reaksi, dan orde reaksi'''
        self.reactor = reaktor
        self.konstanta_reaksi = konstanta_reaksi
        self.orde_reaksi = orde_reaksi

    def calculate_rate(self) -> float:
        '''Hitung laju reaksi berdasarkan konsentrasi reaktan'''
        rate = self.konstanta_reaksi * (self.reactor.konsentrasi_reaktan ** self.orde_reaksi)
        print(f'laju reaksi saat ini adalah {rate}')
        return rate

    def calculate_heat_balance(self) -> tuple[float, float, float]:
        '''Hitung neraca panas dalam reaktor'''
        heat_in = self.reactor.tekanan * self.reactor.volume * self.reactor.temperatur
        heat_out = self.konstanta_reaksi * (self.reactor.konsentrasi_reaktan ** self.orde_reaksi)
        return heat_in - heat_out, heat_in, heat_out