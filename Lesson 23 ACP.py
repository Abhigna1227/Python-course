my_dict = {'codingal':3,'is':2,'for':2,'Coding':1}
value_freq = {}
for value in my_dict.values():
    if value in value_freq:
        value_freq[value] += 1
    else:
        value_freq[value] = 1
print("Frequency of values in the dictionary:")
for val, freq in value_freq.items():
    print(f"{val}: {freq}")
