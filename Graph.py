class Graph:
    def __init__(self, movies, actors, graph):
        self.movies = movies
        self.actors = actors
        self.graph = graph

    # def add_movie(self, name, grossing, year):
    #     if name not in self.move:
    #         self.movies[name]['grossing'] = grossing
    #         self.movies[name]['year'] = year
    #
    # def add_actor(self, name, age):
    #     if name not in self.actors:
    #         self.actors[name] = age

    def add(self, movie, grossing, actor, age):
        # self.add_movie(movie, grossing)
        # self.add_actor(actor, age)
        if movie not in self.graph:
            self.graph[movie] = {}
        if actor not in self.graph:
            self.graph[actor] = {}

        num_of_actors = len(self.graph[movie])
        self.graph[movie][actor] = self.movies[movie]['grossing'] * 1 / (2 ** num_of_actors)
        self.graph[actor][movie] = self.movies[movie]['grossing'] * 1 / (2 ** num_of_actors)

    def movie_grossing(self, movie):
        return self.movies[movie]['grossing']

    def movie_s_actors(self, movie):
        if movie in self.graph:
            for actor, v in self.graph[movie].items():
                yield actor

    def actor_s_movies(self, actor):
        if actor in self.graph:
            for movie, v in self.graph[actor].items():
                yield movie

    def richest_actors(self, n):
        actor_gross = {}
        for actor, v in self.actors.items():
            actor_gross[actor] = 0
            if actor in self.graph:
                for movie, gross in self.graph[actor].items():
                    actor_gross[actor] = actor_gross[actor] + gross
        return sorted(actor_gross, key=actor_gross.get, reverse=True)[:n]

    def oldest_actors(self, n):
        return sorted(self.actors, key=self.actors.get, reverse=True)[:n]

    def year_of_movies(self, year):
        for k, v in self.movies.items():
            if v['year'] == year:
                yield k

    def year_of_actors(self, year):
        actors = {}
        for k, v in self.movies.items():
            if v['year'] == year:
                if k in self.graph:
                    for k_, v_ in self.graph[k].items():
                        actors[k_] = 0
        return actors.keys()



    # def update_actor_grossing(self):
    #     for movie, grossing in self.movies:
    #         total = 0
    #         for actor, weight in self.graph[movie]:
    #             total = total + weight
    #
    #     for k,v in self.graph:
            # if()


