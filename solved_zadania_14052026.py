# Zadanie 1

print("=== Zadanie 1 ===")
user_age = int(input("Podaj swój wiek: "))

if user_age < 12:
    print("Możesz obejrzeć tylko bajkę")
elif 12 <= user_age <= 17:
    print("Czy masz zgodę rodzica? (T/N <- Wpisz T - TAK / N - NIE)")
    parent_signature = str(input().upper())
    if parent_signature == "T":
        print("Możesz wejśc na film")
    else:
        print("Możesz obejrzeć tylko bajkę")
else:
    print("Możesz obejrzeć dowolny film")

# Zadanie 2

print("=== Zadanie 2 ===")


books_read = int(input("Ile książek przeczytał_ś w tym miesiącu? "))

if not books_read:
    print("Musisz zacząć czytać!")
elif 1 <= books_read <= 3:
    print("Dobry początek")
else:
    print("Super! Jesteś molem książkowym")


# Zadanie 3

print("=== Zadanie 3 ===")


current_temperature = int(input("Podaj aktualną temperature (w stopniach celsjusza): "))

if  current_temperature < 0:
    print("Jest mróz, ubierz czapkę!")
elif 0 <= current_temperature <= 15:
    print("Jest chłodno, załóż kurtkę.")
else:
    print("Ciepło, możesz iśc w koszulce")

# Zadanie 4

print("=== Zadanie 4 ===")

users_pet = str(input("Jakie masz zwierze? (pies / kot / rybka): "))

if users_pet == "pies":
    users_pet_dog_question = str(input("Czy lubisz chodzić na spacery? (T/N <- Wpisz T - TAK / N - NIE) ").upper())
    if users_pet_dog_question == "T":
        print("Twój pies będzie szczęśliwy!")
    else:
        print("Pies potrzebuje ruchu!")
elif users_pet == "kot":
    print("Kot lubi drapanie i spanie")
elif users_pet == "rybka":
    print("Pamiętaj o czystej wodzie!")
else:
    print("Nie znam takiego zwierzaka...")


# Zadanie 5

print("=== Zadanie 5 ===")

product_price = float(input("Podaj cenę produktu: "))

product_price_feedback = "Drogi" if product_price > 100 else "Tani" # Użycie ternary, jednolinijkowy warunek
# utworzyłem zmienną product_price_feed_back i w niej zapisałem warunek, na podstawie tego warunku
# zmienna ta będzie miała wartość "Drogi" lub "Tani"
print(product_price_feedback)

# Zadania part II
# Zadanie 1

print("=== Zadanie 1 part II ===")


user_password = input("Wpisz hasło: ")
user_password_is_valid = True

if len(user_password) < 8 :
    print("BŁAD: Hasło jest za krótkie, powinno zawierać minimum 8 znaków!")
    user_password_is_valid = False
if  user_password[0].isdigit():
    print("BŁAD: Pierwszy znak hasła nie może być cyfrą!")
    user_password_is_valid = False
if user_password.find("!") >= -1 or user_password.find("?") >=-1:
    print("BŁAD: W haśle musi znajdować się znak specjalny '? lub '!")
    user_password_is_valid = False
if user_password[0] == user_password[-1]:
    print("BŁAD: Hasło nie może zaczynać się i kończyć tym samym znakiem")
    user_password_is_valid = False
if user_password_is_valid:
    print("Hasło poprawne :) ")


# Zadanie 2 part II

print("=== Zadanie 2 part II ===")




user_text_input = input("Wpisz dowolny tekst: ")
user_text_input_is_valid = True
if not user_text_input.startswith("@"):
    print("Tekst NIE zaczyna się od @!")
    user_text_input_is_valid = False
if not user_text_input[-1].isdigit():
    print("Tekst NIE kończy się liczbą!")
    user_text_input_is_valid = False
if not user_text_input[len(user_text_input) // 2]  == "x":
    print("Środkowy znak tekstu NIE zawiera w sobie 'x'!")
    user_text_input_is_valid = False

# Dodatkowe utrudnienie :)
input_lenght = len(user_text_input)
input_center = input_lenght // 2
if input_lenght % 2 == 0:
    if not user_text_input[input_center] == "x" and not user_text_input[input_center - 1] == "x":
        #Tutaj sprawdziłem, czy x jest dokładnie po środku lub w tym przypadku jak jest parzyście, to czy obok środka
        # jest ten 'x'
        print("Środkowe znaki tekstu NIE zawierają w sobie 'x'!")
        user_text_input_is_valid = False
else:
    if not user_text_input[input_center] == "x":
        print("Środkowy znak tekstu NIE zawiera w sobie 'x'!")
        user_text_input_is_valid = False
if user_text_input_is_valid:
    print("Wiadomośc przyjęta!")


# Zadanie 3 part II

print("=== Zadanie 3 part II ===")


user_nickname = input("Wpisz swój nick: ")
user_nickname_hash_count = 0
user_nickname_is_valid = True

for letter in user_nickname:
    if letter == "#":
        user_nickname_hash_count += 1


if not user_nickname_hash_count == 1:
    user_nickname_is_valid = False
    print("BŁĄD: Nick musi zawierać znak '#'")
if not user_nickname.find("#") >= 3:
    user_nickname_is_valid = False
    print("BŁAD: Brak trzech znaków poprzedzających znak '#'")
if not user_nickname[user_nickname.find("#")+1::].isdigit():
    user_nickname_is_valid = False
    print("BŁAD: Częśc nicku po znaku '#' powinna składać się wyłącznie z cyfr!")
if  not len(user_nickname[user_nickname.find("#")+1::])  == 3:
    user_nickname_is_valid = False
    print("BŁAD: Ostanie trzy znaki nicku muszą być cyframi!")
if not user_nickname == user_nickname.title():
    user_nickname_is_valid = False
    print("BŁAD: Pierwszy znak nicku ma być z wielkiej litery!")
if user_nickname_is_valid:
    print("Nick poprawny")





















