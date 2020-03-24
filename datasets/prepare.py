file = open('questions.csv', 'r+')

content = file.read()

file.seek(0)

file.write(content.replace('.\n', ';\n').replace('.', ';'))

file.truncate()

file.close()