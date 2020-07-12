import csv

track, artist, album = [],[],[]
with open('stinky_crate.csv', 'r') as datafile:
    csv_reader = csv.reader(datafile)
    next(csv_reader)
    for i in csv_reader:
        track.append(str(i[1]))
        artist.append(str(i[2]))
        album.append(str(i[3]))
    
album_count = {}
for i in album:
    album_count[i] = album.count(i)
print(album_count)
