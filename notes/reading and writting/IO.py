with open('newfile.txt', 'r') as file:
    file_data = file.read()

file_data = file_data.replace('spam', 'knowledge')

with open('bye_spam.txt', 'w') as new_file:
    new_file.write(file_data)