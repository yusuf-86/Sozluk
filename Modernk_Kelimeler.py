meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "AFK":"Bilgisayar başında olmamak",
            "NT":"İyiydi bidahakine",
            "EZ":"Kolaydı",
            }
kelime = input("Anlamını merak ettiğin kelimeyi giriniz(Büyük harfle yaz.)")
if kelime in meme_dict.keys():
    print(meme_dict[kelime])
else:
    print("Böyle bir kelime yok tekrar deneyin.")
