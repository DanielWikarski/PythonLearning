import sys
import os
import csv
import json
import pickle


class BaseFormat:
    # baza, którą muszą mieć wszystkie klasy, definiuje tutaj że każda klasa z formatem musi mieć funkcje otwarcia i zapisu pliku

    #argumentem tutaj jest self i ścieżka do pliku, który będziemy otwierać
    def read(self, filepath):
        raise NotImplementedError("Method read() has to be run from format class not the base")
    # tutaj dodatkowo mamy argument data, tutaj przechowuje dane, które będą zapisane
    def save(self, filepath, data):
        raise NotImplementedError("Method save() has to be run from format class not the base")


# w każdej z klas, mamy opcje odczytania i zapisu

#generalnie będziemy robić w każdej formie danych listę-list, żeby było łatwiej potem konwertować itp.
class CSVFormat(BaseFormat):
    # input file musi być w tym samym folderze o skrypt! Bo filepath bierze nazwę wpisaną przez usera,
    # a funkcja open szuka tego TYLKO w folderze z aplikacją
    def read(self, filepath):
        with open(filepath, mode="r", encoding="UTF-8") as f:
            return list(csv.reader(f))

    def save(self, filepath, data):
        with open(filepath, mode="w", encoding="UTF-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)

class JSONFormat(BaseFormat):
    def read(self, filepath):
        with open(filepath, mode="r", encoding="UTF-8") as f:
            return json.load(f)
    def save(self, filepath, data):
        with open(filepath, mode="w", encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

class TXTFormat(BaseFormat):
    def read(self, filepath):
        data = []
        with open(filepath, mode="r", encoding="UTF-8") as f:
            for line in f:
                row = line.strip().split(",")
                data.append(row)
        return data
    def save(self, filepath, data):
        with open(filepath, mode="w", encoding="UTF-8") as f:
            for row in data:
                f.write(",".join(row) + "\n")

class PickleFormat(BaseFormat):
    def read(self, filepath):
        with open(filepath, mode="rb") as f:
            return pickle.load(f)
    def save(self, filepath, data):
        with open(filepath, mode="wb") as f:
            pickle.dump(data, f)

class FileProcessor:
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.data = []  


        # w zależności jaki format będzie wybrany przez usera (sprawdzamy rozszerzenie), taka klasa będzie obsługiwała zdarzenie
        self.format_handlers = {
            "csv": CSVFormat(),
            "json": JSONFormat(),
            "txt": TXTFormat(),
            "pickle": PickleFormat()
        }



    def _get_handler(self, filename):
        extension = filename.split(".")[-1].lower() #sprawdzam jakie rozszerzenie zostało wpisane i czy program to obsługuje
        #odcinam to co po kropce i jakby ktoś wpisał z dużej litery to zmieniam na małe
        #sprawdzam słownik format_handler
        if extension not in self.format_handlers:
            raise ValueError(f"Data format: {extension} is not supported!") # jeśli nie ma tego rozszerzenia w słowniku, to wywalamy błąd
        return self.format_handlers[extension] #jeśli jest - przekazujemy go dalej, do metody process

    def process(self):
        reader = self._get_handler(self.input_file)
        self.data = reader.read(self.input_file)
        self._apply_changes()
        self._display_data()
        writer = self._get_handler(self.output_file)
        writer.save(self.output_file, self.data)
        print(f"\nFile has been saved successfully: {self.output_file}")



    def _apply_changes(self):
        # metoda aplikująca zmiany na pliku
        for change in self.changes:
            x_str, y_str, value = change.split(",", 2) 
            x = int(x_str)  
            # Kolumna
            y = int(y_str)  
            # Wiersz
            

            #jak user wpisze np. za dużą wartość kolumny albo rzędu, którego nie ma to jest błąd
            if y < len(self.data) and x < len(self.data[y]):
                self.data[y][x] = value
            else:
                raise ValueError("Changes cannot be done. Given positions are out of scope of data.")

    def _display_data(self):
        # metoda pokazuje jakie zmiany naszły jak zmieniliśmy plik
        print("\nContent after modyfing:\n")
        for row in self.data:
            print(",".join(str(item) for item in row))


# sprawdzam czy jest wystarczająca ilośc argumentów podanych przy uruchomieniu skryptu, jak nie to jest błąd i podaje
# w jakim formacie to ma być zapisane
if len(sys.argv) < 3:
    raise Exception("Arguments in wrong format. Should've -> [python file name] [input file] [output file] [changes to do]")

in_file = sys.argv[1]
out_file = sys.argv[2]
user_changes = sys.argv[3:]  
processor = FileProcessor(in_file, out_file, user_changes)
processor.process()
