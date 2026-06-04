students_list = {
}

teachers_list = {

}

educators_list = {
}



# testowe dane

students_list = {
    "JAN_NIEZBĘDNY": {
        "IMIE_UCZNIA": "JAN",
        "NAZWISKO_UCZNIA": "NIEZBĘDNY",
        "KLASA_UCZNIA": "1C"
    },
    "ANNA_WANNA": {
        "IMIE_UCZNIA": "ANNA",
        "NAZWISKO_UCZNIA": "WANNA",
        "KLASA_UCZNIA": "1C"
    },
    "JEREMIASZ_LOSOWY": {
        "IMIE_UCZNIA": "JEREMIASZ",
        "NAZWISKO_UCZNIA": "LOSOWY",
        "KLASA_UCZNIA": "2A"
    }
}

teachers_list = {
    "TOMASZ_KĄTOWY": {
        "IMIE_NAUCZYCIELA": "TOMASZ",
        "NAZWISKO_NAUCZYCIELA": "KĄTOWY",
        "PRZEDMIOT_NAUCZYCIELA": "MATEMATYKA",
        "KLASY_NAUCZYCIELA": ["3C", "1C", "2B"]
    },
    "MARIA_MAGDALENA": {
        "IMIE_NAUCZYCIELA": "MARIA",
        "NAZWISKO_NAUCZYCIELA": "MAGDALENA",
        "PRZEDMIOT_NAUCZYCIELA": "RELIGIA",
        "KLASY_NAUCZYCIELA": ["3C", "4A"]
    }
}

educators_list = {
    "ANDRZEJ_BOROWSKI": {
        "IMIE_WYCHOWAWCY": "ANDRZEJ",
        "NAZWISKO_NAUCZYCIELA": "BOROWSKI",
        "KLASA_WYCHOWAWCY": "1C"
    }
}


def create_user(user_choice_create: str) :
    if user_choice_create == "UCZEŃ":
        print("\n=== Wpisz imię ucznia ===\n")
        create_user_student_name = str(input()).upper().strip()
        print("\n=== Wpisz nazwisko ucznia ===\n")
        create_user_student_surname = str(input()).upper().strip()
        print("\n=== Wpisz klase ucznia ===\n")
        create_user_student_class = str(input()).upper().strip()
        return  {
            f"{create_user_student_name}_{create_user_student_surname}":
                {
                  "IMIE_UCZNIA": create_user_student_name,
                  "NAZWISKO_UCZNIA": create_user_student_surname,
                  "KLASA_UCZNIA": create_user_student_class,
                }
        }

    if user_choice_create == "NAUCZYCIEL":
        print("\n=== Wpisz imię nauczyciela ===\n")
        create_user_teacher_name = str(input()).upper().strip()
        print("\n=== Wpisz nazwisko nauczyciela ===\n")
        create_user_teacher_surname = str(input()).upper().strip()
        print("\n=== Wpisz przedmiot prowadzący przez nauczyciela ===\n")
        create_user_teacher_subject = str(input()).upper().strip()
        print("\n=== Wpisz klasy, które uczy nauczyciel ===\n"
              "[BRAK WPISANYCH DANYCH POMIJA TEN ETAP]")

        create_user_teacher_classes = list()
        is_assigning_classes = True
        while is_assigning_classes:
            create_user_teacher_classes.append(str(input()).upper().strip())
            if create_user_teacher_classes[-1] == "":
                create_user_teacher_classes.pop()
                is_assigning_classes = False


        return {
            f"{create_user_teacher_name}_{create_user_teacher_surname}":
                {
                    "IMIE_NAUCZYCIELA": create_user_teacher_name,
                    "NAZWISKO_NAUCZYCIELA": create_user_teacher_surname,
                    "PRZEDMIOT_NAUCZYCIELA": create_user_teacher_subject,
                    "KLASY_NAUCZYCIELA": create_user_teacher_classes
                }
        }
    if user_choice_create == "WYCHOWAWCA":
        print("\n=== Wpisz imię wychowawcy ===\n")
        create_user_educator_name = str(input()).upper().strip()
        print("\n=== Wpisz nazwisko wychowawcy ===\n")
        create_user_educator_surname = str(input()).upper().strip()
        print("\n=== Wpisz klasę, którą prowadzi ten wychowawca ===\n")
        create_user_educator_class = str(input()).upper().strip()

        return {
            f"{create_user_educator_name}_{create_user_educator_surname}":
                {
                    "IMIE_WYCHOWAWCY": create_user_educator_name,
                    "NAZWISKO_NAUCZYCIELA": create_user_educator_surname,
                    "KLASA_WYCHOWAWCY": create_user_educator_class
                }
        }



