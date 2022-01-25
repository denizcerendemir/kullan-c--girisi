print("************* Kullanıcı Girişi *************")

sys_kullanıcı_Adı ="denizcerendemir"
sys_parola ="Mka1881"
giris_Hakkı = 3

while True :
    kullanıcı_Adı= input("Kullanıcı Adı : ")
    parola= input("Parola :")

    if (kullanıcı_Adı == sys_kullanıcı_Adı and parola != sys_parola) :
        print("Parola Hatalı")
        giris_Hakkı -= 1
        print("kalan giriş hakkınız",giris_Hakkı)
    elif (kullanıcı_Adı != sys_kullanıcı_Adı and parola == sys_parola) :
        print("Kullanıcı Adı Hatalı")
        giris_Hakkı -= 1
        print("kalan giriş hakkınız", giris_Hakkı)
    elif kullanıcı_Adı != sys_kullanıcı_Adı and parola != sys_parola :
        print("Kullanıcı Adı Ve Parola Hatalı")
        giris_Hakkı -= 1
        print("kalan giriş hakkınız", giris_Hakkı)

    else:
        print("Sisteme başarıyla giriş yaptınız...")
        break

    if (giris_Hakkı == 0) :

        print("3 kez yanlış bilgi girildi...")
        break