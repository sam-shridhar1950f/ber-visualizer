import os
import copy
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from comparison import getBer



directory = r'C:\vlcchanges\underwatervlc\python\logData'
json_file = open (r'C:\vlcchanges\underwatervlc\python\graph-generator\config.json', "r")
config = json.load(json_file)
precision = int(config["precision"])


FULL_PATHS_LIST = []
REL_PATHS_LIST = []
COPY_REL_PATHS_LIST = []


TRANSMISSIONRATE_PAIRS = {}
SALINITY_PAIRS = {}
PH_PAIRS = {}
TEMPERATURE_PAIRS = {}
TURBIDITY_PAIRS = {}
h = 0
first = True
ind = -1
for entry in os.scandir(directory):
    if entry.path.endswith(".csv") and entry.is_file():
        FULL_PATHS_LIST.append(entry.path)

for entry in FULL_PATHS_LIST:
    rel = entry.split("\\")
    REL_PATHS_LIST.append(rel[-1])
    COPY_REL_PATHS_LIST.append(rel[-1])

for i in range(0, len(REL_PATHS_LIST)):
    if not first:
        ind_1 = 0
    else:
        ind_1 = i
    first = True
    if len(REL_PATHS_LIST) % 2 != 0:
        break
    if not REL_PATHS_LIST:
        break
    # print(REL_PATHS_LIST[i].split("_"))
    parameter = str(REL_PATHS_LIST[ind_1].split("_")[1])
    category = REL_PATHS_LIST[ind_1].split("_")[0] # transmissionrate
    end_type = REL_PATHS_LIST[ind_1].split("_")[-1][:-4]
    if end_type[:-1] == "receiver": 
        for j in range(0, len(COPY_REL_PATHS_LIST) ):
            
            if len(REL_PATHS_LIST) == 2 and h < 1:
                ind = 0
                h += 1
            elif first:
                ind = j
            
            else:
                ind += 1
            
            category_transmit = COPY_REL_PATHS_LIST[j].split("_")[0] # transmissionrate
            end_type_transmit = COPY_REL_PATHS_LIST[j].split("_")[-1][:-4]
            if category_transmit == category and end_type_transmit[:-1] == "transmitter" and end_type[-1] == end_type_transmit[-1]:
                if category == "transmissionrate":
                    start_path = "\\".join(rel[:-1])
                    # print(start_path)
                    TRANSMISSIONRATE_PAIRS[parameter] = [start_path + "\\" + REL_PATHS_LIST[ind_1], start_path + "\\" + COPY_REL_PATHS_LIST[j]]
                    filtered_list = [element for element in REL_PATHS_LIST if element not in [REL_PATHS_LIST[ind_1], COPY_REL_PATHS_LIST[j]]]
                    REL_PATHS_LIST = filtered_list
                    ind -= ind
                    first = False
                    break
                if category == "temperature":
                    start_path = "\\".join(rel[:-1])
                    # print(start_path)
                    TEMPERATURE_PAIRS[parameter] = [start_path + "\\" + REL_PATHS_LIST[ind_1], start_path + "\\" + COPY_REL_PATHS_LIST[j]]
                    filtered_list = [element for element in REL_PATHS_LIST if element not in [REL_PATHS_LIST[ind_1], COPY_REL_PATHS_LIST[j]]]
                    REL_PATHS_LIST = filtered_list
                    ind -= ind
                    first = False
                    break
    if end_type[:-1] == "transmitter": 
        for j in range(0, len(COPY_REL_PATHS_LIST) ):
            if first:
                ind = j
            else:
                ind += 1
            # print(ind)
            # print(REL_PATHS_LIST)
            category_transmit = COPY_REL_PATHS_LIST[j].split("_")[0] # transmissionrate
            end_type_transmit = COPY_REL_PATHS_LIST[j].split("_")[-1][:-4]
            if category_transmit == category and end_type_transmit[:-1] == "receiver" and end_type[-1] == end_type_transmit[-1]:
                if category == "transmissionrate":
                    start_path = "\\".join(rel[:-1])
                    # print(start_path)
                    TRANSMISSIONRATE_PAIRS[parameter] = [start_path + "\\" + REL_PATHS_LIST[j], start_path + "\\" + REL_PATHS_LIST[i]]
                    filtered_list = [element for element in REL_PATHS_LIST if element not in [REL_PATHS_LIST[i], REL_PATHS_LIST[j]]]
                    REL_PATHS_LIST = filtered_list
                    ind -= ind
                    first = False
                    break
                if category == "temperature":
                    start_path = "\\".join(rel[:-1])
                    # print(start_path)
                    TEMPERATURE_PAIRS[parameter] = [start_path + "\\" + REL_PATHS_LIST[j], start_path + "\\" + REL_PATHS_LIST[i]]
                    filtered_list = [element for element in REL_PATHS_LIST if element not in [REL_PATHS_LIST[i], REL_PATHS_LIST[j]]]
                    REL_PATHS_LIST = filtered_list
                    ind -= ind
                    first = False
                    break



    


