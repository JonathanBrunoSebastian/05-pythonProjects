import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

input_data = open('Versagenswahrscheinlichkeit/Eingabe_Simson_3.txt','r')
extracted_data = input_data.readlines()[1::2]
input_data.close()

data = []
for line in extracted_data:
    extracted_data = line.rstrip()
    data.append(extracted_data)

integration_area = int(data[0])
load_deviation = float(data[1]) 
load_expectant = float(data[2])
constant = float(data[6])
constant_k = float(data[7])

if constant==0:
    lower_limit = int(0)
else:
    lower_limit = int(np.ceil(-constant_k/constant))

upper_limit = lower_limit + integration_area

interval = (upper_limit - lower_limit)/integration_area

load_factor_a = math.pi/(load_deviation*math.sqrt(6))

load_factor_b = load_expectant-0.5772/load_factor_a

def get_load_probability(x):
    load_probability = load_factor_a*math.exp(-load_factor_a*(x-load_factor_b)-math.exp(-load_factor_a*(x-load_factor_b)))
    return load_probability

def get_target_values(function_1, function_2):
    target_values = function_1*function_2
    return target_values

x_history = np.arange(lower_limit, upper_limit)
load_probability = np.array(list(map(get_load_probability, x_history)))
material_probability = np.ones(len(load_probability))
target_values = np.array(list(map(get_target_values, load_probability, material_probability)))
failure_probability = integrate.simpson(y=target_values, dx=interval)

with open('Versagenswahrscheinlichkeit/Ausgabe_Simson_3.txt','w') as output_data:
    line_1 = "Versagenswahrscheinlichkeit: " + str(failure_probability) + "\n"
    line_2 = "Untere Grenze: " + str(lower_limit) + "\n"
    line_3 = "Obere Grenze: " + str(upper_limit) 
    output_data.writelines([line_1, line_2, line_3])
output_data.close()

fig_1, ax = plt.subplots(figsize=(6,6))
ax.plot(x_history, load_probability)
ax.set(xlabel='x', ylabel='f(x)')
ax.grid()
plt.savefig("Versagenswahrscheinlichkeit/WVF_Belastung_Simson_3.png", dpi=300)