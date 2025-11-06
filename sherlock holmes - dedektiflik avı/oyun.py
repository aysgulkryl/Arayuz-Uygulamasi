from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Sherlock Holmes - Dedektiflik Avı")
pencere.geometry("700x500")

#Temizleme fonksiyonu

def temizle():
    for widget in pencere.winfo_children():
        widget.destroy()

#Ana menü fonksiyonu

def ana_menu():
    temizle()

    Label(pencere, text="Sherlock Holmes - Dedektiflik Avı",
          font=("Georgia", 24, "bold"), fg="white", bg="#1c1c1c").pack(pady=25)
    
    try:
        img = Image.open("img/1.jpeg") 
        img = img.resize((300, 300))
        sherlock = ImageTk.PhotoImage(img)
        lbl = Label(pencere, image=sherlock, bg="#1c1c1c")
        lbl.image = sherlock
        lbl.pack(pady=10)
    except:
        Label(pencere, text="(Sherlock görseli bulunamadı)", fg="gray", bg="#1c1c1c").pack(pady=20)

    Label(pencere, text="Oyuna hoş geldin dedektif! \n"
                        "Londra’nın sisli sokaklarında yeni bir gizem seni bekliyor. \n"
                        "Suçla savaşmaya hazır mısın?",
          font=("Arial", 14), fg="white", bg="#1c1c1c").pack(pady=15)

    Button(pencere, text="Oyuna Başla", command=vaka_sec,
           font=("Arial", 16, "bold"), bg="#3c3c3c", fg="white", width=20).pack(pady=20)

    Button(pencere, text="Çıkış", command=pencere.destroy,
           font=("Arial", 14), bg="#3c3c3c", fg="white").pack(pady=10)
    
# Vaka Seçme Fonksiyonu

def vaka_sec():
    temizle()

    Label(pencere, text="Vakalar", font=("Georgia", 22, "bold"), fg="white", bg="#1c1c1c").pack(pady=25)

    try:
        img = Image.open("img/2.jpeg")
        img = img.resize((500, 300))
        vakaimg = ImageTk.PhotoImage(img)
        lbl = Label(pencere, image=vakaimg, bg="#1c1c1c")
        lbl.image = vakaimg
        lbl.pack(pady=10)
    except:
        Label(pencere, text="(Vaka görseli bulunamadı)", fg="gray", bg="#1c1c1c").pack(pady=10)

    Button(pencere, text="Benekli Kordon", command=vaka_beneklikordon,
           font=("Arial", 16), bg="#3c3c3c", fg="white", width=20).pack(pady=15)

    Button(pencere, text="Ana Menü", command=ana_menu,
           font=("Arial", 14), bg="#3c3c3c", fg="white").pack(pady=15)

# Vaka Özeti Fonksiyonu

def vaka_beneklikordon():
    temizle()

    Label(pencere, text="Benekli Kordon Vakası",
          font=("Georgia", 20, "bold"), fg="white", bg="#1c1c1c").pack(pady=20)

    Label(pencere, text="Julia Stoner, ikiz kardeşi Helen Stoner ve İngiltere'nin en eski Sakson hanedanından Roylott'ların son temsilcisi olan üvey babasıyla beraber Stoke Moran kasabasında yaşıyordu. Düğününden birkaç hafta önce gizemli bir şekilde odasında ölü bulundu. Geceleri gizemli bir ıslık sesi duyduğunu söyleyen Julia'nın son sözleri 'BENEKLİ KORDON' oldu. Ölümünün arkasındaki sır ise hala çözülemedi.",
          font=("Arial", 14), fg="white", bg="#1c1c1c", justify="center",wraplength=650).pack(pady=25),
        

    Button(pencere, text="Olay yerine git", command=olay_yeri,
           font=("Arial", 16), bg="#3c3c3c", fg="white", width=20).pack(pady=20)

    Button(pencere, text="Geri", command=vaka_sec,
           font=("Arial", 14), bg="#3c3c3c", fg="white").pack(pady=10)
    
# Olay Yeri İnceleme Fonksiyonu

