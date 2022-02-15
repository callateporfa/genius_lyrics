# Мы хотим узнать, какие жанры у какого исполнителя есть
import json

songs = []
with open('song_info.json', encoding='utf8') as file:
    for line in file:
        songs.append(json.loads(line))

# Составляем словарь, в котором ключом будет исполнитель, а значением - множество жанров его песен
# Мы используем множества, чтобы не проводить постоянно проверку, есть ли уже в списке у этого исполнителя такой жанр или нет
artist_genres = {}
for song in songs:
    for tag in song['tags']:
        if artist_genres.get(song['primary_artist']):
            artist_genres[song['primary_artist']].add(tag)
        else:
            artist_genres[song['primary_artist']] = set(tag)

# Теперь приводим значения к спискам вместо множеств, так как в json нельзя записывать множества
for k, v in artist_genres.items():
    artist_genres[k] = list(v)

with open('genre for artist.json', 'w', encoding='utf8') as file:
    json.dump(artist_genres, file, ensure_ascii=False, indent=1)
