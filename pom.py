import tkinter as tk
from tkinter import ttk, messagebox

class PengisianBensinApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Pengisian Pom Bensin")

        self.master.configure(bg="#1e90ff")

        # Frame utama
        self.main_frame = ttk.Frame(master, padding="60")
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Header
        self.header_label = ttk.Label(self.main_frame, text="Pengisian Pom Bensin", font=("Helvetica", 16, "bold"))
        self.header_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))



        # Gambar
        self.image = tk.PhotoImage(file="pom.png")
        self.image_label = ttk.Label(self.main_frame, image=self.image)
        self.image_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Jenis Bensin
        self.label_jenis_bensin = ttk.Label(self.main_frame, text="Jenis Bensin:")
        self.label_jenis_bensin.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.jenis_bensin = tk.StringVar()
        self.jenis_bensin.set("Pertalite")

        self.option_menu = ttk.Combobox(self.main_frame, textvariable=self.jenis_bensin, values=["Pertalite", "Pertamax", "Pertamax Turbo"])
        self.option_menu.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Jumlah Liter
        self.label_liter = ttk.Label(self.main_frame, text="Jumlah Liter:")
        self.label_liter.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_liter = ttk.Entry(self.main_frame)
        self.entry_liter.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Tombol Hitung Biaya
        self.button_hitung = ttk.Button(self.main_frame, text="Hitung Biaya", command=self.hitung_biaya)
        self.button_hitung.grid(row=4, column=0, columnspan=2, pady=10)

        # Total Biaya
        self.label_total_biaya = ttk.Label(self.main_frame, text="Total Biaya:")
        self.label_total_biaya.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

    def hitung_biaya(self):
        try:
            liter = float(self.entry_liter.get())
            if liter <= 0:
                raise ValueError("Jumlah liter harus lebih dari 0")
            
            harga_per_liter = self.get_harga_per_liter()
            total_biaya = liter * harga_per_liter
            self.label_total_biaya.config(text=f"Total Biaya: Rp {total_biaya:.2f}")

            # Tampilkan pop-up informasi
            self.tampilkan_popup_informasi(f"Biaya pengisian untuk {self.jenis_bensin.get()} sebanyak {liter:.2f} liter adalah Rp {total_biaya:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def get_harga_per_liter(self):
        jenis_bensin = self.jenis_bensin.get()
        if jenis_bensin == "Pertalite":
            return 10000 
        elif jenis_bensin == "Pertamax":
            return 12000  
        elif jenis_bensin == "Pertamax Turbo":
            return 15000  

    def tampilkan_popup_informasi(self, pesan):
        messagebox.showinfo("Informasi", pesan)


if __name__ == "__main__": 
    root = tk.Tk()
    root.geometry("500x600+500+50")  
    
    app = PengisianBensinApp(root)
    root.mainloop()
