# PWRRT :racing_car:
PWRRT to repozytorium utworzone do przechowywania plików stworzonych do rekrutacji do koła naukowego PWR Racing Team.

## Ogólne informacje
Projekt został stworzony w programie PyCharm.

-> **program.py** jest programem służącym do obliczania kosztu podróży bolidu między poszczególnymi hangarami (2 etap rekrutacji).

Początkowym zamysłem było utworzenie do programu wizualizatora algorytmu, lecz ze względu na małą ilość czasu zrezygnowałem z tego pomysłu.

### Działanie *program.py*

Pierwszym etapem wykonania zadania było zmapowanie dróg do słowników. Do każdego węzła przypisałem numer, 
za pomocą którego możliwa była identyfikacja miejsc na drodze (obraz).

Następnie stworzyłem drugi słownik przyporządkowujący każdemu odcinkowi kolor drogi.

Ostatnim etapem było zaimplementowanie algorytmu Dijkstry w celu odnalezienia najkrótszej (w tym przypadku najtańszej) 
drogi pomiędzy poszczególnymi hangarami podanymi przez użytownika.
