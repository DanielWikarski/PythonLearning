import random

winning_conditions = [0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8] #kombinacje z których można wygrać

playing_board_spots = [1,2,3,4,5,6,7,8,9]
computer_spots_taken = list()

def show_current_board (playing_board_spots):
    playing_board = f"\n {playing_board_spots[0]} | {playing_board_spots[1]} | {playing_board_spots[2]} \n" \
                    " -----------\n" \
                    f" {playing_board_spots[3]} | {playing_board_spots[4]} | {playing_board_spots[5]} \n" \
                    " -----------\n" \
                    f" {playing_board_spots[6]} | {playing_board_spots[7]} | {playing_board_spots[8]} \n"
    print(playing_board)

def player_movement_pc ():
    print("[TURA KOMPUTERA]")
    # zaczynamy od środka, więcej dostępnych  kombinacji  na wygraną
    if isinstance(playing_board_spots[4], int):
        computer_turn_spot = playing_board_spots[4]
        computer_spots_taken.append(computer_turn_spot - 1) # [-1] żeby zgadzało się z indeksami
        playing_board_spots[4] = "X"
        show_current_board(playing_board_spots)
        return playing_board_spots, computer_spots_taken
    
    else:
        free_spots = list() # sprawdzam free spoty 
        for spot in range(9):
            if isinstance(playing_board_spots[spot], int):
                free_spots.append(spot) 

        for combination in winning_conditions: #iterujemy przez winning conditions 
            check_lineup = [playing_board_spots[spot] for spot in combination] # Tutaj przy iteracji tworzy się "line up" - np. w pierwszej kombinacji sprawdzi nam co jest na  polach 0,1,2, będzie nam to  potrzebne do sprawdzenia, czy są tam nasze "X"
            if check_lineup.count("X") == 2 and check_lineup.count("O") == 0:   #tutaj sprawdzam czy line up ma dwa "X", żeby móc zadać cios kończący  I NIE MA TAM ENEMY pola
                for spot in check_lineup:
                    if isinstance(spot, int):
                        computer_turn_spot = spot
                        computer_spots_taken.append(computer_turn_spot - 1) 
                        playing_board_spots[computer_turn_spot-1] = "X"
                        show_current_board(playing_board_spots)
                        return playing_board_spots, computer_spots_taken

    # jakby komputer nic nie wylosował, to po prostu na randomowe pole postawi X
    computer_turn_spot = random.choice(free_spots)
    computer_spots_taken.append(computer_turn_spot)
    playing_board_spots[computer_turn_spot] = "X" # tutaj nie robie -1, bo free spots wypluło  już zindeksowane miejsca, powyżej to były normalne cyfry i żeby zrobić indeks, musiałem zrobić -1
    show_current_board(playing_board_spots)
    return playing_board_spots, computer_spots_taken
          
def player_movement ():
    is_player_choosing = True
    print("\n[TWOJA TURA]")

    while is_player_choosing:
        player_turn_spot = int(input("\nWpisz numer pola, na które chcesz stanąć: "))

        if playing_board_spots[player_turn_spot-1] == "X":
            print("Pole jest już zajęte!")
            is_player_choosing  = True

        else: 
            playing_board_spots[player_turn_spot-1] = "O"
            show_current_board(playing_board_spots)
            is_player_choosing  = False
def game ():
        print("Cześć, zagrajmy w kółko i krzyżyk! \n")
        print(" == Komputer zaczyna pierwszy == \n")
        is_game_running = True
        while is_game_running:

            player_movement_pc()
            
            if all(isinstance(spot, str) for spot in playing_board_spots): # porównuje czy wszystkie spoty są już stringami, jeśli tak - remis
                print("=== REMIS! ===")
                is_game_running = False
                return
            for combination in winning_conditions:
                if all(number in computer_spots_taken for number in combination): #NOWE!!!! ALL() - zwraca bool, składnia:  all(warunek, pętla do sprawdzenia)
                    print("=== PRZEGRAŁEŚ ===\n")
                    print("=== NIE WYGRASZ Z KOMPUTEREM ===")
                    is_game_running = False
                    return         
            player_movement()
        return computer_spots_taken, playing_board_spots
        
game()