is_program_running = True
while is_program_running:
    print("=== Wpisz funkcje z listy, aby ją wywołać ===")
    user_choice = str(input("\n[UTWÓRZ] \n"
                            "\n[ZARZĄDZAJ] \n"
                            "\n[KONIEC] \n")).upper()


    if user_choice == "UTWÓRZ":
        is_user_creating = True
        while is_user_creating:
            print("\nFUNKCJA: UTWÓRZ \n")
            print("=== Wpisz typ użytkownika, który chcesz "
                                       "utworzyć ===")
            user_choice_create = str(input("\n[UCZEŃ]\n"
                                       "\n[NAUCZYCIEL]\n"
                                       "\n[WYCHOWAWCA]\n"
                                       "\n[KONIEC]\n")).upper()

            if user_choice_create == "UCZEŃ":
                new_student_profile = create_user(user_choice_create)
                students_list = students_list | new_student_profile
            if user_choice_create == "NAUCZYCIEL":
                new_teacher_profile = create_user(user_choice_create)
                teachers_list = teachers_list | new_teacher_profile
            if user_choice_create == "WYCHOWAWCA":
                new_educator_profile = create_user(user_choice_create)
                educators_list = educators_list | new_educator_profile
            if user_choice_create == "KONIEC":
                break
    if user_choice == "ZARZĄDZAJ":
        is_user_choice_manage = True
        while is_user_choice_manage:
            print("\nFUNKCJA: ZARZĄDZAJ \n")
            print("\n=== Wpisz rodzaj profilu, którym chcesz zarządzać ===\n")
            user_choice_manage = str(input("[KLASA]\n"
                                       "\n[UCZEŃ]\n"
                                       "\n[NAUCZYCIEL]\n"
                                       "\n[WYCHOWAWCA]\n"
                                       "\n[KONIEC]\n")).upper()

            if user_choice_manage == "KLASA":
                user_choice_manage_get_class = (str(input
                (" === Wpisz nazwę klasy którą chcesz sprawdzić ===\n")).upper().strip())

                for student_class in students_list:
                    if students_list[student_class]["KLASA_UCZNIA"] == user_choice_manage_get_class:
                        print(students_list[student_class])
                for educator_class in educators_list:
                    if educators_list[educator_class]["KLASA_WYCHOWAWCY"] == user_choice_manage_get_class:
                        print(educators_list[educator_class])
            if user_choice_manage == "UCZEŃ":
                print("=== Podaj dane ucznia, którego chcesz sprawdzić ===\n")
                user_choice_manage_get_student_name = str(input("Imię ucznia: ").upper().strip())
                user_choice_manage_get_student_surname = str(input("Nazwisko ucznia: ").upper().strip())
                user_choice_manage_get_student_key = f"{user_choice_manage_get_student_name}_{user_choice_manage_get_student_surname}"

                if user_choice_manage_get_student_key in students_list:
                    student_get_profile = students_list[user_choice_manage_get_student_key]

                    student_teachers_list = list()
                    for teacher in teachers_list:
                        if student_get_profile["KLASA_UCZNIA"] in teachers_list[teacher]["KLASY_NAUCZYCIELA"]:
                                teacher_subject = teachers_list[teacher]["PRZEDMIOT_NAUCZYCIELA"]
                                student_teachers_list.append([teacher, teacher_subject])



                    print(f"Nauczyciele ucznia: \n{student_teachers_list}\n")
            if user_choice_manage == "NAUCZYCIEL":
                print("=== Podaj dane nauczyciela, którego chcesz sprawdzić ===\n")

                user_choice_manage_get_teacher_name = (str(input("Imię nauczyciela: ")).upper().strip())
                user_choice_manage_get_teacher_surname = (
                    str(input("Nazwisko nauczyciela: ")).upper().strip())

                user_choice_manage_get_teacher_key = f"{user_choice_manage_get_teacher_name}_{user_choice_manage_get_teacher_surname}"
                if user_choice_manage_get_teacher_key in teachers_list:
                    classes_taught_by_teacher = teachers_list[user_choice_manage_get_teacher_key]["KLASY_NAUCZYCIELA"]

                    print(f"Ten nauczyciel uczy klasy: \n{classes_taught_by_teacher}\n")
            if user_choice_manage == "WYCHOWAWCA":
                print("=== Podaj dane wychowawcy, którego chcesz sprawdzić ===\n")

                user_choice_manage_get_educator_name = (str(input("Imię wychowawcy: ")).upper().strip())
                user_choice_manage_get_educator_surname = (
                    str(input("Nazwisko wychowawcy: ")).upper().strip())

                user_choice_manage_get_educator_key = f"{user_choice_manage_get_educator_name}_{user_choice_manage_get_educator_surname}"

                if user_choice_manage_get_educator_key in educators_list:
                    educator_lead_class = educators_list[user_choice_manage_get_educator_key]["KLASA_WYCHOWAWCY"]

                    educator_lead_class_students_list = list()
                    for student in students_list:
                        if students_list[student]["KLASA_UCZNIA"] == educator_lead_class:
                            educator_lead_class_students_list.append(students_list[student])

                    print(f"Wychowawca [{user_choice_manage_get_educator_key}] ma pod sobą uczniów: \n"
                          f"{educator_lead_class_students_list}")

            if user_choice_manage == "KONIEC":
                break




    if user_choice == "KONIEC":
        break












