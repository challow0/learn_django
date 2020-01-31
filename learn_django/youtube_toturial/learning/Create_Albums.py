from music.models import Ablum, Song
from music.models import Album, Song
Album.objects.all()
a = Album(artist='Taylor Swift',album_title='Red',genre='Country',album_logo="https://imgchr.com/i/Kb9vFO")
a.save()
a.artist
a.album_title
a.id
a.pk
b = Album()
b.artist = "Myth"
b.album_title = "High School"
b.genre = "Punk"
b.album_logo = ""
b.album_logo = ""
b.album_logo = "https://imgchr.com/i/KbC100"
b.saz
b.save()
a.artist
b.artist
b.album_title = "Middle School"
b.album_title
Album.objects.all()
%hist -f Create_Albums.py
