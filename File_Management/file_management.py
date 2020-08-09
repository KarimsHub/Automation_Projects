import os
from datetime import date
import pandas as pd


# Looping over files in a specific directory (has to be in the same directory as the script)
data_location = 'Example_Folder/Another_Folder/'
file_list = []
for file in os.listdir(data_location):
    file_list.append(file)

print(file_list)

# Writing new Files
data = {'file_names' : file_list } # creating a dictionary with all file names included
file_df = pd.DataFrame(data)# creating a data framework to 
print(file_df)
new_file_directory = 'Example_Folder/Another_Folder2/' # creating a new directory to a new folder
today = date.today()
#file_df.to_csv(new_file_directory + 'example_file -' + str(today) + '.csv' )

# Moving Files (and not copying them!)
#for file in os.listdir(data_location):
#    os.rename(data_location + file, new_file_directory + file)

# Reading through Files for a specific string
string_to_find = 'Karim'
directory_to_search = 'Example_Folder/Another_Folder2/'
karim_docs = [] # once we found the document with the string we want them to put in a list
for file in os.listdir(directory_to_search):
    with open(directory_to_search + file) as f: # going through this directory, opening the files and creating them as an object called f
        if string_to_find in f.read():
            karim_docs.append(file)

print(karim_docs)

