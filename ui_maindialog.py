# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_maindialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(994, 647)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/qgis2web/icons/qgis2web.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainDialog.setWindowIcon(icon)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(MainDialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(MainDialog)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layersTree = QtWidgets.QTreeWidget(self.splitter)
        self.layersTree.setMinimumSize(QtCore.QSize(400, 0))
        self.layersTree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.layersTree.setObjectName("layersTree")
        self.layersTree.headerItem().setText(0, "1")
        self.layersTree.header().setVisible(False)
        self.layersTree.header().setDefaultSectionSize(200)
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.paramsTreeOL = QtWidgets.QTreeWidget(self.widget)
        self.paramsTreeOL.setMinimumSize(QtCore.QSize(300, 0))
        self.paramsTreeOL.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.paramsTreeOL.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.paramsTreeOL.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.paramsTreeOL.setAutoScroll(False)
        self.paramsTreeOL.setObjectName("paramsTreeOL")
        self.paramsTreeOL.header().setVisible(False)
        self.paramsTreeOL.header().setCascadingSectionResizes(False)
        self.paramsTreeOL.header().setDefaultSectionSize(200)
        self.verticalLayout_5.addWidget(self.paramsTreeOL)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ol3 = QtWidgets.QRadioButton(self.widget)
        self.ol3.setChecked(True)
        self.ol3.setObjectName("ol3")
        self.mapFormat = QtWidgets.QButtonGroup(MainDialog)
        self.mapFormat.setObjectName("mapFormat")
        self.mapFormat.addButton(self.ol3)
        self.horizontalLayout_2.addWidget(self.ol3)
        self.leaflet = QtWidgets.QRadioButton(self.widget)
        self.leaflet.setObjectName("leaflet")
        self.mapFormat.addButton(self.leaflet)
        self.horizontalLayout_2.addWidget(self.leaflet)
        self.buttonPreview = QtWidgets.QPushButton(self.widget)
        self.buttonPreview.setMinimumSize(QtCore.QSize(0, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/qgis2web/icons/preview.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPreview.setIcon(icon1)
        self.buttonPreview.setObjectName("buttonPreview")
        self.horizontalLayout_2.addWidget(self.buttonPreview)
        self.buttonExport = QtWidgets.QPushButton(self.widget)
        self.buttonExport.setIcon(icon)
        self.buttonExport.setObjectName("buttonExport")
        self.horizontalLayout_2.addWidget(self.buttonExport)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.preview = QtWebKitWidgets.QWebView(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy)
        self.preview.setUrl(QtCore.QUrl("about:blank"))
        self.preview.setObjectName("preview")
        self.verticalLayout_2.addWidget(self.preview)
        self.basemaps = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.basemaps.setObjectName("basemaps")
        self.verticalLayout_2.addWidget(self.basemaps)
        self.horizontalLayout.addWidget(self.splitter_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.helpField = QtWidgets.QTextBrowser(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.helpField.setFont(font)
        self.helpField.setStyleSheet("padding: 10px;")
        self.helpField.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.helpField.setFrameShadow(QtWidgets.QFrame.Plain)
        self.helpField.setLineWidth(0)
        self.helpField.setObjectName("helpField")
        self.horizontalLayout_4.addWidget(self.helpField)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.retranslateUi(MainDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Export to web map"))
        self.layersTree.headerItem().setText(1, _translate("MainDialog", "2"))
        self.paramsTreeOL.headerItem().setText(0, _translate("MainDialog", "Setting"))
        self.paramsTreeOL.headerItem().setText(1, _translate("MainDialog", "Value"))
        self.ol3.setText(_translate("MainDialog", "OpenLayers 3"))
        self.leaflet.setText(_translate("MainDialog", "Leaflet"))
        self.buttonPreview.setText(_translate("MainDialog", "Update preview"))
        self.buttonExport.setText(_translate("MainDialog", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainDialog", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainDialog", "Help"))

from PyQt5 import QtWebKitWidgets
import resources_rc
