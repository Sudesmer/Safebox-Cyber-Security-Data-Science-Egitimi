def giris():

    username = input("isminizi girin: ")
    surname = input("soyisminizi girin: ")
    passw = input("şifrenizi girin: ")

    user_infos = open("kullanici_bilgileri.txt", "r")
    
    for a in user_infos:
        a = a.strip().split(",")
        username_1 = satir[0]
        surname_1 = satir[1]
        passw_1 = satir[2]
        if username_1 == username and surname_1 == surname and passw_1 == passw:
            print("Başarili bir şekilde giriş yapilmiştir.")
            user_infos.close()
            return
        else:
            user_infos.close()
            print("Giriş bilgileriniz hatali.")

giris()