import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3


label = QFont("Centruy Gothic", 15)
label_girdi = QFont("Centruy Gothic", 12)
label_combo = QFont("Centruy Gothic", 11)
labelgiris = QFont("Centruy Gothic", 20)

baglanti = sqlite3.connect("kutuphane.db")
etiket = baglanti.cursor()

etiket.execute(
    "Create Table If Not Exists kitaplar(Kitapadi TEXT, Yazaradi TEXT, Yayınevi TEXT, Kitaptürü TEXT, Baski INT, KitapAciklama TEXT, kitapDurum TEXT)")
etiket.execute(
    "Create Table If Not Exists uyeler(kullaniciId TEXT, kullanicipass TEXT, kullaniciemail TEXT, GTarih TEXT,ATarih TEXT,YTarih TEXT,universite TEXT,Bolum TEXT)")
etiket.execute("Create Table If Not Exists uniler(Hangi_uni TEXT)")
etiket.execute("Create Table If Not Exists bölümler(sira TEXT)")
etiket.execute(
    "Create Table If Not Exists emanetler(kitap_adi TEXT, kim_aldi TEXT)")


class giris_pencere(QWidget):

    def kisim(self):
        self.kitapekle = QPushButton("Kitap Ekle", self)
        self.kitapekle.setFont(label)
        self.kitapekle.setGeometry(50, 75, 250, 100)

        self.kitapemanet = QPushButton("Emanet Ekle", self)
        self.kitapemanet.setFont(label)
        self.kitapemanet.setGeometry(330, 75, 250, 100)

        self.uyeekle = QPushButton("Üye Ekle", self)
        self.uyeekle.setFont(label)
        self.uyeekle.setGeometry(610, 75, 250, 100)

        self.kitaplistesi = QPushButton("Kitap Listesi", self)
        self.kitaplistesi.setFont(label)
        self.kitaplistesi.setGeometry(50, 275, 250, 100)

        self.emanetlistesi = QPushButton("Emanet Listesi", self)
        self.emanetlistesi.setFont(label)
        self.emanetlistesi.setGeometry(330, 275, 250, 100)

        self.uyeliste = QPushButton("Üye Listele", self)
        self.uyeliste.setFont(label)
        self.uyeliste.setGeometry(610, 275, 250, 100)

    def kitapekleyegec(self):
        self.gec = kitapekle_gec()
        self.gec.show()

    def kitaplisteyegec(self):
        self.gec2 = kitap_listele()
        self.gec2.show()

    def uyeekleyegec(self):
        self.gec3 = uye_ekle()
        self.gec3.show()

    def uyelisteyegec(self):
        self.gec4 = uye_listele()
        self.gec4.show()

    def emanetekleyegec(self):
        self.gec5 = emanet_ekle()
        self.gec5.show()

    def emanetlisteleyegec(self):
        self.gec6 = emanet_listele()
        self.gec6.show()

    def __init__(self):
        super().__init__()
        self.kisim()
        self.setGeometry(400, 250, 900, 500)
        self.kitapekle.clicked.connect(self.kitapekleyegec)
        self.kitaplistesi.clicked.connect(self.kitaplisteyegec)
        self.uyeekle.clicked.connect(self.uyeekleyegec)
        self.uyeliste.clicked.connect(self.uyelisteyegec)
        self.kitapemanet.clicked.connect(self.emanetekleyegec)
        self.emanetlistesi.clicked.connect(self.emanetlisteleyegec)
        self.show()


