import tkinter as tk
from tkinter import filedialog

def ekle():
    entry_text = e.get()
    if entry_text:
        box.insert(tk.END, entry_text)
        e.delete(0, tk.END)

def sil():
    selected_index = box.curselection()
    if selected_index:
        box.delete(selected_index)

def kaydet():
    dosya_yolu = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Metin Dosyaları", "*.txt")])
    if dosya_yolu:
        try:
            with open(dosya_yolu, "w", encoding="utf-8") as f:
                for i in range(box.size()):
                    f.write(box.get(i) + "\n")
        except Exception as e:
            print("Hata:", e)

def yükle():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("Metin Dosyaları", "*.txt")])
    if dosya_yolu:
        try:
            with open(dosya_yolu, "r", encoding="utf-8") as f:
                for line in f:
                    box.insert(tk.END, line.strip())
        except Exception as e:
            print("Hata:", e)


pencere = tk.Tk()
pencere.title("Yapılacaklar Listesi")
pencere.geometry("400x500")  
pencere.configure(bg='#121212')  


button_style = {
    'bg': '#1DB954',  
    'fg': 'white',
    'font': ('Helvetica', 10, 'bold'),
    'relief': 'flat',
    'cursor': 'hand2',
    'activebackground': '#1ed760'  
}

# Frame ayarları
f = tk.Frame(pencere, bg='#121212')
f.pack(pady=20)

# Listbox ve Scrollbar
box = tk.Listbox(f, 
    width=45, 
    height=12,
    bg='#282828',  
    fg='white',
    font=('Helvetica', 10),
    selectmode=tk.SINGLE,
    selectbackground='#1DB954',
    selectforeground='white',
    borderwidth=0)
box.pack(side=tk.LEFT, padx=5)

scroll = tk.Scrollbar(f, command=box.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
box.config(yscrollcommand=scroll.set)

e = tk.Entry(pencere,
    width=45,
    font=('Helvetica', 10),
    bg='#282828',
    fg='white',
    insertbackground='white',  
    relief='flat')
e.pack(pady=10)
e.focus()


bekle = tk.Button(pencere, 
    text="➕ Görev Ekle",
    width=35,
    command=ekle,
    **button_style)
bekle.pack(pady=5)

bsil = tk.Button(pencere,
    text="❌ Görev Sil",
    width=35,
    command=sil,
    **button_style)
bsil.pack(pady=5)

bkaydet = tk.Button(pencere,
    text="💾 Görev Kaydet",
    width=35,
    command=kaydet,
    **button_style)
bkaydet.pack(pady=5)

byükle = tk.Button(pencere,
    text="📂 Görevleri Yükle",
    width=35,
    command=yükle,
    **button_style)
byükle.pack(pady=5)


def on_enter(e):
    e.widget['background'] = '#1ed760'

def on_leave(e):
    e.widget['background'] = '#1DB954'


for button in [bekle, bsil, bkaydet, byükle]:
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

pencere.mainloop()