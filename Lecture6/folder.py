import os, sys

def read_folders(base_folder):
    folders = {}
    for path, folder_list, file_list in os.walk(base_folder):
        folders[path] = {'path': path,
                         'sub_folders': folder_list,
                         'images': []}
        for file in file_list:
            if os.path.splitext(file)[1].lower() == '.jpg':
                folders[path]['images'].append(file)
    return folders

def print_folders(folders):
    folder_path_list = list(folders.keys())
    folder_path_list.sort()
    for folder_path in folder_path_list:
        print('  ', folder_path, ':', folders[folder_path]['images'])

if __name__ == '__main__':
    top_folder = os.path.normpath(os.path.abspath(sys.argv[1]))
    print('Reading', top_folder, 'folder and the descendents')
    folders = read_folders(top_folder)
    #print(folders)
    print_folders(folders)
