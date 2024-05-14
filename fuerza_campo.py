# Programa: observar el comportamiento de la fuerza eléctrica y 
# el campo eléctrico en función del inverso cuadrado de la distancia. 

#Imports
import numpy as np
import matplotlib.pyplot as plt

# Definir constantes
k = 9*10**9  # Constante electrostática
q1 = 1*10**-6  # Carga 1 
q2 = 1*10**-6  # Carga 2 


r = np.linspace(1, 10, 100)  # rango de distancias
r = r**0.5 # raiz de r

# Hallar la fuerza eléctrica para cada distancia
# Fuerza Positiva 
fuerzaPositiva = k *(q1 * q2) / r**2
# Fuerza Negativa
fuerzaNegativa = k *(q1 * -q2) / r**2

# Graficar Fuerza Positiva
plt.figure()  # Crea una nueva figura
plt.plot(r**2, fuerzaPositiva, label='Fuerza eléctrica (Carga positiva)')
plt.xlabel('Distancia al cuadrado (m^2)')
plt.ylabel('Fuerza eléctrica / $r^2$ (N/m^2)')
plt.title('Comparación Fuerza Electrica Fe (Carga positiva) en funcion de la distancia al cuadrado')
plt.grid(True)
plt.legend()
plt.show()

# Graficar Fuerza Negativa
plt.figure()  # Crea una nueva figura
plt.plot(r**2, fuerzaNegativa, label='Fuerza eléctrica (Carga negativa)')
plt.xlabel('Distancia al cuadrado (m^2)')
plt.ylabel('Fuerza eléctrica / $r^2$ (N/m^2)')
plt.title('Comparación Fuerza Electrica Fe (Carga Negativa) en funcion de la distancia al cuadrado')
plt.grid(True)
plt.legend()
plt.show()