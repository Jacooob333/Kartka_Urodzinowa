imie_nad = input("Proszę podaj swoje imię: ")
data_ur = int(input("Proszę podaj rok urodzenia odbiorcy kartki urodzinowej: "))
sper_wiad = input("Tutaj wpisz własną spersonalizowaną wiadomość dla odbiorcy kartki urodzinowej: ")
imie_odb = input("Proszę podaj imię odbiorcy kartki urodzinowej: ")

wiek = 2024 - (data_ur)

print(20*"-")

print (f"{imie_odb}, wszystkiego najlepszego z okazji {wiek} urodzin!\n\n{sper_wiad}\n\n{imie_nad}")