import fresh_tomatoes
import media

ant_man = media.Movie("Ant Man", "ant man", "http://www.spaziocinema.info/in/film/ant-man-loc.jpg", "https://www.youtube.com/watch?v=UUkn-enk2RU")
mission_impossible = media.Movie("Mission Impossible", "mission impossible", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMbhuJzAyGe3OJI7Jb9KRxbRw1UOb97fwc1wDeQv6KCmPInFDT", "https://www.youtube.com/watch?v=wb49-oV0F78")
wall_e = media.Movie("Wall-E", "Wall-E", "https://m.media-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg", "https://www.youtube.com/watch?v=8-_9n5DtKOc")
fifth_element = media.Movie("Fifth Element", "Fifth Element", "https://m.media-amazon.com/images/M/MV5BZWFjYmZmZGQtYzg4YS00ZGE5LTgwYzAtZmQwZjQ2NDliMGVmXkEyXkFqcGdeQXVyNTUyMzE4Mzg@._V1_SY1000_CR0,0,696,1000_AL_.jpg", "https://www.youtube.com/watch?v=Gg9nzOFVwtQ&pbjreload=10")
movies = [ant_man, mission_impossible, wall_e, fifth_element]
fresh_tomatoes.open_movies_page(movies)
