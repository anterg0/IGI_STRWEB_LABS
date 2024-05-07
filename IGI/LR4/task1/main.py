from classes import MusicAdmissionSystem
from file_handler import FileHandler

def main():
    system = MusicAdmissionSystem() 

    while True:
        print("\n1. Add Music Applicant")
        print("2. Search Applicant")
        print("3. Get Exam List by Genre")
        print("4. Sort Applicants")
        print("5. Display All Applicants")
        print("6. Load Applicants from File")
        print("7. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter applicant's name: ")
            instrument = input("Enter applicant's instrument: ")
            genre = input("Enter applicant's music genre: ")
            system.add_applicant(name, instrument, genre)
        elif choice == '2':
            name = input("Enter applicant's name to search: ")
            applicant = system.search_applicant(name)
            if applicant:
                print(f"Applicant found: {applicant.name}, {applicant.instrument}, {applicant.music_genre}")
            else:
                print("Applicant not found.")
        elif choice == '3':
            genre = input("Enter music genre to get exam list: ")
            exam_list = system.get_genre_exam_list(genre)
            print(f"Exam List for {genre} genre: {exam_list}")
        elif choice == '4':
            sort_key = input("Enter sort key ('name' or 'instrument'): ")
            system.sort_applicants(sort_key)
            print("Applicants sorted successfully.")
        elif choice == '5':
            system.display_all_applicants()
        elif choice == '6':
            file_type = input("Enter file type (csv/pickle): ")
            if file_type.lower() == 'csv':
                filename = 'music_applicants.csv'
                data = FileHandler.load_from_csv(filename)
                system.applicants = data
                print("Data loaded from CSV successfully.")
            elif file_type.lower() == 'pickle':
                filename = 'music_applicants.pickle'
                data = FileHandler.load_from_pickle(filename)
                system.applicants = data
                print("Data loaded from pickle successfully.")
            else:
                print("Invalid file type.")
        elif choice == '7':
            FileHandler.save_to_csv(system.applicants, 'music_applicants.csv')
            FileHandler.save_to_pickle(system.applicants, 'music_applicants.pickle')
            print("Data saved successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
