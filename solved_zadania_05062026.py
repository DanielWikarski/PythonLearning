import random # moduł wartości pseudolosowych
import math # moduł matematyczny np. do obliczania pierwiastka z liczby etc.
import statistics # moduł statystyczny, mogę nim np. wyliczyć średnią arytmetyczną, geometryczną itp.
import string # moduł string - moduł zawierający w sobie wszystkie litery, cyrfy, znaki etc.
# === Zadanie 1 ===



people = [
        ('Basia', 23),
        ('Ania', 19),
        ('Katarzyna', 27),
        ('Ola', 21),
        ('Tomek', False, 30)
    ]




#print(sorted(people, key=lambda person: len(person[0])))
                            #  element: długość(element[każdy pierwszy indeks z tupli]) 
                            # ta funkcja iterujej przez listę z tuplami, pod person podstawia się każda z tupli, potem z elementu tupli (każdy person) bierzemy pierwszy indeks do sortowania
# sortowanie za pomocą klucza lambda (funkcji)




# === Zadanie 2 ===




#password_len = int(input("Podaj długośc hasła: "))
#has_punctuation = str(input("Czy hasło ma zawierać znak specjalny? \n"
#                            "[TAK/NIE]")).upper().strip()

def generate_password(password_len: int, has_punctuation: str) -> str: # funkcja generująca hasło
        generated_password = ""

        for letter in range(password_len): # wrzucamy losowe litery
            random_letter = random.choice(string.ascii_letters)
            generated_password += random_letter
        if has_punctuation == "TAK": # wrzucamy losowy znak specjalny
            generated_password = generated_password[0:password_len-1] # jeśli user chce znak specjalny to zmniejszam ilośc liter, aby mógł być dodany znak bez zwiększania długości hasła
            generated_password += random.choice(string.punctuation)
        elif has_punctuation == "NIE":
            pass

        else:
            print("[Wpisano błędną komendę! - Hasło zostanie stworzone bez "
                  "użycia znaku specjalnego]")



        generated_password_as_list = list()
        # robię listę, żeby móc zrobić shuffle na niej
        for symbol in generated_password:
            generated_password_as_list.append(symbol)

        random.shuffle(generated_password_as_list)

        generated_password = "".join(generated_password_as_list)
        # zshufflowaną listę łączę ponownie w stringa
        return generated_password


#password = generate_password(password_len, has_punctuation)

# print(f"Twoje utworzone hasło to: {password}")





# === Zadanie 3 ===

people = [
        ('Basia', 23),
        ('Ania', 19),
        ('Katarzyna', 27),
        ('Ola', 21),
        ('Tomek', False, 30)
    ]

#print(sorted(people, key=lambda person: person[-1])) 
# w tej funkcji lambda każdorazowo bierze ona ostatnią wartość tupli do sortowania, gdzie person to każda tupla z listy, [-1], bo biorę sortowanie na podstawie wieku



# === Zadanie 4 ===



def sorting_numbers (*numbers): # *numbers, bo * oznacza, że możemy do funkcji wrzucić dowolną liczbę elementów
    odd_numbers = list()
    even_numbers = list()

    

    for number in numbers:
        if isinstance(number, bool):
            try:                        # tutaj jeśli pojawi się bool, to try spróbuje przerobić to na stringa, żeby nie brało tego, jako inta do listy
                number = str(number)
            except:
                pass
        if isinstance(number, int):



            if number % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
        else:
            pass
    print(odd_numbers, even_numbers)
    return odd_numbers, even_numbers






# === Zadanie 5 ===

def is_number_narcisstic(number: int) -> bool: # funkcja sprawdza czy liczba jest narcystyczna (suma cyfr podniesionych do potęgi długości tej liczby jest równa wartości tej liczby.) - zwraca bool -
    number_as_string = str(number) # przerabiamy liczbę na stringa, aby móc po niej iterować
    number_as_list = list()
    for digit in number_as_string: # iterujemy po liczbie i bierzemy z niej każdą cyfrę pokolei, następnie dodajemy ją do listy, jednocześnie zamieniamy na inta z powrotem
        digit = int(digit)
        number_as_list.append(digit)



    number_as_list_lenght = len(number_as_list) # sprawdzamy ile jest cyrf w naszej liczbie (długość listy)

    number_powered_sum: int = 0 # tutaj będziemy wrzucam spotęgowane cyfry z liczby
    for digit in number_as_list:
        number_powered_sum += digit**number_as_list_lenght

    if number_powered_sum == number:
        return True
    else:
        return False


