import random
import requests
def random_pokemon():
       pokemon_number = random.randint(1, 151)
       url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
       response = requests.get(url)
       pokemon = response.json()
       return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
         }
def rounds():
    result=[]
    for i in range(3):
          print('Round: ',i)
          res=run()    
          while res is None:
            print('Retrying round {} due to incorrect input.'.format(i))
            res = run()
          result.append(res)     
    print('The score board is: ',result)      
    if(result.count(1)>result.count(-1)):
         print('You won the match')
    elif(result.count(1)<result.count(-1)) :
         print('Opponent won the match')
    else:
         print("It was a Draw")         
def run():
    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight) ')
    valid_stats=['id','height','weight']
    if stat_choice in valid_stats:  
        opponent_pokemon = random_pokemon()
        print('The opponent chose {}'.format(opponent_pokemon['name']))
        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]
        if my_stat > opponent_stat:
            print('You Win! this round')    
            return 1
        elif my_stat < opponent_stat:
            print('You Lose! this round')
            return -1
        else:
            print('DRAW')
            return 0
    else:
         print('Incorrect option ,please check the spelling')
         
         return None
rounds()

