
apetece_helado = input("¿Te apetece un helado? (Si / No): ")
tiene_dinero = input("¿Tienes dienero para un helado? (Si / No): ")
esta_el_senor_helados = input("¿Esta el señor de los helados? (Si / No)")
esta_tu_tia = input("¿Estas con tu tia?")

if apetece_helado == "Si" and (tiene_dinero == "Si" or esta_tu_tia == "Si") and esta_el_senor_helados == "Si":
    print("Pues comoete un helado")
else:
    print("Pues nada")