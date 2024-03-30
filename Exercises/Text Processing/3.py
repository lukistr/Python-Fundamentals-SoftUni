def subtract_file_name_and_extension(file_path):
    file_name = file_path.split('\\')[-1]
    file_name, extension = file_name.split('.')
    return file_name, extension

file_path = input()

result = subtract_file_name_and_extension(file_path)

print("File name:", result[0])
print("File extension:", result[1])