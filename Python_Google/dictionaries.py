x = {}
print(type(x))

file_ext = {"jpeg":23, "txt":43, "pdf":10, "py":22}
for ext in file_ext:
    print(ext)

for ext, value in file_ext.items():
    print(ext, value)

file_ext.keys()

file_ext.values()

for value in file_ext.values():
    print(value)

del file_ext["py"]
print(file_ext)

file_ext["py"] = 29
print(file_ext)

"html" in file_ext
"jpeg" in file_ext

#defining a script with dictionary:

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result  

print(count_letters("This is my name")) 


def sum_user_server(server):
    total_use_time = 0.0
    for key, value in server.items():
        total_use_time += server[key]
    return round(total_use_time,2)
FileServer = {"user1":2.32, "user2":4.10, "user3":1.32}
print(sum_user_server(FileServer))

def list_full_names(employee_directory):
    full_names = []
    for last_name, first_names in employee_directory.items():
        for first_name in first_names:
            full_names.append(first_name+ " "+last_name)
    return full_names
print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))

def invert_resource_dict(resource_dictionary):
    new_dictionary = {}
    for resource_group, resources in resource_dictionary.items():
        for resource in resources:
            if resource in new_dictionary:
                new_dictionary[resource].append(resource_group)
            else:
                new_dictionary[resource] = [resource_group]
    return(new_dictionary)
print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))   
             