def normalize(pairs):
    for key in pairs:
        receiver = pairs[key][0].split("\\")
        transmitter = pairs[key][1].split("\\")
        pairs[key] = [pd.read_csv("/".join(receiver)), pd.read_csv("/".join(transmitter))]

def x_values(sorted_dict):
    x_vals = []
    for key in sorted_dict:
        if "c" in key:
            noKey = key.replace("c", "")
            x_vals.append(noKey)
        elif "Hz" in key:
            noKey = key.replace("Hz", "")
            x_vals.append(noKey)
        else:
            x_vals.append(key)
    return x_vals

def y_values(sorted_dict):
    y_vals = []
    for key in sorted_dict:
        y_vals.append(sorted_dict[key])
    return y_vals

def extractDigits(string):
    newstr = ""
    for l in string:
        if l.isdigit():
            newstr += l
    return int(newstr)

def errorCalc(y_vals):
    stds_list = []
    for val in y_vals:
        #print(val)
        stds_list.append(np.std(val))
    return stds_list
        
             
def temperature(pairs):
    original = dict(copy.deepcopy(pairs))
    type = "temperature"
    normalize(pairs)
    for key in pairs:
        transmissionrate = extractDigits(original[key][0].split("_")[2])
        fps = extractDigits(original[key][0].split("_")[3])
        
        ber = getBer(pairs[key][1]["bit"], pairs[key][0]["Bit"], transmissionrate, fps, precision)
        pairs[key] = ber
    x_vals = x_values(dict(sorted(pairs.items())))
    y_vals =  y_values(dict(sorted(pairs.items())))
    stds_list = errorCalc(y_vals)
    # print(stds_list)
    plot_type = str(input("Plot type: "))
    if plot_type.lower() == "scatter":
        plt.scatter(x_vals,y_vals)
        plt.xlabel('Temperature')
        plt.ylabel('Bit Error Rate (%)')
        plt.show()
    elif plot_type.lower() == "bar":
        plt.bar(x_vals, list(pairs.values()), yerr=stds_list, color ='blue',
        width = 0.4)
        plt.xlabel("Temperature (C)")
        plt.ylabel("Bit Error Rate (%) ")
        plt.show()

def transmissionrate(pairs):
    original = dict(copy.deepcopy(pairs))
    normalize(pairs)
    for key in pairs:
        transmissionrate = extractDigits(original[key][0].split("_")[2])
        fps = extractDigits(original[key][0].split("_")[3])
        
        ber = getBer(pairs[key][1]["bit"], pairs[key][0]["Bit"], transmissionrate, fps, precision)
        pairs[key] = ber
    x_vals = x_values(dict(sorted(pairs.items())))
    y_vals =  y_values(dict(sorted(pairs.items())))

    plot_type = str(input("Plot type: "))
    if plot_type.lower() == "scatter":
        plt.scatter(x_vals ,y_vals)
        plt.xlabel('Transmission Rate')
        plt.ylabel('Bit Error Rate')
        plt.show()
    elif plot_type.lower() == "bar":
        plt.bar(x_vals, list(pairs.values()), color ='blue',
        width = 0.4)
        plt.xlabel("Transmission Rate (Hz)")
        plt.ylabel("Bit Error Rate (%)")
        plt.show()
    
def pH(pairs):
    original = dict(copy.deepcopy(pairs))
    normalize(pairs)
    for key in pairs:
        transmissionrate = extractDigits(original[key][0].split("_")[2])
        fps = extractDigits(original[key][0].split("_")[3])
        
        ber = getBer(pairs[key][1]["bit"], pairs[key][0]["Bit"], transmissionrate, fps, precision)
        pairs[key] = ber
    x_vals = x_values(dict(sorted(pairs.items())))
    y_vals =  y_values(dict(sorted(pairs.items())))

    plot_type = str(input("Plot type: "))
    if plot_type.lower() == "scatter":
        plt.scatter(x_vals ,y_vals)
        plt.title("Bit Error Rate VS. pH")
        plt.xlabel('pH')
        plt.ylabel('Bit Error Rate (%)')
        plt.show()
    elif plot_type.lower() == "bar":
        plt.bar(x_vals, list(pairs.values()), color ='blue',
        width = 0.4)
        plt.xlabel("Transmission Rate (Hz)")
        plt.ylabel("Bit Error Rate (%)")
        plt.show() 

