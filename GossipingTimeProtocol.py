import random
import time
from threading import Thread

class Node:
    def __init__(self, node_id, neighbors):
        self.id = node_id
        self.neighbors = neighbors
        self.clock = 0
        self.running = False

    def start(self):
        self.running = True
        Thread(target=self._run).start()

    def stop(self):
        self.running = False

    def _run(self):
        while self.running:
            # Update own clock
            self.clock += 1

            # Select random neighbor to gossip with
            neighbor = random.choice(self.neighbors)

            # Exchange clock values
            self.clock = (self.clock + neighbor.gossip(self.clock)) / 2

            # Wait for random amount of time
            time.sleep(random.random())

    def gossip(self, other_clock):
        # Exchange clock values and return updated value
        self.clock = (self.clock + other_clock) / 2
        return self.clock

if __name__ == '__main__':
    # Create nodes and set neighbors
    nodes = [Node(i, []) for i in range(25)] #change the number to how many nodes need to be tested
    for i, node in enumerate(nodes):
        # Randomly select up to 5 neighbors
        neighbors = random.sample(nodes[:i] + nodes[i+1:], min(5, len(nodes)-1))
        node.neighbors = neighbors

    # Start nodes
    for node in nodes:
        node.start()

    # Measure convergence time
    threshold = 0.1  # threshold for convergence
    converged = False
    start_time = time.time()
    while not converged:
        converged = True
        for node in nodes:
            for neighbor in node.neighbors:
                neighbor_clock = neighbor.clock
                node.gossip(neighbor_clock)
            if abs(max(n.clock for n in node.neighbors) - node.clock) > threshold:
                converged = False
        if not converged:
            time.sleep(0.1)

    # Stop nodes
    for node in nodes:
        node.stop()

    # Print final clock values and convergence time
    for node in nodes:
        print(f"Node {node.id}: {node.clock}")
    print(f"Convergence time: {time.time() - start_time}")
