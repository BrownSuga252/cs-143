from mininet.topo import Topo


class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        # Add your logic here ...
        for i in range(fanout):
            host1 = self.addHost('h%s' % i)
            host2 = self.addHost('h%s' % i)
            aggregate_switch = self.addSwitch('s%s' % i)
            edge_switch = self.addSwitch('s%s' % i)
            self.addLink(aggregate_switch, edge_switch, linkopts1["bw"], linkopts1["delay"],linkopts1["loss"], linkopts1["max_queue_size"], linkopts1["use_htb"] )
            self.addLink(edge_switch, host1, linkopts2["bw"], linkopts2["delay"],linkopts2["loss"], linkopts2["max_queue_size"], linkopts2["use_htb"])
            self.addLink(edge_switch, host2, linkopts3["bw"], linkopts3["delay"],linkopts3["loss"], linkopts3["max_queue_size"], linkopts3["use_htb"])
            
        
                    
topos = { 'custom': ( lambda: CustomTopo() ) }
