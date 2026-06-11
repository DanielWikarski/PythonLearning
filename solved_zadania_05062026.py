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
    lock_combination = list()
    print("Zgadnijmy kod do kłódki rowerowej, podaj 5 cyfr, następnie dostosujemy je w taki sposób, aby ułożyła nam kombinacje:")
    while True: 
        for digit in range(5):
            get_number = (input(f"Podaj cyfrę {digit+1} do kombinacji: "))
            try:
                get_number = int(get_number) # zamieniamy input na inta jeśli możliwe
                lock_combination.append(get_number)
            except:
                if  not isinstance(get_number, int): # jeśli błędny argument, zaczynamy od początku
                    print("[BŁĄD] Podano inną wartość niż liczbę!")
                    print("Wpisz ciąg cyfr od początku...")
                    break
        if len(lock_combination) == 5:
            print(f"Oto twoja kombinacja {lock_combination}")
            break

    
    while True: # tryb sprawdzania kombinacji, będzie trwał aż nie uzyskamy kombinacji spełniających wszystkie kryteria
        for digit in lock_combination: # sprawdzam, czy któraś z cyfr jest większa niż 8 oraz inna niż 0 i 6, jeśli tak - proszę o wpisanie innej liczby i podmieniam ją
            if digit > 8 or digit == 0 or digit == 6:
                while True:
                    wrong_digit_index = lock_combination.index(digit)
                    print(f"Aktualny szyfr: {lock_combination}")
                    new_number = int(input(f"Usunięto liczbę {digit} - Wpisz inną cyfrę w te miejsce! [Cyfra ta nie może być większa od 8, i nie może to być liczba 0 lub 6]: "))
                    if not new_number > 8 and not new_number == 0 and not new_number ==6: # walidacja, czy nowa cyfra pasuje do wymagań
                        lock_combination[wrong_digit_index] = new_number # podmieniam błędną cyfrę na nową cyfrę w kombinacji
                        break
                    else:
                        print(f"Aktualny szyfr: {lock_combination}")
                        print("[BŁĄD] Podano błędną cyfrę - Podaj cyfrę wedle wymagań -> [Cyfra ta nie może być większa od 8, i nie może to być liczba 0 lub 6]:  ")

            if lock_combination.count(digit) == 2:
                print("Znaleziono potwórzenie! - Cyfry w szyfrze nie mogą się powtarzać - ")
                while True:
                    wrong_digit_index = lock_combination.index(digit)
                    print(f"Aktualny szyfr: {lock_combination}")
                    new_number = int(input(f"Usunięto liczbę {digit} - Wpisz inną cyfrę w te miejsce! [Cyfra nie może występować już w szyfrze, każda z cyfr musi być unikatowa]: "))
                    if not new_number == digit:
                        lock_combination[wrong_digit_index] = new_number
                        break
                    else:
                        print(f"Aktualny szyfr: {lock_combination}")
                        print("[BŁĄD] Podano błędną cyfrę - Podaj cyfrę wedle wymagań -> [Cyfra nie może występować już w szyfrze, każda z cyfr musi być unikatowa]: ")

        # Znaleźć sposób, żeby pętla się wykonywała dopóki po każdej iteracji wszystkie wymagania nie zostaną spełnione. Pętla aktualnie sprawdza każdą z opcji, ale tylko raz, jeśli znów będzie błąd w szyfrze algorytm go nie sprawdzi



    print(lock_combination)




    
break_lock()