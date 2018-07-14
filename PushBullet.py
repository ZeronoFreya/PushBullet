# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl


class PushBullet(QWebEngineView):
    def __init__(self, parent=None):
        super(PushBullet, self).__init__(parent)
        self.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        path = __file__
        abs_dir = path[:path.rfind("/")]
        self.load(QUrl('file:///%s/index.html' % abs_dir))
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pushbullet = PushBullet()
    pushbullet.show()
    sys.exit(app.exec_())