class kitapekle_gec(QWidget):

    def kisim(self):
        self.kitap_ekle_label = QLabel("Kitap Adı  :", self)
        self.kitap_ekle_label.setFont(label)
        self.kitap_ekle_label.setGeometry(150, 67, 180, 25)

        self.kitap_ekle = QLineEdit(self)
        self.kitap_ekle.setFont(label_girdi)
        self.kitap_ekle.setGeometry(320, 70, 180, 25)

        self.yazar_ekle_label = QLabel("Yazar Adı  :", self)
        self.yazar_ekle_label.setFont(label)
        self.yazar_ekle_label.setGeometry(150, 127, 180, 25)

        self.yazar_ekle = QLineEdit(self)
        self.yazar_ekle.setFont(label_girdi)
        self.yazar_ekle.setGeometry(320, 130, 180, 25)

        self.yayınevi_label = QLabel("Yayın Evi  :", self)
        self.yayınevi_label.setFont(label)
        self.yayınevi_label.setGeometry(150, 187, 180, 25)

        self.yayınevi_ekle = QLineEdit(self)
        self.yayınevi_ekle.setFont(label_girdi)
        self.yayınevi_ekle.setGeometry(320, 190, 180, 25)

        self.kitap_türü = QLabel("Kitap Türü  :", self)
        self.kitap_türü.setFont(label)
        self.kitap_türü.setGeometry(150, 247, 180, 25)

        self.kitap_türü_combo = QComboBox(self)
        self.kitap_türü_combo.setFont(label_combo)
        self.kitap_türü_combo.setGeometry(320, 245, 180, 30)
        self.kitap_türü_combo.addItems(
            ["Seçiniz", "Anı", "Biyografi", "Edebiyat", "Felsefe", "Gezi", "Masal", "Bilim", "Deneme", "Mektup"])

        self.baski = QLabel("Baskı Sayısı  :", self)
        self.baski.setFont(label)
        self.baski.setGeometry(150, 307, 180, 25)

        self.baski_girdi = QLineEdit(self)
        self.baski_girdi.setFont(label_girdi)
        self.baski_girdi.setGeometry(320, 310, 180, 25)

        self.kayit_et = QPushButton("Kayıt Et", self)
        self.kayit_et.setFont(label)
        self.kayit_et.setGeometry(230, 360, 200, 80)

        self.isimbelirtme = QLabel("Kitaplarımız", self)
        self.isimbelirtme.setFont(label)
        self.isimbelirtme.setGeometry(700, 20, 200, 50)

        self.liste = QListWidget(self)
        self.liste.setGeometry(550, 70, 400, 260)
        self.liste.setFont(label)

    def kayitettir(self):
        self.kitapekle = self.kitap_ekle.text()
        self.yazarekle = self.yazar_ekle.text()
        self.yayıneviekle = self.yayınevi_ekle.text()
        self.kitaptürü = self.kitap_türü_combo.currentText()
        self.baskisayisi = self.baski_girdi.text()

        etiket.execute("Insert Into kitaplar VALUES (?,?,?,?,?)",
                       (self.kitapekle, self.yazarekle, self.yayıneviekle, self.kitaptürü, self.baskisayisi))
        baglanti.commit()

    def listele(self):
        etiket.execute("Select * From kitaplar")
        data = etiket.fetchall()
        for i in data:
            self.liste.addItem(i[0])

    def __init__(self):
        super().__init__()
        self.setGeometry(400, 300, 1000, 600)
        self.kisim()
        self.kayit_et.clicked.connect(self.kayitettir)
        self.listele()
        self.show()


