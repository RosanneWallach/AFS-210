
import enum
from random import shuffle


class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        


def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

playlist = [
        Song( "Jailhouse Rock", "Elvis Presely"),
        Song("Immigrant", "Led Zeppelin"),
        Song("Rocket Man", "Elton John"),
        Song("Major Tom", "David Bowie"),
        Song("Hero", "David Bowie"),
        Song("I'am Afraid of Americans", "David Bowie & Trent Reznor")
    ]

playing = 0
running = False

def get_index(playlist, title):
    for i, son in enumerate(playlist):
        if playlist[i].getTitle() == title:
            return i
    return -1

while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        title = input("Please enter a song title: ")
        artist = input("Please enter the name of the artist: ")
        playlist.append(Song(title, artist))
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        # remove song from playlist
        title = input("Please enter the title of the song to remove: ")
        song_i = get_index(playlist, title)
        if song_i < 0:
            print("Sorry! This song doesn't exist in the playlist.")
        else:
            del playlist[song_i]
            if song_i <= playing:
                playing -= 1
            print("Song Removed to Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....")
        running = True
        print("Currently playing:", playlist[playing])
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")
        if playing == len(playlist) - 1:
            playing = 0
        else:
            playing += 1
        print("Playing", playlist[playing])                  
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")
        if playing == 0:
            playing = len(playlist) - 1
        else:
            playing -= 1
        if running:
            print("Playing", playlist[playing])
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")
        shuffle(playlist)       
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        if running:
            print("Currently playing: ", end=" ")
            print(playlist[playing])
        else:
            print("No song is currently playing!")
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        for i, song in enumerate(playlist):
            print("-", i, song)
            
    elif choice == 0:
        print("Goodbye.")
        break

            
