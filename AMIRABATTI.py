#MUHAMMET ENES AY 19010011077
import random
while True:
    oyun_modu = int(input("***AMİRAL BATTI OYUNUNA HOSGELDİNİZ***\nOyun modunuz seciniz;\nACIK MOD(1) GİZLİ MOD (2):"))
    boyut = int(input("Lütfen oyun alanı boyutunu seçiniz (kare matris formatına donusturulecektır) : "))
    if oyun_modu == 1:
        alan = []
        for i in range(boyut):
            alan.append(["?"] * boyut)
        def alanyap(alan):
            for i in alan:
                print(" ".join(i))
        def satir(alan):  #rastgele satır olusturur
            return random.randint(0, len(alan[0]) - 1)
        def sutun(alan):  # rastgele sütun olusturur
            return random.randint(0, len(alan) - 1)
        yon2 = [random.randint(0, 1)]  # yön=1 dikey
        yon3 = [random.randint(0, 1)]  # yön=1 dikey
        yon4 = [random.randint(0, 1)]  # yön=1 dikey
        # 1LİK GEMİ
        x = satir(alan)
        y = sutun(alan)
        alan[x][y] = "1"
        # 2LİK GEMİ
        while True:
            x2 = satir(alan)
            y2 = sutun(alan)
            while x2 == x or y2 == y:
                x2 = satir(alan)
                y2 = sutun(alan)
            if yon2 == [1] and x2 + 2 <= boyut - 1 and x2 - 2 >= 1:  #oyun alanından taşmayı önler
                alan[x2][y2] = "2"
                alan[x2 + 1][y2] = "2"
                break
            elif yon2 == [0] and y2 + 2 <= boyut - 1 and y2 - 2 >= 1:
                alan[x2][y2] = "2"
                alan[x2][y2 + 1] = "2"
                break
        # 3LUK gemi
        while True:
            x3 = satir(alan)
            y3 = sutun(alan)
            while x2 == x3 or y2 == y3 or x == x3 or y == y3:  #gemilerin ust uste gelmesini engeller
                x3 = satir(alan)
                y3 = sutun(alan)
            if yon3 == [1] and x3 + 3 <= boyut - 1 and x3 - 3 >= 1:
                alan[x3][y3] = "3"
                alan[x3 + 1][y3] = "3"
                alan[x3 + 2][y3] = "3"
                break
            elif yon3 == [0] and y3 + 3 <= boyut - 1 and y3 - 3 >= 1:
                alan[x3][y3] = "3"
                alan[x3][y3 + 1] = "3"
                alan[x3][y3 + 2] = "3"
                break
        # 4LUK gemi
        while True:
            x4 = satir(alan)
            y4 = sutun(alan)
            while x3 == x4 or y3 == y4 or y2 == y4 or x2 == x4:
                x4 = satir(alan)
                y4 = satir(alan)
            if yon4 == [1] and x4 + 3 <= boyut - 1 and x4 - 3 >= 1:
                alan[x4][y4] = "4"
                alan[x4 + 1][y4] = "4"
                alan[x4 + 2][y4] = "4"
                alan[x4 + 3][y4] = "4"
                break
            elif yon4 == [0] and y4 + 3 <= boyut - 1 and y4 - 3 >= 1:
                alan[x4][y4] = "4"
                alan[x4][y4 + 1] = "4"
                alan[x4][y4 + 2] = "4"
                alan[x4][y4 + 3] = "4"
                break
        alanyap(alan)
        deneme = 0
        gemi1durum = 0
        gemi2durum = 0
        gemi3durum = 0
        gemi4durum = 0
        while deneme <= (boyut*boyut)/3 :
            satirgir = int(input("Satır tahmininizi giriniz(0-9) : "))
            sutungir = int(input("Sutun tahminizi giriniz(0-9) : "))
            while alan[satirgir][sutungir] == "X" or alan[satirgir][sutungir] == "*":
                print("Aynı konumu 2. kez giremezsiniz. Lütfen tekrar deneyin...")
                satirgir = int(input("Satır tahmininizi giriniz(0-9) : "))
                sutungir = int(input("Sutun tahminizi giriniz(0-9) : "))
            if alan[satirgir][sutungir] == "4":
                alan[satirgir][sutungir] = "X"
                deneme += 1
                gemi4durum += 1
                if gemi4durum == 4:
                    print("Tebrikler 4 numaralı gemiyi batırdınız!")
                else:
                    print("Tebrikler bir gemi vurdunuz!")
            elif alan[satirgir][sutungir] == "3":
                alan[satirgir][sutungir] = "X"
                deneme += 1
                gemi3durum += 1
                if gemi3durum == 3:
                    print("Tebrikler 3 numaralı gemiyi batırdınız!")
                else:
                    print("Tebrikler bir gemi vurdunuz!")
            elif alan[satirgir][sutungir] == "2":
                alan[satirgir][sutungir] = "X"
                deneme += 1
                gemi2durum += 1
                if gemi2durum == 2:
                    print("Tebrikler 2 numaralı gemiyi batırdınız!")
                else:
                    print("Tebrikler bir gemi vurdunuz!")
            elif alan[satirgir][sutungir] == "1":
                alan[satirgir][sutungir] = "X"
                deneme += 1
                gemi1durum += 1
                if gemi1durum == 1:
                    print("Tebrikler 1 numaralı gemiyi batırdınız!")
                else:
                    print("Tebrikler bir gemi vurdunuz!")
            else:
                alan[satirgir][sutungir] = "*"
                deneme += 1
                print("Maalesef isabet ettiremediniz!")
            if deneme == (boyut*boyut)/3 or gemi2durum == 2 and gemi3durum == 3 and gemi4durum == 4 and gemi1durum == 1:
                if (boyut*boyut)/3 != deneme:
                    print("TEBRİKLER OYUNU {} PUAN İLE KAZANDINIZ !!!: ".format(33 - deneme))
                    break
                else:
                    print("Atıs hakkınız bitti.Kaybettınız...")
                    break
            alanyap(alan)
    if oyun_modu == 2:
        alan = []
        sahtealan = []    #Sahte bir alan olusturuldu,orjınal alandakı degısıklıkler buraya işlenıyor
        for i in range(boyut):
            sahtealan.append(["?"] * boyut)
        def sahte(alan):
            for i in sahtealan:
                print(" ".join(i))
        for i in range(boyut):
            alan.append(["?"] * boyut)
        def alanyap(alan):
            for i in alan:
                print(" ".join(i))
        def satir(alan):
            return random.randint(0, len(alan[0]) - 1)
        def sutun(alan):  # rastgele satir olusturur
            return random.randint(0, len(alan) - 1)
        yon2 = [random.randint(0, 1)]  # yön=1 dikey
        yon3 = [random.randint(0, 1)]  # yön=1 dikey
        yon4 = [random.randint(0, 1)]  # yön=1 dikey
        # 1LİK GEMİ
        x = satir(alan)
        y = sutun(alan)
        alan[x][y] = "1"
        # 2LİK GEMİ
        while True:
            x2 = satir(alan)
            y2 = sutun(alan)
            while x2 == x or y2 == y:
                x2 = satir(alan)
                y2 = sutun(alan)
            if yon2 == [1] and x2 + 2 <= boyut - 1 and x2 - 2 >= 1:
                alan[x2][y2] = "2"
                alan[x2 + 1][y2] = "2"
                break
            elif yon2 == [0] and y2 + 2 <= boyut - 1 and y2 - 2 >= 1:
                alan[x2][y2] = "2"
                alan[x2][y2 + 1] = "2"
                break
        # 3LUK gemi
        while True:
            x3 = satir(alan)
            y3 = sutun(alan)
            while x2 == x3 or y2 == y3 or x == x3 or y == y3:
                x3 = satir(alan)
                y3 = sutun(alan)
            if yon3 == [1] and x3 + 3 <= boyut - 1 and x3 - 3 >= 1:
                alan[x3][y3] = "3"
                alan[x3 + 1][y3] = "3"
                alan[x3 + 2][y3] = "3"
                break
            elif yon3 == [0] and y3 + 3 <= boyut - 1 and y3 - 3 >= 1:
                alan[x3][y3] = "3"
                alan[x3][y3 + 1] = "3"
                alan[x3][y3 + 2] = "3"
                break
        # 4LUK gemi
        while True:
            x4 = satir(alan)
            y4 = sutun(alan)
            while x3 == x4 or y3 == y4 or y2 == y4 or x2 == x4:
                x4 = satir(alan)
                y4 = satir(alan)
            if yon4 == [1] and x4 + 3 <= boyut - 1 and x4 - 3 >= 1:
                alan[x4][y4] = "4"
                alan[x4 + 1][y4] = "4"
                alan[x4 + 2][y4] = "4"
                alan[x4 + 3][y4] = "4"
                break
            elif yon4 == [0] and y4 + 3 <= boyut - 1 and y4 - 3 >= 1:
                alan[x4][y4] = "4"
                alan[x4][y4 + 1] = "4"
                alan[x4][y4 + 2] = "4"
                alan[x4][y4 + 3] = "4"
                break
        sahte(sahtealan)
        deneme = 0
        gemi1durum = 0
        gemi2durum = 0
        gemi3durum = 0
        gemi4durum = 0
        while deneme <= (boyut*boyut)/3:
            satirgir = int(input("Satır tahmininizi giriniz(0-9) : "))
            sutungir = int(input("Sutun tahminizi giriniz(0-9) : "))
            while sahtealan[satirgir][sutungir] == "X" or sahtealan[satirgir][sutungir] == "*":
                print("Aynı konumu 2. kez giremezsiniz. Lütfen tekrar deneyin...")
                satirgir = int(input("Satır tahmininizi giriniz(0-9) : "))
                sutungir = int(input("Sutun tahminizi giriniz(0-9) : "))

            if alan[satirgir][sutungir] == "4":
                sahtealan[satirgir][sutungir] = "X"
                deneme += 1
                gemi4durum += 1
                if gemi4durum == 4:
                    print("Tebrikler 4 numaralı gemiyi batırdınız!")
                else:
                    print("Tebrikler bir gemi vurdunuz!")
            elif alan[satirgir][sutungir] == "3":
                sahtealan[satirgir][sutungir] = "X"
                deneme += 1
                gemi3durum += 1
                if gemi3durum == 3:
                    print("Tebrikler 3 numaralı gemiyi batırdınız!")
                else:
                    print("Tebrikler bir gemi vurdunuz!")
            elif alan[satirgir][sutungir] == "2":
                sahtealan[satirgir][sutungir] = "X"
                deneme += 1
                gemi2durum += 1
                if gemi2durum == 2:
                    print("Tebrikler 2 numaralı gemiyi batırdınız!")
                else:
                    print("Tebrikler bir gemi vurdunuz!")
            elif alan[satirgir][sutungir] == "1":
                sahtealan[satirgir][sutungir] = "X"
                deneme += 1
                gemi1durum += 1
                if gemi4durum == 1:
                    print("Tebrikler 1 numaralı gemiyi batırdınız!")
                else:
                    print("Tebrikler bir gemi vurdunuz!")
            else:
                sahtealan[satirgir][sutungir] = "*"
                deneme += 1
                print("Maalesef isabet ettiremediniz!")
            if deneme == (boyut*boyut)/3 or gemi2durum == 2 and gemi3durum == 3 and gemi4durum == 4 and gemi1durum == 1:
                if (boyut*boyut)/3 != deneme:
                    print("TEBRİKLER OYUNU {} PUAN İLE KAZANDINIZ !!!: ".format(((boyut*boyut)/3) - deneme))
                else:
                    print("Atıs hakkınız bitti.Kaybettınız...")
                    break
            sahte(sahtealan)
    secim=input("Cıkmak ıcın 'q' yeniden oynamak için 'p' : ")
    if secim=="q":
        break
    if secim=="p":
        continue