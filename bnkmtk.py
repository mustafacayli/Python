bakiye=5000
hak=3

kartNo='55437592872448677'
sifre='1234'


girdiNo=input('Kart numaranizi giriniz:')
girdiSif=input('Kartinizin sifresini giriniz:')
while hak>0:
    
 if(girdiNo==kartNo)and(sifre==girdiSif):
    print('Hos geldiniz')

    print('Islemler'+'\n'+'1) Bakiye Sorgulama'+'\n'+'2) Para Yatirma'+'\n'+'3) Para Cekme'+'\n'+'4) Havale Yapma')
    islem=int(input('Yapmak istediginiz islemi seciniz:'))

    if(islem==1):
        print('Mevcut bakiyeniz:'+str(bakiye))


    elif(islem==2):
        print('Mevcut bakiyeniz:'+str(bakiye))
        bakiye+=int(input('Yatirmak istediginiz miktari giriniz'))
        print('Mevcut bakiyeniz:'+str(bakiye))


    elif(islem==3):
        print('Mevcut bakiyeniz:'+str(bakiye))
        cekilecek=int(input('Cekmek istediginiz para tutarini giriniz:'))
        if(bakiye<cekilecek):
            print('Yetersiz bakiye')
        else:
            bakiye-=cekilecek
            print('Mevcut bakiyeniz:'+str(bakiye))


    elif(islem==4):
        print('Mevcut bakiyeniz:'+str(bakiye))
        havale=int(input('Havaleyapmak istediginiz para tutarini giriniz:'))
        if(bakiye<havale):
            print('Yetersiz bakiye')
        else:
            bakiye-=havale
            print('Mevcut bakiyeniz:'+str(bakiye))
    



 else:
    hak-=1
    print('Hatali bilgi'+'\n'+'kalan hak:'+str(hak))
    

