

number_to_guess = 2

user_number = int(input("Adivina un numero tienes 5 intentos: "))

if number_to_guess == user_number:
    print("Has ganado makina")
else:
    print("Has perdido te quedan 4 intentos")

    user_number = int(input("Advina un numero: "))
if number_to_guess == user_number:
    print("Has ganado makina")
else:
    print("Has perdido te quedan 3 intentos")

    user_number = int(input("Advina un numero: "))
if number_to_guess == user_number:
    print("Has ganado makina")
else:
    print("Has perdido te quedan 2 intentos")