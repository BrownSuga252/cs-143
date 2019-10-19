from mininet.topo import Topo
import csv

class Q9Topo(Topo):
    def __init__(self):
        # Initialize topology and default options
        Topo.__init__(self)

        lastSwitch = None
        switches = {}
        hosts = {}
        delays = {}

        # Read switches CSV.
        with open('switch_edges.csv') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                switches[(row['s1'], row['s2'])] = row['link']

        # Read host CSV.
        with open('host_edges.csv') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                hosts[row['host']] = row['switch']

        # Read delays CSV.
        with open('delay.csv') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                delays[row['link']] = row['delay']

        # Build topology.
        for edge in switches:
            s1 = self.addSwitch('s%s' % edge[0])
            s2 = self.addSwitch('s%s' % edge[1])

            self.addLink(s1, s2, delay='%sms' % delays[switches[edge]])

        for edge in hosts:
            host = self.addSwitch('h%s' % edge)
            switch = self.addSwitch('s%s' % hosts[edge])

            self.addLink(host, switch)

Q9Topo()
topos = { 'custom': ( lambda: Q9Topo() ) }
