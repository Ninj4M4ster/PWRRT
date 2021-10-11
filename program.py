import math

def okreslCene(ceny, kolory, indeks):
    kolor = kolory[indeks]
    if kolor == 'r':
        return ceny[0]
    elif kolor == 'g':
        return ceny[1]
    else:
        return ceny[2]

def dijkstra(ceny, n, kolejka, kolory, krawedzie):
    cena = 0
    koszta = {}
    for i in range(n-1):
        niesprawdzone = [k for k in krawedzie.keys()]
        start = kolejka[i]
        koniec = kolejka[i+1]
        # ustalenie kosztu podróży na każdy węzeł na nieskończoność
        for k, v in krawedzie.items():
            koszta[k] = math.inf
        koszta[start] = 0
        # algorytm wynokuje się, póki są jakieś nieodwiedzone węzły
        while niesprawdzone:
            min = math.inf
            # wybranie kolejnego sprawdzanego węzła na podstawie tego, do którego droga jest najtańsza w tej chwili
            for k in koszta.keys():
                if koszta[k] < min and k in niesprawdzone:
                    min = koszta[k]
                    aktualny = k

            niesprawdzone.remove(aktualny)

            # obliczany jest koszt podróży po każdej drodze sąsiadującej z aktualnym węzłem
            for sasiad in krawedzie[aktualny]:
                odleglosc = okreslCene(ceny, kolory, (aktualny, sasiad))
                if sasiad in niesprawdzone:
                    stara_cena = koszta[sasiad]
                    nowa_cena = koszta[aktualny] + odleglosc
                    if nowa_cena < stara_cena:
                        koszta[sasiad] = nowa_cena

        cena += koszta[koniec]

    return cena


def main():
    # słownik zawierający wszystkie możliwe połączenia dróg
    krawedzie = {
        "A": [1, 10], "B": [2], 1: ['A', 2, 9, 8], 2: ['B', 1, 3, 4],
        3: [2, 'D'], 4: [2, 5, 8], 5: ['D', 4, 6], "D": [3, 5],
        6: [5, 8, 7], 7: ['C', 6, 8], 8: [7, 6, 4, 1, 9], "C": [7, 11],
        9: [8, 1, 11], 10: ['A', 11], 11: ['C', 9, 10]
    }

    # słownik przypisujący kolor danemu odcinkowi
    kolory = {
        (10, 'A'): 'b', ('A', 10): 'b', (10, 11): 'r', (11, 10): 'r',
        ('A', 1): 'g', (1, 'A'): 'g', ('B', 2): 'b', (2, 'B'): 'b',
        (1, 2): 'r', (2, 1): 'r', (2, 3): 'g', (3, 2): 'g',
        (3, 'D'): 'r', ('D', 3): 'r', ('D', 5): 'r', (5, 'D'): 'r',
        (2, 4): 'b', (4, 2): 'b', (4, 5): 'b', (5, 4): 'b',
        (5, 6): 'r', (6, 5): 'r', (1, 8): 'b', (8, 1): 'b',
        (1, 9): 'g', (9, 1): 'g', (9, 8): 'g', (8, 9): 'g',
        (6, 8): 'r', (8, 6): 'r', (9, 11): 'b', (11, 9): 'b',
        (7, 8): 'g', (8, 7): 'g', (6, 7): 'b', (7, 6): 'b',
        (7, 'C'): 'g', ('C', 7): 'g', (11, 'C'): 'r', ('C', 11): 'r',
        (4, 8): 'g', (8, 4): 'g'
    }

    # wprowadzenie danych przez użytkownika
    ceny = [float(cena) for cena in str(input("Wprowadz ceny przejazdów po różnych kolorach dróg: ")).split()]
    for koszt in ceny:
        assert koszt >= 0, "Opłata za przejazd jest ujemna"

    n = int(input("Wprowadz ilosc odwiedzonych hangarów: "))
    assert n > 1, "Ilosc odwiedzonych hangarów musi być większa od 1"

    kolejka = [hangar for hangar in str(input("Wprowadz liste odwiedzonych hangarów: ")).split()]
    assert len(kolejka) == n, "Ilosc odwiedzonych hangarów nie zgadza się z ich lista"

    # uruchomienie algorytmu
    cena = dijkstra(ceny, n, kolejka, kolory, krawedzie)

    print(f'Koszt przejazdu wynosi {cena}')

if __name__ == '__main__':
    main()
