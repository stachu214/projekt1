# PROJEKT 2: Wtyczka do programu QGIS
Wykonana przez nas wtyczka służy do obliczania różnicy wysokości między dwoma punktami oraz liczy pole powierzchni miedzy conajmniej trzema punktami.

## INSTALACJA WTYCZKI: 
Cały folder "wtyczka_sofg" umieścić w folderze "plugins" odpowiadającego za przechowywanie wtyczek do programu QGIS. Przykładowa lokalizacja:
"C:\Users\Stanisław\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins"
Gdzie, "C:\Users\(nazwa użytkownika)\..."
Następnie przy pomocy wbudowanej funkcji "Zarządzanie wtyczkami" wyszukać, w katalogu wszystkie wtyczki: "wtyczka_SOFG". Zaznaczyć odpowiedniego check-boxa i upewnić się, że wtyczka jest zainstalowana.


## WYMAGANIA:
##### Obsługiwane systemy:
- Windows 10 Home
- Windows 11
##### Obsługiwane wersje Qgis'a:
- QGIS 3.34.4
##### Programy do edycji wtyczki:
- python w wersji 3.11.8
- biblioteka PyQt5
- biblioteka qgis.core
- biblioteka qgis.utilis
- biblioteka qgis.PyQt

## ZASTOSOWANIE WTYCZKI:
Wtyczka 'wtyczka_SOFG' jest wtyczką programu QGIS, posiada dwie podstawowe funkcjonalności:
- obliczanie różnicy wysokości pomiędzy dwoma wybranymi przez użytkownika punktami,
- obliczanie pola powierzchni pomiędzy minimum trzema wybranymi przez użytkownika punktami

## UŻYTKOWANIE WTYCZKI:

Aby wtyczka działała poprawnie należy (wytyczne):
- użytkownik musi wybrać w oknie ,Wybierz warstwę, warstwę na której znajdują sie punkty do wykonania pomiarów,
- wymagane jest od użytkownika podanie odpowiedniej ilości punktów, dostosowanej do wybranej funckcji naszej wtyczki. Gdy użytkownik nie spełni wymagań dotyczącej ilości punktów, program 
zwróci w dolnej części interface-u wtyczki konkretny błąd:
Dla pomiaru przewyższenia:
"Wybrano za mało punktów do obliczenia różnicy wysokoci"
"Wybrano za dużo punktów do obliczenia różnicy wysokoci"
Dla pomiaru pola powierzchni: 
"Wybrano za mało punktów do obliczenia pola powierzchni"
- upewnić się ,że wtyczka odpala sie na pliku o nazwie agencje_zatrudnienia.sph. Wymagane jest to ponieważ program zaciąga nasza wyokość z tabeli atrybutów zawartych w tym pliku punktów:
 h_1 = float(selected_features[0]['wysokosc'])
 h_2 = float(selected_features[1]['wysokosc'])
- Użytkownik musi zaznaczać kolejne punkty pojedyńczo przy pomocy klawisza Ctrl, nie może użyc wbudowanego narzędzia QGIS "Zaznacz obiekty prostokątem"
- Upewnić się, że wszystkie punkty, z których użytkownik chce skorzystać, znajdują się na JEDNEJ wartswie.

##### OBLICZENIE RÓŻNICY WYSOKOŚCI: 

Po instalacji wtyczki i załadowania odpowiedniego pliku należy:
 - Uruchomić wtyczkę w programie QGIS,
 - Wybrać warstwę na której znajdują sie nasze punkty,
 - Przy użyciu klawisza Ctrl zaznaczyć 2 punkty,
 - Następnie należy kliknąć przycisk "Oblicz dh". Zostanie policzona różnica wysokości,
 - Wynik zostanie wyświetlony w metrach,obok napisu "Obliczone przewyższenie", 
 - Jeśli użytkownik chce wykonać kolejne obliczenia, należy powtórzyć powyższe czynności,
 - Jeśli użytkowni chce zakończyć korzystanie z wtyczki, należy kliknąć przycisk "Okej","Anuluj" albo ikonkę "x" w prawym górnym rogu,
 - W przypadku wybrania nieodpowiedniej liczby punktów (tj. innej niż 2) program zwróci odpowiedni komunikat, aby dalej korzystać z programu należy postępować zgodnie z powyższą instrukcją

###### OBLICZENIE POLA POWIERZCHNI: 
Po instalacji wtyczki i załadowania odpowiedniego(według wytycznych) pliku należy:
 - Uruchomić wtyczkę w programie QGIS,
 - Wybrać warstwę na której znajdują sie nasze punkty,
 - Przy użyciu klawisza Ctrl zaznaczyć conajmniej 3 punkty,
 - Następnie należy kliknąć przycisk "Oblicz pole". Przy użyciu wzoru Gaussa zostanie obliczone pole powierzchni a wynik zostanie zwrócony w m2,
 - Jeśli użytkownik chce wykonać kolejne obliczenia, należy powtórzyć powyższe czynności
 - Jeśli użytkowni chce zakończyć korzystanie z wtyczki, należy kliknąć przycisk "Okej","Anuluj" albo ikonkę "x" w prawym górnym rogu
 - W przypadku wybrania nieodpowiedniej liczby punktów (tj. mniejszej niż 3) program zwróci odpowiedni komunikat, aby dalej korzystać z programu należy postępować zgodnie z powyższą instrukcją

## ZNANE BŁĘDY WTYCZKI:
 -Użytkownik nie może zaznaczać punktów przy użyciu wbudownaje funkji QGIS 'Zaznacz obiekty prostokątem' 
