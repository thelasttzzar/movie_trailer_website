import media
import fresh_tomatoes

#All hand-typed data for each instance of class Movie

the_matrix = media.Movie("The Matrix",
                         "What is the Matrix? Keanu Reeves takes pills and does Kung Fu to find out.",
                         "1999",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

blade_runner_2049 = media.Movie("Blad Runner 2049",
                        "Ryan Gosling punches Harrison Ford and looks moody.",
                        "2017",
                        "https://upload.wikimedia.org/wikipedia/en/9/9b/Blade_Runner_2049_poster.png",
                        "https://www.youtube.com/watch?v=gCcx85zbxz4")

the_shining = media.Movie("The Shining",
                        "Jack Nicholson trys (and fails) to murder his family, gets cold.",
                        "1980",
                        "https://upload.wikimedia.org/wikipedia/en/e/ea/The_Shining_%281980%29.png",
                        "https://www.youtube.com/watch?v=5Cb3ik6zP2I")

the_fifth_element = media.Movie("The Fifth Element",
                        "Bruce Wilis in orange tank top, finds love powerful enough to save everything.",
                        "1997",                              
                        "https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg",
                        "https://www.youtube.com/watch?v=fQ9RqgcR24g")

a_space_odyssey = media.Movie("2001: A Space Odyssey",
                         "This film totally proves Kubrick faked the moonlanding. Totally.",
                         "1968",
                         "https://images-na.ssl-images-amazon.com/images/I/41%2BMbGYLI7L.jpg",
                         "https://www.youtube.com/watch?v=Z2UWOeBcsJI")

gladiator = media.Movie("Gladiator",
                         "The frost, sometimes it makes the blade stick...<br><em>(a quote followed by awesome murders)</em>",
                         "2000",
                         "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                         "https://www.youtube.com/watch?v=Q-b7B8tOAQU")

movies = [the_matrix, blade_runner_2049, the_shining, the_fifth_element, a_space_odyssey, gladiator]
fresh_tomatoes.open_movies_page(movies)



