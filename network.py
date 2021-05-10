#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class NetworkSlicingTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Create template host, switch, and link
        host_config = dict(inNamespace=True)
#       normal_link_config = dict(bw=2.5)
#       emergency_link_config = dict(bw=4)
        tunnel_config = dict(bw=5)
        tunnel3_config = dict(bw=0.001)
        host_link_config = dict(bw=2.5)
        emgnc_host_link_config = dict(bw=0.001)

        # Create switch nodes
        for i in range(2):
            sconfig = {"dpid": "%016x" % (i + 1)}
            self.addSwitch("s%d" % (i + 1), **sconfig)

        # Create host nodes
        for i in range(6):
            self.addHost("h%d" % (i + 1), **host_config)

        # Add switch links
        self.addLink("s1", "s2", **tunnel_config)
        self.addLink("s1", "s2", **tunnel_config)
        self.addLink("s1", "s2", **tunnel3_config)
#       self.addLink("s1", "s3", **http_link_config)
#       self.addLink("s3", "s4", **http_link_config)

        # Add host links
        self.addLink("h1", "s1", **host_link_config)
        self.addLink("h2", "s1", **host_link_config)
        self.addLink("h3", "s1", **emgnc_host_link_config)

        self.addLink("h4", "s2", **host_link_config)
        self.addLink("h5", "s2", **host_link_config)
        self.addLink("h6", "s2", **emgnc_host_link_config)


class NetworkSlicingTopo2(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Create template host, switch, and link
        host_config = dict(inNamespace=True)
#        normal_link_config = dict(bw=2.5)
#        emergency_link_config = dict(bw=4)
        tunnel_config = dict(bw=3)
        tunnel3_config = dict(bw=4)
        host_link_config = dict(bw=2.5)
        emgnc_host_link_config = dict(bw=2)

        # Create switch nodes
        for i in range(2):
            sconfig = {"dpid": "%016x" % (i + 1)}
            self.addSwitch("s%d" % (i + 1), **sconfig)

        # Create host nodes
        for i in range(6):
            self.addHost("h%d" % (i + 1), **host_config)

        # Add switch links
        self.addLink("s1", "s2", **tunnel_config)
        self.addLink("s1", "s2", **tunnel_config)
        self.addLink("s1", "s2", **tunnel3_config)
#        self.addLink("s1", "s3", **http_link_config)
#        self.addLink("s3", "s4", **http_link_config)

        # Add host links
        self.addLink("h1", "s1", **host_link_config)
        self.addLink("h2", "s1", **host_link_config)
        self.addLink("h3", "s1", **emgnc_host_link_config)

        self.addLink("h4", "s2", **host_link_config)
        self.addLink("h5", "s2", **host_link_config)
        self.addLink("h6", "s2", **emgnc_host_link_config)

i = 0

val = input("is there an Emergency? \n Enter 'yes' if there's an emergency or 'no' if no emergency: ")

if val == 'no':
    topos = {"networkslicingtopo": (lambda: NetworkSlicingTopo())}

    if __name__ == "__main__":
        topo = NetworkSlicingTopo()
        net = Mininet(
            topo=topo,
            switch=OVSKernelSwitch,
            build=False,
            autoSetMacs=True,
            autoStaticArp=True,
            link=TCLink,
        )
        controller = RemoteController("c1", ip="127.0.0.1", port=6633)
        net.addController(controller)
        net.build()
        net.start()
        CLI(net)
        net.stop()


elif val == 'yes':
    topos = {"networkslicingtopo": (lambda: NetworkSlicingTopo2())}

    if __name__ == "__main__":
        topo = NetworkSlicingTopo2()
        net = Mininet(
            topo=topo,
            switch=OVSKernelSwitch,
            build=False,
            autoSetMacs=True,
            autoStaticArp=True,
            link=TCLink,
        )
        controller = RemoteController("c1", ip="127.0.0.1", port=6633)
        net.addController(controller)
        net.build()
        net.start()
        CLI(net)
        net.stop()
    

else:
        print(" Invalid input!!!")

