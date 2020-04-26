import media
#import fresh_tomatoes
toy_story=media.Movie("toy story" , "story of a boy and his toy" ,
                      "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=4KPTXpQehio")
#print(toy_story.storyline)
avatar=media.Movie("avatar", " story of a marine on a alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
race3 = media.Movie("race 3","story of salman khan fucking physics",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Race_3_-_Poster.jpg/220px-Race_3_-_Poster.jpg",
                    "https://www.youtube.com/watch?v=xBht9TG7ySw")
bahubali = media.Movie("bahubali","a historical Indian drama movie for the throne",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/Baahubali_The_Beginning_Movie_Poster.jpg/220px-Baahubali_The_Beginning_Movie_Poster.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")
pati_patni_aur_vo=media.Movie("pati patni aur vo","story of husband and wife and their extra marital affairs",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/d/d6/Pati_Patni_Aur_Woh_poster.jpg/220px-Pati_Patni_Aur_Woh_poster.jpg",
                              "https://www.youtube.com/watch?v=L7a1JSeqaXk")
paanipat=media.Movie("paanipat","didn't watched yet so no idea about it",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Panipat_%28film%29_poster.jpg/220px-Panipat_%28film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=zpXnmy-6w1g")
#movies = [toy_story,avatar,race3,bahubali,pati_patni_aur_vo,paanipat]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
