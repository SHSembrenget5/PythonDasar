from tkinter import *
from tkinter import messagebox

def hapus():
    # Membersihkan entri data siswa
    nama_entry.delete(0, END)
    tanggal_lahir_entry.delete(0, END)
    asal_sekolah_entry.delete(0, END)
    nisn_entry.delete(0, END)
    nama_ayah_entry.delete(0, END)
    nama_ibu_entry.delete(0, END)
    nomor_telepon_entry.delete(0, END)
    alamat_text.delete(1.0, END)

def simpan():
    # Ambil nilai dari setiap entri data siswa baru
    nama = nama_entry.get()
    tanggal_lahir = tanggal_lahir_entry.get()
    asal_sekolah = asal_sekolah_entry.get()
    nisn = nisn_entry.get()
    nama_ayah = nama_ayah_entry.get()
    nama_ibu = nama_ibu_entry.get()
    nomor_telepon = nomor_telepon_entry.get()
    alamat = alamat_text.get(1.0, END)

    # Tampilkan jendela baru dengan menggunakan Toplevel dari Tkinter
    jendela_baru = Toplevel(root)
    jendela_baru.title("DATA SISWA BARU")

    # Frame judul
    judul_frame = Frame(jendela_baru, bg="cyan", padx=10, pady=10)
    judul_frame.pack()

    # Label judul di jendela baru
    judul_label = Label(judul_frame, text="DATA SISWA BARU", font=("Arial", 14), bg="cyan")
    judul_label.pack()

    # Frame data siswa di jendela baru
    data_siswa_frame = Frame(jendela_baru, padx=10, pady=10)
    data_siswa_frame.pack()

    # Menampilkan data siswa yang baru saja disimpan
    nama_label = Label(data_siswa_frame, text="Nama Lengkap:")
    nama_label.grid(row=0, column=0, sticky=W)
    nama_label_value = Label(data_siswa_frame, text=nama)
    nama_label_value.grid(row=0, column=1)

    tanggal_lahir_label = Label(data_siswa_frame, text="Tanggal Lahir:")
    tanggal_lahir_label.grid(row=1, column=0, sticky=W)
    tanggal_lahir_label_value = Label(data_siswa_frame, text=tanggal_lahir)
    tanggal_lahir_label_value.grid(row=1, column=1)

    asal_sekolah_label = Label(data_siswa_frame, text="Asal Sekolah:")
    asal_sekolah_label.grid(row=2, column=0, sticky=W)
    asal_sekolah_label_value = Label(data_siswa_frame, text=asal_sekolah)
    asal_sekolah_label_value.grid(row=2, column=1)

    nisn_label = Label(data_siswa_frame, text="NISN:")
    nisn_label.grid(row=3, column=0, sticky=W)
    nisn_label_value = Label(data_siswa_frame, text=nisn)
    nisn_label_value.grid(row=3, column=1)

    nama_ayah_label = Label(data_siswa_frame, text="Nama Ayah:")
    nama_ayah_label.grid(row=4, column=0, sticky=W)
    nama_ayah_label_value = Label(data_siswa_frame, text=nama_ayah)
    nama_ayah_label_value.grid(row=4, column=1)

    nama_ibu_label = Label(data_siswa_frame, text="Nama Ibu:")
    nama_ibu_label.grid(row=5, column=0, sticky=W)
    nama_ibu_label_value = Label(data_siswa_frame, text=nama_ibu)
    nama_ibu_label_value.grid(row=5, column=1)

    nomor_telepon_label = Label(data_siswa_frame, text="Nomor Telepon / HP:")
    nomor_telepon_label.grid(row=6, column=0, sticky=W)
    nomor_telepon_label_value = Label(data_siswa_frame, text=nomor_telepon)
    nomor_telepon_label_value.grid(row=6, column=1)

    alamat_label = Label(data_siswa_frame, text="Alamat:")
    alamat_label.grid(row=7, column=0, sticky=W)
    alamat_label_value = Label(data_siswa_frame, text=alamat)
    alamat_label_value.grid(row=7, column=1)

    # Menampilkan tombol OK di jendela baru untuk menutupnya
    ok_button = Button(jendela_baru, text="OK", command=jendela_baru.destroy)
    ok_button.pack()

    # Lakukan apa pun yang perlu dilakukan dengan data siswa yang telah disimpan
    # Misalnya, menyimpannya di database atau menuliskannya ke file

