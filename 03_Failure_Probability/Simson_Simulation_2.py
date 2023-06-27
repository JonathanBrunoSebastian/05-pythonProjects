import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

input_data = open('Versagenswahrscheinlichkeit/Eingabe_Simson_2.txt','r')
extracted_data = input_data.readlines()[1::2]
input_data.close()

data = []
for line in extracted_data:
    extracted_data = line.rstrip()
    data.append(extracted_data)

integration_area = int(data[0])
load_deviation = float(data[1]) 
load_expectant = float(data[2]) 
material_deviation = float(data[3]) 
material_expectant = float(data[4]) 
material_limit = float(data[5]) 
constant = float(data[6])

if constant==0:
    lower_limit = int(1)
else:
    lower_limit = int(np.ceil(-material_limit/constant))

upper_limit = lower_limit + integration_area

interval = (upper_limit - lower_limit)/integration_area

load_factor_a = math.pi/(load_deviation*math.sqrt(6))

load_factor_b = load_expectant-0.5772/load_factor_a

def get_load_probability(x):
    load_probability = load_factor_a*math.exp(-load_factor_a*(x-load_factor_b)-math.exp(-load_factor_a*(x-load_factor_b)))
    return load_probability

def get_y_value(x):
    y_value = 1/material_deviation*(math.log(-constant*x-material_limit)-material_expectant)
    return y_value

def get_material_probability(y):
    material_probability = 1/math.sqrt(2*math.pi)*math.exp(-(y**2)/2)
    return material_probability

def get_target_values(function_1, function_2):
    target_values = function_1*function_2
    return target_values

x_history = np.arange(lower_limit, upper_limit)
y_history = np.array(list(map(get_y_value, x_history)))
load_probability = np.array(list(map(get_load_probability, x_history)))
material_probability = np.array(list(map(get_material_probability, y_history)))
target_values = np.array(list(map(get_target_values, load_probability, material_probability)))
failure_probability = integrate.simpson(y=target_values, dx=interval)

with open('Versagenswahrscheinlichkeit/Ausgabe_Simson_2.txt','w') as output_data:
    line_1 = "Versagenswahrscheinlichkeit: " + str(failure_probability) + "\n"
    line_2 = "Untere Grenze: " + str(lower_limit) + "\n"
    line_3 = "Obere Grenze: " + str(upper_limit) 
    output_data.writelines([line_1, line_2, line_3])
output_data.close()

fig_1, ax = plt.subplots(figsize=(6,6))
ax.plot(x_history, load_probability)
ax.set(xlabel='x', ylabel='f(x)')
ax.grid()
plt.savefig("Versagenswahrscheinlichkeit/WVF_Belastung_Simson_2.png", dpi=300)

fig_2, ax = plt.subplots(figsize=(6,6))
ax.plot(y_history, material_probability)
ax.set(xlabel='y', ylabel='phi(y)')
ax.grid()
plt.savefig("Versagenswahrscheinlichkeit/WVF_Material_Simson_2.png", dpi=300)