import pandas as pd
import os, collections, numpy


def Funkcja1(sciezka, sposob):
    if os.path.exists(os.path.abspath(sciezka)) == False:
       raise AssertionError("Nie znaleziono pliku!")

    df = pd.read_csv(sciezka)
    ile = df['id'].count()
    print("Liczba wszystkich partii = ", ile)

    wygrane = df['id'][df['winner'] == sposob].count()
    procent = (wygrane/ile)*100
    print(f"Procent partii zakonczonych przez {sposob} = {procent}%")
    return ile, procent

def Funkcja2(sciezka, ciag):
    if os.path.exists(os.path.abspath(sciezka)) == False:
       raise AssertionError("Nie znaleziono pliku!")

    df = pd.read_csv(sciezka)
    ile = df.loc[df['opening_name'].str.contains(ciag)]['opening_name'].count()
    print(f"Znaleziono {ile} partii z podanym ciągiem znaków: {ciag}")
    unikalne = pd.unique(df.loc[df['opening_name'].str.contains(ciag)]['opening_name'])
    #print(unikalne) #zakomentowane, bo duzo wypisuje
    lista = numpy.ndarray.tolist(unikalne)
    uniq = len(lista)
    print(f"Ilość unikalnych nazw: {uniq}")
    return ile, uniq