# Membuat instance dari Tkinter
root = Tk()
root.title("DATA SISWA BARU")

# Frame judul dengan background berwarna cyan
judul_frame = Frame(root, bg="cyan", padx=10, pady=10)
judul_frame.pack()

# Label judul
judul_label = Label(judul_frame, text="DATA SISWA BARU", font=("Arial", 14), bg="cyan")
judul_label.pack()

# Frame data siswa
data_siswa_frame = Frame(root, padx=10, pady=10)
data_siswa_frame.pack()

# Label dan Entry untuk Nama Lengkap
nama_label = Label(data_siswa_frame, text="Nama Lengkap:")
nama_label.grid(row=0, column=0, sticky=W)
nama_entry = Entry(data_siswa_frame)
nama_entry.grid(row=0, column=1)

# Label dan Entry untuk Tanggal Lahir
tanggal_lahir_label = Label(data_siswa_frame, text="Tanggal Lahir:")
tanggal_lahir_label.grid(row=1, column=0, sticky=W)
tanggal_lahir_entry = Entry(data_siswa_frame)
tanggal_lahir_entry.grid(row=1, column=1)

# Label dan Entry untuk Asal Sekolah
asal_sekolah_label = Label(data_siswa_frame, text="Asal Sekolah:")
asal_sekolah_label.grid(row=2, column=0, sticky=W)
asal_sekolah_entry = Entry(data_siswa_frame)
asal_sekolah_entry.grid(row=2, column=1)

# Label dan Entry untuk NISN
nisn_label = Label(data_siswa_frame, text="NISN:")
nisn_label.grid(row=3, column=0, sticky=W)
nisn_entry = Entry(data_siswa_frame)
nisn_entry.grid(row=3, column=1)

# Label dan Entry untuk Nama Ayah
nama_ayah_label = Label(data_siswa_frame, text="Nama Ayah:")
nama_ayah_label.grid(row=4, column=0, sticky=W)
nama_ayah_entry = Entry(data_siswa_frame)
nama_ayah_entry.grid(row=4, column=1)

# Label dan Entry untuk Nama Ibu
nama_ibu_label = Label(data_siswa_frame, text="Nama Ibu:")
nama_ibu_label.grid(row=5, column=0, sticky=W)
nama_ibu_entry = Entry(data_siswa_frame)
nama_ibu_entry.grid(row=5, column=1)

# Label dan Entry untuk Nomor Telepon / HP
nomor_telepon_label = Label(data_siswa_frame, text="Nomor Telepon / HP:")
nomor_telepon_label.grid(row=6, column=0, sticky=W)
nomor_telepon_entry = Entry(data_siswa_frame)
nomor_telepon_entry.grid(row=6, column=1)

# Frame untuk Alamat
alamat_frame = Frame(root, padx=10, pady=10)
alamat_frame.pack()

# Label untuk Alamat
alamat_label = Label(alamat_frame, text="Alamat:")
alamat_label.pack()

# Text widget untuk Alamat
alamat_text = Text(alamat_frame, height=5, width=30)
alamat_text.pack()

# Frame untuk tombol Hapus dan Simpan
tombol_frame = Frame(root, padx=10, pady=10)
tombol_frame.pack()

# Tombol Hapus
hapus_button = Button(tombol_frame, text="Hapus", command=hapus)
hapus_button.grid(row=0, column=0)

# Tombol Simpan
simpan_button = Button(tombol_frame, text="Simpan", command=simpan)
simpan_button.grid(row=0, column=1)

# Menjalankan main loop Tkinter
root.mainloop()
