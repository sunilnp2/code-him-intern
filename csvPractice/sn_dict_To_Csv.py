import csv

def add_dictionary_to_csv(dictionary, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(dictionary.values())

# Example dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Call the function to add dictionary values to CSV
add_dictionary_to_csv(my_dict, 'data.csv')
