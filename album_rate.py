## album_rate.py
# stores title, artist, genre and rating of an music albums
# allows the user to add, delete and edit an album
# allows user to rate album and recommends album of same genre

def printing(dictionary):
    for id, song in dictionary.items():
        """
        Accepts a dictionary , loops through it and
        prints out the album's information
        """
        print("Id: {}\tTitle: {}\tArtist: {}\tGenre: {}\tRating: {}".format (id,
                                                                        song["title"],
                                                                        song["artist"],
                                                                        song["genre"],
                                                                        song["rating"],))

def add(dictionary):
dictionary.update({num{"title": , "artist": , "genre}})
    
#def edit():

def delete():
    del dictionary[""]
    return dictionary

#def rate():

#def recommend():


albums = {}
if __name__ == "__main__":
    albums = {1:{"title":"Blond", "artist":"Frank Ocean", "genre":"Contemporary R&B", "rating":98},
              2:{"title":"Call Me If You Get Lost", "artist":"Tyler the Creator", "genre":"Hip-Hop / Rap", "rating":97},
              3:{"title":"Ctrl", "artist":"SZA", "genre":"R&B / Soul", "rating":98}}
    printing(albums)
