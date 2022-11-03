KulMustafa={
    'ad':'Mustafa',
    'soyad':'Cayli',
    'hesapNo':'7566823982752261',
    'bakiye':50000
}
KulAhmet={
    'ad':'Ahmet',
    'soyad':'Kurek',
    'hesapNo':'75668258309229662',
    'bakiye':13500
}



def paraCek(hesap):
    print(f"Hello dear{hesap['ad']} your current balance {hesap['bakiye']}")
    miktar=int(input("Enter how much money you want to withdraw"))

    if(hesap['bakiye']<miktar):
        print('Insufficient balance')
    else:
        hesap['bakiye']-=miktar
        print(f"Your proccess succesfully, your new balance {hesap['bakiye']}")



def paraYuk(hesap):
    print(f"Hello dear{hesap['ad']} your current balance {hesap['bakiye']}")
    
    miktar=int(input("Enter the emount you want to deposit"))

    hesap['bakiye']+=miktar
    
    print(f"Your proccesssuccesfully completed, your new balance {hesap['bakiye']}")

def bakiye(hesap):
    print(f"your current balance{hesap['bakiye']}")






islem=int(input("Which account you want to log in"+"\n"+"1)KulAhmet"+"\n"+"2)KulMustafa"+"\n"))
hak=3
while(hak>0):

 if(islem==1):
    kartNo=input("Enter the account No")

    if(kartNo==KulAhmet['hesapNo']):
        print(f"Hello {KulAhmet['ad']}")
        yapilacak=int(input("Choos what do you want to do"+"\n"+"1)Whitdraw Money"+"\n"+"2)Load Money"+"\n"+"3)Balance Inquiry"))
        
        if(yapilacak==1):
            paraCek(KulAhmet)
        elif(yapilacak==2):
            paraYuk(KulAhmet)
        elif(yapilacak==3):
            bakiye(KulAhmet)


    else:
        hak=hak-1
        print("Un acceptable account")

  
 elif(islem==2):
    kartNo=input("Enter the account No")

    if(kartNo==KulMustafa['hesapNo']):

        print(f"Hello {KulMustafa['ad']}")
        yapilacak=int(input("Choos what do you want to do"+"\n"+"1)Whitdraw Money"+"\n"+"2)Load Money"+"\n"+"3)Balance Inquiry"))
        
        if(yapilacak==1):
            paraCek(KulMustafa)
        elif(yapilacak==2):
            paraYuk(KulMustafa)
        elif(yapilacak==3):
            bakiye(KulMustafa)



    else:
        hak=hak-1
        print("Un acceptable account")

 elif((islem!=1) and (islem!=2)):
    print("You need to choose acceptable number")
    continue


 if(hak==0):
    print("You have no rights,your account has been blocked"+"\n"+"You have to go to the bank to open it")

    

















