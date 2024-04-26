filename = "dataset/detail_record_2017_01_02_08_00_00"
# File name should be put here

with open(filename, 'r', encoding='utf-8') as file:
    data = file.readlines()

grouped_data = {}

for item in data:
    columns = item.strip().split(",")
    if (len(columns) > 8):
        key = columns[0]
        values = [columns[0], columns[4], columns[7]]
        if columns[13] and columns[13] == '1':
            values.append(columns[13])
        else:
            values.append("0")
        if key in grouped_data:
            grouped_data[key].append(values)
        else:
            grouped_data[key] = [values]
    else:
        key = columns[0]
        values = [columns[0], columns[4], columns[7], "0"]
        if key in grouped_data:
            grouped_data[key].append(values)
        else:
            grouped_data[key] = [values]


output_filename = "resultB.txt"

with open(output_filename, 'w', encoding='utf-8') as output_file:
    for key, values in grouped_data.items():
        # output_file.write(f"{key}\n")
        for value in values:
            output_file.write(f"{','.join(value)}\n")
        # output_file.write("\n")