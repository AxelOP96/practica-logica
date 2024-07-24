import random
horaInicio = 8;
horaFin = 21;
variableAleatoria =random.randint(10, 60);
tiempo = (21 *8) * 60  + variableAleatoria;

for x in range(tiempo, 0, -1):
    print("Faltan ", x , " minutos para terminar de trabajar")