def olay_yeri():
    temizle()

    Label(pencere, text="Olay Yeri İncelemesi",
          font=("Georgia", 20, "bold"), fg="white", bg="#1c1c1c").pack(pady=20)

    try:
        img = Image.open("img/3.jpeg")
        img = img.resize((500, 300))
        evimg = ImageTk.PhotoImage(img)
        lbl = Label(pencere, image=evimg, bg="#1c1c1c")
        lbl.image = evimg
        lbl.pack(pady=10)
    except:
        Label(pencere, text="(Ev görseli bulunamadı)", fg="gray", bg="#1c1c1c").pack(pady=10)

    Button(pencere, text="Julia'nın Odası", command=julia_oda,
           font=("Arial", 14), bg="#3c3c3c", fg="white", width=25).pack(pady=5)
    Button(pencere, text="Dr. Roylott'un Odası", command=dr_oda,
           font=("Arial", 14), bg="#3c3c3c", fg="white", width=25).pack(pady=5)
    Button(pencere, text="Bahçe İncelemesi", command=bahce,
           font=("Arial", 14), bg="#3c3c3c", fg="white", width=25).pack(pady=5)

    Button(pencere, text="Adli Tıpa Git", command=adli_tip,
           font=("Arial", 14, "bold"), bg="#5a5a5a", fg="white", width=25).pack(pady=20)

    Button(pencere, text="Geri", command=vaka_beneklikordon,
           font=("Arial", 13), bg="#3c3c3c", fg="white").pack(pady=10)
    
# Odaların Fonksiyonları

def oda_ekrani(baslik, img_dosya, metin):
    temizle()

    Label(pencere, text=baslik, font=("Georgia", 20, "bold"),
          fg="white", bg="#1c1c1c").pack(pady=15)

    try:
        img = Image.open(img_dosya)
        img = img.resize((400, 300))
        odaimg = ImageTk.PhotoImage(img)
        lbl = Label(pencere, image=odaimg, bg="#1c1c1c")
        lbl.image = odaimg
        lbl.pack(pady=10)
    except:
        Label(pencere, text="(Görsel bulunamadı)", fg="gray", bg="#1c1c1c").pack(pady=10)

    Label(pencere, text=metin, font=("Arial", 13), fg="white", bg="#1c1c1c",justify="center", wraplength=650).pack(pady=15)

    Button(pencere, text="Geri", command=olay_yeri,
           font=("Arial", 14), bg="#3c3c3c", fg="white").pack(pady=15)

def julia_oda():
    oda_ekrani("Julia'nın Odası", "img/4.png", " Odayı inceleyelim. Dikkatimizi ilk yatak çekiyor. Julia'nın yatağı yere sabitlenmiş, kıpırdamıyor. Bu durum oldukça garip. Yatağın yanında yere kadar uzanan bir hizmetçi zil kordonu var ancak evde hiçbir çalışan yok. Yani bu sahte. Birde yatağın yanında duvarda bir havalandırma deliği bulunuyor. Bu delik dışarıya değil yandaki Dr. Roylott'ın odasına açılıyor. Hadi bir sonraki odaya geçelim.")

def dr_oda():
    oda_ekrani("Dr.Roylott'un Odası", "img/5.png", "Bu oda Dr. Roylott'a ait. Oldukça dağınık. Duvarda biraz önce gördüğümüz havalandırma deliğinin diğer ucunu görüyoruz. Odanın köşesinde kilitli demir bir kasa var. Üzerinde de bir kase süt bulunuyor. Dr. Roylott'ın vahşi hayvanlara meraklı olduğunu biliyoruz. Evinde maymun ve bahçesinde leopar besliyor. Ancak sütü içebilecek bir kedisi yok. Öyleyse bu süt ne için? Bahçeye de bir göz atalım." )

def bahce():
    oda_ekrani("Bahçe İncelemesi", "img/6.png", "Julia'nın odasının penceresinde demirden parmaklıklar var. Oldukça sağlam görünüyor. Dışarıdan birileri pencereden odaya girmiş olamaz. Bahçenin bir köşesinde Dr. Roylott'ın kalmalarına izin verdiği çingeneler kamp kurmuşlar. Dikkat çeken bir detay var. Başlarına 'BENEKLİ MENDİLLER' takmışlar. Kurbanın son sözleri 'BENEKLİ KORDON'du. Bu bir tesadüf mü, yoksa aradığımız ipucu bu mu? Bir de cesedi inceleyelim.")


# Adli Tıp Sonucu Fonksiyonu

