'''
Documentação:
Gera gráficos de funções escolhidas

Ao digitar o comando no terminal deve-se colocar:
python (ou python3) nomedoarquivo.py 'equação f(x)' valor_do_intervalo_inicial valor_do_intervalo_final 
'''

# Biblioteca
import numpy as np
import math
import sys
import matplotlib.pyplot as plt

# Função
def f(x):
    # Documentação:
    """
    Digite em forma de string a sua função

    Parâmetros: x
    Retorno: y (float)
    """
    y = eval(sys.argv[1])
    return y

# Gráfico da função para diversos pontos
intervalo1 = float(sys.argv[2])
intervalo2 = float(sys.argv[3])
x_f = np.linspace(intervalo1, intervalo2)
f_x = f(x_f)
plt.plot(x_f, f_x, 'r-', label = 'f(x)')
plt.xlim(left = intervalo1, right = intervalo2)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfico f(x)")
plt.legend()
plt.grid(True)
plt.show()