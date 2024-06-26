def hesap_makinesi():
    print("hesap makinesi")
    print("Yapmak İstediğiniz işlemi seçin:")
print("1-toplama")
print("2-çikarma")
print("3-carpma")
print("4-bölme")
print("Çikmak için 'q' tusuna basin")

while True:
    secim= input("Secimiz (1/2/3/4 veya q): ")
    if secim=='q':
        print("hesap makinesinden çikiliyor")
        break
    if secim in ['1','2','3','4']:
             try:
                sayi1= float(input("Birinci sayiyi girin:"))
                sayi2=float(input("ikinci sayiyi girin"))
             except ValueError:
                  print("Lütfen geçerli bir sayi girin")
                  continue
             if secim=='1':
                  sonuc1 = sayi1 +sayi2
                  print("sonuç:",sonuc1)
                  if secim=='2':
                    sonuc2=sayi1-sayi2
print("sonuç:",sonuc2)
if secim=='4':
 if sayi2 == 0:
     print("HATA: bir sayiyi 0 a bölemezsiniz")
else:
     sonuc4=sayi1/sayi2
     print("sonuc:",sonuc4)
     if print("gecersiz giris lutfen 1,2,3,4 veya 'q' tuşuna basin"):
         
         hesap_makinesi()
