import fresh_tomatoes
import media

ant_man = media.Movie("Ant Man", "ant man", "http://www.spaziocinema.info/in/film/ant-man-loc.jpg", "https://www.youtube.com/watch?v=UUkn-enk2RU")
mission_impossible = media.Movie("Mission Impossible", "mission impossible", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMbhuJzAyGe3OJI7Jb9KRxbRw1UOb97fwc1wDeQv6KCmPInFDT", "https://www.youtube.com/watch?v=wb49-oV0F78")
movies = [ant_man, mission_impossible]
fresh_tomatoes.open_movies_page(movies)
