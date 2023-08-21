
# Author: Blake Jennings
# GitHub username: BlakeJenn
# Email: blakej94@gmail.com
# Description: Creates a Movie, StreamingService, and StreamingGuide Class and adds Movie objects
# to a StreamingService Dictionary, adds StreamingService Dictionaries to a StreamingGuide list,
# and determines which StreamingService dictionaries contain which Movie Objects

class Movie:
    '''Documents a Movie object'''
    def __init__(self, title, genre, director, year):
        '''Creates a Movie object with a title, genre, director, and year'''
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        '''Returns the title of a Movie object'''
        return self._title

    def get_genre(self):
        '''Returns the genre of a Movie object'''
        return self._genre

    def get_director(self):
        '''Returns the director of a Movie object'''
        return self._director

    def get_year(self):
        '''Returns the year of a Movie object'''
        return self._year

class StreamingService:
    '''Documents a StreamingService dictionary'''
    def __init__(self, name):
        '''Creates a StreamingService dictionary with a name'''
        self._name = name
        self._catalog = {}

    def get_name(self):
        '''Returns the name of a StreamingService dictionary'''
        return self._name

    def get_catalog(self):
        '''Returns the dictionary of a StreamingService dictionary'''
        return self._catalog

    def add_movie(self, movie):
        '''Adds a movie object to the StreamingService dictionary'''
        self._catalog[movie.get_title()] = [movie.get_genre(), movie.get_director(), movie.get_year()]

    def delete_movie(self, movie):
        '''Removes a movie object from the StreamingService dictionary'''
        if movie in self._catalog:
            self._catalog.pop(movie)

class StreamingGuide:
    '''Documents a StreamingGuide list'''

    def __init__(self):
        '''Creates a StreamingGuide list'''
        self._service_list = []

    def add_streaming_service(self, service):
        '''Adds a StreamingService dictionary to the StreamingGuide list'''
        self._service_list.append(service)

    def delete_streaming_service(self, service):
        '''Removes a StreamingService dictionary from the StreamingGuide list'''
        for serv in self._service_list:
            if serv.get_name() == service:
                self._service_list.remove(serv)

    def who_streams_this_movie(self, movie_title):
        '''Determines what StreamingService dictionaries contain a specified movie and, if any do,
        returns a dictionary that provides the movies title, year, and what streaming services
        provide the movie. Otherwise, returns None'''
        self._result_dict = {}
        self._result_dict["title"] = movie_title
        self._result_dict["year"] = ''
        self._result_dict["services"] = []
        for service in self._service_list: #iterates over list of services (list)
            for title in service.get_catalog(): #iterates over catalog of movies (dictionary)
                if title == movie_title:
                    self._result_dict["year"] = service.get_catalog()[title][2]
                    self._result_dict["services"].append(service.get_name())
        final = self._result_dict
        if len(final['services']) == 0:
            return None
        else:
            return final


#---------------- Testing -----------------------

movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.who_streams_this_movie('Little Women')
