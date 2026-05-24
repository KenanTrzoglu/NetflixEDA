import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)




df =pd.read_csv("netflıx.csv",engine='python')
df.dropna(inplace=True)

kopyasatırlar = df[df["Title"].duplicated()]
print(kopyasatırlar)

for col in df.columns:
    print("Sutün İsmi==",col)
    print(df[col].unique)

#print(df[df["Vote_Average"]=="Animation"])

df["Vote_Average"] = df["Vote_Average"].astype("float")


df["Vote_Count"] = df["Vote_Count"].astype("int64")

C = df["Vote_Average"].mean()
m = df["Vote_Count"].quantile(0.75)
df["IMDB"] = (df["Vote_Count"]/(df["Vote_Count"]+m))*(df["Vote_Average"]+(m/(m+df["Vote_Count"]))*C)
print(df.info())
df["IMDB"] = df["IMDB"].apply(lambda x: math.floor(x*10)/10)


def dildaireciz():
    dildaire2= df["Original_Language"].value_counts(normalize=True)
    dildaire2.plot.pie(
        autopct="%1.1f%%",  # Dilimlerin üzerine yüzde oranlarını yazar (örn: %45.0)
        startangle=90,  # Grafiğin başlangıç açısını ayarlar (daha simetrik durur)
        shadow=True,  # Hafif bir gölgelendirme ekler
        figsize=(6, 6)  # Grafiğin boyutunu ayarlar
    )
    plt.title("Original Language Oranları")
    plt.ylabel("")
    plt.show()
    return
dildaireciz()

def popularityenyuksek5film():
    a = df.sort_values(by="Popularity",ascending=False)[["Title","Popularity"]][0:5]
    plt.figure(figsize=(12,12))
    sns.barplot(a,x="Title",y="Popularity")
    plt.xticks(rotation=45)
    plt.title("Best Five Popularity")
    plt.xlabel("Movie Title")
    plt.ylabel("Popularity")
    plt.show()
    return

def IMDBENYUKSEK5FİLM():
    b = df.sort_values(by="IMDB",ascending=False)[["Title","IMDB"]][0:5]
    plt.figure(figsize=(12,12))
    sns.barplot(b,x="Title",y="IMDB")
    plt.xticks(rotation=45)
    plt.title("best five IMDB")
    plt.xlabel("Movie Title")
    plt.ylabel("IMDB")
    plt.show()



def türegörebarplot():
    tum_turlerin_sayilari = df["Genre"].str.split(", ").explode().value_counts()
    plt.figure(figsize=(12,12))
    sns.barplot(x=tum_turlerin_sayilari.index,y=tum_turlerin_sayilari.values)
    plt.xticks(rotation=45)
    plt.xlabel("Genre")
    plt.title("")
    plt.show()


def türegöredaire():
    list1 = []
    list2 = []
    tum_tür_sayıları = df["Genre"].str.split(", ").explode().value_counts(normalize=True)
    tum_tür_sayıları.plot.pie(
            autopct="%1.1f%%",
            startangle=90,
            shadow=True,
            figsize=(6, 6))
    plt.title("Genres oranları")
    plt.show()

türegöredaire()
türegörebarplot()
IMDBENYUKSEK5FİLM()
popularityenyuksek5film()
dildaireciz()

print(df)