# === Zadanie 6 ===


def narc_num_from_range(range_min:int, range_max:int) -> list:

    if isinstance(range_min, int) and isinstance(range_min, int): # walidacja, czy zakres jest tylko z liczb całkowitych


        if range_min > range_max: # walidacja czy początek zakresu nie jest większa niż jego maksymalna wartość, inaczej - podnieś błąd
            print("[BŁĄD ZAKRESU] Początek zakresu nie może być większy niż jego maksymalna wartość")

        narcisstic_num_list = list()

        for number in range(range_min, range_max+1): # bierzemy wszystkie liczby z zakresu od minimalnego do maksymalnego (+1, żeby brało też pod uwagę max range włączając)
            if is_number_narcisstic(number):    # wywołuje funkcje, którą napisałem w zadaniu 5 - sprawdza każdą liczbę z zakresu, zwraca bool na podstawie czy liczba jest narcystyczna
                narcisstic_num_list.append(number) # dodaje liczbę do listy, jeśli jest narcystyczna
            else:
                continue
    
        return narcisstic_num_list




    else:
        print("[BŁĄD ZAKRESU] Zakres powinien składać się tylko z liczb całkowitych!") # podnosi błąd, jeśli zakres jest wyrażony w zły sposób



# === Zadanie 7 ===



def guess_number(range_min, range_max):
    mystery_number = random.randint(range_min, range_max+1) # tutaj losujemy naszą tajemniczą liczbę z przedziału, włączając w to maks zakres
    player_attempts = 1

    while not player_attempts == 5:
        print(f"Odgadnij liczbę z przedziału od {range_min} do {range_max}... ")
        print(f"To twoje {player_attempts} podejście, pozostało {5-player_attempts} prób")
        player_guess = int(input(f"Twoj strzał to? -> "))

        if player_guess > mystery_number:
            print("Podał_ś zbyt dużą liczbę, spróbuj ponownie")
            player_attempts += 1
        elif player_guess < mystery_number:
            print("Podał_ś zbyt małą liczbę, spróbuj ponownie")
            player_attempts += 1
        elif player_guess == mystery_number:
            print(f"Gratulacje, strzał w dziesiątkę! Udało Ci się tego dokonać po następującej liczbie prób: {player_attempts} ")
            return
        elif range_min > player_guess > range_max:
            print("[BŁĄD] Podana liczba jest z poza zakresu!")
    if player_attempts == 5:
        print("Niestety nie udało Ci się, może następnym razem? ;)")        


# === Zadanie 8 ===



def quadratic_equation_root(a:int, b:int, c:int):
    delta:int
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)): # walidacja, czy wszystkie argumenty są liczbami
        print("Wszystkie argumenty muszą być liczbami!")
        return


    elif a == 0: # sprawdzam czy a=0, jeśli tak to funkcja jest liniowa
            print("Ta funkcja jest liniowa")
            return

    else: # w przeciwnym razie przechodzimy do wyliczania delty
        delta = (b**2)-(4*a*c)
        if delta > 0:
            # wyliczam pierwiastki wedle wzoru dla x1 i x2
            x1 = (-b-math.sqrt(delta)) / (2*a)
            x2 =(-b+math.sqrt(delta)) / (2*a)
            print(f"Delta ma dwa różne pierwiastki: x1 = {x1} oraz x2 = {x2}")
            return x1, x2

        if delta == 0: 
            x0 = -b/(2*a)
            print(f"Delta ma tylko jeden pierwiastek x0= {x0}")
            return x0
        
        if delta < 0:
            print("Delta nie ma pierwiastków")
            return None



# === Zadanie 9===