def adli_tip():
    temizle()

    Label(pencere, text="Adli Tıp Raporu", font=("Georgia", 20, "bold"),
          fg="white", bg="#1c1c1c").pack(pady=15)

    try:
        img = Image.open("img/7.jpeg")
        img = img.resize((400, 300))
        raporimg = ImageTk.PhotoImage(img)
        lbl = Label(pencere, image=raporimg, bg="#1c1c1c")
        lbl.image = raporimg
        lbl.pack(pady=10)
    except:
        Label(pencere, text="(Adli tıp görseli bulunamadı)", fg="gray", bg="#1c1c1c").pack(pady=10)

    Label(pencere, text="Kurban: Julia Stoner.\n"
                        "Vücutta herhangi bir yara izi, boğuşma veya darp izine rastlanmamıştır.\n"
                        "Toksikoloji raporu temizdir. Bilinen hiçbir zehre (arsenik vb.) rastlanmamıştır.\n"
                        "SONUÇ: Ölüm nedeni BİLİNMİYOR. Ani bir şok veya tespit edilemeyen, egzotik bir toksin olabilir.",
          font=("Arial", 13), fg="white", bg="#1c1c1c", wraplength=650, justify="center").pack(pady=20)

    Button(pencere, text="Tanıkları Sorgula", command=sorgu_odasi,
           font=("Arial", 15), bg="#3c3c3c", fg="white", width=25).pack(pady=20)

    Button(pencere, text="Geri", command=olay_yeri,
           font=("Arial", 13), bg="#3c3c3c", fg="white").pack(pady=10)
    
# Sorgu Odası Fonksiyonu

def sorgu_odasi():
    temizle()

    Label(pencere, text="Sorgu Odası",
          font=("Georgia", 20, "bold"), fg="white", bg="#1c1c1c", justify="center", wraplength=650).pack(pady=15)
    
    try:
        img = Image.open("img/8.jpeg")
        img = img.resize((400, 300))
        sorguimg = ImageTk.PhotoImage(img)
        lbl = Label(pencere, image=sorguimg, bg="#1c1c1c")
        lbl.image = sorguimg
        lbl.pack(pady=10)
    except:
        Label(pencere, text="(Sorgu odası görseli bulunamadı)", fg="gray", bg="#1c1c1c").pack(pady=10)

    Button(pencere, text="Tanık 1 - Dr. Roylott", command=lambda: tanik("Dr. Roylott", "img/9.png", "Holmes, değil mi? Bir zamanlar Hindistan'da çalışmıştım. Vahşi hayvanlara olan tutkum buradan geliyor. Eşimin vefatından sonra hayvanlara iyice bağlandım. Üvey kızlarımla olan ilişkim gayet normaldi. Julia evlenmek istediğini söylediğinde bile karşı çıkmamıştım. O süt tabağı ve kasa da benim kişisel eşyalarım. Çingenelerin bahçede kalmasına da ben izin verdim. Ne olmuş yani? Burnunu benim işlerime sokma!"),
           font=("Arial", 14), bg="#3c3c3c", fg="white", width=25).pack(pady=8)

    Button(pencere, text="Tanık 2 - Helen Stoner", command=lambda: tanik("Helen Stoner", "img/10.png", "Kardeşimi çok seviyordum. Onun bir yuva kurmasını ve mutlu olmasını çok istiyordum ancak ne yalan söyleyeyim o evlenip gidince bu koca evde üvey babamla yalnız kalmaktan korkuyordum. O garip bir adam. Bazen gereksiz yere aşırı sinirlenebiliyor, hatta şiddete de eğilimli olduğunu söyleyebilirim. Öyle ki Julia evlenmek istediğini söylediğinde ona şiddetle karşı çıkmıştı. Belki de annemin bıraktığı mirası kaybetmekten korkuyordu. Çünkü biz evlendiğimizde annemin kalan mirasının bize geçeceğini gösteren bir sözleşme var. Julia'ya dair o gece hatırlayabildiğim tek şey onun sanki korkudan bembeyaz kesilmiş suratı. Onu çok özlüyorum. "),
           font=("Arial", 14), bg="#3c3c3c", fg="white", width=25).pack(pady=8)

    Button(pencere, text="Tanık 3 - Çingeneler", command=lambda: tanik("Çingeneler", "img/11.png", "Biz bir şey görmedik, efendim.O gece kamptaydık. Dr. Roylott bize karşı hep iyi davranmıştır, arazisinde kalmamıza izin verir.Başımızdaki şu benekli mendilleri soruyorsanız, bunlar bizim geleneksel kıyafetimizdir. 'Benekli Kordon' diye bir şeyi hiç duymadık."),
           font=("Arial", 14), bg="#3c3c3c", fg="white", width=25).pack(pady=8)

    Button(pencere, text="Sorgulamayı Bitir", command=katil_kim,
           font=("Arial", 15, "bold"), bg="#5a5a5a", fg="white", width=25).pack(pady=20)

    Button(pencere, text="Geri", command=adli_tip,
           font=("Arial", 13), bg="#3c3c3c", fg="white").pack(pady=10)

# Tanıkların Fonksiyonları

