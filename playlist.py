class Song:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class PlayList():
    def __init__(self):
        self.head = None
        self.tail = None
    

    def append(self,data):
        new_song = Song(data)
        if self.tail is not None:
            self.tail.next = new_song
            new_song.previous = self.tail
        self.tail = new_song
        if self.head is None:
            self.head = new_song
    
    def prepend(self,data):
        new_song = Song(data)
        new_song.next = self.head
        if self.head is not None:
            self.head.previous = new_song
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

    def delete_from_head(self):
        self.head = self.head.next
        self.head.previous = None


    def delete_from_tail(self):
        self.tail.previous.next = None
        self.tail = self.tail.previous

    def find(self,item):
        current = self.head
        while current is not None:
            if current.data is item:
                return True
            current = current.next

        return False

    def delete(self,item):
        current = self.head
        while current is not None:
            if current.data is item:
                current.previous.next = current.next
                current.next.previous = current.previous
                print(f"Removed {item}")
                return
            current = current.next
        print(f"{item} was not in the playlist")

    def reverse(self):
        current = self.tail
        self.tail = self.head
        self.head = current
        while current is not None:
            nxt = current.previous
            current.previous = current.next
            current.next = nxt
            current = current.next