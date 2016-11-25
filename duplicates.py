import argparse
import os


def get_files_data(input_directory):
    data = {}
    for current_dir, folders, files in os.walk(input_directory):
        for file in files:
            key = (file, os.path.getsize('{0}/{1}'.format(current_dir, file)))
            if key in data:
                data[key].append(current_dir)
            else:
                data[key] = [current_dir]
    return data


def get_files_duplicates(files_data):
    files_duplicates = {}
    for key in files_data:
        if len(files_data[key]) > 1:
            files_duplicates[key] = files_data[key]
    return files_duplicates


def print_files_duplicates(files_duplicates):
    for key in files_duplicates:
        print('File {0} (size: {1}) has duplicates in the following directories:'.format(key[0], key[1]))
        for path in files_duplicates[key]:
            print('{0}/{1}'.format(path, key[0]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for search of files duplicates')
    parser.add_argument('dir', help='Directory for search')
    args = parser.parse_args()
    files_data = get_files_data(args.dir)
    files_duplicates = get_files_duplicates(files_data)
    print_files_duplicates(files_duplicates)
