alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]
aprobados = 0
total = 0
suspendidos = 0
for i in alumnos:
    if(i["nota"] >= 5):
        print(i["nombre"].upper() + " ha aprobado con un " + str(i["nota"]))
        aprobados += 1
    elif(i["nota"] < 5):
        print(i["nombre"].upper() + " ha suspendido con un " + str(i["nota"]))
        suspendidos += 1
    total += 1

def calcular_media(alumnos = 0):
    """Calcula la nota media de los alumnos

    Args:
        alumnos (int, optional): _description_. Defaults to 0.
    """
    totalNota = 0
    numeroAlumnos = 0
    for i in alumnos:
        totalNota += i["nota"]
        numeroAlumnos += 1
    return totalNota / numeroAlumnos
        
print(f"El numero total de alumnos es de {total}")
print(f"La nota media de los alumnos es de {calcular_media(alumnos)}")
print(f"El numero de alumnos que ha aprobado es de {aprobados}")
print(f"El numero de alumnos que ha suspendido es de {suspendidos}")