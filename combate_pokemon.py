
pokemon_elegido = input("¿Contra qué pokemon quieres combatir? / (Squirtle / Charmander / Bulbasaur): ")

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100


while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque vamos a utilizar? (Chispazo / Bola Voltio)")
    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "Bola Voltio":
        vida_enemigo -= 12

    print("La vida del enemigo ahora es de {}".format(vida_enemigo))

    elif pokemon_elegido == "Squirtle":
        print ("Squirtle te hace un ataque de 8 de daño")
        vida_pikachu -= 8

    elif pokemon_elegido == "Charmander":
        print("Charmander te hace un ataque de 7 de daño")
        vida_pikachu -= 7

    elif pokemon_elegido == "Bulbasaur":
        print("Bulbasaur te hace un ataque de 10 de daño")
        vida_pikachu -= 10

    print("La vida de pikachu ahora es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("Has Ganado makina mastodonte crack")

if vida_pikachu <= 0:
    print("Has perdido ante entrenador Máximo")


print("El combate ha terminado")