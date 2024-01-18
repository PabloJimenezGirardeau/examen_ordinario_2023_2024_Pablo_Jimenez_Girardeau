import time 
def partida():
    tiempo_carlsen = 180
    tiempo_nakamura = 180
    tiempo_movimiento = 10
    
    turno = "Carlsen"
    
    
    while tiempo_carlsen > 0 and tiempo_nakamura >0:
        print(f"Juega {turno} \n Tiempo de Carlsen:{tiempo_carlsen} \n Tiempo de Nakamura:{tiempo_nakamura}")
        try:
            siguiente_movimiento = input("Ingrese quien es el siguiente en mover,'Carlsen' o 'Nakamura', o si quiere Salir  ").lower()
            if siguiente_movimiento not in ['carlsen', 'nakamura', 'salir']:
                print("Movimiento no válido. Debe ser 'Carlsen', 'Nakamura' o 'Salir'.")
                continue
            if (turno == 'carlsen' and siguiente_movimiento == 'nakamura') or (turno == 'nakamura' and siguiente_movimiento == 'carlsen'):
                print (f"NO es el turno de {siguiente_movimiento}")
                continue
            if siguiente_movimiento == 'salir':
                break
        except ValueError: 
            print("Introduce turno correcto")
            continue
        
        if turno == 'carlsen' and siguiente_movimiento != 'carlsen':
            print ("NO es el turno de Carlsen")
            continue            
        elif turno == 'nakamura' and siguiente_movimiento != 'nakamura':
            print ("NO es el turno de Nakamura")
            continue
        
        if turno == 'carlsen':
            if tiempo_carlsen <= 60:
                tiempo_movimiento = 5
                
            tiempo_carlsen -= tiempo_movimiento
            turno = 'nakamura'
        
        else:
            if tiempo_carlsen <= 60:
                tiempo_movimiento = 5
    
            tiempo_nakamura -= tiempo_movimiento
            turno = 'carlsen'

    if tiempo_carlsen <= 0:
        print("Carlsen agotó su tiempo, GANA NAKAMURA")
    elif tiempo_nakamura <= 0:
        print("Carlsen agotó su tiempo, GANA NAKAMURA")

        
partida()