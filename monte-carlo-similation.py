######
import numpy as np
import random
import sys
sys.setrecursionlimit(999999999)

sutun=int(input ("matris sutun sayısını girin :"))
satir=int(input ("matris satır sayısını girin :"))
A = np.zeros(shape=(satir,sutun))   
def matris_create(satir,sutun):
    for i in range(satir):
        print(str(i) + " nci satırı giriniz")
        for j in range(sutun):
            A[i][j]=int(input (str(i)+" "+str(j)+". hücreyi gir : "))
    #print (A)

matris_create(satir,sutun)
B = [0]
C = np.zeros(shape=(satir,sutun))
def kumulatif_olustur(satir,sutun):
   
    for a in range(satir-1):
        B.append(0)

    for i in range(satir):
        toplam=0
        satir_toplami=0
        for j in range(sutun):
            toplam=toplam + A[i][j]
        satir_toplami=toplam
        #print(str(i) + " . satır toplamı " + str(satir_toplami))
        B[i] = (satir_toplami)
    kumulatif=0.0
    btoplam=0.0
    b_deger=0.0
    for b in range(satir):
        kumulatif=0.0
        toplam=0.0
        btoplam=0.0  
        b_deger=B[b]
       
        for c in range(sutun):
            a_deger=int(A[b][c])
            btoplam=btoplam + A[b][c]       
            #print("a nın deperi "+str(a_deger)+ " b nin değeri "+ str(b_deger))
            kumulatif = btoplam / float(b_deger)
            
            C[b][c]= round(kumulatif, 1)
   

kumulatif_olustur(satir,sutun)

#print("B matrisi\n " + str(B))
print("C matrisi\n " + str(C))
#### yukardaki işlemler bir A matrisinin girilmesi ve kümülatif olarak olasılık matrisinin C matrisinin oluşturulması
D = np.zeros(shape=(satir,sutun))
satir_tpl=0
def D_sifirla():
 
    for i in range(satir):
        for j in range(sutun):
            D[i][j]=0



def D_son_matris(satir,fark,rastgele):
    
    for i in range(sutun):
        if abs(C[satir][i]-rastgele)==fark:
            D[satir][i]=D[satir][i]+1
    
def fark_hesapla(satir,sutun):
    for i in range(satir):
        satir_tpl=int(B[i])
        print(str(satir_tpl) + "---------------------")
        for j in range(satir_tpl):
            rastgele=round(random.uniform(0, 1), 1)
            #random tuttuktan sonra fark alma işlemi
            fark=abs(C[i][0]-rastgele)
            sayac=0
            for m in range(sutun):
                olasilik=C[i][m]
                if abs(olasilik-rastgele)<fark:
                    fark=abs(olasilik-rastgele)
            D_son_matris(i,fark,rastgele)
            print("tutulan random sayı : " + str(rastgele)+ " fark " + str(fark))
    son_matris_kontrol()

def son_matris_kontrol():
    A_satir_toplamlari=(np.sum(A, axis=1))
    A_sutun_toplamlari=(np.sum(A, axis=0))
    satir_toplamlari=(np.sum(D, axis=1))
    sutun_toplamlari=(np.sum(D, axis=0))  
    for i in range(satir):
        for j in range (sutun):
            if i==j:
                if satir_toplamlari[i]==sutun_toplamlari[j]:
                    print("problem yok çünkü D matrisinin satır sutun sayısı toplamları aynı")
                elif A_satir_toplamlari[i]!=satir_toplamlari[i]:
                    print("problem yok çünkü aynı olasılıklar olduğu için o satır sutun atlatıldı")
                else :
                    D_sifirla()
                    print("D matrisi\n " + str(D))
                    print("sıkıntı oldu başa")
                    fark_hesapla(satir,sutun)


print("--------------------------------------------------------")
print("A matrisi\n " + str(A))
print("--------------------------------------------------------")
fark_hesapla(satir,sutun)
print("--------------------------------------------------------")
print("D matrisi\n " + str(D))
#D_son_matris(satir,sutun)






