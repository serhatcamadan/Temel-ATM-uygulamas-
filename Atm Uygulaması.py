print("""
****************************

ATM'mize Hoşgeldiniz

---Lütfen işlem seçiniz---
1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

****************************
""")

bakiye= 2000
while True:
 islem = int(input("Yapmak istediğiniz işlemi seçiniz:"))
 if islem==0:
    print("Güle güle...")
    break
 elif islem==1:
    print("Bakiyeniz {} TL dir.".format(bakiye))
 elif islem==2:
    para=int(input("Yatırmak istediğiniz tutarı giriniz:"))
    bakiye +=para
    print("Yeni hesap bakiyeniz {} TL dir.".format(bakiye))
 elif islem==3:
    para=int(input("Çekmek istediğiniz tutarı giriniz:"))
    if bakiye < para:
        print("Bakiye yetersiz.")
        continue

    bakiye -= para
    print("Kalan bakiyeniz {} TL dir".format(bakiye))
 else:
    print("Geçersiz işlem....")