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

def add(dictionary, num):
    dictionary[num] = {}
    dictionary[num]["title"] = input("Album title: ")
    dictionary[num]["artist"] = input("Artist: ")
    dictionary[num]["genre"] = input("Genre: ")
    dictionary[num]["rating"] = input("Rating: ")
    return dictionary

def delete(dictionary):
    del_id = int(input("Id of the album you would like to delete: "))
    del dictionary[del_id]
    return dictionary

def edit(dictionary):
    edit_id = int(input("Id of the album you'd like to edit: "))
    if edit_id in dictionary:
        edit_value = input("Which value would you like to edit? \n"
                           "title?\n"
                           "artist?\n"
                           "genre?\n"
                           "rating?\n")
        if edit_value == "title":
            new_title = input("Enter new title: ")
            dictionary[edit_id]["title"] = new_title
        elif edit_value == "artist":
            new_artist = input("Enter new artist: ")
            dictionary[edit_id]["artist"] = new_artist
        elif edit_value == "genre":
            new_genre = input("Enter new genre: ")
            dictionary[edit_id]["genre"] = new_genre
        elif edit_value == "rating":
            new_rating = int(input("Enter new rating: "))
            dictionary[edit_id]["rating"] = new_rating
        return dictionary 

#def rate():

#def recommend():

if __name__ == "__main__":
    albums = {1: {"title":"Blond", "artist":"Frank Ocean", "genre":"Contemporary R&B", "rating":98},
              2: {"title":"Call Me If You Get Lost", "artist":"Tyler the Creator", "genre":"Hip-Hop / Rap", "rating":97},
              3: {"title":"Ctrl", "artist":"SZA", "genre":"R&B / Soul", "rating":98}}
    curr_id = 4
    while True:
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
            add(albums, curr_id)
        elif mode == 3:
            delete(albums)
            curr_id = curr_id - 1
        elif mode == 4:
            edit(albums)
        elif mode == 5:
            rate(albums)
            recommend(albums)
        elif mode == 6:
            break

