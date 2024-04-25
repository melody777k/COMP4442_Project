filename = "dataset/detail_record_2017_01_02_08_00_00"

with open(filename, 'r', encoding='utf-8') as file:
    data = file.readlines()

grouped_data = {}

for item in data:
    columns = item.strip().split(",")
    key = columns[0]
    values = [columns[0], columns[4], columns[7]]
    if key in grouped_data:
        grouped_data[key].append(values)
    else:
        grouped_data[key] = [values]

output_filename = "b.txt"

with open(output_filename, 'w', encoding='utf-8') as output_file:
    for key, values in grouped_data.items():
        output_file.write(f"DriverID: {key}\n")
        for value in values:
            output_file.write(f"Speed: {', '.join(value)}\n")
        output_file.write("\n")