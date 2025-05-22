# Problem: MPRT (Finding a Protein Motif )

## Description
Finding a protein motif N{P}[ST]{P} in specific protein sequences.

## Tok myślenia
- Znalezienie sposobu na pobranie sekwencji fasta białek
- Stworzenie dictionary, w którym będą przechowywane miejsca wystąpienia motywu na wzór:
-   Klucz - Nazwa białka (protein id)
-   Wartość - lista z miejscami wystąpienia patternu
- Stoworzenie tymczasowej listy przechowującej pozycje motywu w sekwencji
- Użycie NCBI-API by pobrać sekwencje do pliku tymczasowego
- Znalezienie pozycji sekwencji poprzez iterację przez sekwencję i znalezienie tej sekwencji 
- Dodanie do dictionary protein id oraz liste z miejscami wystąpienia motywu
- Wydrukowanie dopasowanego do Rosalynd formatu wczesniej stworzonego dictionary

## Trudności
- Trying to use "re.finditer()", but it skipped the whole 4 nucelotydes and motif can be next to each other (only 1 nucleotyde difference)
- I forget about '.strip()', which caused errors while creating API-friendly protein sequence IDs
- I forget about 0-indexing and was using '.find()' without adding +1 to position place, where it is 1 indexing in file.
## Wnioski
- Nalezy pamiętać, że odczyty z sekwencji fasta mają najcześciej "/n" na końcu wiersza oraz przy każdym odczycie z pliku txt też tak jest
- ".find()" pozwala szybko znaleźć miejsce wystąpienia wzoru (patternu) w sekwencji
