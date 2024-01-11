input_string = input("Введите строку: ")
first_h_index = input_string.find("h")
last_h_index = input_string.rfind("h")

if first_h_index != -1 and last_h_index != -1:
    start = input_string[:first_h_index + 1]
    middle = input_string[first_h_index + 1:last_h_index]
    end = input_string[last_h_index:]
    
    replaced_middle = middle.replace("h", "H")
    
    result_string = start + replaced_middle + end
else:
    result_string = input_string

print(result_string)
