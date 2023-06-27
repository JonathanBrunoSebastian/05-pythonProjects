# Object Orientated Programming in Python
import math
from tracemalloc import start
import matplotlib.pyplot as plt
import numpy as np

class Funktionen:
    @staticmethod
    def get_ln_dichte(x, sigma, mu):
        f = 1/(math.sqrt(2*math.pi*sigma)*x)*math.exp(-(math.log(x)-mu)/(2*sigma**2))
        return f

    @staticmethod
    def get_ln_verteilung(x, sigma, mu):
        f = Spez_Funktionen.get_phi((math.log(x)-mu)/sigma)
        return f

class Spez_Funktionen:
    @staticmethod
    def get_phi(y):
        phi = 1/math.sqrt(2*math.pi)*math.exp(-y**2/2)
        return phi

    @staticmethod
    def get_hermit_expr(idx, x):
        expr = -1**idx*math.exp(x**2)
        return expr

    @staticmethod
    def get_hermit_pol(n, x):
        for idx in range(n):
            hermit =  Diff_Quotient.get_diff(idx) *math.exp(-x**2)
        return hermit

class Folgen:
    @staticmethod
    def get_fibonaci(fin):
        for idx in range(2):
            x_vec[idx] = idx
            y_vec[idx] = idx
        for idx in range(2,fin):
            a = idx-2
            b = idx-1
            x_vec[idx] = idx
            y_vec[idx] = y_vec[a] + y_vec[b]
        return x_vec,y_vec

    @staticmethod
    def get_stern_brocot(fin):
        for idx in range(2):
            x_vec[idx] = idx
            y_vec[idx] = idx
        for idx in range(2,fin):
            x_vec[idx] = idx
            if idx % 2 == 0:
                v = int(idx/2)
                y_vec[idx] = y_vec[v]
            else:
                n = int((idx+1)/2)
                y_vec[idx] = y_vec[v] + y_vec[n]
        return x_vec,y_vec
          
class Diff_Quotient:
    @staticmethod
    def get_diff(n):
        x_1 = np.zeros(n)
        x_0 = np.zeros(n)
        f_1 = np.zeros(n)
        f_0 = np.zeros(n)
        diff_quotienten = np.zeros(n)
        for idx in range(n):
            x_1[idx] = idx + 1
            x_0[idx] = idx
            f_1[idx] = Spez_Funktionen.get_hermit_expr(x_1, x_1)
            f_0[idx] = Spez_Funktionen.get_hermit_expr(x_0, x_0)
            diff_quotienten[idx] = (f_1-f_0)/(x_1-x_0)
        diff_quot = np.sum(diff_quotienten)
        return diff_quot

class Diagramm:
    @staticmethod
    def plotResults(x,y):
        plt.figure()
        plt.plot(x, y,'rx-',markersize=5,linewidth=1)
        plt.grid()
        plt.show()

# print(Spez_Funktionen.get_hermit_expr(1,1))
# print(Diff_Quotient.get_diff(1))

a = 0
fin = 1001
sigma = 0.758
mu = 2.423
length = fin-a

x_vec = np.zeros(shape=(length))
y_vec = np.zeros(shape=(length))
z_vec = np.zeros(shape=(length))
u_vec = np.zeros(shape=(length))


x_vec,y_vec = Folgen.get_stern_brocot(fin) 
print(y_vec)
D1 = Diagramm.plotResults(x_vec, y_vec)

x_vec,y_vec = Folgen.get_fibonaci(fin)
print(y_vec)
D2 = Diagramm.plotResults(x_vec, y_vec)
