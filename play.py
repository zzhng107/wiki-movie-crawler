from Graph import Graph
import json
with open('graph.json') as my_json:
    data = json.load(my_json)
    my_graph = Graph(data[0], data[1], data[2])

    print(my_graph.movie_grossing('Batman Begins'))
    print(list(my_graph.movie_s_actors('Batman Begins')))
    print(list(my_graph.actor_s_movies('Morgan Freeman')))
    print(list(my_graph.richest_actors(2)))
    print(list(my_graph.oldest_actors(2)))
    print(list(my_graph.year_of_movies('2017')))
    print(list(my_graph.year_of_actors('2017')))