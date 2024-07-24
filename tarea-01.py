horaCafe = 15;
limiteMensual = 450;
diasEnMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
contadorMeses =0;
for x in range(len(diasEnMes)):
    if (horaCafe * diasEnMes[x]) < 450:
        contadorMeses += 1;

print("La cantidad de meses en que Facundo no tiene un descuento en su sueldo es de ", contadorMeses)
