#!/usr/bin/env python

import os
import sys
import urllib
from PySide.QtWebKit  import QWebView
from PySide.QtGui     import QApplication, QWidget, QStackedLayout
from PySide.QtCore    import QUrl, SIGNAL, SLOT, QTimer
from PySide.QtNetwork import QTcpServer, QTcpSocket, QHostAddress

app = QApplication(sys.argv)

class Site:
  def __init__(self, url, time, zoom):
    self.url  = url
    self.time = time
    self.zoom = zoom

class Browser(QWidget):
  def __init__(self):
    super(Browser, self).__init__()
    
    self.layout    = QStackedLayout(self)
    self.frontView = QWebView(self)
    self.backView  = QWebView(self)
    
    self.frontView.page().networkAccessManager().sslErrors.connect(self.onSslErrors)
    self.backView.page().networkAccessManager().sslErrors.connect(self.onSslErrors)
    
    self.hostname  = os.uname()[1]
    
    self.layout.setStackingMode(QStackedLayout.StackAll)
    self.layout.addWidget(self.frontView)
    self.layout.addWidget(self.backView)
    
    self.commands = {
      'help'          : self.cmdHelp,
      'refresh'       : self.cmdRefresh,
      'add'           : self.cmdAdd,
      'del'           : self.cmdDel,
      'list'          : self.cmdList,
      'zoom'          : self.cmdZoom,
      'fs'            : self.cmdFs,
      'exit'          : self.cmdExit,
      'next'          : self.cmdNext,
      'restart'       : self.cmdRestart,
      'upgrade'       : self.cmdUpgrade,
    }
    
    self.timer = QTimer()
    self.timer.setSingleShot(False)
    
    self.sites = list()
    self.siteId = -1
    
    self.socket = False
    
	url = QUrl("http://www.zoobab.com")
	self.sites.append(Site(url, 5, 1))
	   
	url = QUrl("http://www.linuxfr.org")
	self.sites.append(Site(url, 5, 1))

    self.server = QTcpServer()
    self.server.listen(QHostAddress.Any, 4242)

    self.connect(self.server,     SIGNAL("newConnection()"),    self, SLOT("onConnection()"));
    self.connect(self.timer,      SIGNAL("timeout()"),          self, SLOT("goNext()"));
    
    self.goNext()
    self.goNext()
  
  def goNext(self):
    self.cmdNext(list())
   
  def onConnection(self):
    self.socket = self.server.nextPendingConnection()
    self.socket.write(self.hostname + ' % ')
    self.connect(self.socket, SIGNAL("readyRead()"), self, SLOT("onDataReceived()"));
    
  def print_(self, text):
    if (self.socket != False):
      self.socket.write(text + '\n')
    print(text)


  def onDataReceived(self):
    data = self.socket.readAll().data().strip()
    try:
      args = data.split(' ')
      map(lambda x : x.strip(), args)
      self.commands.get(args[0])(args)
    except Exception:
      self.print_('>> syntax error')
      self.printCommandsList()
    if self.socket.isOpen():
      self.socket.write(self.hostname + ' % ')
      
  def printCommandsList(self):
    self.print_('avaible commands:')
    for command in self.commands:
      self.print_('  ' + command)
      
      
  def onSslErrors(self, reply, errors):
    url = unicode(reply.url().toString())
    reply.ignoreSslErrors()
  
  # commands
  def cmdHelp(self, args):
    self.print_('>> help')
    self.printCommandsList()
  
  def cmdRefresh(self, args):
    self.print_('>> refresh ' + self.url.toString().encode())
    self.frontView.reload()
  
  def cmdAdd(self, args):
    self.print_('>> add ' + args[1] + ' ' + args[2] + ' ' + args[3])
    self.sites.append(Site(QUrl(args[1]), int(args[2], int(args[3]))))
    
  def cmdDel(self, args):
    self.print_('>> del ' + args[1])
    self.sites.pop(int(args[1]))
  
  def cmdList(self, args):
    self.print_('>> list')
    self.print_('current list:')
    sitesCount = len(self.sites)
    i = 0
    while i < sitesCount:
      self.print_('%1c[%1d] %2ds : %3s' % ((i==self.siteId) and '*' or ' ' ,i, self.sites[i].time, self.sites[i].url.toString().encode()))
      i = i + 1
  
  def cmdZoom(self, args):
    self.print_('>> zoom ' + args[1])
    self.frontView.setZoomFactor(float(args[1]))
    
  def cmdFs(self, args):
    self.print_('>> fs ' + args[1])
    if (args[1] == '1'):
      self.showFullScreen()
    else:
      self.showNormal()

  def cmdExit(self, args):
    self.print_('>> exit')
    self.socket.close()
    
  def cmdNext(self, args):
    self.timer.stop()
    self.timer.start(self.sites[self.siteId].time * 1000)
    self.siteId = (self.siteId + 1) % len(self.sites)
    print('>> next ' + self.sites[self.siteId].url.toString().encode())
    self.backView.show()
    self.frontView, self.backView = self.backView, self.frontView
    self.backView.load(self.sites[self.siteId].url)
    self.backView.setZoomFactor(self.sites[self.siteId].zoom)
    self.backView.hide()
    
  def cmdRestart(self, args):
    self.print_('>> restart')
    self.close()
    
  def cmdUpgrade(self, args):
    self.print_('>> upgrade')
    update = urllib.urlopen('https://raw.github.com/pol51/monitoring_browser/master/webkit.py').read()
    script = file('webkit.py', 'w')
    script.write(update)
    script.close()
    self.close()

# main
browser = Browser()
browser.showFullScreen()

sys.exit(app.exec_())
