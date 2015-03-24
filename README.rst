proxtop
=======

Proxmox resource monitor -- list top resource consumers of your Proxmox
VM platform.

It will list columns of the top users of these resources:
 * cpu
 * diskread
 * diskwrite
 * netin
 * netout


Quick jump
----------

* `Requirements`_
* `Example`_
* `License`_
* `TODO`_



Requirements
------------

.. code::

    $ pip install proxmoxer  # tested with 0.1.7 and 0.2.0
    $ pip install requests   # tested with 2.2.1 and 2.5.3



Example
-------

.. code::

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

.. code::

    usage: proxtop [-h] [-T TOP] [-t TIMEFRAME] [-g AGGREGATION]
                   hostname username [only_vms [only_vms ...]]

    proxtop lists the top resource consumers on your Proxmox VM platform.

    positional arguments:
      hostname              Use this API hostname (e.g. proxmox.example.com)
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

    Default values may be placed in ~/.proxtoprc. Lines should look like:
    hostname=HOSTNAME, username=USERNAME, password=PASSWORD



License
-------

proxtop is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation, version 3 or any later version.



TODO
----

* Explain how server-side AGGREGATION affects the values
  (or perhaps remove the AVG/MAX subtypes and show only one, based
  on -g).
* Add alternate modes of output?
* Limit results to only one item (cpu, diskread, ...)?
