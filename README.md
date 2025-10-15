# Simulasi Reaktor Kimia Sederhana

Proyek ini merupakan simulasi reaktor kimia berbasis OOP Python, yang terdiri dari beberapa komponen utama: reaktor, model kinetika, sistem kontrol, dan visualisasi (fitur mendatang).

## Struktur Proyek

- `main.py` — Entry point untuk menjalankan simulasi.
- [`reactor.py`](reactor.py) — Implementasi kelas [`Reactor`](reactor.py) untuk merepresentasikan reaktor kimia.
- [`kinetic_model.py`](kinetic_model.py) — Implementasi kelas [`kineticModel`](kinetic_model.py) untuk perhitungan laju reaksi dan neraca panas.
- [`controller.py`](controller.py) — Implementasi kelas [`controlSystem`](controller.py) untuk mengatur simulasi dan logging.
- [`visualizer.py`](visualizer.py) — Placeholder untuk fitur visualisasi di masa depan.
- `simulation_log.json` — Hasil log simulasi dalam format JSON.
- `LICENSE` — Lisensi MIT.

## Cara Menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Masukkan parameter simulasi yang dibutuhkan di `main.py`.
3. Jalankan perintah berikut di terminal:
   ```sh
   python main.py
   ```
4. Hasil simulasi akan dicatat di file `simulation_log.json`.

## Konfigurasi Simulasi

Parameter simulasi dapat diubah di [`main.py`](main.py):

- Volume reaktor
- Suhu
- Tekanan
- Konsentrasi reaktan
- Konstanta laju reaksi
- Orde reaksi
- Jumlah langkah simulasi

## Lisensi

Proyek ini menggunakan [MIT License](LICENSE).

---

Dikembangkan oleh Muhammad Resky Rachmanto.
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
