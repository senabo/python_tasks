from notes_about_authors import Notes


notes = Notes('4_Notes/test.csv')

notes.print()

notes.write_notes('Ostin', 'note about os', '0.6')
notes.write_notes('Charlie', 'note about ch', '0.87')

print('After writing: ')
notes.print()

print('Highest rating:', notes.get_author_highest_rating())
print('Lowest rating:', notes.get_author_lowest_rating())
print('Average rating: ', notes.get_average_rating())
