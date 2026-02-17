import numpy as np
import networkx as nx
import random

class Service:
    def __init__(self, name):
        self.name = name
        self.cpu = np.random.normal(0.55, 0.05, 300)
        self.latency = np.random.normal(120, 15, 300)
        self.error_rate = np.random.normal(0.01, 0.004, 300)
        self.autoscale_limit = 0.85
        self.iam_complexity = random.uniform(0.3, 0.9)
        self.network_surface = random.uniform(0.2, 0.8)
        self.region = random.choice(["eastus", "westeurope", "centralus"])

def create_environment():
    G = nx.DiGraph()
    services = {}

    names = [
        "auth", "orders", "gateway",
        "billing", "payment",
        "inventory", "search", "analytics"
    ]

    for n in names:
        services[n] = Service(n)
        G.add_node(n)

    edges = [
        ("gateway", "auth"),
        ("gateway", "orders"),
        ("orders", "inventory"),
        ("orders", "payment"),
        ("billing", "payment"),
        ("analytics", "orders")
    ]

    G.add_edges_from(edges)
    return G, services
