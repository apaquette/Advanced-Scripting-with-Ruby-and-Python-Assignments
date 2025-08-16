import pandas as pd

generatorsDict = {
    "Generator 1":{
        "Volt 1":122.5,
        "Volt 2":122.7,
        "Volt 3":123.0
    },
    "Generator 2":{
        "Volt 1":120.2,
        "Volt 2":127.0,
        "Volt 3":123.1
    },
    "Generator 3":{
        "Volt 1":121.7,
        "Volt 2":124.9,
        "Volt 3":126.0
    },
    "Generator 4":{
        "Volt 1":122.9,
        "Volt 2":123.8,
        "Volt 3":126.7
    },
    "Generator 5":{
        "Volt 1":121.5,
        "Volt 2":124.7,
        "Volt 3":122.6
    }
}

generatorsDataFrame = pd.DataFrame.from_dict(generatorsDict)

print(f"{generatorsDataFrame}\n")
print(f"{generatorsDataFrame.T}\n")
gen2Volt = generatorsDataFrame.get("Generator 2")
print(f"Generator 2 Voltages:\n{gen2Volt}\n")
mean = generatorsDataFrame.get("Generator 3").mean()
print(f"Generator 3 Mean Voltage: {mean} Volts\n")



max = generatorsDataFrame.max().max()
filter = (generatorsDataFrame == max).any()
loc = generatorsDataFrame.loc[:, filter].columns.values[0]
print(f"Maximum Voltage: {max} Volts @{loc}")