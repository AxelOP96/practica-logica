import math
diasEnfadada = 0;
diasEnMes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
for x in range(len(diasEnMes)):
    if x % 2==1:
        diasEnfadada += math.ceil(diasEnMes[x] * 0.7)
    else:
        diasEnfadada += math.ceil(diasEnMes[x] * 0.3)

print("La cantidad de dias que pasa enfadada en el año es de: " , diasEnfadada);
fechaAEvitar = diasEnfadada/2;
diasEnfadada =0;
for x in range(len(diasEnMes)):
    if x % 2==1:
        diasEnfadada += math.ceil(diasEnMes[x] * 0.7)
        if diasEnfadada > fechaAEvitar:
            answer = x;
            break;
    else:
        diasEnfadada += math.ceil(diasEnMes[x] * 0.3)
        if diasEnfadada > fechaAEvitar:
            answer = x;
            break;


print("Debe evitar a su jefa en el mes " , answer)
