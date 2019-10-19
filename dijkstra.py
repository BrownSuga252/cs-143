from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
import csv

graph = {}

class Dijkstra (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)

        # Build delays dictionary
        delays =  {}
        file = csv.DictReader(open('delay.csv'))
        for row in file:
            link = row['link']
            delay = row['delay']
            delays[link] = delays

        # Build graph
        graph = {
            's11': {
                's12': delays['g'],
                's18': delays['k']
            },
            's12': {
                'h13': 1,
                's14': delays['h'],
                's16': delays['m'],
                's18': delays['l'],
                's11': delays['g']
            },
            's14': {
                'h15': 1,
                's12': delays['h'],
                's18': delays['n'],
                's16': delays['i']
            },
            's16': {
                'h17': 1,
                's12': delays['m'],
                's14': delays['i'],
                's18': delays['j']
            },
            's18': {
                'h19': 1,
                's12': delays['l'],
                's16': delays['j'],
                's14': delays['n'],
                's11': delays['k']
            },
            'h13': {
                's12': 0
            },
            'h15': {
                's14': 0
            },
            'h17': {
                's16': 0
            },
            'h19': {
                's18': 0
            },
        }

    # Runs Dijkstra's algorithm on a graph
    def dijkstra(g, src, dest, visited=[], distances={}, predecessors={}):
        if src not in g:
            raise TypeError('The root of the shortest path tree cannot be found in the graph')
        if dest not in g:
            raise TypeError('The target of the shortest path cannot be found in the graph')

        if src == dest:
            # Reconstruct shortest path by walking backwards
            path = []
            pred = dest

            while pred != None:
                path.append(pred)
                pred = predecessors.get(pred, None)

            return path
        else :
            if not visited:
                distances[src] = 0

            # Update shortest paths
            for neighbor in g[src]:
                if neighbor not in visited:
                    distance = distances[src] + g[src][neighbor]

                    if distance < distances.get(neighbor, float('inf')):
                        distances[neighbor] = distance
                        predecessors[neighbor] = src

            visited.append(src)
            unvisited = {}

            for u in g:
                if u not in visited:
                    unvisited[u] = distances.get(u, float('inf'))

            x = min(unvisited, key=unvisited.get)
            dijkstra(g, x, dest, visited, distances, predecessors)

    def _handle_ConnectionUp (self, event):
        # Create network flows
        for u in graph.keys():
            for v in graph.keys():
                path = self.dijkstra(graph, u, v)

                # Create flow for every node in the path
                for l1 in path:
                    l1 = l1 + 1

                    for l1 in path:
                        fm = of.ofp_flow_mod()
                        fm.match.in_port = l1
                        fm.actions.append(of.ofp_action_output(port = l1))

def launch ():
    core.registerNew(Dijkstra)
