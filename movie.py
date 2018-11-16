print("Hi, welcome to movie rating")

begin = input("Would you like to rate a movie? (Yes / No): ")

if begin == "Yes":
    movie1 = input("Name a video that you saw recently: ")
    movie1_rating = (float(input("On a scale of 1 to 5, how many stars will you rate the movie: ")))

else:
    print("Cya")

def anothermovie():
    anothermovie = input("Would you like to rate another movie? ( Yes / No): ")
    anothermovie_rating = (float(input("On a scale of 1 to 5, how many stars will you rate the movie: ")))
    
if anothermovie == "Yes":
    anothermovie()

else:
    print("Hi")

#if next_movie == "Yes":
    #movie2 = input("Name another video that you saw recently: ")
    #movie2_rating = (float(input("On a scale of 1 to 5, how many stars will you rate the movie: ")))


#movie3 = input("Name a third video that you saw recently: ")
#movie3_rating = (float(input(" On a scale of 1 to 5, how many stars will you rate the movie: ")))


#if movie2_rating < movie1_rating > movie3_rating:
#    print("Your favorite movie was: {}".format(movie1))

#if movie1_rating < movie2_rating > movie3_rating:
#    print("Your favorite movie was: {}".format(movie2))

#if movie1_rating < movie3_rating > movie2_rating:
#    print("Your favorite movie was: {}".format(movie3))
