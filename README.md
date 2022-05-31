Repo zawiera zdjęcia o rozmiarach: 250KB, 1MB, 4MB
Wykonanie testów: Uruchomić program.  
Opcja 3) wykona testy na "szybkość".  
Opcja 4) wykona test na "rozmiar obrazka".


Testy na szybkość:  

Testy dla pliku ./image_1mb.png  

Testy dla wiadomości o rozmiarze 10  
Średni czas szyfrowania wynosi 0.1456 sekund, standardowe odchylenie wynosi 0.0148  
Średni czas deszyfrowania wynosi 0.1120 sekund, standardowe odchylenie wynosi 0.0044

Testy dla wiadomości o rozmiarze 100  
Średni czas szyfrowania wynosi 0.1383 sekund, standardowe odchylenie wynosi 0.0032  
Średni czas deszyfrowania wynosi 0.1124 sekund, standardowe odchylenie wynosi 0.0024  

Testy dla wiadomości o rozmiarze 1000  
Średni czas szyfrowania wynosi 0.1647 sekund, standardowe odchylenie wynosi 0.0052
Średni czas deszyfrowania wynosi 0.1371 sekund, standardowe odchylenie wynosi 0.0051

Testy dla pliku ./image_4mb.png  

Testy dla wiadomości o rozmiarze 10  
Średni czas szyfrowania wynosi 0.7441 sekund, standardowe odchylenie wynosi 0.0205  
Średni czas deszyfrowania wynosi 0.5603 sekund, standardowe odchylenie wynosi 0.0076    

Testy dla wiadomości o rozmiarze 100  
Średni czas szyfrowania wynosi 0.7753 sekund, standardowe odchylenie wynosi 0.0989  
Średni czas deszyfrowania wynosi 0.6478 sekund, standardowe odchylenie wynosi 0.1454  

Testy dla wiadomości o rozmiarze 1000  
Średni czas szyfrowania wynosi 0.8168 sekund, standardowe odchylenie wynosi 0.0638  
Średni czas deszyfrowania wynosi 0.6311 sekund, standardowe odchylenie wynosi 0.0726  


Testy dla pliku ./image_250kb.png  

Testy dla wiadomości o rozmiarze 10  
Średni czas szyfrowania wynosi 0.0392 sekund, standardowe odchylenie wynosi 0.0074  
Średni czas deszyfrowania wynosi 0.0293 sekund, standardowe odchylenie wynosi 0.0021  

Testy dla wiadomości o rozmiarze 100  
Średni czas szyfrowania wynosi 0.0407 sekund, standardowe odchylenie wynosi 0.0036  
Średni czas deszyfrowania wynosi 0.0324 sekund, standardowe odchylenie wynosi 0.0013  

Testy dla wiadomości o rozmiarze 1000  
Średni czas szyfrowania wynosi 0.0832 sekund, standardowe odchylenie wynosi 0.0246  
Średni czas deszyfrowania wynosi 0.0612 sekund, standardowe odchylenie wynosi 0.0106  

Wnioski: czas szyfrowania/deszyfrowania rośnie mniej więcej linowo wraz z wzrostem rozmiaru pliku.  
Ponadto dla dłuższych wiadomości rośnie czas szyfrowania.

Testy na rozmiar plików:

obrazek: ./image_1mb.png

rozmiar wiadomości: 10  
stosunek rozmiaru nowego obrazka do starego: 1.0227618599142678  

rozmiar wiadomości: 100  
stosunek rozmiaru nowego obrazka do starego: 1.022759838883421

rozmiar wiadomości: 1000  
stosunek rozmiaru nowego obrazka do starego: 1.0228103646545956

obrazek: ./image_4mb.png  

rozmiar wiadomości: 10  
stosunek rozmiaru nowego obrazka do starego: 1.0432210988103119

rozmiar wiadomości: 100  
stosunek rozmiaru nowego obrazka do starego: 1.0432298717669461

rozmiar wiadomości: 1000  
stosunek rozmiaru nowego obrazka do starego: 1.0432574439163682

obrazek: ./image_250kb.png  

rozmiar wiadomości: 10  
stosunek rozmiaru nowego obrazka do starego: 1.0111764400643444

rozmiar wiadomości: 100  
stosunek rozmiaru nowego obrazka do starego: 1.011156482135658

rozmiar wiadomości: 1000  
stosunek rozmiaru nowego obrazka do starego: 1.0113800109369449

Wniosek: Stosunek (rozmiar nowego obrazka) / (rozmiar bazowego obrazka) jest większy im większy rozmiar ma obrazek bazowy
Rozmiar wiadomości nie ma większego znaczenia dla wynikowego rozmiaru obrazka
