from mininet.topo import Topo


class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        # Add your logic here ...
        # Make Core 
        core = self.addSwitch('c1')
        track_edge = track_host = 1

        # Build aggregation layer
        for iterator in range(fanout):
            aggregation_switch = self.addSwitch('s%s' % iterator)
            self.addLink(aggregation_switch, core,  **linkopts1)

            # Build edge layer
            for iterator2 in range (fanout):
                edge_switch = self.addSwitch('s%s' % track_edge)
                track_edge += 1
                self.addLink(edge_switch, aggregation_switch,  **linkopts2)

                # Build host layer
                for iterator2 in range (fanout):
                    host = self.addHost('h%s' % track_host)
                    track_host += 1
                    self.addLink(host, edge_switch, **linkopts3)

linkopts1 = dict(bw=10, delay='5ms', max_queue_size=1000, use_htb=True)
linkopts2 = dict(bw=10, delay='5ms', max_queue_size=1000, use_htb=True)
linkopts3 = dict(bw=10, delay='5ms', max_queue_size=1000, use_htb=True)

topos = { 'custom': ( lambda: CustomTopo(linkopts1,linkopts2,linkopts3)) }