class kitap_listele(QWidget):

    def kisim(self):
        self.liste = QListWidget(self)
        self.liste.setGeometry(40, 70, 400, 500)
        self.liste.setFont(label)
        data = etiket.execute("Select * from kitaplar")
        for i in data:
            self.liste.addItem(i[0])

        self.kitapismi = QLabel("Kitap İsminden Arayınız :", self)
        self.kitapismi.setFont(label)
        self.kitapismi.setGeometry(550, 100, 230, 30)

        self.kitapismi_girdi = QLineEdit(self)
        self.kitapismi_girdi.setFont(label_girdi)
        self.kitapismi_girdi.setGeometry(800, 104, 180, 25)

        self.yazarismi = QLabel("Yazar İsminden Arayınız :", self)
        self.yazarismi.setFont(label)
        self.yazarismi.setGeometry(550, 160, 230, 30)

        self.yazarismi_girdi = QLineEdit(self)
        self.yazarismi_girdi.setFont(label_girdi)
        self.yazarismi_girdi.setGeometry(800, 163, 180, 25)

        self.aramayap = QPushButton("Arama Yap", self)
        self.aramayap.setFont(label)
        self.aramayap.setGeometry(660, 210, 200, 70)

        self.ara_sonuc = QLabel("Arama Sonuçları :", self)
        self.ara_sonuc.setFont(label)
        self.ara_sonuc.setGeometry(550, 290, 300, 30)

        self.listeli = QListWidget(self)
        self.listeli.setFont(label_girdi)
        self.listeli.setGeometry(547, 328, 450, 240)
        self.listeli.itemClicked.connect(self.clicked)
        self.liste.itemClicked.connect(self.clicked)
        self.delete = QPushButton("Sil", self)
        self.delete.setFont(label)
        self.delete.setGeometry(670, 600, 170, 60)

        ekle = emanet_ekle()

    def kitapadindan_sorgula(self):
        etiket.execute("Select * From kitaplar")
        for i in etiket.fetchall():
            if i[0] == self.kitapismi_girdi.text():
                self.listeli.addItem(i[0])
            elif i[1] == self.yazarismi_girdi.text():
                self.listeli.addItem(i[0])
        baglanti.commit()

    def clicked(self, item):
        kitapismi = item.text()
        kontrol = etiket.execute("Select * from kitaplar WHERE Kitapadi = ?",(kitapismi,))
        durum = kontrol.fetchall()[0][0]

    def sil(self):
        cevap = QMessageBox.question(kitap_listele(), "Kayıt Sil", "Kitabı silmek istediğinize eminmisiniz?", \
                                     QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.Yes:
            self.secili = self.listeli.selectedItems()
            self.silinecek = self.secili[0].text()
            etiket.execute("Delete FROM kitaplar WHERE Kitapadi= ?",(self.silinecek,))
            baglanti.commit()

    def kitap_sorgu_emanet(self):
        secilecek = self.listeli.selectedItems()
        sec = secilecek[0].text()
        fetch = etiket.execute("Select kitap_adi FROM emanetler WHERE kitap_adi = '%s'" % (sec))
        for i in fetch.fetchall():
            if sec == i[0]:
                QMessageBox.about(self, "Bilgilendirme", "Bu Kitap Şuanda Başkasında Emanet Verilemez!")
                baglanti.commit()
            else:
                QMessageBox.about(self, "as", "asdlfkmlas")
                baglanti.commit()

    def __init__(self):
        super().__init__()
        self.setGeometry(400, 100, 1100, 760)
        self.kisim()
        self.aramayap.clicked.connect(self.kitapadindan_sorgula)
        self.listeli.itemClicked.connect(self.kitap_sorgu_emanet)
        self.delete.clicked.connect(self.sil)
        self.show()


class uye_ekle(QWidget):
    def uye_ekle(self):
        self.kullaniciadi = QLabel("Adınız ve Soyadınız :", self)
        self.kullaniciadi.move(40, 30)
        self.kullaniciadi.setFont(label)
        self.kullaniciadi_girdi = QLineEdit(self)
        self.kullaniciadi_girdi.setGeometry(264, 32, 178, 24)

        self.kullanicipass = QLabel("Kullanıcı Parolanız :", self)
        self.kullanicipass.move(40, 80)
        self.kullanicipass.setFont(label)
        self.kullanicipass_girdi = QLineEdit(self)
        self.kullanicipass_girdi.setGeometry(264, 82, 178, 24)

        self.kullaniciemail = QLabel("Kullanıcı Email :", self)
        self.kullaniciemail.move(40, 130)
        self.kullaniciemail.setFont(label)
        self.kullaniciemail_girdi = QLineEdit(self)
        self.kullaniciemail_girdi.setGeometry(264, 132, 178, 24)

        self.tarih = QLabel("Kullanıcı Kayıt Tarihi :", self)
        self.tarih.setFont(label)
        self.tarih.move(40, 180)
        self.gun = QComboBox(self)
        self.gun.setFont(label_girdi)
        self.gun.move(250, 180)
        for p in range(1, 32):
            self.ş = str(p)
            self.gun.addItems([self.ş])
        ay = ["Ay", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım",
              "Aralık"]
        self.ay = QComboBox(self)
        self.ay.addItems(ay)
        self.ay.setFont(label_girdi)
        self.ay.move(305, 180)
        self.yil = QComboBox(self)
        self.yil.setFont(label_girdi)
        self.yil.move(400, 180)
        for i in range(2020, 2030):
            self.h = str(i)
            self.yil.addItems([self.h])

        self.hangiunii = QLabel("Hangi Üniversite :", self)
        self.hangiunii.setFont(label)
        self.hangiunii.move(40, 240)
        self.hangiuni = QListWidget(self)
        self.hangiuni.setGeometry(220, 250, 400, 150)
        self.hangiuni.setFont(label_girdi)

        self.bolum_label = QLabel("Bölüm Seçiniz :", self)
        self.bolum_label.setFont(label)
        self.bolum_label.move(40, 450)
        self.blm_girdi = QLineEdit(self)
        self.blm_girdi.setGeometry(190, 455, 178, 24)
        self.blm_girdi.setFont(label_girdi)
        self.kayitet = QPushButton("Ekle", self)
        self.kayitet.setGeometry(200, 500, 150, 40)
        self.kayitet.setFont(label)

        self.list = QListWidget(self)
        self.list.setFont(label_girdi)
        self.list.setGeometry(400, 450, 400, 150)

        self.kayitol = QPushButton("Kayıt Ol", self)
        self.kayitol.setFont(label)
        self.kayitol.setGeometry(310, 630, 250, 90)

    def sorgula(self):
        etiket.execute("Select * from uniler")
        for i in etiket.fetchall():
            self.hangiuni.addItem(i[0])
        baglanti.commit()

    def sorgula2(self):
        etiket.execute("Select * from bölümler")
        for i in etiket.fetchall():
            self.list.addItem(i[0])
        baglanti.commit()

    def eklemeyap(self):
        self.gir = self.blm_girdi.text()
        etiket.execute('Insert Into bölümler VALUES (?)', (self.gir,))
        baglanti.commit()

    def fullkayit(self):
        self.kullaniciadii = self.kullaniciadi_girdi.text()
        self.kullanicipasw = self.kullanicipass_girdi.text()
        self.kullaniciemaill = self.kullaniciemail_girdi.text()
        self.day = self.gun.currentText()
        self.month = self.ay.currentText()
        self.year = self.yil.currentText()
        self.hangiunide = self.hangiuni.currentItem()
        self.bolumsec = self.list.currentItem()

        etiket.execute('Insert Into uyeler VALUES (?,?,?,?,?,?,?,?)',
                       (self.kullaniciadii, self.kullanicipasw, self.kullaniciemaill, self.day, self.month, self.year,
                        self.hangiunide.text(), self.bolumsec.text()))
        baglanti.commit()

    def __init__(self):
        super().__init__()
        self.setGeometry(400, 150, 1000, 800)
        self.uye_ekle()
        self.sorgula()
        self.sorgula2()
        self.kayitet.clicked.connect(self.eklemeyap)
        self.kayitol.clicked.connect(self.fullkayit)
        self.show()


class uye_listele(QWidget):
    def aramalar(self):
        self.isimden_ara = QLineEdit(self)
        self.isimden_ara.setPlaceholderText("İsimden,Soyisimden Arama...")
        self.isimden_ara.setGeometry(600, 100, 240, 30)
        self.isimden_ara.setFont(label_girdi)

        self.mailden_ara = QLineEdit(self)
        self.mailden_ara.setPlaceholderText("Mailden Arama...")
        self.mailden_ara.setGeometry(600, 150, 240, 30)
        self.mailden_ara.setFont(label_girdi)

        self.unidenarama = QLineEdit(self)
        self.unidenarama.setPlaceholderText("Universite İsminden Arama...")
        self.unidenarama.setGeometry(600, 200, 240, 30)
        self.unidenarama.setFont(label_girdi)

        self.bolumdenarama = QLineEdit(self)
        self.bolumdenarama.setPlaceholderText("Bölümüzden Arama...")
        self.bolumdenarama.setGeometry(600, 250, 240, 30)
        self.bolumdenarama.setFont(label_girdi)

        self.aramayap = QPushButton("Arama Yap", self)
        self.aramayap.setGeometry(620, 320, 200, 50)
        self.aramayap.setFont(label)

        self.sonuc = QLabel("Arama Sonuçları :", self)
        self.sonuc.setFont(label)
        self.sonuc.move(530, 420)

        self.aramasonuc = QListWidget(self)
        self.aramasonuc.setGeometry(530, 450, 400, 200)
        self.aramasonuc.setFont(label_combo)

        self.uyeler_label = QLabel("ÜYELER :", self)
        self.uyeler_label.setFont(label)
        self.uyeler_label.move(60, 70)

        self.uyeler = QListWidget(self)
        self.uyeler.setFont(label)
        self.uyeler.setGeometry(60, 100, 400, 600)

        self.silmeislemi = QPushButton("Üyeyi Sil",self)
        self.silmeislemi.setFont(label)
        self.silmeislemi.setGeometry(630,685,180,60)

    def ara(self):
        etiket.execute("Select * from uyeler")
        for i in etiket.fetchall():
            if i[0] == self.isimden_ara.text():
                self.aramasonuc.addItem(i[0])
            elif i[2] == self.mailden_ara.text():
                self.aramasonuc.addItem(i[0])
            elif i[6] == self.unidenarama.text():
                self.aramasonuc.addItem(i[0])
            elif i[7] == self.bolumdenarama.text():
                self.aramasonuc.addItem(i[0])
        baglanti.commit()

    def kompleekle(self):
        etiket.execute("Select * from uyeler")
        for i in etiket.fetchall():
            self.uyeler.addItem(i[0] + " - " + i[6] + " - " + i[7])

    def delete(self):
        cevap = QMessageBox.question(kitap_listele(), "Kayıt Sil", "Kitabı silmek istediğinize eminmisiniz?", \
                                     QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.Yes:
            self.secili = self.aramasonuc.selectedItems()
            self.silinecek = self.secili[0].text()
            etiket.execute("Delete FROM uyeler WHERE kullaniciId='%s'" % (self.silinecek,))
            baglanti.commit()

    def __init__(self):
        super().__init__()
        self.setGeometry(400, 150, 1000, 800)
        self.aramalar()
        self.silmeislemi.clicked.connect(self.delete)
        self.kompleekle()
        self.aramayap.clicked.connect(self.ara)
        self.show()


class emanet_ekle(QWidget):

    def metot1(self):
        self.kitaplistele_label = QLabel("Kitaplar :", self)
        self.kitaplistele_label.setFont(label)
        self.kitaplistele_label.move(50, 22)
        self.kitaplistele = QListWidget(self)
        self.kitaplistele.setFont(label)
        self.kitaplistele.setGeometry(50, 50, 300, 200)
        self.kitaplistele_line = QLineEdit(self)
        self.kitaplistele_line.setFont(label_girdi)
        self.kitaplistele_line.setGeometry(77, 270, 240, 30)
        self.kitaplistele_line.setPlaceholderText("Kitap İsmini Giriniz...")
        self.ara = QPushButton("Ara", self)
        self.ara.setFont(label)
        self.ara.setGeometry(100, 310, 200, 50)
        self.aramasonuc = QLabel("Arama Sonuçları :", self)
        self.aramasonuc.setFont(label)
        self.aramasonuc.move(50, 380)
        self.aramasonuc_widget = QListWidget(self)
        self.aramasonuc_widget.setFont(label)
        self.aramasonuc_widget.setGeometry(50, 410, 300, 150)

        self.uyeler_label = QLabel("Üyeler :", self)
        self.uyeler_label.setFont(label)
        self.uyeler_label.move(420, 22)
        self.uyelistele = QListWidget(self)
        self.uyelistele.setFont(label)
        self.uyelistele.setGeometry(420, 50, 300, 200)
        self.uyelistele_line = QLineEdit(self)
        self.uyelistele_line.setFont(label_girdi)
        self.uyelistele_line.setGeometry(447, 270, 240, 30)
        self.uyelistele_line.setPlaceholderText("Üye İsmini Giriniz...")
        self.ara2 = QPushButton("Ara", self)
        self.ara2.setFont(label)
        self.ara2.setGeometry(470, 310, 200, 50)
        self.ara2_sonuc = QLabel("Arama Sonuçları :", self)
        self.ara2_sonuc.setFont(label)
        self.ara2_sonuc.move(420, 380)
        self.ara2sonuc_widget = QListWidget(self)
        self.ara2sonuc_widget.setFont(label)
        self.ara2sonuc_widget.setGeometry(420, 410, 300, 150)

        self.emanetlereekle = QPushButton("Emanetlere Ekle", self)
        self.emanetlereekle.setFont(label)
        self.emanetlereekle.setGeometry(120, 580, 500, 60)

    def kitaplar(self):

        etiket.execute("Select * from kitaplar")
        for i in etiket.fetchall():
            self.kitaplistele.addItem(i[0])

    def uyeler(self):
        etiket.execute("Select * from uyeler")
        for i in etiket.fetchall():
            self.uyelistele.addItem(i[0])

    def sorgula(self):
        self.kitaplistele_linee = self.kitaplistele_line.text()
        etiket.execute("Select * from kitaplar")
        for i in etiket.fetchall():
            if self.kitaplistele_linee == i[0]:
                self.aramasonuc_widget.addItem(i[0])

    def sorgula2(self):
        self.uyelistele_linee = self.uyelistele_line.text()
        etiket.execute("Select * from uyeler")
        for i in etiket.fetchall():
            if self.uyelistele_linee == i[0]:
                self.ara2sonuc_widget.addItem(i[0])

    def emanetlerr(self, item):
        self.bir = self.aramasonuc_widget.currentItem()
        self.iki = self.ara2sonuc_widget.currentItem()
        etiket.execute('Insert Into emanetler Values(?,?)',
                       (self.bir.text(), self.iki.text()))
        baglanti.commit()
        sayac = True

    def kitap_sorgu_emanet(self):
        secilecek = self.aramasonuc_widget.selectedItems()
        sec = secilecek[0].text()
        fetch = etiket.execute("Select kitap_adi FROM emanetler WHERE kitap_adi = '%s'" % (sec))
        for i in fetch.fetchall():
            if sec == i[0]:
                QMessageBox.information(self, "Bilgilendirme", "Bu Kitap Şuanda Başkasında Emanet Verilemez !")
                self.close()
                baglanti.commit()

    def uye_sorgu_emanet(self):
        secilecek = self.ara2sonuc_widget.selectedItems()
        sec = secilecek[0].text()
        fetch = etiket.execute("Select kim_aldi FROM emanetler WHERE kim_aldi = '%s'" % sec)
        for i in fetch.fetchall():
            if sec == i[0]:
                QMessageBox.information(self, "Bilgilendirme", i[0] + " isimli üyede zaten bir adet kitap mevcut !")
                baglanti.commit()
                self.close()

    def __init__(self):
        super().__init__()
        self.setGeometry(490, 150, 800, 680)
        self.metot1()
        self.kitaplar()
        self.uyeler()
        self.ara.clicked.connect(self.sorgula)
        self.ara2.clicked.connect(self.sorgula2)
        self.aramasonuc_widget.itemClicked.connect(self.kitap_sorgu_emanet)
        self.ara2sonuc_widget.itemClicked.connect(self.uye_sorgu_emanet)
        self.emanetlereekle.clicked.connect(self.emanetlerr)
        self.show()


class emanet_listele(QWidget):

    def ekle(self):
        labelsorgu = QFont("Centruy Gothic", 12)
        labelline = QFont("Centruy Gothic", 9)
        self.labell = QLabel("Emanet Listesi:", self)
        self.labell.setFont(label)
        self.labell.setGeometry(140, 80, 140, 40)
        self.bir = QListWidget(self)
        self.bir.setGeometry(140, 120, 500, 300)
        self.bir.setFont(label_girdi)
        self.label_ks = QLabel("Silmek istediğiniz kitabın ismi :", self)
        self.label_ks.setFont(labelsorgu)
        self.label_ks.setGeometry(140, 450, 500, 40)
        self.kitapdan_sorgu = QLineEdit(self)
        self.kitapdan_sorgu.setGeometry(380, 455, 220, 30)
        self.kitapdan_sorgu.setFont(labelline)
        self.sil = QPushButton("Emaneti Sil", self)
        self.sil.setFont(label)
        self.sil.setGeometry(310, 510, 170, 60)

        etiket.execute("Select * from emanetler")
        for i in etiket.fetchall():
            self.bir.addItem(i[0] + " - " + i[1])

    def delete(self):
        cevap = QMessageBox.question(emanet_listele(), "Kayıt Sil", "Emaneti silmek istediğinize eminmisiniz?", \
                                     QMessageBox.Yes | QMessageBox.No)
        fet = etiket.execute("Select * FROM emanetler")
        self.line = self.kitapdan_sorgu.text()
        if cevap == QMessageBox.Yes:
            for i in fet.fetchall():
                if i[0] == self.line:
                    etiket.execute("Delete From emanetler Where kitap_adi='%s'" %(self.line))
                    baglanti.commit()
        elif cevap == QMessageBox.No:
            self.close()

    def __init__(self):
        super().__init__()
        self.ekle()
        self.sil.clicked.connect(self.delete)
        self.setGeometry(490, 150, 800, 680)
        self.show()


uygulama = QApplication(sys.argv)
pencere = giris_pencere()
sys.exit(uygulama.exec_())
