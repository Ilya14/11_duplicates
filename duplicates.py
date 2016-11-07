import sys
import os


def get_files_data(input_directory):
    data = {}
    for current_dir, folders, files in os.walk(input_directory):
        for file in files:
            file_attributes = {
                'path': current_dir,
                'size': os.path.getsize(current_dir + '/' + file)
            }
            if file in data:
                data[file].append(file_attributes)
            else:
                data[file] = [file_attributes]
    return data


def get_files_duplicates(files_data):
    files_duplicates = {}
    for file_name in files_data:
        file_name_duplicates_count = len(files_data[file_name])

        if file_name_duplicates_count > 1:

            file_duplicates_indexes = []
            for i in range(0, file_name_duplicates_count):
                size = files_data[file_name][i]['size']
                for j in range(i + 1, file_name_duplicates_count):
                    if size == files_data[file_name][j]['size']:
                        file_duplicates_indexes.append(i)
                        file_duplicates_indexes.append(j)
            file_duplicates_indexes = set(file_duplicates_indexes)

            if file_duplicates_indexes:
                files_duplicates[file_name] = [files_data[file_name][ind] for ind in file_duplicates_indexes]

    return files_duplicates


def print_files_duplicates(files_duplicates):
    for file_name in files_duplicates:
        print('File {0} has duplicates in the following directories:'.format(file_name))
        for duplicate in files_duplicates[file_name]:
            print('{0} (Size: {1})'.format(
                duplicate['path'] + '/' + file_name,
                duplicate['size']
            ))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        input_directory = input('Enter directory > ')
    else:
        if len(sys.argv) > 2:
            print("Error: too many parameters are transferred")
            sys.exit(1)
        input_directory = sys.argv[1]

    files_data = get_files_data(input_directory)
    files_duplicates = get_files_duplicates(files_data)
    print_files_duplicates(files_duplicates)
