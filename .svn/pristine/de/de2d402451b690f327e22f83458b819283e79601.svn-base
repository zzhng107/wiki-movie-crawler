import json
from Graph import Graph

def main():
    my_graph = Graph({}, {}, {})
    with open('out.json') as my_json:
        data = json.load(my_json)
        for item in data:
            for name, value in item.items():
                if type(value) is int:
                    my_graph.actors[name] = value
                elif isinstance(value, dict):
                    my_graph.movies[name] = value

        for item in data:
            for name, value in item.items():
                if type(value) is list:
                    if name in my_graph.movies:
                        for actor in value:
                            if actor in my_graph.actors:
                                my_graph.add(name, my_graph.movies[name]['grossing'], actor, my_graph.actors[actor])

                    if name in my_graph.actors:
                        for movie in value:
                            if movie in my_graph.movies:
                                my_graph.add(movie, my_graph.movies[movie]['grossing'], name, my_graph.actors[name])

    with open('graph.json', 'w') as graph_json:
        out = [my_graph.movies, my_graph.actors, my_graph.graph]
        json.dump(out, graph_json)

main()