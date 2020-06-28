'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
'''


import random                                       # random programı için kullanmamız gerekiyor.
a = int(input('başlangıç: '))                         # kullanıcıdan başlangıç sayısı istendi
b = int(input('son : '))                         # kullanıcıdan son sayı istendi
sayi = random.randint(a,b)                       # iki sayı arasında random yapıldı

can = int(input('kaç hakkınız olsun: '))     # kullanıcıdan can sayısı istedik
hak = can                                   # can sayısı bozulmasın diye haka eşitledim

sayac = 0                                   # sayac ile puanlama yapılır
while hak > 0:                                 # hak sayısı 0a gelene kadar döndürdük
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print(f'TEBRİKLER {sayac}. DEFADA BİLDİNİZ. TOPLAM PUANINIZ: {100 - (100/can) * (sayac - 1)} ')
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')

    if hak == 0:
        print(f'HAKKINIZ BİTTİ.TUTULAN SAYI : {sayi}')





















