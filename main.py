from playlist import PlayList

my_playlist = PlayList()
my_playlist.append("Country Roads")
my_playlist.append("Heart on Ice")
my_playlist.append("Rap God")
my_playlist.append("Chicken in the CornBread")
my_playlist.print_songs()
my_playlist.prepend("Apple Bottom Jeans")
my_playlist.print_songs()
my_playlist.delete_from_head()
my_playlist.print_songs()
my_playlist.delete_from_tail()
my_playlist.print_songs()