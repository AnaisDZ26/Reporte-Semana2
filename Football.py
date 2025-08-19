n = int(input())    # Casos de prueba
equipo_1 = input().strip()  # Primer equipo encontrado
goles_1 = 1 # Se asume que hizo un gol pues por eso se lee el nombre

equipo_2 = None # Pueden haber casos donde no haya un segundo equipo
goles_2 = 0

for i in range(n - 1):  # Ya se analizo el primer caso
    gol = input().strip()
    if gol == equipo_1:
        goles_1 += 1
    else:
        if equipo_2 is None: # Es la primera vez que se encuentra el equipo_2, por lo que se inicializa
            equipo_2 = gol
            goles_2 = 1 # Y su contador de goles es 1
        else:
            goles_2 += 1    # En caso de que se haya encontrado antes el equipo_2, solo se le suma el gol

if goles_1 > goles_2:  # Solo hay dos casos posibles, por lo mismo se omite la condicion de goles_2 > goles_1
    print(equipo_1)
else:
    print(equipo_2)