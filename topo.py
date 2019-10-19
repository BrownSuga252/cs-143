from mininet.topo import Topo


class Q9Topo(Topo):
    def __init__(self):
        # Initialize topology and default options
        Topo.__init__(self)

        # Add your logic here ...
        lastSwitch = None
        switch_list = {(12, 11): 10,
                    (12, 14): 50,
                    (14, 16): 10,
                    (16, 18): 30,
                    (11, 18): 30,
                    (12, 18): 10,
                    (12, 16): 100,
                    (18, 14): 20 }
        hosts = {13: 12,
                 15: 14,
                 19: 18,
                 17: 16, }
        for pair in switch_list:
            first = self.addSwitch('s%s' % pair[0])
            second = self.addSwitch('s%s' % pair[1])
            self.addLink(first, second, switch_list[pair])
        for entry in hosts:
            host = self.addSwitch('h%s' % entry)
            switch = self.addSwitch('s%s' % hosts[entry])
            self.addLink(host, switch)


Q9Topo()
topos = {'custom': (lambda: Q9Topo())}
