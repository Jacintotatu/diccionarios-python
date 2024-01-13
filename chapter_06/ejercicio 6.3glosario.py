diccionario = {'Bucle For': """El for es un tipo de bucle parecido al while pero con ciertas
    diferencias. La principal es que el número de iteraciones de un for está
    definido de antemano, mientras que en un while no. La diferencia 
    principal con respecto al while es en la condición. Mientras que en el 
    while la condición era evaluada en cada iteración para decidir si volver
    a ejecutar o no el código, en el forno existe tal condición, sino un 
    iterableque define las veces que se ejecutará el código. En el 
    siguiente ejemplo vemos un bucle forque se ejecuta 5 veces, y donde 
    la incrementa su valor “automáticamente” en 1 en cada iteración.""", 
    'Bucle While': """El uso del while nos permite ejecutar una sección de código
    repetidas veces, de ahí su nombre. El código se ejecutará mientras una 
    condición determinada se cumpla. Cuando se deje de cumplir, se saldrá del 
    bucle y se continuará la ejecución normal. Llamaremos iteración a una 
    ejecución completa del bloque de código.
    Cabe destacar que existe dos tipos de bucles, los que tienen un número de 
    iteraciones no definidas, y los que tienen un número de iteraciones definidas. 
    El while estaría dentro del primer tipo. Mas adelante veremos los for, 
    que se engloban en el segundo."""
    }
print(f"Significado de For: \n {diccionario['Bucle For']}")
print(f"\nSignificado de While: \n {diccionario['Bucle While']}")