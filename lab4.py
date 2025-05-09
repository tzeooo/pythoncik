def calcul_greutate_ideala():
    print("\n--- Calculator Greutate Ideala ---")


     
    while True:
        ш = input("Introduceti inaltimea (cm): ")
        try:
            inaltime = int(ш)
        except ValueError:
            print("Eroare: Introduceti o valoare numerica valida pentru inaltime.")
            continue
    
        if inaltime < 150:
            print("Eroare: Înălțimea este prea mică! Trebuie să fie cel puțin 150 cm.")
            continue  

        if inaltime > 220:
            print("Eroare: Înălțimea este prea mare! Nu poate depăși 220 cm.")
            continue  
    
        print("Înălțimea este validă!")
        break

    while True:
        try:
            greutate_actuala = float(input("Introduceti greutatea actuala (kg): "))
            if 45 <= greutate_actuala <= 300:
                break
            else:
                print("Eroare: Greutatea trebuie sa fie intre 45 si 300 kg.")
        except ValueError:
            print("Eroare: Introduceti o valoare numerica valida pentru greutate.")

    while True:
        try:
            varsta = int(input("Introduceti varsta (ani): "))
            if 20 <= varsta <= 120:
                break
            else:
                print("Eroare: Varsta trebuie sa fie intre 20 si 120 de ani.")
        except ValueError:
            print("Eroare: Introduceti o valoare numerica valida pentru varsta.")

    while True:
        sex = input("Introduceti sexul (M sau F): ").strip().upper()
        if sex in ['M', 'F']:
            break
        else:
            print("Eroare: Sexul trebuie sa fie 'M' sau 'F'.")

    if sex == 'M':
        greutate_ideala = inaltime - 100 - ((inaltime - 150) / 4 + (varsta - 20) / 4)
    else:
        greutate_ideala = inaltime - 100 - ((inaltime - 150) / 2.5 + (varsta - 20) / 6)

    print(f"\nGreutatea ideala este: {greutate_ideala:.2f} kg")

    diferenta = greutate_actuala - greutate_ideala
    if diferenta > 0:
        print("Recomandare: Ar fi bine sa slabiti putin.")
    elif diferenta < 0:
        print("Recomandare: Ar fi bine sa adaugati in greutate.")
    else:
        print("Felicitari! Aveti greutatea ideala.")


def calcul_varsta_pisica():
    print("\n--- Convertor Varsta Pisica ---")
    raspuns = input("Pisica are mai putin de un an? (Da/Nu): ").strip().lower()

    if raspuns in ["da", "yes"]:
        cat_age_dict = {
            1: "6 luni", 2: "10 luni", 3: "2 ani", 4: "5 ani", 5: "8 ani",
            6: "14 ani", 7: "15 ani", 8: "16 ani", 9: "16 ani", 10: "17 ani", 11: "17 ani"
        }
        while True:
            try:
                luni = int(input("Introduceti varsta pisicii in luni (1-11): "))
                if luni in cat_age_dict:
                    print(f"Varsta in ani umani: {cat_age_dict[luni]}")
                    break
                else:
                    print("Introduceti o valoare intre 1 si 11.")
            except ValueError:
                print("Introduceti un numar intreg.")
    elif raspuns in ["nu", "no"]:
        while True:
            try:
                ani = int(input("Introduceti varsta pisicii in ani (1-35): "))
                if ani < 1 or ani >= 35:
                    print("Introduceti o valoare intre 1 si 34.")
                    continue

                if ani == 1:
                    umani = 18
                elif ani == 2:
                    umani = 25
                elif 3 <= ani <= 15:
                    umani = 25 + (ani - 2) * 4
                else:
                    umani = 25 + 13 * 4 + (ani - 15) * 3

                print(f"Varsta in ani umani: {umani} ani")
                break
            except ValueError:
                print("Introduceti un numar intreg.")
    else:
        print("Raspuns invalid. Rulati programul din nou si introduceti 'Da' sau 'Nu'.")

calcul_greutate_ideala()
calcul_varsta_pisica()
