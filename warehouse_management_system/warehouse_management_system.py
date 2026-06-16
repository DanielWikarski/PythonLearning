import json # w formacie json będę zapisywać dane tj. saldo, produkty, historię operacji etc.
from datetime import datetime # import datetime żeby pobierać datę i czas, będę wrzucał datę i czas wykonanej akcji, do historii wraz z czynnością, która została wykonanna
# nowe!!
with open("data.json", "r", encoding="utf-8") as data: # with open("nazwa_pliku", "r" - r oznacza, że odczytujemy ten plik, encoding="utf-8" - system znaków, dzięki temu mogą występować Polskie znaki, mogę to pominąć, ale jeśli to zrobię to może być błędne odczytywanie polskich znaków ) as nazwa_zmiennej_tymczasowej - w niej będzie zapisywany plik tymczasowo
    # nazwa_zmiennej - nazwa zmiennej, w której ma być zapisany plik = json.load(nazwa_zmiennej) 
    # w tej sposób mogę importować plik json do pythona, który potem będziemy sobie manipulować i na końcu programu jego zmienioną wersje zastępować orginał (po zmianach)
    data = json.load(data)



account_balance = data[0]
warehouse = data[1]
account_history = data[2]


def warehouse_management_system(account_balance,warehouse,account_history):

    while True:
        user_choice_option = str(input("\nWybierz opcje z listy za pomocą komendy: \n\n"
                                "[SALDO]\n"
                                "[SPRZEDAŻ]\n"
                                "[ZAKUP] \n"
                                "[KONTO]\n"
                                "[LISTA]\n"
                                "[MAGAZYN]\n"
                                "[PRZEGLĄD]\n"
                                "[KONIEC]\n\n")).upper()


        if user_choice_option == "SALDO": # moduł sprawdzający stan konta, oraz pozwala na jego modyfikacje
            user_choice_option_balance = str(input(f"\n[FUNKCJA: {user_choice_option}]\n"
                                            "\n---------------------------------------------------------------\n"
                                            f"Aktualne saldo konta: {round(account_balance["account_balance"],2)}zł\n"
                                            "---------------------------------------------------------------\n\n"
                                            f"Wybierz opcje z listy za pomocą komendy: \n\n"
                                            f"[DODAJ]\n"
                                            f"[ODEJMIJ] \n\n")).upper()
            if user_choice_option_balance == "DODAJ":
                balance_modifier_add = (input("\nWpisz wartość do dodania, do salda konta: "))
                try:
                    balance_modifier_add = float(balance_modifier_add)
                except:
                    print("[BŁĄD] Suma musi być liczbą! Wprowadzono niepoprawny tym danych")
                    balance_modifier_add = 0
                account_balance["account_balance"] = round(account_balance["account_balance"],2) + balance_modifier_add
                print(f"\nDodano do salda konta: {balance_modifier_add}zł \n"
                f"Na koncie jest łącznie: {account_balance["account_balance"]}zł")
                account_history[f"{datetime.now()}"] = f"Dodano do salda {balance_modifier_add}zł"
            elif user_choice_option_balance == "ODEJMIJ":
                balance_modifier_subtract = (input("\nWpisz wartość do odjęcia od salda konta: "))
                try:
                    balance_modifier_subtract = float(balance_modifier_subtract)
                except:
                    print("[BŁĄD] Suma musi być liczbą! Wprowadzono niepoprawny tym danych")
                    balance_modifier_subtract = 0
                account_balance["account_balance"] = round(account_balance["account_balance"],2) - balance_modifier_subtract
                print(f"\nOdjęto od salda konta: {balance_modifier_subtract}zł \n"
                f"Na koncie jest łącznie: {round(account_balance["account_balance"],2)}zł")
                account_history[f"{datetime.now()}"] = f"Odjęto od salda {balance_modifier_subtract}zł"
            else:
                print("\n[BŁĄD] Wprowadzoną nieprawidłową komendę\n")
        elif user_choice_option == "KONIEC":
            print("\nZakończono działanie programu, zapisuję wprowadzone zmiany...")
            return account_balance, warehouse, account_history
        elif user_choice_option == "ZAKUP":
            print("\n[FUNKCJA: ZAKUP]")
            print(f"Aktualny stan konta: {account_balance["account_balance"]}")
            user_choice_option_buy_product_name = str(input("\nPodaj nazwę produktu: \n")).upper()
            user_choice_option_buy_product_price =(input("\nPodaj cenę produktu(zł): \n"))
            user_choice_option_buy_product_qty =(input("\nPodaj ilość sztuk produktu: \n"))

            try:
                user_choice_option_buy_product_price = float(user_choice_option_buy_product_price)
                user_choice_option_buy_product_qty = int(user_choice_option_buy_product_qty )
            except:
                pass


            if user_choice_option_buy_product_name.strip() == "" or not isinstance(user_choice_option_buy_product_price, float) or not isinstance(user_choice_option_buy_product_qty, int):
                print("[BŁĄD] Nie wprowadzono danych o produkcie, lub podano je w złej formie. (Cena oraz ilośc muszą być cyfrą)")
            elif user_choice_option_buy_product_price * user_choice_option_buy_product_qty <= account_balance["account_balance"]:
                #odejmuje kase z konta, jak mogę kupić
                account_balance["account_balance"] = account_balance["account_balance"] - (user_choice_option_buy_product_price * user_choice_option_buy_product_qty)


                if user_choice_option_buy_product_name in warehouse:
                    warehouse[user_choice_option_buy_product_name] = {
                        "ILOŚĆ": warehouse[user_choice_option_buy_product_name]["ILOŚĆ"] + user_choice_option_buy_product_qty,
                        "CENA": user_choice_option_buy_product_price
                    }


                else:    
                    warehouse[user_choice_option_buy_product_name] = {
                        "ILOŚĆ": user_choice_option_buy_product_qty,
                        "CENA": user_choice_option_buy_product_price
                    }


                account_history[f"{datetime.now()}"] = f"Zakupiono: {user_choice_option_buy_product_name} | Sztuk: {user_choice_option_buy_product_qty} | Cena jednostkowa: {user_choice_option_buy_product_price}"
                print(f"\nDodano do stanu magazynowego: \n"
                    f"[PRODUKT]: {user_choice_option_buy_product_name}\n"
                    f"[CENA]: {user_choice_option_buy_product_price}zł\n"
                    f"[SZTUK]: {user_choice_option_buy_product_qty}\n"
                    f"ZA ZAKUP ZAPŁACONO: {user_choice_option_buy_product_price * user_choice_option_buy_product_qty}zł")
            else:
                price = user_choice_option_buy_product_price * user_choice_option_buy_product_qty
                print(f"\n[BRAK WYSTARACZAJĄCYCH ŚRODKÓW] \n"
                    f"Aby dokonać zakupu brakuje: {price - round(account_balance["account_balance"],2)}zł")
        elif user_choice_option == "MAGAZYN":
            print(f"\n[FUNKCJA: MAGAZYN]")
            print(f"Aktualny stan magazynu: \n") #printuje stan magazynowy

            for item in warehouse:
                print(f"Produkt: {item}")
                print(f"Ilość dostępna: {warehouse[item]["ILOŚĆ"]}")
                print(f"Cena jednostkowa: {warehouse[item]["CENA"]}")
                print(f"--------------------------------------------")


        elif user_choice_option == "SPRZEDAŻ":
            print(f"\n[FUNKCJA: SPRZEDAŻ]")
            user_choice_option_sales_item = (input("\nPodaj nazwę produktu: \n")).upper()
            user_choice_option_sales_qty =(input("\nPodaj ilość sztuk produktu: \n"))
            try:
                user_choice_option_sales_qty = int(user_choice_option_sales_qty)
            except:
                pass

            if user_choice_option_sales_item.strip() == "" or not isinstance(user_choice_option_sales_qty, int):
                print("[BŁĄD] Podano błędną nazwę produktu lub ilość sztuk produktu")
            
            elif user_choice_option_sales_item in warehouse: # jeśli produkt znajduje się w magazynie
                if warehouse[user_choice_option_sales_item]["ILOŚĆ"] >= user_choice_option_sales_qty: # czy mam wystarczająco sztuk produktu

                        warehouse[user_choice_option_sales_item]["ILOŚĆ"] = warehouse[user_choice_option_sales_item]["ILOŚĆ"] - user_choice_option_sales_qty
                        #zdejmuje ilośc sztuk tego co chce klient
                        account_balance["account_balance"] = account_balance["account_balance"]+ (warehouse[user_choice_option_sales_item]["CENA"]*user_choice_option_sales_qty)
                        # dodajemy kase do konta jak zrobimy sprzedaż
                        print(f"Sprzedano produkt: {user_choice_option_sales_item} | Sztuk: {user_choice_option_sales_qty} | Po cenie jednostkowej: {warehouse[user_choice_option_sales_item]["CENA"]} | Dodano do konta: {(warehouse[user_choice_option_sales_item]["CENA"]*user_choice_option_sales_qty)}zł")
                        print(f"Po wykonanej sprzedaży saldo wynosi: {round(account_balance["account_balance"],2)}zł")
                        account_history[f"{datetime.now()}"] = f"Sprzedano produkt: {user_choice_option_sales_item} | Sztuk: {user_choice_option_sales_qty} | Po cenie jednostkowej: {warehouse[user_choice_option_sales_item]["CENA"]} | Dodano do konta: {(warehouse[user_choice_option_sales_item]["CENA"]*user_choice_option_sales_qty)}zł"
                else:
                    print(f"[BŁĄD] Brak wystarczającej ilości produktu {user_choice_option_sales_item} na stanie magazynowym. Wymagana: {user_choice_option_sales_qty} | Posiadana: {warehouse[user_choice_option_sales_item]["ILOŚĆ"]}")
            else:
                print(f"[BŁĄD] Brak produktu {user_choice_option_sales_item} na stanie magazynowym")
        elif user_choice_option == "KONTO":
            print(f"\n[FUNKCJA: KONTO]\n")
            print("----------------------------------------------------------------")
            print(f"AKTUALNY STAN KONTA: {account_balance["account_balance"]}zł")
            print("----------------------------------------------------------------")

        elif user_choice_option == "LISTA":
            print(f"\n[FUNKCJA: LISTA OPERACJI]")
            if len(account_history) == 0: #wyrzucam błąd jak nic nie zrobiłem, żadnych akcji w historii
                print("Brak zarejestrowanych operacji.")
            else:
                for event in account_history: # za pomocą for wyprintuje każdy event z historii
                    print(f"{"-"*len(event+account_history[event])}")
                    print(f"- {event} : {account_history[event]}")

        elif user_choice_option == "PRZEGLĄD":
            print(f"\n[FUNKCJA: PRZEGLĄD]")
            print(f"W systemie jest łącznie {len(account_history)} operacji.\n")

            print("[BRAK WPISANYCH DANYCH WYŚWIETLA CAŁĄ HISTORIĘ]")
            from_timeline= str(input("Podaj początek przedziału daty do sprawdzenia operacji (format: YYYY-MM-DD)"))
            to_timeline = str(input("Podaj koniec przedziału daty do sprawdzenia operacji (format: YYYY-MM-DD)"))

            print(f"Operacje w przedziale czasowym od {from_timeline} do {to_timeline}")
            for event in account_history:
                if from_timeline in event or to_timeline in event:
                    print(f"{"-"*len(event+account_history[event])}")
                    print(f"{event} : {account_history[event]}")
        else:
             print("\n[BŁĄD] Wprowadzoną nieprawidłową komendę\n")
        


new_data =warehouse_management_system(account_balance, warehouse, account_history)
# nowe!!!
# tym  sposobem znów na koniec odpalamy nasz plik json z danymi, a potem podmieniam dane, które dam są z danymi, które zwróciła nam funkcja
with open("data.json", "w", encoding="utf-8") as data:
    json.dump(new_data, data, indent = 4, ensure_ascii = False ) # za pomocą json.dump(nazwa_nowych_danych, zmienna tymczasowa z odpalania pliku (wyżej ją napisałem jako as nazwa_zmiennej_tymczasowej), indent = 4 -tutaj mówimy, żeby python z jsonie powstawiał odstępy, jak tego nie  zrobię, to w json będzie wszystko "spłaszczone", ensure_ascii = False - żeby brało polskie znaki) 

