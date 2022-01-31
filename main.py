import funkcje as f

if __name__ == '__main__':
    try:
        f.Funkcja1("./chess_games.csv", "white")
        f.Funkcja1("./chess_games.csv", "black")
        f.Funkcja1("./chess_games.csv", "draw")
        f.Funkcja1('./asd', 'black')
        f.Funkcja1("./chess_games.csv", "remis")
    except Exception as err:
        print("Błąd: ", err)
    finally:
        print("Program zakończył działanie")