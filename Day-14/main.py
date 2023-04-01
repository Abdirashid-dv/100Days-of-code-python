from game_data import data
from art import logo,vs
from replit import clear
import random

def get_arandom():
  return random.choice(data)

def account_data(account):
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name}, {description}, {country}."
  
def answer_check(followers_a,followers_b,answer):
  if followers_a > followers_b:
    return answer == 'a'
  else:
    return answer == 'b'
  

def game():
  score =0
  should_countinue = True
  print(logo)
  account_a = get_arandom()
  account_b = get_arandom()

  while should_countinue:
    account_a = account_b
    account_b = get_arandom()
    
    while account_a == account_b:
      account_b = get_arandom()
      
    print("Compare A: ",account_data(account_a))
    print(vs)
    print("Against B: ",account_data(account_b))
    
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']
    is_check = answer_check(followers_a,followers_b,answer)
    
    clear()
    print(logo)
    
    if is_check:
      score +=1
      print(f"You're right! Current score: {score}")
    else:
      should_countinue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
