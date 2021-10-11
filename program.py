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
    for i in range(n-1):
        start = kolejka[i]
        koniec = kolejka[i+1]

    return cena


def main():
    krawedzie = {
        "A": [1, 10], "B": [2], 1: ['A', 2, 9, 8], 2: ['B', 1, 3, 4],
        3: [2, 'D'], 4: [2, 5, 8], 5: ['D', 4, 6], "D": [3, 5],
        6: [5, 8, 7], 7: ['C', 6, 8], 8: [7, 6, 4, 1, 9], "C": [7, 11],
        9: [8, 1, 11], 10: ['A', 11], 11: ['C', 9, 10]
    }
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
        (7, 'C'): 'g', ('C', 7): 'g', (11, 'C'): 'r', ('C', 11): 'r'
    }
    ceny = [float(cena) for cena in str(input("Wprowadz ceny przejazdów po różnych kolorach dróg: ")).split()]
    n = int(input("Wprowadz ilosc odwiedzonych hangarów: "))
    kolejka = [hangar for hangar in str(input("Wprowadz liste odwiedzonych hangarów: ")).split()]
    cena = dijkstra(ceny, n, kolejka, kolory, krawedzie)

    print(f'Koszt przejazdu wynosi {cena}')

if __name__ == '__main__':
    main()
