import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('*' * 23, '\nEsa opcion no es valida')
    print('*' * 23)
    return None, None
    
  return user_option, random.choice(options)

def show_round(num_round):
  print('*' * 7, '\nROUND', num_round)
  print('*' * 7)
  num_round += 1
  return num_round

def show_results(wins_user, wins_computer):
  if wins_user > 0 or wins_computer > 0:
    print('*' * 30, f'\nResults: User {wins_user} and Computer {wins_computer}')
    print('*' * 30)
    finish_user = finish_game('User', wins_user)
    finish_computer = finish_game('Computer', wins_computer)
    return finish_user or finish_computer

def finish_game(player, counter):
  if counter > 2:
    print(f'Ha ganado {player}.')
    print('*' * 30)
    return True
  return False

def play():
  game = {
    'piedra': { 'tijera': 'win', 'papel': 'lost' },
    'papel': { 'piedra': 'win', 'tijera': 'lost' },
    'tijera': { 'papel': 'win', 'piedra': 'lost' }
  }
  round = 1
  wins_user = wins_computer = 0
  while True:
    user_option, computer_option = choose_options()
  
    if user_option == None or computer_option == None:
      continue
      
    # Show information by round
    round = show_round(round)  
    
    if user_option == computer_option:
      print('Empate')
      print('*' * 25)
      continue
  
    if game[user_option][computer_option] == 'win':
      wins_user += 1
      print(f'{user_option} gana a {computer_option}\nGanaste! :D')
    else:
      wins_computer += 1
      print(f'{computer_option} gana a {user_option}\nPerdiste! :(')
  
    # show results
    if show_results(wins_user, wins_computer):
      break

play()