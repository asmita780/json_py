# import json

# # JSON string
# employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
# print("This is JSON", type(employee))

# print("\nNow convert from JSON to Python")

# # Convert string to Python dict
# employee_dict = json.loads(employee)
# print("Converted to Python", type(employee_dict))
# print(employee_dict)

# # import module
# import json

# # Data to be written
# data = {
# 	"user": {
# 		"name": "satyam kumar",
# 		"age": 21,
# 		"Place": "Patna",
# 		"Blood group": "O+"
# 	}
# }

# # Serializing json and
# # Writing json file
# with open( "datafile.json" , "w" ) as write:
# 	json.dump( data , write )

import json
data = {"username":"asmita",
        "password":"asmi123",
         "age":"18",
   "jender":"famle"}

filename = 'data.json'

with open(filename, 'w') as file_object:

    json.dump(data, file_object)


# print(type(data))
# trass = json.dumps (data)
# print(type(trass))






