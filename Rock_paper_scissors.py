import random


def get_choices():
  player_choice= input("Enter a choice (rock,paper,scissor)")
  options = ["rock","paper","scissors"]
  computer_choice= random.choice(options)
  Choices={"player": player_choice, "Computer": computer_choice}
  return Choices

def check_win(player,computer):
  print(f"You chose: {player}, computer chose: {computer}")
  if player == computer:
    return "its a tie"
  elif player=="rock":
    if computer == "scissors":
      return "Rock smashes scissors you win"
    else:
      return "Paper covers rock you lose"
  elif player=="paper":
    if computer == "rock":
      return "Paper covers rock you win"
    else:
      return "Scissors slices paper you lose"

  elif player=="scissors":
    if computer == "paper":
      return "Scissors slices paper you win"
    else:
      return "Rock smahes scissors you lose"


choices =get_choices()
result = check_win(choices["player"],choices["Computer"])
print(result)
