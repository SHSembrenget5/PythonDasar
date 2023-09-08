import tkinter as tk
from tkinter import messagebox

class ParkirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Parkir")
        
        self.biaya_per_jam = 2000
        
        self.label_biaya = tk.Label(root, text="Biaya Per Jam Rp. {}".format(self.biaya_per_jam))
        self.label_biaya.pack(side=tk.TOP, padx=10, pady=10)
        
        self.frame_input = tk.Frame(root)
        self.frame_input.pack(padx=10, pady=10)
        
        self.label_nopol = tk.Label(self.frame_input, text="No Plat Polisi:")
        self.label_nopol.grid(row=0, column=0, sticky=tk.W)
        self.entry_nopol = tk.Entry(self.frame_input)
        self.entry_nopol.grid(row=0, column=1)
        
        self.button_cari = tk.Button(self.frame_input, text="Cari", command=self.cari_pelanggan)
        self.button_cari.grid(row=0, column=2, padx=5)
        
        self.frame_pelanggan = tk.Frame(root)
        self.frame_pelanggan.pack(padx=10, pady=10)
        
        self.label_pelanggan = tk.Label(self.frame_pelanggan, text="List Pelanggan")
        self.label_pelanggan.pack(side=tk.TOP)
        
        self.listbox_pelanggan = tk.Listbox(self.frame_pelanggan, width=40)
        self.listbox_pelanggan.pack(fill=tk.BOTH, expand=True)
        
        self.label_pelanggan_kembali = tk.Label(self.frame_pelanggan, text="List Pelanggan Terakhir Keluar")
        self.label_pelanggan_kembali.pack(side=tk.TOP)
        
        self.listbox_pelanggan_kembali = tk.Listbox(self.frame_pelanggan, width=40)
        self.listbox_pelanggan_kembali.pack(fill=tk.BOTH, expand=True)
        
        self.frame_bayar = tk.Frame(root)
        self.frame_bayar.pack(padx=10, pady=10)
        
        self.label_masuk = tk.Label(self.frame_bayar, text="Waktu Masuk:")
        self.label_masuk.grid(row=0, column=0, sticky=tk.W)
        self.entry_masuk = tk.Entry(self.frame_bayar)
        self.entry_masuk.grid(row=0, column=1)
        
        self.label_keluar = tk.Label(self.frame_bayar, text="Waktu Keluar:")
        self.label_keluar.grid(row=1, column=0, sticky=tk.W)
        self.entry_keluar = tk.Entry(self.frame_bayar)
        self.entry_keluar.grid(row=1, column=1)
        
        self.label_biaya = tk.Label(self.frame_bayar, text="Biaya:")
        self.label_biaya.grid(row=2, column=0, sticky=tk.W)
        self.entry_biaya = tk.Entry(self.frame_bayar)
        self.entry_biaya.grid(row=2, column=1)
        
        self.button_kirim = tk.Button(self.frame_bayar, text="Kirim", command=self.simpan_pelanggan)
        self.button_kirim.grid(row=3, columnspan=2, pady=5)
        
    def cari_pelanggan(self):
        nopol = self.entry_nopol.get()
        
        if nopol == "AB 1234 CD":
            self.entry_masuk.insert(0, "08:00")
            self.entry_keluar.insert(0, "10:00")
            self.entry_biaya.insert(0, "4000")
        else:
            messagebox.showerror("Error", "Pelanggan tidak ditemukan!")
        
    def simpan_pelanggan(self):
        nopol = self.entry_nopol.get()
        masuk = self.entry_masuk.get()
        keluar = self.entry_keluar.get()
        biaya = self.entry_biaya.get()
        
        # Lakukan penambahan data pelanggan ke database atau list pelanggan
        
        self.listbox_pelanggan.insert(tk.END, "No Plat Polisi: {}".format(nopol))
        self.listbox_pelanggan.insert(tk.END, "Waktu Masuk: {}".format(masuk))
        self.listbox_pelanggan.insert(tk.END, "Waktu Keluar: {}".format(keluar))
        self.listbox_pelanggan.insert(tk.END, "Biaya: {}".format(biaya))
        
        self.listbox_pelanggan_kembali.insert(tk.END, "No Plat Polisi: {}".format(nopol))
        self.listbox_pelanggan_kembali.insert(tk.END, "Waktu Masuk: {}".format(masuk))
        self.listbox_pelanggan_kembali.insert(tk.END, "Waktu Keluar: {}".format(keluar))
        self.listbox_pelanggan_kembali.insert(tk.END, "Biaya: {}".format(biaya))
        
# Inisialisasi Tkinter
root = tk.Tk()

# Menjalankan aplikasi
app = ParkirApp(root)
root.mainloop()
