from pprint import pprint
import datetime
import csv
## Zadanie 1 

# with open("data/notatki.txt", mode="r", encoding="UTF-8") as f:
#     content = f.read()

# content = content.split()


# content_word_count = 0
# content_word_count_long_ones = 0
# for word in content:
#     content_word_count +=1
#     if len(word) > 4:
#         content_word_count_long_ones +=1



# print(f"W tekście jest {content_word_count} słów, z czego {content_word_count_long_ones} ma więcej niż 4 litery!")

# ## Zadanie 2

# with open("data/liczby.txt", mode="r", encoding="UTF-8") as f:
#     line = 0
#     list_of_numbers = list()
#     for element in f:
#         line += 1
#         try:
#             element = int(element)
#             list_of_numbers.append(element)
#         except:
#              print(f"{element} nie jest liczbą, błąd w linii {line}")




# # Liczby parzyste z listy liczb dodaje do nowego pliku
# list_of_numbers_even = list()
# for number in list_of_numbers:
#     if number % 2 ==0:
#         list_of_numbers_even.append(number)


# with open("data/parzyste.txt", mode="w", encoding="UTF-8") as f:
#     for number in list_of_numbers_even:
#         f.write(str(number)+"\n")

# # Liczby nieparzyste
# list_of_numbers_odd = list()
# for number in list_of_numbers:
#     if number % 2 !=0:
#         list_of_numbers_odd.append(number)

# print(f"Suma liczb nieparzystych występujących w pliku: {len(list_of_numbers_odd)}")

## Zadanie 3

# with open("data/dziennik.txt", mode="r", encoding="UTF-8") as f:
#     events = f.read()
# events = events.split("\n")

# liczniki = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
# ostatnie = {}


# for event in events:
#     if "INFO" in event:
#         liczniki["INFO"] += 1
#         ostatnie["INFO"] = event
#     elif "WARNING" in event:
#         liczniki["WARNING"] += 1
#         ostatnie["WARNING"] = event
#     elif "ERROR" in event:
#         liczniki["ERROR"] +=1
#         ostatnie["ERROR"] = event

# log_stats = (
#     f"\n---Podsumowanie logów---\n"
#     f"INFO: {liczniki['INFO']} | WARNING: {liczniki['WARNING']} | ERROR: {liczniki['ERROR']}\n"
#     f"Data importu logów: {datetime.datetime.now().strftime('%d/%m/%Y | %H:%M')}\n"
#     f"----------------------\n"
# )

# print(log_stats)

# with open("data/dziennik.txt", mode="a", encoding="UTF-8") as f:
#     f.write(log_stats)


## Zadanie 4
# mature_people = []
# with open("data/osoby.csv", mode="r", encoding="UTF-8") as f:
#     people = csv.DictReader(f, delimiter=";") # deserializacja

#     for person in people:
#         if int(person["wiek"]) >=18:
#             mature_people.append(person)


# mature_people_age_sorted = sorted(mature_people, key=lambda person: person["wiek"]) # sortowanie względem wieku, key=lambda, gdzie sprawdzany jest tylko klucz "wiek" z każdego obiektu person


# with open("data/pelnoletni.csv", mode="w", encoding="UTF-8", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["imie", "nazwisko", "wiek", "miasto"]) # serializacja
#     writer.writeheader()
#     writer.writerows(mature_people_age_sorted)


## Zadanie 5


with open("data/osoby.csv", mode="r", encoding="UTF-8") as f:
    people = csv.DictReader(f, delimiter=";")
    miasta = {}
    for person in people:
        if person["miasto"] in miasta:
            miasta[person["miasto"]] +=1
        else:
            miasta[person["miasto"]] =1

miasta_popularity_sorted = dict(sorted(miasta.items(), key=lambda miasto: miasto[1], reverse=True)) # żeby posortować słownik, musimy uzyć dict na początku i następnie przy pierwszym argumencie (tam, gdzie wrzucamy co chcemy sortować, nazwa zmiennej) daje items() żeby sortowało po każdej parze klucz:wartość,
# miasto[1], bo sortuje tylko po liczbie mieszkańców z danego miasta, reverse=True, żeby pokazywało od największego do najmniejszego

miasta_most_popular = list(miasta_popularity_sorted)[0] # żeby wydobyć pierwszy klucz to zamieniam słownik na listę i biorę pierwszy(0) index, tutaj dostaniemy pierwsze miasto z największą liczbą mieszkańców ze zmiennej miasta_popularity_sorted

with open("data/statystyki_miast.txt", mode="w", encoding="UTF-8") as f:
    for miasto in miasta_popularity_sorted:
        writer = f.write(f"{str(miasto)} : {miasta_popularity_sorted[miasto]} mieszkańców\n")
    writer = f.write(f"Najbardziej popularne miasto to {miasta_most_popular} z liczbą mieszkańców: {miasta_popularity_sorted[miasta_most_popular]}")