def calc_mean(*args) -> float:
    numbers_set = list()
    while True:
        print("[KOMENDA (koniec) ZAKAŃCZA DODAWANIE DANYCH]")
        number =(input("Podaj liczbę do zbioru, z której wyliczymy średnią: "))

        if number == "koniec":
            break

        
        if not isinstance(number, float):
            try:
                number = float(number)
                numbers_set.append(number)
            except:
                print("[BŁĄD] Podana wartość nie jest wartością numeryczną!")


    print(f"Jakim sposobem chcesz wyliczyć średnią z podanych liczb? {numbers_set} \n")
    print((f"[ŚREDNIA ARYTMETYCZNA(1)]\n"))
    print((f"[ŚREDNIA GEOMETRYCZNA(2)]\n"))
    print((f"[ŚREDNIA HARMONICZNA (3)]\n"))
    while True:                      
        mean_pick = (input(f"Wpisz cyfrę aby wybrać: "))

        try: # konwertujemy input do inta jeśli jest taka możliwość
            mean_pick = int(mean_pick)
        except:
            pass

        if mean_pick == 1:
            # zaimportowałem moduł statistics, gdzie możemu użyć funkcji mean() gdzie wylicza ona średnią arytmetyczą ze zbioru liczb
            arithmetic_mean = statistics.mean(numbers_set)
            print(f"Średnia arytmetyczna ze zbioru liczb {numbers_set} to: {round(arithmetic_mean,2)}")
            print("[Wynik jest zaokrąglony do dwóch miejsc po przecinku]")
            return arithmetic_mean
    
        elif mean_pick == 2:
            # tutaj z modułu statistics używam geometric mean aby wyliczyć średnią geometryczną
            geometric_mean = statistics.geometric_mean(numbers_set)
            print(f"Średnia geometryczna ze zbioru liczb {numbers_set} to: {round(geometric_mean,2)}")
            print("[Wynik jest zaokrąglony do dwóch miejsc po przecinku]")
            return geometric_mean

        elif mean_pick == 3:
            harmonic_mean = statistics.harmonic_mean(numbers_set)
            print(f"Średnia harmoniczna ze zbioru liczb {numbers_set} to: {round(harmonic_mean,2)}")
            print("[Wynik jest zaokrąglony do dwóch miejsc po przecinku]")
            return harmonic_mean
        else: # podnosimy błąd, wracamy do ponownego wyboru
            print("[BŁĄD] Niepoprawna komenda!")
  

# === Zadanie 10 ===

def break_lock():

    while True:
        lock_combination = random.sample(range(1,8),5) # random.sample() NOWOŚĆ! Zwraca unikalną liste, w środek możemy wrzuić range, żeby zrobić listę liczb z przedziału range.
        digits_sum = sum(lock_combination)

        if digits_sum == 21 and lock_combination[-1]%2==1 and  not 6 in lock_combination: # walidacja do jakiego momentu ma nam szukać kombinacji
            break

    print(f"Oto Twoja kombinacja: {lock_combination}")

#break_lock()


# === Zadanie 11 ===

#number = (input("Wpisz liczbę, a ja sprawdzę, czy podana to liczba to liczba pierwsza: "))
def is_number_prime(number:int):
    try:
        number = int(number) # Próba konwersji inputa na insta
    except:
        print("[BŁĄD] Podana wartość nie jest liczbą!") # jeśli się nie powiedzie, podnosimy feedback i program kończy pracę
        return
    if not number >= 2: # walidacja czy liczba jest większa lub równa 2
        print("[BŁĄD] Liczby mniejsze niż 2 nie mogą być liczbami pierwszymi!")

    else:
        for num in range(2,number): # iteracja przez wszystkie liczby w zakresie od 2 do argumentu liczby przyjętego od użytkownika
            if  number % num == 0: # zwraca false, jeśli liczba nie jest pierwsza
                return False

        is_prime = True
        return is_prime # funkcja zwróci wartość True, jeśli liczba jest pierwsza




