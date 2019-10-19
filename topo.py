from mininet.topo import Topo


class Q9Topo(Topo):
    def __init__(self):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        # Add your logic here ...
        lastSwitch = None
        switches = {("s12", "s11"): "10",
                    ("s12", "s14"): "50",
                    ("s14", "s16"): "10",
                    ("s16", "s18"): "30",
                    ("s11", "s18"): "30",
                    ("s12", "s18"): "10",
                    ("s12", "s16"): "100",
                    ("s18", "s14"): "20", }
        hosts = {"h13": "s12",
                 "h15": "s14",
                 "h19": "s18",
                 "h17": "s16", }
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
