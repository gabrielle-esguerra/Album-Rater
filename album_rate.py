## album_rater.py
# stores title, artist, genre and rating of an music albums
# allows the user to add, delete and edit an album
# allows user to rate album and recommends album of same genre

def printing(dictionary):
    for id, album in dictionary.items():
        """
        Accepts a dictionary , loops through it and
        prints out the album's information
        """
        print("Id: {}\tTitle: {}\tArtist: {}\tGenre: {}\tRating: {}".format (id,
                                                                        album["title"],
                                                                        album["artist"],
                                                                        album["genre"],
                                                                        album["rating"],))

def add(dictionary):
    num = len(dictionary) + 1
    dictionary[num] = {}
    dictionary[num]["title"] = input("Album title: ")
    dictionary[num]["artist"] = input("Artist: ")
    dictionary[num]["genre"] = input("Genre: ")
    dictionary[num]["rating"] = input("Rating: ")
    return dictionary

def delete():
    del dictionary[""]
    return dictionary

#def edit():

#def rate():

#def recommend():

if __name__ == "__main__":
    albums = {1: {"title":"Blond", "artist":"Frank Ocean", "genre":"Contemporary R&B", "rating":98},
              2: {"title":"Call Me If You Get Lost", "artist":"Tyler the Creator", "genre":"Hip-Hop / Rap", "rating":97},
              3: {"title":"Ctrl", "artist":"SZA", "genre":"R&B / Soul", "rating":98}}
    mode = int(input("\nMenu \n"
                     "1. Print out all albums \n"
                     "2. Add an album \n"
                     "3. Delete an album \n"
                     "4. Edit an album\n"
                     "5. Rate an album \n"
                         "6. Exit \n"))
    if mode == 1:
        printing(albums)
    elif mode == 2:
        add(albums)
    elif mode == 3:
        delete(albums)
    elif mode == 4:
        edit(albums)
    elif mode == 5:
        rate(albums)
    #elif mode == 6:
       
