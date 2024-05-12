# PROJEKT 1: TRANSFORMACJE WSPÓŁRZĘDNYCH 
Wykonany przez nas skrypt służy do transformacji danych między kolejnymi układami.

##### Obsługiwane transformacje 
- XYZ (geocentryczne) -> BLH (elipsoidalne) 
- BLH -> XYZ
- XYZ -> NEUp (topocentryczne) 
- BL -> PL1992 
- BL -> PL2000 

##### Obsługiwane elipsoidy 
- GRS80 
- WGS84 
- elipsoida Krasowskiego 

## WYMAGANIA 
 - python 3.11.8 
 - system operacyjny Windows 11 lub Windows 10 
 - biblioteka numpy == 1.26.4
 - biblioteka sys (biblioteka standardowa python)
 
## UŻYTKOWANIE PROGRAMU 
Program obsługiwany jest przy użyciu flag ,które pozwalają nam na podanie 
pliku z danymi, wybór elipsoidy oraz transformacji którą wskaże użytkownik.

##### FLAGA NUMER 1: 
```sh
-plik <nazwa_pliku>
```
Wymaga od użytkownika wprowadzenia ścieżki do pliku z danymi wejściowymi. Plik powinien zostać podany ze swoim rozszerzeniem.

##### FLAGA NUMER 2: 
```sh
-elip 
```
Po wprowadzeniu powyższej flagi należy podać nazwę elipsoidy użytej do rozwiązania.
Obsługiwane elipsoidy: 
- GRS80 
- WGS84 
- KRASOWSKI
UWAGA: Należy wpisywać przy użyciu wielkich liter!! 

##### FLAGA NUMER 3:
```sh
- trans
```
Przyjmuje ona nazwe wybranej przez użytkownika transfomacji transofmacji. 
Obsługiwane transformacje: 
- XYZ2BLH 
- BLH2XYZ 
- XYZ2NEUP 
- PL1992 
- PL2000
UWAGA: Należy wpisywać przy użyciu wielkich liter!!

##### PRZYKŁADOWE WYWOŁANIE PROGRAMU W TERMINALU: 
```sh
projekt1_skrypt.py -plik wsp_inp.txt -elip GRS80 -trans XYZ2BLH 
```

Jeżeli użytkownik spełnił wszystkie powyższe wymagania t.j.: 
- Podał wszystkie flagi 
- Podał jedynie te elipsoidy oraz transformacje, które obsługuje program 
- Użytkownik podał w argumencie -plik ścieżkę do istniejącego pliku

Program zakończy swoje działanie, a na konsoli pojawi się komunikat: 
```python
Program zakończył działanie. Wyniki znajdują się w pliku wsp_trans.txt
```
Oznacza to, że program zadziałał pomyślnie, a w rezultacie został utworzony plik o nazwie ,,wsp_trans.txt" który zawiera wyniki transformacji wskazanej przez użytkownika.

# PRZYKŁADOWE UŻYCIA PROGRAMU: 

## Transformacja XYZ -> BLH

- XYZ2BLH.txt : 
```sh
Współrzedne geocentryczny ECEF stacji pemanentnej GNSS
Obserwatorium Astronomiczno-Geodezyjne w Józefosławiu
  X[m]         Y[m]        Z[m]
# -----------------------------------------------------
3664940.500,1409153.590,5009571.170
3664940.510,1409153.580,5009571.167
3664940.520,1409153.570,5009571.167
3664940.530,1409153.560,5009571.168
3664940.520,1409153.590,5009571.170
3664940.514,1409153.584,5009571.166
```
- Wywołanie prgramu: 
```sh
projekt1_skrypt.py -plik XYZ2BLH.txt -elip GRS80 -trans XYZ2BLH
```

-WYNIK (B[°] , L[°] , H[m]) : 
```sh
52.0972722193266 21.03153333279777 141.3986623911187 
52.09727216202451 21.031533144230153 141.3998245196417 
52.0972721212852 21.031532955662534 141.403353812173 
52.09727208606682 21.03153276709492 141.4076721612364 
52.0972720869496 21.031533228061544 141.4101303620264 
52.09727211984851 21.03153317776271 141.40221093595028 
```

## Transformacja BLH -> XYZ

