################################################### Homework #2 #########################################################
# Trabajo realizado por: 
#    -Jose Manuel Vergara Alvarez
# Colaboradores:
#    -David Velez Cadavid 
#
#
#
# Nota: Para este trabajo se utilizo el siguiente algoritmo como referencia: 
# - https://github.com/VedantPro/dynamic_TSP/blob/master/TSP.py



# 1) importamos la libreria itertools
#Itertools es un modulo de la libreria estandar de Python que incorpora funciones que devuelven objetos iterables, 
#es decir, estructuras de #datos basadas en elementos que pueden recorrerse secuencialmente y que pueden utilizarse
#en procesos repetitivos (bucles)

#para nuestro algoritmos usaremos itertools.combinations
#este devuelve un objeto iterable basado en tuplas con las combinaciones sin repeticion posibles,
#de una longitud r, a partir de los elementos del objeto de entrada. 


import itertools 
import time

# 2) se crea una matriz de 6 x 6 asimetrica en donde guardamos los costos de viaje de las 6 ciudades

w = [
	[0, 100, 200, 150, 310, 50],
	[230, 0, 800, 190, 440, 360],
	[700, 580, 0, 850, 255, 750],
	[150, 149, 860, 0, 69, 210],
	[311, 414, 250, 669, 0, 790],
	[508, 356, 700, 210, 755, 0]
    ]

#Funcion dinamica del problema del agente viajero

def travelplan(w):
	global time_tot
	n = len(w) #Variable del tamano de la matriz que representa las ciudades


	#valor inicial de 0 a todos los demas puntos
	A = {(frozenset([0, i+1]), i+1): (costo, [0, i+1]) for i, costo in enumerate(w[0][1:])}

	tt = time.time()

	for m in range(2, n):
		B = {}
		#movimiento recursivo para recorrer mas puntos          
		for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, n), m)]:
			for j in S - {0}:
				#encontramos el camino con el costo "minimo" 
				B[(S, j)] =min((A[(S-{j},k)][0] + w[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j) 
		A = B
		#Agregamos el camino final al inicial
	res = min([(A[d][0] + w[0][d[1]], A[d][1]) for d in iter(A)])
	#Hallamos el valor minimo, siendo esta la solucion mas optima

	Resultado = res[0], ["Ciudad "+str(i+1) for i in  res[1] ] 
	# se nombra la solucion mas optima en el orden de sus respectivas ciudades
	
        time_tot = float(time.time()) - float(tt)
	# nos da el tiempo de demora del algoritmo

	return Resultado

print "La mejor ruta es:", travelplan(w)[1]," y regreso a la 'Ciudad 1' " , "Con un costo total de:", travelplan(w)[0]

print "Tiempo Total: " + str(float(time_tot))







		
		
