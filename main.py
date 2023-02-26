import random
user_option= input('Elija una opcion:  piedra, papel o tijera.  ')
option=('piedra','papel' , 'tijera')
computer_option= random.choice(option)

if user_option.lower()=='piedra'
    if computer_option=='piedra'
        print ('Es un empate')
    elif computer_option=='papel'
        print ('Computer ha hanado. Lo siento') 
     elif computer_option=='tijera'
        print('Ha ganado, Computador ha elegido tijeras')      
else:
    print('No ha ingresado un opcion valida')

