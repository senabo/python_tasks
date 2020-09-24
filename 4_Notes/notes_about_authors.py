import csv


class Notes:
    """
    Class that allows users to work with notes about books authors
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = []
        self.write_data = {}
        self.fieldnames = ['author_name', 'note', 'rating']

    def read(self):
        """Reading csv file and writing data into self.notes"""

        with open(self.file_name) as file_obj:
            reader = csv.DictReader(file_obj, delimiter=',')
            self.notes = []
            for line in reader:
                self.notes.append(line)

    def print(self):
        """Print notes to console"""

        self.read()
        for line in self.notes:
            print(line)

    def write_notes(self, author, note, rating):
        """Write notes to file"""

        self.__prepare_data_for_writing([author, note, rating])
        self.read()

        with open(self.file_name, 'a',) as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=self.fieldnames)

            if not self.notes:
                writer.writeheader()

            writer.writerow(self.write_data)

    def __prepare_data_for_writing(self, data):
        """Checking the rating and creating dictionary to writing"""

        try:
            rating = float(data[2])
            if rating > 1 or rating < 0:
                data[2] = '0'
        except ValueError:
            data[2] = '0'

        self.write_data = dict(zip(self.fieldnames, data))

    def get_author_highest_rating(self):
        """Return the author with highest rating"""

        self.read()
        try:
            return max(self.notes, key=lambda x: x['rating'])['author_name']
        except ValueError:
            print('Error. Wrong rating data.')

    def get_author_lowest_rating(self):
        """Return the author with lowest rating"""

        self.read()
        try:
            return min(self.notes, key=lambda x: x['rating'])['author_name']
        except ValueError:
            print('Error. Wrong rating data.')

    def get_average_rating(self):
        """Return average rating among all the authors """

        self.read()
        try:
            list_ratings = list(map(
                    lambda x: float(x['rating']),
                    self.notes
                ))
            return sum(list_ratings)/len(list_ratings)
        except ValueError:
            print('Error. Wrong rating data.')
