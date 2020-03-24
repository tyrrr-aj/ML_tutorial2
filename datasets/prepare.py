file = open('questions.csv', 'r+')

content = file.read()

file.seek(0)

file.write(content.replace(';\n', '.\n'))

file.truncate()

file.close()