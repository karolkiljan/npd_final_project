<h1>Projekt zaliczeniowy w ramach kursu 
"Narzędzia programistyczne w Pythonie wspierające analizę danych (Mat) 20/21"
</h1>

<h2>
Przygotowanie danych do obliczeń
</h2>

<p>
Wykorzystane zostały dwa zbiory danych:

1. Wykaz_szkół_i_placówek_wg_stanu_na_30.IX._2018_w.5.xlsx
2. tabela12.xls

Z tabeli pierwszej wydobywane były dane o szkołach, a w tabeli drugiej znajdowały się
dane o liczbie osób w określony wieku w gminie i z pomocą tych danych
wyliczona została liczba osób urodzona w danym roku w gminie.

W analizie wzięte zostaly pod uwagę szkoły następujących typów:
1. Przedszkole
2. Punkt przedszkolny
3. Szkoła podstawowa
4. Gimnazjum
5. Liceum ogólnokształcące
6. Technikum
7. Sześcioletnia szkoła muzyczna I stopnia
8. Czteroletnie liceum plastyczne
9. Zespoły szkół

W efekcie utracone zostało 433334 z 857406 danych o dzieciach, co oznacza stratę na poziomie 6.78%
oraz utracone zostało 85103 z 857406 danych o nauczycielach, co oznacza stratę na poziomie 9.93%
tak więc mieści się to w 10 procentowym marginesie utraty danych.

Analiza rozpoczyna się od ograniczenia danych o szkołach jedynie do tych wymienionych powyżej.
W danych o liczbie uczniów oraz nauczycieli w szkołach nie było żadnych braków w danych.
Jako liczbę uczniów traktuję dane z kolumny 'Uczniowie, wychow., słuchacze', a liczba nauczycieli w placówce to suma kolumn
'Nauczyciele pełnozatrudnieni' oraz 'Nauczyciele niepełnozatrudnieni (stos.pracy)'.
Następnie założyłem, że szkoły oraz zespoły szkół posiadające ten sam numer RSPO dzielą ze sobą uczniów oraz nauczycieli.
W zespołach szkół w każdym wierszu było zero uczniów, tak więc rozdzielenie sprowadzało się jedynie do nauczycieli.
Do każdej szkoły o danym numerze RSPO dodawane była liczba nauczycieli zależna od liczby uczniów danej szkole według formuły:

dodawani nauczyciele = (liczba uczniów w danej szkole / liczba uczniów)* liczba dostępnych jeszcze nauczycieli z puli
oraz z tej wartości brana była "podłoga".

Potem dla każdej placówki policzony został stosunek uczniów do nauczycieli, gdzie w przypadku zera uczniów lub nauczycieli
interpretowane to było jako zero uczniów per nauczyciel. Wartość została zaokrąglona.

Ostatnim krokiem dla pozadania 1 było policzenie statystyk- min, max, średnia
dla stosunku uczniów do nauczycieli w jednej szkole dla każdej gminy z podziałem na typ szkoły, oraz takich samych statystyk,
ale dla rodzajów gmin, gdzie punktem odniesienia były wartości kolumny 'Typ gminy'

W podzadaniu 2 pierwszym krokiem było odczytanie całkowitej liczby ludzi w danym wieku, zależnie od gminy.
brane pod uwagę były jedynie osoby do 30 roku życia w związku z faktem, że najstarsza osoba uczęszczająca do jednej z rozpatrywanych
w analizie placówek mogła miec co najwyżej 20 lat. 

Następnie otrzymane dane zostały przekształcone z danych o wieku na dane o roku urodzenia biorąc za punkt odniesienia rok 2020,
ponieważ w tabeli, z której były brane dane widnieje informacja, że są to dane na 2020 rok.
Każdy wiersz danych indeksowany był kodem gminy, z pomocą którego można było powiązać dane z uczniami oraz nauczycielami w szkołach
i danymi o liczbie osób z danych roczników w danej gminie. Algorytm był następujący:
1 i 2 numer indeksu połączone dawały numer województwa odpowiadający danej w kolumnie 'woj' z danych o szkołach
3 i 4 numer indeksu połączone dawały numer powiatu odpowiadający danej w kolumnie 'pow' z danych o szkołach
5 i 6 numer indeksu połączone dawały numer gminy odpowiadający danej w kolumnie 'gm' z danych o szkołach

Potem utworzony został zbiór danych, w których zależnie od szkoły w kolumnach z latami, które dana szkoła obejmuje
wyliczana była liczba dzieci z danego rocznika w danej placówce za pomocą wzoru:

liczba dzieci z danego rocznika w szkole = liczba dzieci w szkole * (liczba dzieci z danego rocznika / 
suma liczb dzieci z roczników objętych przez daną placówkę)

Roczniki dla szkół wyglądały następująco:
* Przedszkole: 2012-2015
* Punkt przedszkolny: 2012-2015
* Szkoła podstawowa: 2006-2002
* Gimnazjum: 2003-2005
* Liceum ogólnokształcące: 2000-2002
* Technikum: 1999-2002
* Sześcioletnia szkoła muzyczna I stopnia: 2007-2012
* Czteroletnie liceum plastyczne: 1999-2002

Na koniec policzone zostały statystyki min, max oraz średnia dla dla liczby dzieci z danego rocznika w szkole w zależności od rodzaju gminy,
gdzie rodzaj gminy był taki sam jak w poprzednim podpunkcie.

Wszystkie dane wynikowe został zapisane w plikach odpowiednio:
* 'result_kids_per_teacher_a' dla podpunktu pierwszego z danymi dla gmin
* 'result_kids_per_teacher_B' dla podpunktu pierwszego z danymi dla gmin zależnie od rodzaju gminy
* 'result_kids_per_year' dla podpunktu drugiego z danymi dla gmin zależnie od rodzaju gminy
</p>
