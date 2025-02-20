import numpy as np
import pandas as pd

#Pandas, Python'da veri analizi ve veri manipülasyonu için kullanılan güçlü bir kütüphanedir. En yaygın kullanılan iki veri yapısı Series ve DataFrame'dir.

#1. Pandas Series (Seriler)
#Bir Series, tek boyutlu bir dizidir. NumPy array'ine benzer ama bir index (etiket) içerir.

data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

###Özel Index ile Series
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(s)


#2. Pandas DataFrame (Veri Çerçevesi)
#DataFrame, tabloları temsil eden iki boyutlu bir veri yapısıdır (satır ve sütunlardan oluşur). Excel tablolarına benzer.

data = {
    "İsim": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
    "Yaş": [25, 30, 22, 35],
    "Maaş": [5000, 7000, 4500, 8000]
}

df = pd.DataFrame(data)
print(df)

###CSV Dosyasından DataFrame Yükleme
# df = pd.read_csv("veri.csv")  # "veri.csv" adlı dosyayı oku
# print(df)

###Excel Dosyasından DataFrame Yükleme
# df = pd.read_excel("veri.xlsx")
# print(df)


#3. DataFrame Temel İşlemler

print(df.head())  # İlk 5 satır
print(df.head(10))  # İlk 10 satır
print(df.tail())  # Son 5 satır
print(df.info())  # Veri tipi, eksik değerler ve sütun bilgileri
print(df.describe())  # Sayısal veriler için özet istatistikler
print(df["İsim"])  # Sadece "İsim" sütununu seç
print(df[["İsim", "Yaş"]])  # Birden fazla sütun seç
print(df.iloc[0])  # İlk satırı getir
print(df.iloc[1:3])  # 1. ve 2. satırları getir
print(df.loc[df["Yaş"] > 25])  # Yaşı 25'ten büyük olanları seç


#4. DataFrame Üzerinde Veri Manipülasyonu

###Yeni Sütun Ekleme
df["Şehir"] = ["İstanbul", "Ankara", "İzmir", "Bursa"]
print(df)

###Sütun Silme
df.drop(columns=["Şehir"], inplace=True)

###Satır Silme
df.drop(index=2, inplace=True)  # 2. indeksteki satırı sil

###Eksik Verileri Doldurma
df.fillna(0, inplace=True)  # Eksik değerleri 0 ile doldur
df.dropna(inplace=True)  # Eksik verileri içeren satırları sil


#5. Filtreleme ve Koşullu Seçimler

print(df[df["Maaş"] > 5000])  # Maaşı 5000'den fazla olanları getir
print(df[(df["Maaş"] > 5000) & (df["Yaş"] < 30)])

#6. DataFrame’de Gruplama (groupby)
#Yeni bir dataframe oluşturmam lazım data2 adında

data2 = {
    "İsim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Burak", "Fatma", "Emre", "Can"],
    "Yaş": [25, 30, 22, 35, 40, 29, 33, 27],
    "Maaş": [5000, 7000, 4500, 8000, 9000, 7200, 6600, 5400],
    "Şehir": ["İstanbul", "Ankara", "İzmir", "İstanbul", "Ankara", "İzmir", "İstanbul", "Ankara"]
}

# DataFrame oluştur
df2 = pd.DataFrame(data2)

print("Orijinal DataFrame:")
print(df2)

# Şehirlere göre maaşların ortalamasını hesapla
ortalama_maas = df2.groupby("Şehir")["Maaş"].mean()
print("\nŞehirlere Göre Ortalama Maaş:")
print(ortalama_maas)

# Şehirlere göre birden fazla istatistiksel işlem yap
agg_df = df2.groupby("Şehir")["Maaş"].agg(["mean", "max", "min", "sum", "count"]).reset_index()

print("\nŞehirlere Göre Maaş Analizi:")
print(agg_df)

#7. DataFrame’i Sıralama

df = df.sort_values(by="Yaş")  # Yaşa göre küçükten büyüğe sıralar
df = df.sort_values(by="Maaş", ascending=False)  # Maaşa göre büyükten küçüğe sıralar


#8. DataFrame’i Farklı Formatlarda Kaydetme

df.to_csv("yeni_veri.csv", index=False)  # CSV olarak kaydet
df.to_excel("yeni_veri.xlsx", index=False)  # Excel olarak kaydet





























