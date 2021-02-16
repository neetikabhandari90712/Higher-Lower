from game_data import data
import art
import random
count = 0
print(art.logo)
Lost = False
random_dict_A = random.choice(data)
random_dict_B = random.choice(data)
def Compare_follower_count(user_input,A,B):
  global count
  if user_input == 'a':
    if A['follower_count'] > B['follower_count']:
      count += 1
      A = A
      B = random.choice(data)
      compare_A_B(A,B)
    else:
      Lost = True
      return print(f'Your score = {count}')
  if user_input == 'b':
    if B['follower_count'] > A['follower_count']:
      count += 1
      A = B
      B = random.choice(data)
      compare_A_B(A,B)
    else:
      Lost = True
      return print(f'Your score = {count}')
    

def compare_A_B(random_dict_A,random_dict_B):
  global Lost
  while not Lost:
    
    # # print(random_dict_A)
    # print(random_dict_B)
    # print(random_dict_A['name'])
    # print(random_dict_B['name'])


    A_name = random_dict_A['name']
    B_name = random_dict_B['name']
    A_follower_count = random_dict_A['follower_count']
    B_follower_count = random_dict_B['follower_count']
    A_description = random_dict_A['description']
    B_description = random_dict_B['description']
    A_country = random_dict_A['country']
    B_country = random_dict_B['country']


    print(f"Compare A : {A_name} a, {A_description} from {A_country}\n {art.vs}\nAgainst B : {B_name} a, {B_description} from {B_country}")  

    user_input = input("Who has more followers ? Type 'A' or 'B': ").lower()

    Compare_follower_count(user_input,random_dict_A,random_dict_B)




    Lost = True
compare_A_B(random_dict_A,random_dict_B)
from replit import clear
