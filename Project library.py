class Library:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi
        self.dosya = open(self.dosya_adi, 'a+')  # 'a+' moda alınarak dosya varsa açılır, yoksa oluşturulur.

    def dosyaya_yaz(self, metin):
        self.dosya.write(metin + '\n')

    def dosyadan_oku(self):
        self.dosya.seek(0)
        icerik = self.dosya.read()
        print("Dosya İçeriği:\n", icerik)

    def listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.read().splitlines()
        for kitap in kitaplar:
            print(kitap)

    def kitap_ekle(self):
        kitap_adi = input("Kitap Başlığı: ")
        yazar = input("Yazar: ")
        yayin_yili = input("Yayın Yılı: ")
        sayfa_sayisi = input("Sayfa Sayısı: ")

        yeni_kitap = f"{kitap_adi}, {yazar}, {yayin_yili}, {sayfa_sayisi}"
        self.dosyaya_yaz(yeni_kitap)
        print(f"{kitap_adi} kitabı kütüphaneye eklendi.")

    def kitap_kaldir(self, kitap_adi):
        self.dosya.seek(0)
        kitaplar = self.dosya.read().splitlines()

        for kitap in kitaplar:
            if kitap.startswith(kitap_adi):
                kitaplar.remove(kitap)
                print(f"{kitap_adi} kitabı kütüphaneden kaldırıldı.")
                break
        else:
            print(f"{kitap_adi} kitabı bulunamadı.")

        # Dosyayı temizle
        self.dosya.truncate(0)

        # Güncellenmiş kitap listesini dosyaya yaz
        for kitap in kitaplar:
            self.dosya.write(kitap + '\n')

    def __del__(self):
        if hasattr(self, 'dosya') and self.dosya is not None:
            self.dosya.close()

lib = Library("Books.txt")

while True:
    # Menüyü ekrana yazdır
    print("\n*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitabı Kaldır")
    print("4) Çıkış")

    # Kullanıcı girişini iste
    secim = input("Lütfen bir seçenek girin (1-4): ")

    # Kullanıcı girişini kontrol et
    if secim == "1":
        lib.listele()
    elif secim == "2":
        lib.kitap_ekle()
    elif secim == "3":
        kitap_adi_silinecek = input("Silinecek kitabın adını girin: ")
        lib.kitap_kaldir(kitap_adi_silinecek)
    elif secim == "4":
        # Kullanıcı çıkış seçeneğini seçtiğinde döngüyü kır
        break
    else:
        print("Geçersiz seçenek, lütfen tekrar deneyin.")

# lib nesnesi otomatik olarak kapatılır (yıkıcı metodu çağrılır)
del lib