def tanik(isim, img_dosya, ifade):
    temizle()

    Label(pencere, text=f"{isim} ifadesi", font=("Georgia", 20, "bold"),
          fg="white", bg="#1c1c1c").pack(pady=15)

    try:
        img = Image.open(img_dosya)
        img = img.resize((350, 300))
        timg = ImageTk.PhotoImage(img)
        lbl = Label(pencere, image=timg, bg="#1c1c1c")
        lbl.image = timg
        lbl.pack(pady=10)
    except:
        Label(pencere, text="(Tanık görseli bulunamadı)", fg="gray", bg="#1c1c1c").pack(pady=10)

    Label(pencere, text=ifade, font=("Arial", 13), fg="white", bg="#1c1c1c",
          justify="center", wraplength=650).pack(pady=15)

    Button(pencere, text="Geri", command=sorgu_odasi,
           font=("Arial", 14), bg="#3c3c3c", fg="white").pack(pady=15)

# Karar Fonksiyonu

def katil_kim():
    temizle()

    Label(pencere, text="Katil Kim?",
          font=("Georgia", 22, "bold"), fg="white", bg="#1c1c1c").pack(pady=20)
    
    try:
        img = Image.open("img/12.png")
        img = img.resize((400, 300))
        kimimg = ImageTk.PhotoImage(img)
        lbl = Label(pencere, image=kimimg, bg="#1c1c1c")
        lbl.image = kimimg
        lbl.pack(pady=10)
    except:
        Label(pencere, text="(Katil kim görseli bulunamadı)", fg="gray", bg="#1c1c1c").pack(pady=10)

    Button(pencere, text= "Dr. Roylott", command=dogru_cevap,
           font=("Arial", 15), bg="#3c3c3c", fg="white", width=20).pack(pady=10)
    Button(pencere, text="Helen Stoner", command=yanlis_cevap,
           font=("Arial", 15), bg="#3c3c3c", fg="white", width=20).pack(pady=10)
    Button(pencere, text="Çingeneler", command=yanlis_cevap,
           font=("Arial", 15), bg="#3c3c3c", fg="white", width=20).pack(pady=10)

    Button(pencere, text="Geri", command=sorgu_odasi,
           font=("Arial", 13), bg="#3c3c3c", fg="white").pack(pady=15)

def dogru_cevap():
    temizle()

    Label(pencere, text="Aferin Dedektif!\n"
                        "Vaka Çözüldü!",
          font=("Georgia", 22, "bold"), fg="#ff2600").pack(pady=20)

    try:
        img = Image.open("img/13.png")
        img = img.resize((300, 300))
        arrest = ImageTk.PhotoImage(img)
        lbl = Label(pencere, image=arrest, bg="#1c1c1c")
        lbl.image = arrest
        lbl.pack(pady=10)
    except:
        Label(pencere, text="(Tutuklu görseli bulunamadı)", fg="gray", bg="#1c1c1c").pack(pady=10)

    Label(pencere, text="Dr. Roylott tutuklandı!\n"
                        "Karısından kalan mirası üvey kızına vermemek için onu zehirledi. Demir kasasının içinde Hindistan'dan özel getirttiği benekli kordon yılanı bulunuyordu. Her gece havalandırma deliğinden yılanı Julia'nın odasına yolluyordu. Islık çalarak ve sütün kokusu sayesinde yılanı tekrar odasına çağırıyordu.\n"
                        "Bir gizemi daha çözdün, Sherlock!",
          font=("Arial", 14), fg="white", bg="#1c1c1c",wraplength=650, justify="center").pack(pady=20)

    Button(pencere, text="Ana Menüye Dön", command=ana_menu,
           font=("Arial", 14), bg="#3c3c3c", fg="white").pack(pady=10)

    Button(pencere, text="Çıkış", command=pencere.destroy,
           font=("Arial", 14), bg="#3c3c3c", fg="white").pack(pady=5)

def yanlis_cevap():
    temizle()

    Label(pencere, text="Başaramadın!",
          font=("Georgia", 22, "bold"), fg="red").pack(pady=20)

    Label(pencere, text="Yanlış şüpheliyi seçtin.\n"
                        "Vakayı tekrar dene.",
          font=("Arial", 14), fg="white", bg="#1c1c1c").pack(pady=20)

    Button(pencere, text="Vakayı Tekrar Dene", command=vaka_beneklikordon,
           font=("Arial", 14), bg="#3c3c3c", fg="white").pack(pady=10)

    Button(pencere, text="Ana Menüye Dön", command=ana_menu,
           font=("Arial", 14), bg="#3c3c3c", fg="white").pack(pady=10)

    Button(pencere, text="Çıkış", command=pencere.destroy,
           font=("Arial", 14), bg="#3c3c3c", fg="white").pack(pady=5)
    

# Oyunu Başlat

ana_menu()
pencere.mainloop()

