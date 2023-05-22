import json

film_adi = input("Lütfen bir film adı girin: ")

dosya_adi = "film_listesi.json"  # Kaydedilecek dosyanın adı

try:
    with open(dosya_adi, "r") as dosya:
        film_listesi = json.load(dosya)
except FileNotFoundError:
    film_listesi = []

film_listesi.append(film_adi)

with open(dosya_adi, "w") as dosya:
    json.dump(film_listesi, dosya)

print("Film adı başarıyla kaydedildi.")