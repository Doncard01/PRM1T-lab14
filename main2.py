import funkcje as f

if __name__ == '__main__':
    try:
        f.Funkcja2("./chess_games.csv", "Gambit")
        f.Funkcja2('./asd', 'black')
    except Exception as err:
        print("Błąd: ", err)
    finally:
        print("Program zakończył działanie")