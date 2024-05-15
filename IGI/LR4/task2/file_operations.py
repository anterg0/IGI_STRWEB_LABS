import zipfile
import os

def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def write_results_to_file(filename, results):
    with open(filename, 'w', encoding='utf-8') as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")

def archive_results(filename):
    with zipfile.ZipFile('results.zip', 'w') as zipf:
        zipf.write(filename)
        print('These files were successfully archived:')
        for file in zipf.namelist():
            print(f'File name: {zipf.getinfo(file).filename}')
            print(f'Compressed size: {zipf.getinfo(file).compress_size}')
            print(f'Uncompressed size: {zipf.getinfo(file).file_size}')

    os.remove(filename)