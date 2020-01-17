|proxtop|
=========

*Proxmox resource monitor*

|pypi_version| |pypi_downloads|

Proxtop lists the top resource consumers of your Proxmox VM platform.

It will list columns of the top users of these resources:
 * cpu
 * diskread
 * diskwrite
 * netin
 * netout

*IMPORTANT CHANGES IN proxtop 0.3.0:*

* Shows only one of AVERAGE, MEDIAN, MAX now. See the -g option.
* The --partial-match option has been removed in favor of globbing
  (e.g. ``*server-name*``).
* The default output is now MEDIAN.

*IMPORTANT CHANGES IN proxtop 0.2.0:*

* The default port is now 443. This was tested with Proxmox 4.0-57.
  If you want the old default port 8006 back, you may append ":8006"
  to the hostname.
* The VM container type is now used in the REST path: i.e. ``/qemu/``
  (or lxc) instead of ``/openvz/``.


Quick jump
----------

* `Installation`_
* `Example`_
* `License`_
* `Future`_



Installation
------------

Via pip:

.. code-block:: console

    $ pip install proxtop

Via git:

.. code-block:: console

    $ pip install proxmoxer  # tested with 0.1.7 and 0.2.0
    $ pip install requests   # tested with 2.2.1 and 2.5.3
    $ git clone https://github.com/ossobv/proxtop.git
    $ cd proxtop
    $ python setup.py install



Example
-------

.. code-block:: console

    $ ./proxtop -t day proxmox.example.com:8006 monitor@pve
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

.. code-block:: console

    usage: proxtop [-h] [-T TOP] [-t TIMEFRAME] [-g AGGREGATION]
                   [--only-storage ONLY_STORAGE]
                   hostname username [only_vms [only_vms ...]]

    proxtop lists the top resource consumers on your Proxmox VM platform.

    positional arguments:
      hostname              Use this API hostname (e.g. proxmox.example.com[:443])
      username              Use this API username (e.g. monitor@pve)
      only_vms              Limit results to these VM names (globbing is allowed)

    optional arguments:
      -h, --help            show this help message and exit
      -T TOP, --top TOP     Limit results to TOP VMs
      -t TIMEFRAME, --timeframe TIMEFRAME
                            Timeframe, can be one of: hour* | day | week | month |
                            year
      -g AGGREGATION, --aggregation AGGREGATION
                            RRD aggregation, can be one of: AVERAGE | MAX |
                            MEDIAN*
      --only-storage ONLY_STORAGE
                            Filter VMs by storage glob (e.g. "nfs03*")

    Default values may be placed in ~/.proxtoprc. Lines should look like:
    hostname=HOSTNAME, username=USERNAME, password=PASSWORD


License
-------

proxtop is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation, version 3 or any later version.



Future
------

Possible future enhancements:

* Explain how server-side AGGREGATION affects the values
  (or perhaps remove the AVG/MAX subtypes and show only one, based
  on -g).
* Add alternate modes of output?
* Limit results to only one item (cpu, diskread, ...)?


.. |pypi_version| image:: https://img.shields.io/pypi/v/proxtop.svg
    :target: https://pypi.python.org/pypi/proxtop

.. |pypi_downloads| image:: https://img.shields.io/pypi/dm/proxtop.svg
    :target: https://pypi.python.org/pypi/proxtop

.. |proxtop| image:: assets/proxtop_head.png
    :alt: proxtop
