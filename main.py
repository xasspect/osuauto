import os
import shutil

source_folder = 'C:/Users/xasspect/Downloads'

target_folder = 'C:/Users/xasspect/AppData/Local/osu!/Songs'

extension = '.osz'

files_to_move = [file for file in os.listdir(source_folder) if file.endswith(extension)]

for file in files_to_move:
    source_file_path = os.path.join(source_folder, file)
    target_file_path = os.path.join(target_folder, file)
    shutil.move(source_file_path, target_file_path)

