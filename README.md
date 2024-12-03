# Trabajo Práctico: Juegos de Hermanos

## Ingresar parametros a la parte 1 del TP

### ¿Que parametros aceptamos?
Aceptamos un archivo .txt.
Esto en base a los ejemplos de archivos dados por el curso.

### ¿Como debe estar estructurado ese archivo .txt?
En la segunda linea los valores de las monedas separados por solo un ";"
Ejemplo:
```
# Mensaje no importante
72;165;794;892;880;341
```

### ¿Como pongo el parametro?

Si estas no estan dentro de ninguna carpeta y ademas quieres usar uno de los ejemplos dados por el curso:
```bash
python3 parte_1/monedas_greedy_ingresar_datos.py parte_1/datos_parte_1/100.txt
```

Si estas dentro de la carpeta parte_1 y ademas quieres usar uno de los ejemplos dados por el curso:
```bash
python3 monedas_greedy_ingresar_datos.py datos_parte_1/100.txt
```

## Ingresar parametros a la parte 2 del TP

### ¿Que parametros aceptamos?
Aceptamos un archivo .txt.
Esto en base a los ejemplos de archivos dados por el curso.

### ¿Como debe estar estructurado ese archivo .txt?
En la segunda linea los valores de las monedas separados por solo un ";"
Ejemplo:
```
# Mensaje no importante
72;165;794;892;880;341
```

### ¿Como pongo el parametro?

Si estas no estan dentro de ninguna carpeta y ademas quieres usar uno de los ejemplos dados por el curso:
```bash
python3 parte_2/monedas_dinamicas_ingresar_datos.py parte_2/datos_parte_2/100.txt
```

Si estas dentro de la carpeta parte_2 y ademas quieres usar uno de los ejemplos dados por el curso:
```bash
python3 monedas_dinamicas_ingresar_datos.py datos_parte_2/100.txt
```


## Ingresar parametros a la parte 3 del TP

### ¿Que parametros aceptamos?
Aceptamos un archivo .txt.
Esto en base a los ejemplos de archivos dados por el curso.

### ¿Como debe estar estructurado ese archivo .txt?
Comenzando desde la segunda linea, ponemos en cada linea un numero que es el que le da valor a una fila
Ponemos un espacio
Luego va, otra vez, por cada linea un numero pero esta vez le estamos dando valor a las columnas
Otro espacio
Por ultima vez, por cada linea un numero que sera el tamaño del barco a posicionar

Un ejemplo porque lo complique:
```txt
# Algo no importante
# Otra cosa no importante
3
1
2

3
2
0

1
1
```

### ¿Como pongo el parametro?

Si estas no estan dentro de ninguna carpeta y ademas quieres usar uno de los ejemplos dados por el curso:
```bash
python3 parte_3/ejercicio_3_batalla_naval.py parte_3/datos_parte_3/15_10_15.txt
```

Si estas dentro de la carpeta parte_3 y ademas quieres usar uno de los ejemplos dados por el curso:
```bash
python3 ejercicio_3_batalla_naval.py datos_parte_3/15_10_15.txt
```
