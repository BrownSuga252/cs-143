from mininet.topo import Topo


class Q9Topo(Topo):
    def __init__(self):
        # Initialize topology and default options
        Topo.__init__(self)

        # Add your logic here ...
        lastSwitch = None
        switches = {(12, 11): 10,
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
        for edge in switches:
            s1 = self.addSwitch('s%s' % edge[0])
            s2 = self.addSwitch('s%s' % edge[1])
            self.addLink(s1, s2, delay='%sms' % switches[edge])
        for edge in hosts:
            host = self.addSwitch('h$s' % edge)
            switch = self.addSwitch('s%s' % hosts[edge])
            self.addLink(host, switch)


Q9Topo()
topos = {'custom': (lambda: Q9Topo())}
