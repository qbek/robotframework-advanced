### Komendy do uruchomienia przykładu:

Test raport w todoist (potrzebne konto i token)

`robot --listener TestReport.py:twoj_token:Reports ./`

Stworzenie raportu błedu w github (potrzebne konto i token):

`robot --listener TestReport.py:twoj_token:pełna_nazwa_repo ./`


Raport z testow i bug report jednocześnie:

`robot --listener TestReport.py:twoj_token:Reports --listener TestReport.py:twoj_token:pełna_nazwa_repo ./`
