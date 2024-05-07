import csv
import pickle
from classes import MusicApplicant

class FileHandler:
    @staticmethod
    def save_to_csv(data, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Instrument', 'Genre'])  # Добавляем 'Genre' в заголовок
            for item in data:
                writer.writerow([item.name, item.instrument, getattr(item, 'music_genre', '')])

    @staticmethod
    def load_from_csv(filename):
        data = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаем заголовок
            for row in reader:
                name, instrument, genre = row
                data.append(MusicApplicant(name, instrument, genre))
        return data

    @staticmethod
    def save_to_pickle(data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_from_pickle(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
