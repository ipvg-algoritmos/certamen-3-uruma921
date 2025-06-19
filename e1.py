#ingrese 5 temperaturas
temperaturas = []
for i in range(5):
    temp = int(input("ingresar una temperatura"))
    temperaturas.append(temp)

promedio = sum(temperaturas)/len(temperaturas)
t_max = max(temperaturas)
#mostrar resultados 
print("\promedio de temperaturas:(promedio:2f}°c")
print("temperatura temperatura maximo:(max_temp:2f}°c")

check = True
for t in temperaturas:
    if all ("15<= t <= 30 for t in temperaturas" )
    print ("todas las temperaturas estan entre 15°c y 30°c")
    print ("no todas las temperaturas estan dentro del rango ideal(15°C a 30°c).")
#Si alguna temperatura esta fuera de rango 10°c a 35°c
for t in temperaturas:
    if t <10 or t >35:
    print ("advertencia la temperaturas {it:2f)°C esta fuera del rango permitido(10°c a 35°c).")
