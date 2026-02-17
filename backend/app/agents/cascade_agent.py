import numpy as np

class CascadeAgent:

    def simulate(self, graph, service_name):

        impacted = set([service_name])
        queue = [service_name]

        while queue:
            node = queue.pop(0)

            for successor in graph.successors(node):
                # Probability weighted by dependency strength
                if np.random.random() < 0.6:
                    impacted.add(successor)
                    queue.append(successor)

        return list(impacted)
