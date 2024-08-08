# Route Optimization for Delivery Service (Java GUI)
# This scenario explores a Java GUI application using graph algorithms to optimize delivery routes for a courier
# service.
# Features:
# Delivery list: Import or manually enter a list of delivery points with addresses and order priorities.
# Algorithm selection: Choose an optimization algorithm for route planning.
# Vehicle options: Specify vehicle capacity and driving distance constraints.
# Optimize button: Initiates the chosen algorithm to calculate the optimal delivery route.
# Route visualization: Highlight the calculated route, showing stops and travel distances.
# Challenges:
# Implement chosen optimization algorithms using multithreading for faster calculations.
# Visualize the calculated route effectively with clear highlighting and labeling.
# Handle vehicle constraints and capacity limitations during route planning.
# Implementation:
# Swing/JavaFX GUI: Design a graphical interface using appropriate libraries to:
# Provide input options for delivery list, vehicle specifications, and algorithm selection.
# Show the optimized route visually.
# User input on delivery list, vehicle options, and algorithm selection.
# Initiating the route optimization and handling completion.
# Interacting with the map display (optional).

import customtkinter as ctk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

def create_sample_graph():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ("kathmandu", "bhaktapur", 1),
        ("bhaktapur", "lalitpur", 2),
        ("lalitpur", "pokhara", 1),
        ("pokhara", "kathmandu", 3),
        ("kathmandu", "lalitpur", 4),
        ("bhaktapur", "pokhara", 5)
    ])
    return G

class RouteOptimizationApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Route Optimization")
        self.geometry("600x500")

        # Initialize sample graph
        self.graph = create_sample_graph()

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Delivery List Section
        ctk.CTkLabel(self.main_frame, text="Delivery Points (comma-separated addresses):").pack(pady=5)
        self.delivery_points = ctk.CTkEntry(self.main_frame, width=400)
        self.delivery_points.pack(pady=5)

        # Optimize Button
        self.optimize_button = ctk.CTkButton(self.main_frame, text="Optimize Route", command=self.optimize_route)
        self.optimize_button.pack(pady=10)

        # Result Area
        self.route_display = ctk.CTkTextbox(self.main_frame, height=200, width=500)
        self.route_display.pack(pady=10)

    def optimize_route(self):
        delivery_points = self.delivery_points.get().split(',')

        if not delivery_points:
            messagebox.showerror("Input Error", "Please enter delivery points.")
            return

        delivery_points = [point.strip().lower() for point in delivery_points]

        if len(delivery_points) < 2:
            messagebox.showerror("Input Error", "At least two delivery points are required.")
            return

        try:
            path = self.nearest_neighbor_tsp(delivery_points)
            self.route_display.delete("1.0", ctk.END)
            self.route_display.insert(ctk.END, f"Optimal Path: {path}\n")
            self.visualize_route(path)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def nearest_neighbor_tsp(self, nodes):
        start = nodes[0]
        path = [start]
        unvisited = set(nodes)
        unvisited.remove(start)

        current = start
        while unvisited:
            next_node = min(unvisited, key=lambda node: self.graph[current][node]['weight'])
            path.append(next_node)
            unvisited.remove(next_node)
            current = next_node

        path.append(start)  # Return to start
        return path

    def visualize_route(self, path):
        plt.clf()
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=16)
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(self.graph, pos, nodelist=path, node_color='lightgreen')
        nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.title("Route Visualization")
        plt.show()

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
    app = RouteOptimizationApp()
    app.mainloop()
