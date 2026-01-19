

music = {
            "back in black": "https://www.youtube.com/watch?v=XgWUDbYfNe4&pp=ygUKYmVzdCBzb25ncw%3D%3D",
            "believer": "https://youtu.be/7wtfhZwyrcc",
            "faded": "https://youtu.be/60ItHLz5WEA"
}

def clean_search_text(command, remove_words):
    text = command.lower()
    for word in remove_words:
        text = text.replace(word, "")
    return " ".join(text.split())



def getVideoLink(command):
    video = clean_search_text(
        command,
        remove_words=["youtube", "play", "search", "for", "on"]
    )

    query = video.replace(" ", "+")
    return video, f"https://www.youtube.com/results?search_query={query}"


def getSongLink(command):
    song = clean_search_text(
        command,
        remove_words=["play", "song", "music", "on"]
    )

    query = song.replace(" ", "+")
    return song, f"https://music.youtube.com/search?q={query}"



