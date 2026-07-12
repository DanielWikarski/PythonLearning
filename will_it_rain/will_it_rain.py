import datetime
import requests
import os
import json
cwd = os.getcwd()




with open("queries_results.json", mode="r", encoding="UTF-8") as f:
    queries_results = json.load(f)



# dane dla Białegostoku
latitude = 53.1426772999997
longitude = 23.131738654996585

def date_validator(date_arguments)-> str:
    try:
        date_arguments_str = datetime.datetime.strptime(f"{date_arguments[0]}-{date_arguments[1]}-{date_arguments[2]}", "%Y-%m-%d")
        date_arguments_formated = date_arguments_str.strftime("%Y-%m-%d")
    # walidacja daty, jeśli np. jest 7 miesiąc, to zrobi się z tego 07, API przyjmuje format 07 jako miesiąc a nie 7.
    # Dodatkowo jeśli będzie wpisana błędna data, np. 31 luty, to wyrzuci błąd daty
        return date_arguments_formated
    except:
        raise Exception("Błąd daty, taka data nie istnieje!")
    

def rain_possibility(weather_data: list):
    possibility = [hour+hour for hour in weather_data]
    if sum(possibility) == 0: # nie pada
        return f"Nie będzie padać"
    elif sum(possibility) > 0: # będzie padać
        return f"Będzie padać"
    else: # błędny response, brak wyniku ze strony API lub wynik ujemny
        return f"Nie wiadomo, nie udało się sprawdzić danych"


def get_weather_data_rain(latitude, longitude, searched_date):
    try:
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}")
        response = response.json()
        response = response["hourly"]["rain"]
        return response
    except:
        raise Exception("Wprowadzone dane są poza możliwościami wyszukiwania [BŁĄD DATY LUB ZBYT ODLEGŁA]")





def main_app():
    
    print("Sprawdźmy czy będzie padać!")
    print("---------------------------")
    date_arguments = input(f"Wpisz datę w formacie YYYY-MM-DD (np: 2026-07-10), a ja sprawdzę czy danego dnia będzie padać -> ").split("-")


    try:
        if len(date_arguments) !=1:
            date_arguments = [int(argument)for argument in date_arguments]
            
    except:
        raise ValueError("Podano błędne dane wejściowe, dane muszą być liczbami!")


    if len(date_arguments) == 3:
        print("Sprawdzam pogodę...")
        date_arguments_formated = date_validator(date_arguments)
        for querry in queries_results:
            if querry == date_arguments_formated:
                print(f"Wynik wyszukiwania znajduje się już w bazie: DATA: {querry} | WERDYKT: {queries_results[querry]}")
                return querry,queries_results[querry]
        weather_data = get_weather_data_rain(latitude, longitude, date_arguments_formated)
        rain_possibility_data = rain_possibility(weather_data)
        print(rain_possibility_data)
        return rain_possibility_data, date_arguments_formated
    elif len(date_arguments) == 1:
        tomorrow_date = datetime.date.today()+datetime.timedelta(days=1) # nowe!! timedelta(days=x) możemy zrobić delay na dacie i nie tylko (np. godzina itp.)
        print(f"Nie podano daty, sprawdzam pogodę na jutro ({tomorrow_date})...")
        for querry in queries_results:
            if querry == str(tomorrow_date):
                print(f"Wynik wyszukiwania znajduje się już w bazie: DATA: {querry} | WERDYKT: {queries_results[querry]}")
        weather_data = get_weather_data_rain(latitude, longitude, tomorrow_date)
        rain_possibility_data = rain_possibility(weather_data)
        print(rain_possibility_data)
        return rain_possibility_data, tomorrow_date
    else:
        raise Exception(f"Wymagane są 3 argumenty - podano: {len(date_arguments)}")








####################################### part 2 zadania ################################################################################

class WeatherForecast():
    # inicjator klasy, co dzieje się podczas inicjowania instancji klasy
    def __init__(self) -> None:
        self.queries_results_file = "queries_results.json" # nazwa pliku do pobrania
        self.queries_results = dict() # tutaj będę przetrzymywał to co przejmiemy z pliku

        # próbujemy pobrać plik json i go otworzyć
        try:
            with open(self.queries_results_file, mode="r", encoding="UTF-8") as f:
                self.queries_results = json.load(f) # do słownika, który zrobiłem wyżej zapisuje to co zwrócił mi json podczas deserializacji
        except FileNotFoundError: # jeśli nie znajdziei pliku, to idziemy dalej - nie jest nam on potrzebny jeśli user używa aplikacji pierwszy raz, finalnie i tak doprowadzimy do zrobienia nowego pliku
            print(f"[INFO] Nie znaleziono pliku {self.queries_results_file}, tworzę nową bazę danych.")
        

    def __setitem__(self, date, rain_possibility_data): # definiuję zachowanie instacji w przypadku jakbyśmy traktowali ją jak słownik -  instancja klasy zachowuje się jak słownik i jak wpiszę wf["2026-07-13"] = "pada" to doda dokładnie te dane do pliku queries_results.json, lecz tak na prawde jest
        # ona potrzebna do __getitem__, żeby móc potem przypisać wyniki które otrzymamy do pliku json
        self.queries_results[date] = rain_possibility_data
        with open(self.queries_results_file, mode="w", encoding="UTF-8") as f:
            json.dump(self.queries_results,f,ensure_ascii=False, indent=4)

    def __getitem__(self, date): # definiuje zachowanie instacji, jeśli podamy klucz, np jak zrobimy wf["2026-07-13"] ma to nam zwrócić wartość, którą możemy potem zapisać do zmiennej. Przepytujemy instacje, czy ma w sobie dany klucz, jeśli nie - to odwołujemy się do API.
        if date in self.queries_results: # sprawdzam czy data jest w słowniku z danymi
            print(f"Wynik wyszukiwania znajduje się już w bazie: DATA: {date} | WERDYKT: {self.queries_results[date]}")
            return self.queries_results[date] # zwracam werdykt dla daty
        else: # jeśli nie - odpalam funkcję, która pobiera dane pogodowe z API, następnie z dane z tej funkcji przekazuje do kolejnej funkcji, która ustala na podstawie tych danych, czy będzie padało, czy też nie.
            weather_data = get_weather_data_rain(latitude, longitude, date) # pobranie danych pogodowych z  API
            rain_possibility_data = rain_possibility(weather_data) # sprawdzanie na podstawie danych werdyktu
            self[date] = rain_possibility_data # pobrane dane przypisuje do instancji, powoduje to jednoczesnym zapisaniem danych do pliku json, stąd definiowaliśmy zachowannie przypisania
            return rain_possibility_data # zwracam werdykt dla daty

    def __iter__(self):  # umożliwiamy iterowanie po instancji, definiujemy zachowanie, jeśli user będzie chciał przeiterować przez nią - czyli co ma się zadziać
        for data in self.queries_results: # ma się zrobić pętla for
            yield data # ma zwrócić daty znane już w pliku json

    def items(self):
        for data in self.queries_results:
            yield data, self.queries_results[data]
wf = WeatherForecast()

