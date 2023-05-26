import csv

def add_dictionary_to_csv(dictionary, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        
        # Retrieve the current number of rows in the CSV file
        with open(filename, 'r') as file_read:
            reader = csv.reader(file_read)
            row_count = sum(1 for row in reader)
        
        # Add the ID as the first column in the row
        row = [row_count + 1] + list(dictionary.values())
        
        writer.writerow(row)

# Example dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Call the function to add dictionary values to CSV
add_dictionary_to_csv(my_dict, 'data.csv')
