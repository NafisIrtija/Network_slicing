# Realizing Network Slicing #

In this project, we demonstrate how to implement network slicing in an SDN to enable the isolation of network resources. The goal of this example is to show that the different requirements can be fulfilled on a shared physical infrastructure by using network slicing. We assume there are six hosts (h1, h2, h3, h4, h5, h6) and two switches (s1, s2) in the network:

```text
                                              Normal Scenario

h1 ---- 2.5mbps                 2.5mbps--- h3
       |                              |
       |             5mbps            |
        s1 ======================= s2        
       |             5mbps            |
       |                              |
h2 ---- 2.5mbps                 2.5mbps--- h4
```




```text
                                              Emergency Scenario

h1 ---- 2.5mbps                 2.5mbps --- h4
       |   ----------3mbps---------  |
2.5mbps|  |                        | |2.5mbps
h2 ---- s1 -----------3mbps-------  s2 ----h5
       |  |                        | |
       |   -----------4mbps--------  |
h3 ---- 2mbps                    2mbps  --- h6
```
This folder contains the following files:

1. network.py: Script to build a network with six hosts and two switches.

2. slicing.py: Application to isolate the network topology into multiple slices.

    

### How to Run ###
You can simple run the emulation applications with following commands in ./app/NetworkSlicing/.

1. Enabling Ryu controller to load the application and to run background:
    ```bash
    $ ryu-manager slicing.py &
    ```
2. Starting the network with Mininet:
    ```bash
    $ sudo python3 network.py
    ```
3. is there an Emergency? 
 Enter 'yes' if there's an emergency or 'no' if no emergency: no




### Normal Scenario ###
There are three modes to verify the slice:

a. ping mode: verifying connectivity, e.g.
    ```bash
    mininet> pingall
    *** Ping: testing ping reachability
    h1 -> X X h4 X X 
    h2 -> X X X h5 X 
    h3 -> X X X X h6 
    h4 -> h1 X X X X 
    h5 -> X h2 X X X 
    h6 -> X X h3 X X 
    *** Results: 80% dropped (6/30 received)
    ```
b. iperf mode: verifying bandwidth, e.g.
    ```bash
    mininet> iperf h1 h4
    *** Iperf: testing TCP bandwidth between h1 and h4 
    *** Results: ['2.39 Mbits/sec', '2.64 Mbits/sec']
    mininet> iperf h2 h5
    *** Iperf: testing TCP bandwidth between h2 and h5 
    *** Results: ['2.38 Mbits/sec', '2.68 Mbits/sec']
    ```


4. Ctrl C (to exit mininet)

5. Starting the network with Mininet:
    ```bash
    $ sudo python3 network.py
    ```
    
6. ```bash
 is there an Emergency? 
 Enter 'yes' if there's an emergency or 'no' if no emergency: yes 
 ```
 
 
 
 




### Emergency Scenario ###
There are three modes to verify the slice:

a. ping mode: verifying connectivity, e.g.
    ```bash
    mininet> pingall
    *** Ping: testing ping reachability
    h1 -> X X h4 X X 
    h2 -> X X X h5 X 
    h3 -> X X X X h6 
    h4 -> h1 X X X X 
    h5 -> X h2 X X X 
    h6 -> X X h3 X X 
    *** Results: 80% dropped (6/30 received)
    ```
b. iperf mode: verifying bandwidth, e.g.
    ```bash
    mininet> iperf h1 h4
    *** Iperf: testing TCP bandwidth between h1 and h4 
    *** Results: ['2.28 Mbits/sec', '2.53 Mbits/sec']
    mininet> iperf h2 h5
    *** Iperf: testing TCP bandwidth between h2 and h5 
    *** Results: ['2.18 Mbits/sec', '2.42 Mbits/sec']
    mininet> iperf h3 h6
    *** Iperf: testing TCP bandwidth between h3 and h6 
    *** Results: ['1.91 Mbits/sec', '2.31 Mbits/sec']
    ```


​    

