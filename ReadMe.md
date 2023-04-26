# Gossiping Time Protocol Implementation

This implementation simulates the Gossiping Time Protocol in a network of nodes. Each node maintains a clock and exchanges its value with a randomly selected neighbor at random intervals. The protocol is designed to synchronize the clocks of all nodes in the network.

## Usage

The implementation requires Python 3.x and the threading module.

To run the implementation, simply execute the script. You can modify the number of nodes by changing the argument of the `Node` constructor in the following line:

```python
nodes = [Node(i, []) for i in range(25)] #change the number to how many nodes need to be tested
```

The implementation measures the convergence time and prints the final clock values of each node. The convergence threshold can be adjusted by modifying the `threshold` variable.

## Implementation Details

The implementation creates a `Node` class that contains the node's id, neighbors, clock, and running status. Each node runs on a separate thread, and the `_run()` method is responsible for the gossiping behavior. 

When a node is started, it enters a loop that updates its clock, selects a random neighbor to gossip with, exchanges clock values, and sleeps for a random interval. The `gossip()` method is called when a neighbor exchanges clock values, and it updates the node's clock with the average of the node's and neighbor's clocks.

After all nodes are started, the implementation measures the convergence time. It enters a loop that checks if all nodes have converged, which means that the maximum difference between the clocks of a node and its neighbors is less than the threshold. If not converged, it sleeps for a fixed interval and repeats the loop.

Once convergence is achieved, the implementation stops all nodes and prints the final clock values and convergence time. 

## Conclusion

This implementation demonstrates the Gossiping Time Protocol's behavior in a network of nodes. The implementation is scalable and can handle large networks efficiently. The convergence time depends on the size and connectivity of the network and the convergence threshold.