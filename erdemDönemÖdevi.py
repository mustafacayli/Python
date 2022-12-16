tercih=1

x=0
list=[]
while x<400:
    
    list.append("-")
    x+=1

def xYazma(a): 
    list[a]="X"               
            
    



def yazdir():
    
        i=0 
        while i<400:
            print(list[i],end="")
            i+=1
            if(i%20==0):
                print("\n")
            


            

def bilet_func1(katagori):

    if katagori==1:
        
        sira=0
        koltuk=5
        adet=int(input("Bilet adedi (1-10)"))
        sayi=0
        list1=[]
    

        if(adet>10):
            print("hata")
        while sayi!=adet:


            if koltuk==15:
                sira+=1
                koltuk=5
        
            list1.append(str(sira+1)+"-"+str(koltuk+1))
        
            
            c=sira*10*2+koltuk
            xYazma(c)
        
            koltuk+=1
            sayi+=1

#****************************************************************************************************

    elif katagori==3:
        
        sira=9
        koltuk=5
        adet=int(input("Bilet adedi (1-10)"))
        sayi=0
        list1=[]
    

        if(adet>10):
            print("hata")
        while sayi!=adet:

            list1.append(str(sira+1)+"-"+str(koltuk+1))

            if koltuk%15==0:
                sira+=1
                koltuk=5
        
        
            
            c=sira*10*2+koltuk
            xYazma(c)
            
    
        
            koltuk+=1
            sayi+=1        
            
        
            
    print(koltuk)
    print(sira)
    if(sira==10 and koltuk==16):
        print("yer kalmadi")
    print(list1)
    yazdir()
    
    

def bilet_func2(katagori):
    
    if katagori==2:
        sira=0
        koltuk=4
        adet=int(input("Bilet adedi (1-10)"))
        sayi=0
        list1=[]
    
        if(adet>10):
            print("hata")
        while sayi!=adet:
            on=1
        

            if koltuk==-1:
                koltuk=15

            if koltuk==20:
                koltuk=4
                sira+=1


            if koltuk>10:
                on=2
            if koltuk<10:
                on=1

        

            list1.append(str(sira+1)+"-"+str(koltuk+1))

        
            
            c=sira*10*2+koltuk
            xYazma(c)
            
       

            if on==1:
                koltuk-=1
            else:
                koltuk+=1
            
            sayi+=1

            
        print(koltuk)
        print(sira)
        if(sira==10 and koltuk==21):
            print("yer kalmadi")
        print(list1)

#****************************************************************************************************************
    if katagori==4:
        sira=9
        koltuk=4
        adet=int(input("Bilet adedi (1-10)"))
        sayi=0
        list1=[]
    
        if(adet>10):
            print("hata")
        while sayi!=adet:
            on=1
        

            if koltuk==-1:
                koltuk=15

            if koltuk==20:
                koltuk=4
                sira+=1


            if koltuk>10:
                on=2
            if koltuk<10:
                on=1

        

            list1.append(str(sira+1)+"-"+str(koltuk+1))

        
            
            c=sira*10*2+koltuk
            xYazma(c)
            
       

            if on==1:
                koltuk-=1
            else:
                koltuk+=1
            
            sayi+=1

            
        print(koltuk)
        print(sira)
        if(sira==10 and koltuk==21):
            print("yer kalmadi")
        print(list1)
    
while(tercih>0):
    print("\n******************\n***  ANA MENU  ***\n******************")
    print("1.Rezervasyon\n2.Salon Yazdir\n3.Yeni  Etkinlik\n0.Cikis\n")

    islem=int(input("Yapmak istediginiz islemi seciniz: "))
    
    if(islem==0):
        break
    
    elif(islem==1):
        katagori=int(input("Katagori (1-4) ? "))
        if(katagori==1):
            bilet_func1(katagori)
        elif(katagori==2):
            bilet_func2(katagori)
        elif(katagori==3):
            bilet_func1(katagori)
        elif(katagori==4):
            bilet_func2(katagori)

    elif(islem==2):
        yazdir()
    elif(islem==3):
        pass


    


