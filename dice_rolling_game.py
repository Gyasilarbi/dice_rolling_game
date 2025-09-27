import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(f"You rolled {dice1} and {dice2} (Total = {total})")
    return total

def play_round(player_name):
    input(f"{player_name}, press Enter to start game")
    total = roll_dice()

    if total in [7, 11]:
        print("You win this round")
        return 1
    elif total in [2, 3, 12]:
        print("You lose this round")
        return 0
    else:
        print("It's a draw, no points to this round")
        return 0.5    

def play_game():
    print("---=== Welcome to the Dice Game ===---")
    player1 = input("Enter player 1 name: ") 
    player2 = input("Enter player 2 name: ")

    rounds = 3
    score1 = 0
    score2 = 0
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        
        print(f"{player1}'s turn:")  
        score1 += play_round(player1)

        print(f"{player2}'s turn:")  
        score2 += play_round(player2)

        print(f"\nCurrent score: {player1} = {score1}, {player2} = {score2}")

    # Final Result
    print(f"\n=== Final Result ===")
    print(f"{player1}: {score1} points")
    print(f"{player2}: {score2} points")

    if score1 > score2:
        print(f"{player1} wins! 🎉")
    elif score2 > score1:
        print(f"{player2} wins! 🎉")
    else:
        print("It's a tie 🤝")

if __name__ == "__main__":
    play_game()
