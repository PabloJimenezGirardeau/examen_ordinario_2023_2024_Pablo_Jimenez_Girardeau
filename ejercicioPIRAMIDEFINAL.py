'''Escribe un programa en Python que solicite al usuario un número entero n y luego genere una pirámide de 
asteriscos con n niveles.  La pirámide debe ser centrada y consistir en niveles de asteriscos, comenzando 
con 1 asterisco en el nivel superior y aumentando en 2 asteriscos por nivel. Asegúrate de que el programa
valide que el número ingresado por el usuario sea mayor o igual a 1 antes de continuar.'''

# esta funcion sirve para pedir al usuario el numero de filas de la pirámide, y verificar que este sea válido
def main():
    while True:
        filas = input ("Introduzca un numero de filas para la pirámide:  ")
        try:
            filas = int(filas)
            if filas > 0: #ha de ser mayor que 0 obligatoriamente
                pintar_piramide(filas)
            else :
                print ("Por favor, ingrese un número entero mayor que 0")
        except:
            print ("Por favor, ingrese un número entero mayor que 0")
            
                
                
# la funcion recoge el valor de filas             
def pintar_piramide(filas):
    for i in range(1,filas * 2, 2):
        espacios = (filas * 2 - i)//2 
        print (" " * espacios + "*" * i)
        
    
main()