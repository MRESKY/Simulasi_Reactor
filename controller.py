'''Controller modul untuk mengatur alur simulasi reaktor kimia'''
import json

class controlSystem():
    '''Kelas untuk mengontrol alur simulasi reaktor kimia'''
    def __init__(self, reactor, kinetic_model) -> None:
        '''Inisialisasi dengan objek reaktor dan model kinetik'''
        self.reactor = reactor
        self.kinetic_model = kinetic_model
        self.steps = 0
        self.data_log = []

    def run_step(self) -> None:
        '''Jalankan satu langkah kontrol dalam simulasi'''
        print('-'*20)
        print(f'--- langkah kontrol ke-{self.steps + 1} ---')
        reactor = self.reactor
        model = self.kinetic_model
        reactor.get_status()
        rate = model.calculate_rate()
        heat_balance, heat_in, heat_out = model.calculate_heat_balance()
        print(f'laju reaksi adalah {rate}')
        print(f'panas masuk dalam reaktor adalah {heat_in}')
        print(f'panas keluar dalam reaktor adalah {heat_out}')
        print(f'selisih panas dalam reaktor adalah {heat_balance}')
        reactor.update_status(
            volume_baru=reactor.volume * 0.99,
            temperatur_baru=reactor.temperatur + 5,
            tekanan_baru=reactor.tekanan * 1.01,
            konsentrasi_baru=reactor.konsentrasi_reaktan - rate * 0.1
        )
        print('--- langkah kontrol selesai --- \n')

    def run_simulation(self, steps: int) -> None:
        '''Jalankan simulasi untuk sejumlah langkah tertentu'''
        print('Memulai simulasi reaktor kimia...')
        for _ in range(steps):
            self.run_step()
            self.steps += 1
            self.log_data()
        self.save_log()

    def log_data(self) -> None:
        '''Catat data simulasi pada setiap langkah'''
        rate = self.kinetic_model.calculate_rate()
        heat_balance, heat_in, heat_out = self.kinetic_model.calculate_heat_balance()
        self.data_log.append({
            'step': self.steps,
            'rate': rate,
            'heat_balance': heat_balance,
            'heat_in': heat_in,
            'heat_out': heat_out
        })

    def save_log(self) -> None:
        '''Simpan log data simulasi ke file JSON'''
        filename = f'simulation_log.json'
        with open (filename, 'w') as f:
            json.dump(self.data_log, f, indent=4)

if __name__ == "__main__":
    pass