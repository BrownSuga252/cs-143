from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.util import dumpNodeConnections, irange


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
            self.addLink(aggregate_switch, edge_switch, linkopts1["bw"], linkopts1["delay"])
            self.addLink(edge_switch, host1, linkopts2["bw"], linkopts2["delay"])
            self.addLink(edge_switch, host2, linkopts3["bw"], linkopts3["delay"])
            

linkopts1 = dict(bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
linkopts2 = dict(bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
linkopts3 = dict(bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
                    
topos = { 'custom': ( lambda: CustomTopo(linkopts1,linkopts2,linkopts3) ) }
