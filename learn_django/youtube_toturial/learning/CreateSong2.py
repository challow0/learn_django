from music.models import Album,Song
album1.song_set.all()
album1 = Album.objects.get(pk=1)
album1.artist
song = Song()
song.album = album1
song.file_type = 'mp3'
song.song_title = 'I love my boyfirend'
song.save()
album1.song_set.all()
album1.song_set.create(song_title = 'I love bacon',file_type = 'mp3')
album1.song_set.create(song_title = 'Bucky is Lucky',file_type = 'mp3')
album1.song_set.create(song_title = 'Ice Cream',file_type = 'mp3')
song = album1.song_set.create(song_title = 'Ice Cream',file_type = 'mp3')
song.album
song.song_title
album1.song_set.all()
album1.song_set.count()
%hist -f CreateSong2.py
