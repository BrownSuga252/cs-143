from mininet.topo import Topo
from mininet.link import TCLink

class Q9Topo(Topo):
    def __init__(self):
        # Initialize topology and default options
        Topo.__init__(self)

        # Add your logic here ...
        lastSwitch = None
        switch_list = {(12, 11): "10ms",
                    (12, 14): "50ms",
                    (14, 16): "10ms",
                    (16, 18): "30ms",
                    (11, 18): "30ms",
                    (12, 18): "10ms",
                    (12, 16): "100ms",
                    (18, 14): "20ms" }
        hosts = {13: 12,
                 15: 14,
                 19: 18,
                 17: 16, }
        for pair in switch_list:
            first = self.addSwitch('s%s' % pair[0])
            second = self.addSwitch('s%s' % pair[1])
            self.addLink(first, second, bw=10, switch_list[pair])
        for entry in hosts:
            host = self.addSwitch('h%s' % entry)
            switch = self.addSwitch('s%s' % hosts[entry])
            self.addLink(host, switch)


Q9Topo()
topos = {'custom': (lambda: Q9Topo())}
