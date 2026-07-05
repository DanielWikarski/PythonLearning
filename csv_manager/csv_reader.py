import sys
import os
app_args = sys.argv


pwd = os.getcwd()
input_file = app_args[1] # nazwa pliku wejściowego na którym będziemy pracować
output_file = app_args[2] # nazwa pliku wyjściowego, tutaj podajemy nazwę jaki plik ma się utworzyć po modyfikacji pliku wejściowego
changes_to_do = app_args[3:] # argument 3 i dalej to bedą zmiany jakie chcemy przeprowadzić na pliku
# sytax zmian X,Y,nowe_dane, gdzie 0 to pierwszy indeks każdego
# -- ważne -- plik input musi być w tym samym folderze, co plik reader.py

changes_to_do = [change.split(",") for change in changes_to_do] # rozbijam zmiany, żebyśmy mieli konkretne dane

with open(f"{pwd}/{input_file}", "r", encoding="UTF-8") as f: # otwieram plik z nazwą jaka jak arugment nazwy input_file, ścieżka 
    # jest automatycznie taka jak lokalizacja csv_manager
    input_file_data = f.read()



rows = input_file_data.split('\n') # podzieliłem na rzędy plik input_file żebyśmy mieli Y

input_file_data = [element.split(",") for element in rows] # w każdego rzędu usunąłem przecinek, żebyśmy mieli same dane,
# czyli listę z listami w których są rzędy


for change in changes_to_do:
    try:
        x = int(change[0])
        y = int(change[1])
    except:
        print("Wprowadzono niepoprawne argumenty - SYNTAX X(int),Y(int),new_data")
        continue # jeśli jakieś dane będą niepoprawnie zapisane, program się nie wywali, tylko da komunikat i przejdzie do
        # kolejnej iteracji
    new_data = change[2]
    input_file_data[y][x] = new_data 


output_file_data = ""  # output_file_data to zmienna, która będzie przekazywana do pliku CSV jako dane
for element in input_file_data: # jako, że do write nie można przekazywać listy, do zmiennej jako strin wrzucam zawartość input_file_data
    output_file_data +=",".join(element)+"\n"


with open(f"{pwd}/{output_file}", "w", encoding="UTF-8") as f:
    f.write(output_file_data)







    


