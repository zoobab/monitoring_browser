monitoring_browser
==================

A fullscreen monitoring browser in PySide and Qt Webkit.

It can rotate between multiple URLs with a given amount of seconds.

Configuration
=============

To display websites in fullscreen, just edit webkit.py and change the lines to have:

    url = QUrl("http://www.zoobab.com")
    self.sites.append(Site(url, 5, 1))
    
    url = QUrl("http://www.linuxfr.org")
    self.sites.append(Site(url, 5, 1))

Be careful to add 4 spaces in front for python indentation.

Dependencies
============

Tested on gentoo, you will need to install dev-python/pyside with the webkit USE flag:

$ USE="webkit" emerge -1 dev-python/pyside

For other distros, your feedback in welcomed.

Would love to see documentation on how to install it for Raspbian.

Video
=====

Coming soon...