def salinity(pairs):
    original = dict(copy.deepcopy(pairs))
    normalize(pairs)
    for key in pairs:
        transmissionrate = extractDigits(original[key][0].split("_")[2])
        fps = extractDigits(original[key][0].split("_")[3])
        
        ber = getBer(pairs[key][1]["bit"], pairs[key][0]["Bit"], transmissionrate, fps, precision)
        pairs[key] = ber
    x_vals = x_values(dict(sorted(pairs.items())))
    y_vals =  y_values(dict(sorted(pairs.items())))

    plot_type = str(input("Plot type: "))
    if plot_type.lower() == "scatter":
        plt.scatter(x_vals ,y_vals)
        plt.xlabel('Salinity')
        plt.ylabel('Bit Error Rate (%)')
        plt.show()
    elif plot_type.lower() == "bar":
        plt.bar(x_vals, list(pairs.values()), color ='blue',
        width = 0.4)
        plt.xlabel("Transmission Rate (Hz)")
        plt.ylabel("Bit Error Rate (%)")
        plt.show()   

def turbidity(pairs):
    original = dict(copy.deepcopy(pairs))
    normalize(pairs)
    for key in pairs:
        transmissionrate = extractDigits(original[key][0].split("_")[2])
        fps = extractDigits(original[key][0].split("_")[3])
        
        ber = getBer(pairs[key][1]["bit"], pairs[key][0]["Bit"], transmissionrate, fps, precision)
        pairs[key] = ber
    x_vals = x_values(dict(sorted(pairs.items())))
    y_vals =  y_values(dict(sorted(pairs.items())))

    plot_type = str(input("Plot type: "))
    if plot_type.lower() == "scatter":
        plt.scatter(x_vals ,y_vals)
        plt.xlabel('Turbidity')
        plt.ylabel('Bit Error Rate (%)')
        plt.show()
    elif plot_type.lower() == "bar":
        plt.bar(x_vals, list(pairs.values()), color ='blue',
        width = 0.4)
        plt.xlabel("Transmission Rate (Hz)")
        plt.ylabel("Bit Error Rate (%)")
        plt.show()

def averages():
    pairs_list = [TEMPERATURE_PAIRS, TRANSMISSIONRATE_PAIRS, PH_PAIRS, TURBIDITY_PAIRS, SALINITY_PAIRS]
    names = ["Temperature", "Transmission", "pH", "Turbidity", "Salinity"]
    new_pairs = []
    x_vals = []
    y_vals = []
    stds = []
    i = -1
        

    for pair in pairs_list:
        original = dict(copy.deepcopy(pair))
        normalize(pair)
        for key in pair:
            transmissionrate = extractDigits(original[key][0].split("_")[2])
            fps = extractDigits(original[key][0].split("_")[3])
        
            ber = getBer(pair[key][1]["bit"], pair[key][0]["Bit"], transmissionrate, fps, precision)
            pair[key] = ber

    for pair in pairs_list:
        if not pair:
            continue
        i += 1
        avg = sum(pair.values()) / len(pair)
        std = np.std(list(pair.values()))
        stds.append(std)
        new_pairs.append({names[i]: avg})
    #print(stds)
    
    for val in new_pairs:
        x_vals.append(next(iter(val)))
        y_vals.append(next(iter(val.items()))[1])

    plt.bar(x_vals, y_vals, color ='blue', yerr=stds, capsize=5,
        width = 0.4)
    plt.xlabel("Method")
    plt.ylabel("Average Bit Error Rate (%)")
    plt.show()
#print(TEMPERATURE_PAIRS)
#print(TRANSMISSIONRATE_PAIRS)

print("This tool is for analyzing the BERs as they relate to the various variables the VLC system was tested with.\n1. transmissionrate\n2. temperature\n3. pH\n4. Turbidity\n5. Salinity\n6. Average (compares the average BER of each category.) ")
option = input("Enter your selection: ")


if option == "transmissionrate":
    transmissionrate(TRANSMISSIONRATE_PAIRS)
elif option == "temperature":
    temperature(TEMPERATURE_PAIRS)
elif option == "pH":
    pH(PH_PAIRS)
elif option == "turbidity":
    turbidity(TURBIDITY_PAIRS)
elif option == "salinity":
    salinity(SALINITY_PAIRS)
elif option == "average":
    averages()
elif option.lower() == "break":
    cont = False
else:
    print("Invalid option chosen")
