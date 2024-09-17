class Applicant:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

class AdmissionSystem:
    def __init__(self):
        self.applicants = []

    def add_applicant(self, name, instrument):
        applicant = Applicant(name, instrument)
        self.applicants.append(applicant)

    def search_applicant(self, name):
        for applicant in self.applicants:
            if applicant.name == name:
                return applicant
        return None

    def get_exam_list(self, instrument):
        exam_list = []
        for applicant in self.applicants:
            if applicant.instrument == instrument:
                exam_list.append(applicant.name)
        return exam_list

class MusicApplicant(Applicant):
    def __init__(self, name, instrument, music_genre):
        super().__init__(name, instrument)
        self.__music_genre = music_genre 

    def get_music_genre(self):
        return self.__music_genre

    def set_music_genre(self, music_genre):
        self.__music_genre = music_genre

    music_genre = property(get_music_genre, set_music_genre)

    def display_info(self):
        print(f"{self.name} plays {self.instrument} in {self.music_genre} genre.")


class MusicAdmissionSystem(AdmissionSystem):
    def __init__(self):
        super().__init__()
        self.__applicants = []

    def get_applicants(self):
        return self.__applicants

    def set_applicants(self, applicants):
        self.__applicants = applicants

    applicants = property(get_applicants, set_applicants)
    
    def get_genre_exam_list(self, genre):
        exam_list = []
        for applicant in self.applicants:
            if isinstance(applicant, MusicApplicant) and applicant.music_genre.lower() == genre.lower():
                exam_list.append(applicant.name)
        return exam_list

    def add_applicant(self, name, instrument, music_genre):
        applicant = MusicApplicant(name, instrument, music_genre)
        self.applicants.append(applicant)
    
    def sort_applicants(self, key='name'):
        if key == 'name':
            self.applicants.sort(key=lambda x: x.name.lower())
        elif key == 'instrument':
            self.applicants.sort(key=lambda x: x.instrument.lower())
        else:
            print("Invalid sort key.")

    def display_all_applicants(self):
        for applicant in self.applicants:
            print(f"Name: {applicant.name}, Instrument: {applicant.instrument}, Genre: {applicant.music_genre}")
