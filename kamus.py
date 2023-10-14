meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "OTW" : "Sedang dalam perjalanan",
            "GTG" : "Harus segera pergi",
            "TBH" : "Mengatakan dengan jujur",
            }
for i in range (5):
    word = input("Masukan kata :")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("kata tidak ditemukan")
    
