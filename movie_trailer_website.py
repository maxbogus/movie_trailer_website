import fresh_tomatoes
import media

saw = media.Movie(
    'Saw',
    'Two strangers are pawns in a deadly game perpetrated by a serial killer.',
    'http://goo.gl/K3dLh9',
    'https://www.youtube.com/watch?v=S-1QgOMQ-ls')

terminator_par2 = media.Movie(
    'Terminator 2',
    'A cyborg must now protect her young son from a more advanced cyborg.',
    'http://goo.gl/OQlnuQ',
    'https://www.youtube.com/watch?v=HgV7-MJwUBw')

unforgiven = media.Movie(
    'Unforgiven',
    'Retired gunslinger William Munny reluctantly takes on one last job',
    'http://goo.gl/UfsbRv',
    'https://www.youtube.com/watch?v=N-bNAXtCa_A')

beverly_hills_cop = media.Movie(
    'Beverly Hills Cop',
    'Using rock music to learn',
    'http://goo.gl/S7E5KJ',
    'https://www.youtube.com/watch?v=XQGi4eB3RZI')

true_detective = media.Movie(
    'True Detective',
    'Detectives are in pursuit of a serial killer over a 17-year period.',
    'http://goo.gl/B0eEtE',
    'https://www.youtube.com/watch?v=mXG1netn9_g')

fargo = media.Movie(
    'Fargo',
    'Fargo is a black-comedy drama',
    'http://goo.gl/qv29qv',
    'https://www.youtube.com/watch?v=gKs8DzjPDMU')

movies = [
    saw,
    terminator_par2,
    unforgiven,
    beverly_hills_cop,
    true_detective,
    fargo]

fresh_tomatoes.open_movies_page(movies)
