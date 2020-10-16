[![noswpatv3](http://zoobab.wdfiles.com/local--files/start/noupcv3.jpg)](https://ffii.org/donate-now-to-save-europe-from-software-patents-says-ffii/)
monitoring_browser
==================

A fullscreen monitoring browser in PySide and Qt Webkit.

It can rotate between multiple URLs with a given amount of seconds.

Configuration
=============

To display websites in fullscreen, just edit webkit.py and change the lines to have:

    url = QUrl("http://www.zoobab.com")
    self.sites.append(Site(url, 10, 1.5))
    
    url = QUrl("http://www.linuxfr.org")
    self.sites.append(Site(url, 10, 1))

    url = QUrl("http://demo.kibana.org")
    self.sites.append(Site(url, 15, 1))

    url = QUrl("http://demo.mathias-kettner.de/demo/check_mk/")
    url.setUserName("demo897");
    url.setPassword("demo");
    self.sites.append(Site(url, 15, 1))

Be careful to add 4 spaces in front for python indentation.

The second argument is the time delay, and the third one is the zoom level.

Dependencies
============

Tested on gentoo, you will need to install dev-python/pyside with the webkit USE flag:

$ USE="webkit" emerge -1 dev-python/pyside

For other distros, your feedback in welcomed.

Would love to see documentation on how to install it for Raspbian.

Telnet interface
================

It is also accessible via telnet localhost port 4242 where you can change some
configs on the fly (like zoom level, refresh, delay, get the status of the
list, add or remove an URL, etc...)

    zoobab@turmes /home/zoobab [1]$ telnet 127.1 4242
    Trying 127.0.0.1...
    Connected to 127.1.
    Escape character is '^]'.
    turmes % help
    >> help
    avaible commands:
      fs
      help
      restart
      upgrade
      list
      zoom
      refresh
      next
      add
      del
      exit
    turmes % list
    >> list
    current list:
     [0] 10s : http://status.mobilevikings.com/
     [1] 10s : http://ihackernews.com
     [2] 10s : http://demo.kibana.org
    *[3] 10s : http://logstash.openstack.org
     [4] 15s : http://demo897:demo@demo.mathias-kettner.de/demo/check_mk/
    turmes %

TODO
====

* Raspberrypi / raspbian installation
* Change user-agents for certain sites
* Handle URLs that fails
* Document the API accessible at: $ telnet 127.0.0.1 4242 

Video
=====

See here:

http://www.youtube.com/watch?v=UwPF1F0_Uao
