from urllib.request import urlopen
import urllib.request
import json
import os
import MyKey

title = input("Enter movie title : ")

endpoint = "http://www.omdbapi.com/?apikey="
key = MyKey.api_key #get your api_key from OMDB and replace it with MyKey.api_key
parameter = "&t="+title
url = endpoint+key+parameter


source = urlopen(url).read()

try:
    data = json.loads(source)

    #movie info
    movie_title = data["Title"]
    movie_rated = data["Rated"]
    movie_released_year = data["Released"]
    movie_runtime = data["Runtime"]
    movie_genre = data["Genre"]
    movie_Director = data["Director"]
    movie_writer = data["Writer"]
    movie_actors = data["Actors"]
    movie_plot = data["Plot"]
    movie_language = data["Language"]
    movie_country = data["Country"]
    movie_awards = data["Awards"]
    movie_ratings = data["Ratings"]
    movie_metascore = data["Metascore"]
    movie_imdb_rating = data["imdbRating"]
    movie_box_office = data["BoxOffice"]
    movie_production = data["Production"]

    print()
    print(f"Title : {movie_title}\n"
          f"Rated : {movie_rated}\n"
          f"Released : {movie_released_year}\n"
          f"Runtime : {movie_runtime}\n"
          f"Genre : {movie_genre}\n"
          f"Director : {movie_Director}\n"
          f"Writer : {movie_writer}\n"
          f"Actors : {movie_actors}\n"
          f"Plot : {movie_plot}\n"
          f"Language : {movie_language}\n"
          f"Country : {movie_country}\n"
          f"Awards : {movie_awards}\n"
          )
    for rating in movie_ratings:
        print(f"Source : {rating['Source']} = {rating['Value']}\n")
    print(f"Metascore : {movie_metascore}\n"
          f"IMDB : {movie_imdb_rating}\n"
          f"Box Office : {movie_box_office}\n"
          f"Production : {movie_production}\n"
          )
    print()
    # downloading poster
    urllib.request.urlretrieve(data["Poster"], title + ".jpg")
    ans = input("Show poster? (y/n)")
    if ans=='y':
        # showing poster in console
        os.system(title + ".jpg")
    print()
    ans = input("Delete poster ? (y/n)")
    if ans=='y':
        os.remove(title+".jpg")

except KeyError as ke:
    print(f"There is no movie named \"{title}\"")
#print full json output
#print(json.dumps(data,indent=2))
