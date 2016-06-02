# -*- coding: utf-8 -*-
# Author: Zack Bin
# Created on: 2016.06.01   22:11:33

# Import 
import sys
from PyQt4 import QtGui

# Function
app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('Test PyQt4')
widget.show()

sys.exit(app.exec_())