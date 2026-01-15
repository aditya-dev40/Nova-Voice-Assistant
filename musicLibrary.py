

music = {
            "back in black": "https://www.youtube.com/watch?v=XgWUDbYfNe4&pp=ygUKYmVzdCBzb25ncw%3D%3D",
            "believer": "https://youtu.be/7wtfhZwyrcc",
            "faded": "https://youtu.be/60ItHLz5WEA"
}



def getSongLink(command):
    song = command.lower().replace("play", "").strip()

    if song in music:
        return song, music[song]

    song_query = song.replace(" ", "+")
    return song, f"https://music.youtube.com/search?q={song_query}"


