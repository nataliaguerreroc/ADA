from sys import stdin
"""
Nombre: Natalia Guerrero Caicedo
Código: 8938849
Código de honor: "Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica."
"""


def expBinaria(a, n, m):
	"""
	Se le pasan como paramentros a(base), n(exponente) y m(módulo = 7340033)
	Esta función hace referencia al algoritmo de exponenciación binaria.
	"""
	if n == 0:
		return 1
	if n%2 == 0:
		t = expBinaria(a, n//2, m)%m
		return (t*t)%m
	else:
		t = expBinaria(a, n-1, m)%m
		return (t*(a%m))%m

def calcularInversa(a,m): 
	"""
	Esta función es equivalente al pequeño teorema de Fermat: a^m-1 es equivalente 1 mod m

	"""
	return expBinaria(a, m-2, m)


def combinatoria(n,k):
	"""
	Esta función se hace para saber el número de combinacíones que se pueden hacer teniendo en cuenta los
	parámetros n, k (n corresponde a la cantidad de puntos que hay en un cuadrante y k corresponde a la
	cantidad de puntos que se toman del cuadrante). 
	Para el desarrollo se hace uso de la fórmula de la combinatoria.
	Retorna el calculo de la fórmula de la combinatoria según n y k.
	"""
	global factorial
	return (factorial[n]*(calcularInversa((factorial[k]*factorial[n-k])%7340033, 7340033)))%7340033

def definirPolinomio(n,m): 
	"""
	Recibe como parámetros n y m, que corresponden a la cantidad de puntos
	en la pareja de cuadrantes (1y3 ó 2y4).
	Esta función se hace para calcular el polinomio resultante de operar con n y m haciendo uso
	de la función combinatoria.
	Retorna un arreglo (polinomio) con los coeficientes del polinomio.
	"""
	K = min(n,m) + 1
	polinomio = [0 for _ in range(K)]
	for k in range(K):
		polinomio[k]= (combinatoria(n,k) * combinatoria(m,k))%7340033
	return polinomio



def solve(cuadrante):
	"""
	Función principal para la solución del problema.
	Recibe un arreglo (cuadrantes) con la cantidad de puntos que hay por cuadrante.
	En esta se construyen los dos polinomios (el del cuadrante 1 y 3, y el del cuadrante 2 y 4)
	Se hace la multiplicación de estos polinomios.
	Se retorna el arreglo ans, el cual contendrá respuestas para las propuestas pares.
	"""
	global factorial
	polinomio1 = definirPolinomio(cuadrante[0], cuadrante[2])
	polinomio2 = definirPolinomio(cuadrante[1], cuadrante[3])
	n = len(polinomio1)
	m = len(polinomio2)
	ans = [0 for _ in range(n+m-1)]
	for i in range(n):
		for j in range(m):
			ans[i+j] += polinomio1[i] * polinomio2[j]
	return ans[1::]




def cantidadPuntosCuadrante(puntos):
	"""
	Esta función recibe el arreglo puntos.
	A su vez se inicializa un arreglo llamado cantPuntosCuadrante en 0's, este será el arreglo que
	guardará la cantidad de puntos que hay por cuadrante.
	Retorna un arreglo (cantidadPuntosCuadrante) con la cantidad de puntos que hay por cuadrante.
	"""
	cantPuntosCuadrante = [0, 0, 0, 0]
	for punto in puntos:
		x, y = punto[0], punto[1]
		if x > 0 and y > 0:
			cantPuntosCuadrante[0] += 1
		if x < 0 and y > 0:
			cantPuntosCuadrante[1] += 1
		if x < 0 and y < 0:
			cantPuntosCuadrante[2] += 1
		if y < 0 and x > 0:
			cantPuntosCuadrante[3] += 1
	return cantPuntosCuadrante


def main():
	global factorial
	numcaso = 0
	casos = int(stdin.readline().strip())
	#se hace un precalculo de todos los factoriales para usarlos en la combinatoria
	factorial = [0 for _ in range(10**5+1)]
	factorial[1] = 1
	factorial[0] = 1
	for i in range(2, 10**5+1):
		factorial[i] = factorial[i-1]*(i%7340033)%7340033

	while casos > 0:
		n = int(stdin.readline().strip())
		puntos = []

		for i in range(n):
			x, y = map(int, stdin.readline().strip().split())
			puntos.append([x, y])
		casos -= 1

		cuadrantes = cantidadPuntosCuadrante(puntos)
		ans = solve(cuadrantes)

		numcaso += 1 #formato de salida
		print("Case {}:".format(numcaso))
		for i in range(1, n+1):
			if i%2 == 0 and (i//2) <= len(ans):
				print(ans[(i//2)-1],end = "")
			else:
				print("0",end = "")
			if i < n :
				print(" ", end= "")
		print()

main()

