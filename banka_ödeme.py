import os
import pandas as pd


dosya = []  # txt doslarınıın içeriklerini liste olarak alır
liste = []  # yeni değişkenler oluşturur
df_data = []  # Dataframe oluşturma için yeni liste oluşturur

# txt Dosyalarının olduğu klasörün içinde ki txt dosyalarının isimlerini bir listeye atar
def folder_transfer():
    folder = os.listdir("C:/Users/gokhan.kaya/OneDrive - Aster Textile/Desktop/BELGELERİM/PycharmProjects/PandasProjects/Txt_rapor")
    txt_name = []
    for search in folder:
        if "txt" in search:
            txt_name.append(search)
    return txt_name


# yukarıdaki txt_name listesinindeki dosya isimlerini alıp, txt dosyalarını açıp satır sonu ifadesini ("\n") gördü yerden
# bölüp verileri dosya değişkeni içinde liste olarak döndürür
for aktar in folder_transfer():
    file = open(aktar, "r")
    dosya.append(file.read().split("\n"))
    file.close()

# DataFrame e daha iyi aktarabilmek için, dosya değişkeni içindeki listeleri (",") idasini gördüğü yerden bölüp liste değişkeni
# içinde şekillendirir
for i in range(len(dosya)):
    for dd in dosya[i][1:-2]:
        liste.append(dd.split(","))

for x in liste:
    df_data.append(
        [int(x[0][2:13]), x[0][13:38], float(x[0][39:54]), x[0][54:78], x[0][79:108], int(x[0][109:120]), x[0][120:170],
         int(x[0][171:178])])

tabel_colum = ["HesapNo", "IBAN", "Tutar", "AdıSoyadı", "Açıklama", "TCNo", "Görev", "Mkodu"]

df = pd.DataFrame(data=df_data, columns=tabel_colum)

df.to_excel("banka_ödeme.xlsx")


