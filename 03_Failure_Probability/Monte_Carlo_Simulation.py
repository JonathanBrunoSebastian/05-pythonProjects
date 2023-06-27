import math
import numpy as np

input_data = open('Versagenswahrscheinlichkeit/Eingabe_Monte_Carlo.txt','r')
extracted_data = input_data.readlines()[1::2]
input_data.close()

data = []
for line in extracted_data:
    extracted_data = line.rstrip()
    data.append(extracted_data)

lower_limit = int(data[0])
upper_limit = int(data[1])
given_repititions = int(data[2])
load_deviation = float(data[3]) 
load_expectant = float(data[4]) 
material_deviation = float(data[5]) 
material_expectant = float(data[6]) 
material_limit = float(data[7])
moment = float(data[8])
resistance_moment = float(data[9])
confidence_interval = float(data[10])
confidence_level = float(data[11])

def get_load_probability(x):
    value_1 = math.pi/(load_deviation*math.sqrt(6))
    value_2 = load_expectant - 0.577216/value_1
    value_3 = -math.log(x)
    if value_3 <= 0:
        load_probability = value_2
    else:
        load_probability = value_2 - 1/value_1*(math.log(value_3))
    return load_probability

def raw_material_probability(y):
    value_1 = math.log(1/y**2)
    if value_1 <= 0:
        value_2 = 0
    else:
        value_2 = math.sqrt(value_1)
    denominator = 2.515517+0.802853*value_2+0.010328*value_2**2
    numerator = 1+1.432788*value_2+0.189269*value_2**2+0.001308*value_2**3
    material_probability = -value_2 + denominator/numerator
    return material_probability

def get_material_probability(y):
    transformed_deviation = math.sqrt(math.log(1+(material_deviation/(material_expectant-material_limit))**2))
    transformed_expectant = math.log(material_expectant-material_limit)-(transformed_deviation**2/2)
    if y > 0 and y <= 0.5:
        raw_probability = raw_material_probability(y)
    elif y > 0.5 and y <= 1:
        raw_probability = -raw_material_probability(y)
    material_probability = material_limit + math.exp(transformed_expectant+transformed_deviation*raw_probability)
    return material_probability

def get_limit(x, y):
    limit = get_material_probability(y) - moment/resistance_moment*get_load_probability(x)
    return limit

def get_indicator(limit):
    if limit > 0:
        indicator = 0   # kein Versagen
    else:
        indicator = 1   # Versagen
    return indicator

def get_main_indicator(repititions):
    x = np.random.uniform(lower_limit, upper_limit, repititions)
    y = np.random.uniform(lower_limit, upper_limit, repititions)
    limits = np.array(list(map(get_limit, x, y)))
    indicators = np.array(list(map(get_indicator, limits)))
    main_indicator = sum(indicators)
    return main_indicator

def get_failure_probability(repititions, indicator):
    return 1/repititions*indicator

def get_required_repititions(probability):
    required_repititions = np.ceil(1/(1-confidence_level)*(probability*(1-probability))/confidence_interval**2)
    return required_repititions.astype(int)

main_indicator = get_main_indicator(given_repititions)
failure_probability = get_failure_probability(given_repititions, main_indicator)

required_repititions = get_required_repititions(failure_probability)

new_indicator = get_main_indicator(required_repititions)
new_failure_probability = get_failure_probability(required_repititions, new_indicator)

with open('Versagenswahrscheinlichkeit/Ausgabe_Monte_Carlo.txt','w') as output_data:
    line_1 = "Versagenswahrscheinlichkeit: " + str(failure_probability) + " bei " + str(given_repititions) + " Wiederholungen" + "\n"
    line_2 = "Versagenswahrscheinlichkeit: " + str(new_failure_probability) + " bei " + str(required_repititions) + " Wiederholungen" + "\n"
    line_3 = "Untere Grenze: " + str(lower_limit) + "\n"
    line_4 = "Obere Grenze: " + str(upper_limit) 
    output_data.writelines([line_1, line_2, line_3, line_4])
output_data.close()