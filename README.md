proxtop
=======

Proxmox resource monitor -- list top resource users of your proxmox VM
platform.

It will list columns of the top users of these resources:
* diskread
* diskwrite
* netin
* netout
* cpu


Requirements
------------

    $ pip install proxmoxer  # tested with 0.1.7


Example
-------

    $ ./proxtop -t day proxmox.example.com monitor@pve
    Password:<enter password>
    SORTED BY: diskread, avg
    ------------------
    #0:    3.1 MiB/s  pve10 (acme-bugs-bunny)
    #1:    1.3 MiB/s  pve07 (customerX-private)
    #2:  992.3 KiB/s  pve10 (acme-road-runner)
    ...
    SORTED BY: cpu, max
    ------------------
    #0:     91 %      pve07 (customerX-private)
    #1:     89 %      pve10 (acme-bugs-bunny)
    #2:     66 %      pve10 (acme-elmer-fudd)

See the help for more options:

    usage: proxtop [-h] [-T TOP] [-t TIMEFRAME] [-g AGGREGATION]
                   hostname username [only_vms [only_vms ...]]
    
    positional arguments:
      hostname              Use this API hostname (e.g. raposso.example.com)
      username              Use this API username (e.g. monitor@pve)
      only_vms              Limit results to these VMs
    
    optional arguments:
      -h, --help            show this help message and exit
      -T TOP, --top TOP     Limit results to TOP VMs
      -t TIMEFRAME, --timeframe TIMEFRAME
                            Timeframe, can be one of: hour* | day | week | month |
                            year
      -g AGGREGATION, --aggregation AGGREGATION
                            RRD aggregation, can be one of: AVERAGE* | MAX