-BLH2XYZ.txt : 
```sh
Współrzedne geocentryczny ECEF stacji pemanentnej GNSS
Obserwatorium Astronomiczno-Geodezyjne w Józefosławiu
  B[°]         L[°]        H[m]
# -----------------------------------------------------
51.2457, 21.1122, 123.000
52.1627, 19.9341, 189.000
56.3562, 21.6356, 125.000
51.3059, 19.0335, 278.000
53.7562, 20.4890, 169.000
```
- Wywołanie prgramu: 
```sh
projekt1_skrypt.py -plik BLH2XYZ.txt -elip GRS80 -trans BLH2XYZ
```

-WYNIK (X[m] , Y[m] , Z[m]) : 
```sh
3732279.9669159506 1441080.098754062 4950796.959167662 
3685881.9533848525 1336752.3153665361 5014077.935921076 
3292422.6161753344 1305929.3004261325 5286622.159366982 
3777247.116604646 1303081.3262331765 4955107.763926353 
3540157.562777071 1322836.0601088614 5120883.564491956 
```

## Transformacja BL -> PL1992/2000 
-BL21992_2000.txt :
```sh
Współrzedne geocentryczny ECEF stacji pemanentnej GNSS
Obserwatorium Astronomiczno-Geodezyjne w Józefosławiu
  B[°]         L[°]        H[m]
# -----------------------------------------------------
51.2457, 21.1122
52.1627, 19.9341
56.3562, 21.6356
51.3059, 19.0335
53.7562, 20.4890
```
- Wywołanie prgramu: 
```sh
projekt1.py -plik BL21992_2000.txt -elip GRS80 -trans PL2000
```
-WYNIK PL2000 (X[m] , Y[m]) : 
```sh
5678988.668489667 7507833.904233483 
5781537.61820694 7427068.441742791 
6247924.428653828 7539287.992842931 
5686186.943528178 6572064.810123053 
5958442.807034232 7466298.019972926  
```

## Transformacja XYZ -> NEUp

-XYZ2NEUp.txt : 
```sh
Współrzedne geocentryczny ECEF stacji pemanentnej GNSS
Obserwatorium Astronomiczno-Geodezyjne w Józefosławiu
  X0[m]   Y0[m]   Z0[m]  X[m]   Y[m]   Z[m]
# -----------------------------------------------------
3664940.500, 1409153.590, 5009571.170
3.234878264399999976e+07, 1.470312568000000119e+07, 2.847713269999999942e+04
-2.391130946000000089e+07, -1.089180339500000142e+07, -2.229962486000000034e+06
1.256775858699999936e+07, 1.288512925399999879e+07, 1.944924987600000203e+07
1.982159728800000250e+07, 3.882086669999999925e+06, 1.731373310199999809e+07
``` 
'' Pierwszy wiersz zawiera wartości X0 Y0 i Z0 a kolejne wiersze to wartości X Y Z ''

- Wywołanie prgramu: 
```sh
projekt1.py -plik XYZ2NEUp.txt -elip GRS80 -trans XYZ2NEUP
```

-WYNIK (X[m] , Y[m] , Z[m]) : 
```sh
[-27949925.95510591   2114262.20294082  15447825.94157988] 
[ 19345585.73404936  -1584893.29903232 -24236550.4558055 ] 
[ -935953.10455414  7516422.70893525 19028659.69820582] 
[-5040774.67547936 -3490134.6413819  19518066.202581  ] 
```

# Błędy 

- program nie wykonuje transformacji dla plików w których dane zajmują tylko jeden wiersz 
- jeśli użytkownik nie rozdzieli podanych przez siebie danych w swoim pliku przy użyciu "," program zwróci błąd o błędnym formacie danych
- błędna kombinacją pliku wejściowego, wraz z niemożliwą dla niego transformacją zakończy się błędem
- mechanizm odczytu flag powinien poinformować użytkownika o popełnionym błędzie, posiada on jednak niedoskonałości, które dla przypadków skrajnych wprowadzonych flag, mogą zakończyć działanie programu nieobsłużonym błędem
- skrypt musi zostać odpalony w środowisku umożliwiającym utworzenie pliku z danymi wyjściowymi oraz przez użytkownika z odpowiednimi uprawnieniami
