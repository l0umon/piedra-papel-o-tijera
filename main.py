import random

user_option= input('Elija: piedra, papel o tijera:  ')
option=('piedra','papel' , 'tijera')
computer_option= random.choice(option)

if user_option.lower() == 'piedra':
    if computer_option == 'piedra':
        print ('Es un empate')
    elif computer_option == 'papel':
        print ('Computer ha hanado, ha elejido papel. Lo siento') 
    elif computer_option == 'tijera':
        print('Ha ganado!! Computador ha elegido tijeras')   
elif user_option.lower() == 'papel':
    if computer_option == 'papel':
        print ('Es un empate')
    elif computer_option == 'tijera':
        print ('Computer ha hanado, ha elejido tijera. Lo siento') 
    elif computer_option == 'piedra':
        print('Ha ganado!! Computador ha elegido piedra')   
elif user_option.lower() == 'tijera':
    if computer_option == 'tijera':
        print ('Es un empate')
    elif computer_option == 'piedra':
        print ('Computer ha hanado, ha elejido piedra. Lo siento') 
    elif computer_option == 'papel':
        print('Ha ganado!! Computador ha elegido papel')                   
else:
    print('No ha ingresado un opcion valida')