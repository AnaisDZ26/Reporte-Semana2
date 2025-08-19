n = int(input())
equipo_1 = input().strip()
goles_1 = 1

equipo_2 = None
goles_2 = 0

for i in range(n - 1):
    gol = input().strip()
    if gol == equipo_1:
        goles_1 += 1
    else:
        if equipo_2 is None:
            equipo_2 = gol
            goles_2 = 1
        else:
            goles_2 += 1

if goles_1 > goles_2:  # Solo hay dos casos posibles, por lo mismo se omite la condicion de goles_2 > goles_1
    print(equipo_1)
else: 
    print(equipo_2)