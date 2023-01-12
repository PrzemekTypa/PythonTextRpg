# PythonProjectTextRpg

1. Wstęp:
Gra przedstawia fabułę, w której gracz jest zatrudniony przez króla do odsieczy księżniczki, która jest uwięziona przez smoka.
Gracz musi pokonać różne przeszkody i bossów, aby dotrzeć do smoczej jaskini i uratować księżniczkę.
Gra oferuje różne ścieżki, które mogą być obrane przez gracza, a także zbieranie przedmiotów, które mogą pomóc graczowi w pokonaniu przeciwników.

2. Moduły używane w grze:
'os' i 'sys' służą do obsługi systemu operacyjnego.
'time' jest używany do opóźniania ekranów.

3. Zmienne:
'a', 'b' i 'c' służą do opóźniania ekranów w module 'time'.

4. Funkcje:
'prompt()' jest używana do wyświetlenia menu startowego gry.
'clear()' jest używana do wyczyszczenia ekranu.

5. Mapa:
'rooms' to słownik, który przechowuje informacje o pokojach w grze, w tym położenie pomieszczeń, przedmiotów i bossów.

'current_room' to zmienna, która przechowuje informacje o aktualnie przebywanym pokoju przez gracza.

6. Inventarz:
'inventory' to lista, która przechowuje informacje o przedmiotach zdobytych przez gracza.

7. Pętla gry:
Pętla while jest używana do gry, która kończy się tylko po zakończeniu zadania przez gracza.
Wewnątrz pętli są warunki, które w zależności od aktualnie przebywanego pokoju wyświetlają odpowiednie informacje i opcje dostępne dla gracza.

8. Zakończenie:
Gracz kończy grę po dotarciu do smoka, pokonaniu go.
Gracz może także zakończyć grę przed ukończeniem zadania, decydując się na opuszczenie jaskini(Exit), lub ginąć np. przegrywając w walce z którymś z bossów.

9. Implementacja:
Gra jest napisana w języku Python i korzysta z konsoli do interakcji z graczem.
Gracz może poruszać się po mapie, korzystając z komendy 'go' i wskazując kierunek.
Gracz może także zbierać przedmioty, korzystając z komendy 'get/take' i podając nazwę przedmiotu.
Gracz jest również zmuszony do rozwiązania zagadek, aby przejść dalej.

10. Testowanie:
Gra powinna zostać przetestowana przez kilku graczy, aby upewnić się, że działa poprawnie i jest bezbłędna.
Testowanie powinno obejmować sprawdzenie funkcjonalności wszystkich komend i opcji dostępnych dla gracza.
Testowanie powinno również obejmować sprawdzenie poprawności zagadek i walk z bossem.

11. Dalsze rozwijanie:
Gra może być rozwijana poprzez dodanie nowych pokojów, przedmiotów i bossów.
Gra może być również rozwijana poprzez dodanie nowych funkcjonalności, takich jak system ekwipunku, rozwijanie postaci gracza 
poprzez dodanie punktów życia/many/czarów oraz zaimplementowanie walki łącznie z (import random).
Gra może być także rozwijana poprzez dodanie grafiki i dźwięku, aby zwiększyć immersję gracza.

12. Wymagania systemowe:
Aby uruchomić grę, wymagany jest komputer z systemem operacyjnym Windows, macOS lub Linux oraz interpreter języka Python.
Gra jest przeznaczona do użytku z konsolą, więc nie wymaga specjalnego sprzętu graficznego ani dźwiękowego.
Gra powinna działać na większości komputerów osobistych bez konieczności dokonywania dodatkowych ustawień.
