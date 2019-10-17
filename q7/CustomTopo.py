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
        edge_num = 1
        host_num = 1

        # Build aggregation layer
        for i in range(1, fanout + 1):
            aggregation_switch = self.addSwitch('a%s' % i)
            self.addLink(aggregation_switch, core,  **linkopts1)

            # Build edge layer
            for j in range (1, fanout + 1):
                edge_switch = self.addSwitch('e%s' % edge_num)
                edge_num += 1
                self.addLink(edge_switch, aggregation_switch,  **linkopts2)

                # Build host layer
                for j in range (1, fanout + 1):
                    host = self.addHost('h%s' % host_num)
                    host_num += 1
                    self.addLink(host, edge_switch, **linkopts3)

linkopts1 = dict(bw=10, delay='5ms', max_queue_size=1000, use_htb=True)
linkopts2 = dict(bw=10, delay='5ms', max_queue_size=1000, use_htb=True)
linkopts3 = dict(bw=10, delay='5ms', max_queue_size=1000, use_htb=True)

topos = { 'custom': ( lambda: CustomTopo(linkopts1,linkopts2,linkopts3)) }
