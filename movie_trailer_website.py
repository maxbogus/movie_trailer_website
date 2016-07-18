import fresh_tomatoes
import media

saw = media.Movie(
    'Saw',
    'Two strangers discover they are pawns in a deadly game perpetrated by a notorious serial killer.',
    'http://ia.media-imdb.com/images/M/MV5BMjE4MDYzNDE1OV5BMl5BanBnXkFtZTcwNDY2OTYwNA@@._V1_SY1000_SX675_AL_.jpg',
    'https://www.youtube.com/watch?v=S-1QgOMQ-ls')

terminator_par2 = media.Movie(
    'Terminator 2',
    'A cyborg must now protect her young son from a more advanced cyborg, made out of liquid metal.',
    'http://t1.gstatic.com/images?q=tbn:ANd9GcS5J6Ay6y1UT7WAI4U7Zm2KDYITrvfOI3vmaCNdGhx_0jmWiI1d',
    'https://www.youtube.com/watch?v=HgV7-MJwUBw')

unforgiven = media.Movie(
    'Unforgiven',
    'Retired Old West gunslinger William Munny reluctantly takes on one last job',
    'http://ia.media-imdb.com/images/M/MV5BMTkzNTc0NDc4OF5BMl5BanBnXkFtZTcwNTY1ODg3OA@@._V1_.jpg',
    'https://www.youtube.com/watch?v=N-bNAXtCa_A')

beverly_hills_cop = media.Movie(
    'Beverly Hills Cop',
    'Using rock music to learn',
    'http://www.gstatic.com/tv/thumb/movieposters/8676/p8676_p_v8_aa.jpg',
    'https://www.youtube.com/watch?v=XQGi4eB3RZI')

true_detective = media.Movie(
    'True Detective',
    'The first season follows a pair of detectives, and their pursuit of a serial killer over a 17-year period.',
    'http://www.gstatic.com/tv/thumb/tvbanners/11689212/p11689212_b_v8_ac.jpg',
    'https://www.youtube.com/watch?v=mXG1netn9_g')

fargo = media.Movie(
    'Fargo',
    'Fargo is a black-comedy drama',
    'http://www.gstatic.com/tv/thumb/tvbanners/12031927/p12031927_b_v8_aa.jpg',
    'https://www.youtube.com/watch?v=gKs8DzjPDMU')

movies = [
    saw,
    terminator_par2,
    unforgiven,
    beverly_hills_cop,
    true_detective,
    fargo]

fresh_tomatoes.open_movies_page(movies)