# range_min = input("Wpisz początek zakresu: ")
# range_max = input("Wpisz koniec zakresu: ")
def prime_in_range(range_min, range_max):
    prime_numbers_list = list()
    try:
        range_min = int(range_min)
        range_max = int(range_max)
    except:
        print(f"[BŁĄD] Dane wejściowe niepoprawne, zakres musi być wyrażony liczbą całkowitą!")
        return
    
    if range_min > range_max:
        print("[BŁĄD] Błędny zakres, minimalny zakres nie może być większy niż jego maksymalna wartość!")
        return
    
    for number in range(range_min, range_max+1): # iteruje po zakresie 
        if is_number_prime(number): # używam funkcji, którą napisałem wyżej do określenia, czy dana liczba jest pierwsza, jeśli funkcja zwróci True - to jest liczba pierwsza
            prime_numbers_list.append(number)
    return prime_numbers_list # funkcja zwraca listę liczb pierwszych



# === Zadanie 13 ===


# text = (input("Wpisz dowolny tekst, a ja zliczę liczbę: \n"
# "[LITER]\n" \
# "[CYFR]\n" \
# "[SPACJI]\n" \
# "------------------------\n" \
# "Twój tekst: "))

def check_text_elements(text):
    letter_count = 0
    digits_count = 0
    spaces_count = 0

    for element in text:
        if element == " ": # jeśli jest blanc space, to dodajemy zliczenia pusty miejsc
            spaces_count +=1

        try:
            element = int(element) # próbujemy każdy element przerobić na inta, żeby sprawdzić czy dany element może być intem
            digits_count +=1
        except:
            continue # jeśli nie - nie podnoś błędu
        finally:
                if not isinstance(element,int) and not element == " " and not element in string.punctuation: # finalnie jeśli element nie jest intem, pustym miejscem i nie znajduje się w zbiorze elementów punctuation (znaki specjalne), to zaliczamy go do liter
                    letter_count +=1

    print(f"W tekście {text} znajduje jest: \n" \
        f"[LITER: {letter_count}]\n" \
        f"[CYFR: {digits_count}]\n" \
        f"[SPACJI {spaces_count}]\n" \
        "------------------------\n" \
          )



# === Zadanie 14 ===


def remove_duplications(item_list:list):

    duplicate_free_list = list() # nowa, czysta lista
    for item in item_list:
        if item_list.count(item) >=2 and item not in duplicate_free_list: # jeśli coś się powtarza i nie ma go w nowej liście, to go dodajemy
            duplicate_free_list.append(item)

        if item_list.count(item) ==1 and item not in duplicate_free_list: # jeśli jest tylko jedna sztuka itemu oraz nie ma go na liście, to go dodajemyt
            duplicate_free_list.append(item)
        

    return duplicate_free_list # funkcja zwraca listę bez duplikatów




# === Zadanie 15 ===

def shopping_basket():
    basket= {}
    basket_sum = 0
          
    while True:
        user_choice = int(input("Wybierz komendę: \n" \
        "[DODAJ PRODUKT][1]\n" \
        "[ZAKOŃCZ  DODAWANIE PRODUKTÓW][2]\n"
        "--> "))

        if user_choice == 1:

            new_item_name =(input("Wprowadź nazwę produktu, który wkładasz do koszyka: "))
            print("---------------------------------------------------------------------")
            new_item_price =((input("Wprowadź cenę produktu, który wkładasz do koszyka: ")))
            print("---------------------------------------------------------------------")

            try:
                new_item_price = float(new_item_price)
            except:
                print("[BŁĄD] Cena produktu musi być liczbą! - Powrót do menu głównego...\n")

            if isinstance(new_item_price,float):
                if new_item_price <=0:
                    print("[BŁĄD] Cena produktu musi być wartością dodatnią! - Powrót do menu głównego...\n")
            
                else:
                    basket[new_item_name] = new_item_price


        if user_choice == 2:
            print("[ZAKOŃCZONO DODAWANIE PRODUKTÓW DO KOSZYKA]")
            
            for item in basket:
                basket_sum =+ basket[item]

            print("Lista zakupionych produktów: \n")

            # ogarnąć printowanie listy produktów






            print(f"Łączna suma zakupów: {basket_sum}zł")
            print("=====================================")
            return



shopping_basket()




