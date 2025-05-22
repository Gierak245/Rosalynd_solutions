# Eng:
# Problem: MPRT (Finding a Protein Motif )

## Description
Finding a protein motif N{P}[ST]{P} in specific UniProt protein sequences.

## Thought Process

* Finding a method to retrieve protein FASTA sequences
* Creating a dictionary to store the motif positions in the format:

  * **Key** – UniProt ID
  * **Value** – List of motif positions
* Creating a temporary list to store the positions of the motif in the sequence
* Using the UniProt API to download the sequences into a temporary file
* Identifying motif positions by iterating over the sequence and searching for matches
* Adding the protein ID and the list of motif positions to the dictionary
* Printing the final dictionary in the Rosalind-compatible output format

## Challenges

* Tried using `re.finditer()`, but it skipped overlapping patterns — in this case, the motif can appear with only one nucleotide in between
* Forgot to use `.strip()`, which caused issues with generating API-compatible protein sequence IDs
* Forgot about 1-based indexing in the output and was using `.find()` without adding `+1` to the position, which led to incorrect results

## Learnings

* Remember that FASTA sequences often contain newline characters (`\n`) at the end of lines, and the same applies when reading from `.txt` files
* `.find()` is a quick way to locate a pattern within a sequence

# PL:
## Opis
Znalezienie motywu N{P}[ST]{P} w sekwencjach białkowych UniProt.

## Tok myślenia

* Znalezienie sposobu na pobranie sekwencji fasta białek
* Stworzenie dictionary, w którym będą przechowywane miejsca wystąpienia motywu na wzór:
  
  * **Klucz** – UniProt ID
  * **Wartość** – lista z miejscami wystąpienia patternu
* Stoworzenie tymczasowej listy przechowującej pozycje motywu w sekwencji
* Użycie UniProt API by pobrać sekwencje do pliku tymczasowego
* Znalezienie pozycji sekwencji poprzez iterację przez sekwencję i znalezienie tej sekwencji 
* Dodanie do dictionary protein id oraz liste z miejscami wystąpienia motywu
* Wydrukowanie dopasowanego do Rosalynd formatu wczesniej stworzonego dictionary

## Trudności

* Próbowałem użyć `re.finditer()`, ale pomijało całe 4 nukleotydy, a motywy mogą znajdować się tuż obok siebie (różnica tylko 1 nukleotydu).
* Zapomniałem o `.strip()`, co powodowało błędy podczas tworzenia przyjaznych dla API identyfikatorów sekwencji białek.
* Zapomniałem o indeksowaniu od zera i używałem `.find()` bez dodania `+1` do pozycji, mimo że w pliku pozycje są indeksowane od 1.

## Wnioski

* Nalezy pamiętać, że odczyty z sekwencji fasta mają najcześciej (`\n`) na końcu wiersza oraz przy każdym odczycie z pliku `.txt` też tak jest
* `.find()` pozwala szybko znaleźć miejsce wystąpienia wzoru (patternu) w sekwencji
