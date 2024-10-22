from collections import defaultdict, deque

class AirportConnectivity:
    def __init__(self):
        # Graph to represent the flight routes
        self.graph = defaultdict(list)

    def add_route(self, from_airport: str, to_airport: str) -> None:
        #Adds a one-way route from one airport to another
        self.graph[from_airport].append(to_airport)

    def find_reachable(self, start: str) -> set:
        """Finds all airports reachable from the starting airport using Breadth First Search."""
        visited = set()  # To track visited airports
        queue = deque([start])  # Start Breath First Search from the given airport

        while queue:
            airport = queue.popleft()
            if airport not in visited:
                visited.add(airport)
                for neighbor in self.graph[airport]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return visited

    def find_unreachable(self, start: str, all_airports: set) -> set:
        #Finds airports which cannot be reached from the start point
        reachable_airports = self.find_reachable(start)
        return all_airports - reachable_airports  # Unreachable airports

    def min_new_routes(self, start: str, all_airports: set) -> list:
        new_routes = []
        # Loop until all airports are reachable
        while True:
            unreachable_airports = self.find_unreachable(start, all_airports)
            if not unreachable_airports:
                break  # All airports are reachable

            # Add a new route from the starting airport to one of the unreachable airports
            unreachable_airport = unreachable_airports.pop()
            new_route = (start, unreachable_airport)
            new_routes.append(new_route)

            # Update the graph by adding the new route
            self.add_route(start, unreachable_airport)

        return new_routes


# involke
def main():
    # Create an instance of AirportConnectivity class
    network = AirportConnectivity()

    # Define a list of existing routes based on the image
    routes = [
        ("DSM", "ORD"), ("ORD", "BGI"), ("BGI", "LGA"), ("JFK", "LGA"),
        ("JFK", "ICN"), ("HND", "ICN"), ("EWR", "HND"), ("TLV", "DEL"),
        ("DEL", "DOH"), ("DEL", "CDG"), ("CDG", "BUD"), ("CDG", "SIN"),
        ("SFO", "SAN"), ("SAN", "EYW"), ("EYW", "LHR"), ("LHR", "SFO")
    ]

    # Add these routes to the network
    for route in routes:
        network.add_route(*route)

    start_airport = "DSM"
    all_airports = {"DSM", "ORD", "BGI", "LGA", "JFK", "ICN", "HND", "EWR",
                    "TLV", "DEL", "DOH", "CDG", "BUD", "SIN", "SFO", "SAN",
                    "EYW", "LHR"}

    # Find the minimum number of new routes needed
    new_routes = network.min_new_routes(start_airport, all_airports)

    #result
    print(f"Starting from {start_airport}")
    print(f"Number of new routes needed: {len(new_routes)}")
    print("New routes to add:")
    for route in new_routes:
        print(f"  {route[0]} -> {route[1]}")

# Run the example
if __name__ == "__main__":
    main()
