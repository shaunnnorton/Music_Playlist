class Song:
    def __init__(self,data):
        self.data = data
        self.next = None

class PlayList():
    def __init__(self):
        self.head = None
        self.tail = None
    

    def append(self,data):
        new_song = Song(data)
        if self.tail is not None:
            self.tail.next = new_song
        self.tail = new_song
        if self.head is None:
            self.head = new_song
    
    def prepend(self,data):
        new_song = Song(data)
        new_song.next = self.head
        self.head = new_song
        if self.tail is None:
            self.tail = new_song

    def print_songs(self):
        current_song = self.head
        print("_________________SONGS IN YOUR PLAYLIST_________________")
        while current_song is not None:
            print(current_song.data)
            current_song = current_song.next
        if self.head is None:
            print("Your PlayList is Empty")
        print("__________________END OF YOUR PLAYLIST__________________")