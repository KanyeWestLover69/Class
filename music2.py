import vlc

def play_song(song):
    try:
        player = vlc.MediaPlayer(song)
        player.play()
        print(f"Playing: {song}")
        while player.get_state() != vlc.State.Ended:
            pass
        player.stop()
    except Exception as e:
        print(f"Error playing song: {e}")

# List of songs
songs = [
    "Never gonna give you up.mp3",
    "beauty and a beat.mp3",
    "what do you mean.mp3",
    "ghost.mp3",
    "one less.mp3",
]

while True:
    try:
        print("\nPick a song (1-5):")
        for i, song in enumerate(songs, start=1):
            print(f"{i}. {song}")
        choice = int(input("Enter your choice (1-5): ")) - 1
        if choice < 0 or choice >= len(songs):
            raise ValueError("Invalid choice")
        play_song(songs[choice])
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Exiting...")
        break