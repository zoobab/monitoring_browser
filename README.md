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

Video
=====

See here:

http://www.youtube.com/watch?v=UwPF1F0_Uao
