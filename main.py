def newSong(title, artist, genre):
    return {
        "title": title,
        "artist": artist,
        "genre": genre
    }

def LinearSearch(favList, song):
    for i in range(len(favList)):
        if favList[i]["title"] == song:
            return i
    return - 1

songs = []
songs.append(newSong("Here With Me", "d4vd", "pop"))
songs.append(newSong("Wiss", "mike dimes", "rap"))
songs.append(newSong("Crossing field", "lisa", "j-pop"))
songs.append(newSong("Anti fragile", "Le Sserafim", "k-pop"))
songs.append(newSong("Goo Gaa", "siwon", "pop"))

favList = []

loop = True
while loop:


#Print main menu
    print("Main Menu")
    print("1. Display all song")
    print("2. Display some of the song (filter)")
    print("3. Sort the song based on properties")
    print("4. Add to fav list")
    print("5. Remove from fav list")
    print("6. Display fav list")
    print("7. Exit")

#menu Selection
    select = input ("Enter Selection (1-6): ")

#Display all data
    if select == "1":
        print("Display all song")
        for song in songs:
            print(song["title"])

#Display some of the data(search/filter based on criteria)
    elif select == "2": 
        print("Display some of the song by searching")
        firstLetter = input("what is the first letter of the song: ")
        for song in songs:
            if song['title'][0] == firstLetter:
                print(f"{song['title']} by {song['artist']} genre: {song['genre']}")
        
#Sort the data(based on one of the properties)
    elif select == "3":
        print("sort the song based on genre")
        genreOf = input("what is the genre of the song: ")
        for song in songs:
            if song['genre'] == genreOf:
                print(f"{song['title']} by {song['artist']} genre: {song['genre']}")

#Select data to add to a favourites list 
    elif select == "4":
        print("select song to add to your fav list")
        favSong = input("what is your fav songs?")
        for song in songs:
            if song['title'] == favSong:
                favList.append(song)
                print("song has been added to fav list")
                
#Remove data from favourites list 
    elif select == "5":
        print("select song to remove from fav list")
        byeSong = input("enter a song to remove: ")
        result = LinearSearch(favList, byeSong)
        if(result == -1):
            print("song does not exist")
        else:
            favList.pop(result)
            print("song has been removed")
        
#Display favourites list 
    elif select == "6":
        print("Display favourites list")
        for song in favList:
            print(song["title"])

#EXIT
    elif select == "7":
        print("EXIT")
        loop = False
