from file_manager import FileManager

class RouteManager:

    def __init__(self):
        # Load routes from file
        self.routes = FileManager.load_data("routes.json")

        # Graph representation
        self.graph = {}

        # Build graph from stored routes
        self.build_graph()

    def build_graph(self):
        self.graph = {}

        for route in self.routes:

            source = route["source"]

            if source not in self.graph:
                self.graph[source] = []

            self.graph[source].append(
                {
                    "destination": route["destination"],
                    "distance": route["distance"],
                    "travel_time": route["travel_time"]
                }
            )

    def add_route(self, route_id, source,
                  destination, distance,
                  travel_time):

        route = {
            "route_id": route_id,
            "source": source,
            "destination": destination,
            "distance": distance,
            "travel_time": travel_time
        }

        self.routes.append(route)

        FileManager.save_data(
            "routes.json",
            self.routes
        )

        self.build_graph()

    def display_routes(self):
        return self.routes

    def search_route(self, source):

        if source in self.graph:
            return self.graph[source]

        return []

    def delete_route(self, route_id):

        for route in self.routes:

            if route["route_id"] == route_id:
                self.routes.remove(route)
                break

        FileManager.save_data(
            "routes.json",
            self.routes
        )

        self.build_graph()

    def display_graph(self):
        return self.graph

