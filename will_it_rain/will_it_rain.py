import datetime
import requests
import os
import json
cwd = os.getcwd()



print("Sprawdźmy czy będzie padać!")
print("---------------------------")
date_arguments = input(f"Wpisz datę w formacie YYYY-MM-DD (np: 2026-07-10), a ja sprawdzę czy danego dnia będzie padać -> ").split("-")

with open("queries_results.json", mode="r", encoding="UTF-8") as f:
    queries_results = json.load(f)



# dane dla Białegostoku
latitude = 53.1426772999997
longitude = 23.131738654996585

def date_validator()-> str:
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



try:
    if len(date_arguments) !=1:
        date_arguments = [int(argument)for argument in date_arguments]
            
except:
    raise ValueError("Podano błędne dane wejściowe, dane muszą być liczbami!")

def main_app():
    if len(date_arguments) == 3:
        print("Sprawdzam pogodę...")
        date_arguments_formated = date_validator()
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
                return querry,queries_results[querry]
        weather_data = get_weather_data_rain(latitude, longitude, tomorrow_date)
        rain_possibility_data = rain_possibility(weather_data)
        print(rain_possibility_data)
        return rain_possibility_data, tomorrow_date
    else:
        raise Exception(f"Wymagane są 3 argumenty - podano: {len(date_arguments)}")


results = main_app()
queries_results[str(results[1])] = results[0]

with open("queries_results.json", mode="w", encoding="UTF-8") as f:
    json.dump(queries_results,f,ensure_ascii=False, indent=4)


