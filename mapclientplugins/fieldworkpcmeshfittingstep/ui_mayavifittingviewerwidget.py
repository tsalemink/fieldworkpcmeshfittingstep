# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mayavifittingviewerwidget.ui'
#
# Created: Sun Jun  8 14:05:22 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1087, 771)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget1 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setMinimumSize(QtCore.QSize(350, 0))
        self.widget1.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtGui.QTableWidget(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.toolBox = QtGui.QToolBox(self.widget1)
        self.toolBox.setObjectName("toolBox")
        self.page_fitting = QtGui.QWidget()
        self.page_fitting.setGeometry(QtCore.QRect(0, 0, 319, 542))
        self.page_fitting.setObjectName("page_fitting")
        self.verticalLayout = QtGui.QVBoxLayout(self.page_fitting)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.page_fitting)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBoxDistanceMode = QtGui.QComboBox(self.groupBox)
        self.comboBoxDistanceMode.setObjectName("comboBoxDistanceMode")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxDistanceMode)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spinBoxPCsToFit = QtGui.QSpinBox(self.groupBox)
        self.spinBoxPCsToFit.setObjectName("spinBoxPCsToFit")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBoxPCsToFit)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinBoxSurfDisc = QtGui.QSpinBox(self.groupBox)
        self.spinBoxSurfDisc.setObjectName("spinBoxSurfDisc")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBoxSurfDisc)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBoxMWeight = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxMWeight.setObjectName("doubleSpinBoxMWeight")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxMWeight)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.spinBoxMaxfev = QtGui.QSpinBox(self.groupBox)
        self.spinBoxMaxfev.setObjectName("spinBoxMaxfev")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.spinBoxMaxfev)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.checkBoxFitSize = QtGui.QCheckBox(self.groupBox)
        self.checkBoxFitSize.setText("")
        self.checkBoxFitSize.setObjectName("checkBoxFitSize")
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.checkBoxFitSize)
        self.lineEditXTol = QtGui.QLineEdit(self.groupBox)
        self.lineEditXTol.setObjectName("lineEditXTol")
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEditXTol)
        self.lineEditLandmarks = QtGui.QLineEdit(self.groupBox)
        self.lineEditLandmarks.setObjectName("lineEditLandmarks")
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEditLandmarks)
        self.lineEditLandmarkWeights = QtGui.QLineEdit(self.groupBox)
        self.lineEditLandmarkWeights.setObjectName("lineEditLandmarkWeights")
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEditLandmarkWeights)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.verticalLayout.addWidget(self.groupBox)
        self.fitButtonsGroup = QtGui.QGridLayout()
        self.fitButtonsGroup.setObjectName("fitButtonsGroup")
        self.acceptButton = QtGui.QPushButton(self.page_fitting)
        self.acceptButton.setObjectName("acceptButton")
        self.fitButtonsGroup.addWidget(self.acceptButton, 1, 1, 1, 1)
        self.resetButton = QtGui.QPushButton(self.page_fitting)
        self.resetButton.setObjectName("resetButton")
        self.fitButtonsGroup.addWidget(self.resetButton, 0, 1, 1, 1)
        self.abortButton = QtGui.QPushButton(self.page_fitting)
        self.abortButton.setObjectName("abortButton")
        self.fitButtonsGroup.addWidget(self.abortButton, 1, 0, 1, 1)
        self.fitButton = QtGui.QPushButton(self.page_fitting)
        self.fitButton.setObjectName("fitButton")
        self.fitButtonsGroup.addWidget(self.fitButton, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.fitButtonsGroup)
        self.errorGroup = QtGui.QGroupBox(self.page_fitting)
        self.errorGroup.setObjectName("errorGroup")
        self.formLayout_2 = QtGui.QFormLayout(self.errorGroup)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.RMSELabel = QtGui.QLabel(self.errorGroup)
        self.RMSELabel.setObjectName("RMSELabel")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.RMSELabel)
        self.RMSELineEdit = QtGui.QLineEdit(self.errorGroup)
        self.RMSELineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RMSELineEdit.setReadOnly(True)
        self.RMSELineEdit.setObjectName("RMSELineEdit")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.RMSELineEdit)
        self.meanErrorLabel = QtGui.QLabel(self.errorGroup)
        self.meanErrorLabel.setObjectName("meanErrorLabel")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.meanErrorLabel)
        self.meanErrorLineEdit = QtGui.QLineEdit(self.errorGroup)
        self.meanErrorLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.meanErrorLineEdit.setReadOnly(True)
        self.meanErrorLineEdit.setObjectName("meanErrorLineEdit")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.meanErrorLineEdit)
        self.SDLabel = QtGui.QLabel(self.errorGroup)
        self.SDLabel.setObjectName("SDLabel")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.SDLabel)
        self.SDLineEdit = QtGui.QLineEdit(self.errorGroup)
        self.SDLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SDLineEdit.setReadOnly(True)
        self.SDLineEdit.setObjectName("SDLineEdit")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.SDLineEdit)
        self.verticalLayout.addWidget(self.errorGroup)
        self.toolBox.addItem(self.page_fitting, "")
        self.Screenshot = QtGui.QWidget()
        self.Screenshot.setGeometry(QtCore.QRect(0, 0, 332, 499))
        self.Screenshot.setObjectName("Screenshot")
        self.formLayout = QtGui.QFormLayout(self.Screenshot)
        self.formLayout.setObjectName("formLayout")
        self.pixelsXLabel = QtGui.QLabel(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelsXLabel.sizePolicy().hasHeightForWidth())
        self.pixelsXLabel.setSizePolicy(sizePolicy)
        self.pixelsXLabel.setObjectName("pixelsXLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pixelsXLabel)
        self.screenshotPixelXLineEdit = QtGui.QLineEdit(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotPixelXLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelXLineEdit.setSizePolicy(sizePolicy)
        self.screenshotPixelXLineEdit.setObjectName("screenshotPixelXLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.screenshotPixelXLineEdit)
        self.pixelsYLabel = QtGui.QLabel(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelsYLabel.sizePolicy().hasHeightForWidth())
        self.pixelsYLabel.setSizePolicy(sizePolicy)
        self.pixelsYLabel.setObjectName("pixelsYLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pixelsYLabel)
        self.screenshotPixelYLineEdit = QtGui.QLineEdit(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotPixelYLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelYLineEdit.setSizePolicy(sizePolicy)
        self.screenshotPixelYLineEdit.setObjectName("screenshotPixelYLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.screenshotPixelYLineEdit)
        self.screenshotFilenameLabel = QtGui.QLabel(self.Screenshot)
        self.screenshotFilenameLabel.setObjectName("screenshotFilenameLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.screenshotFilenameLabel)
        self.screenshotFilenameLineEdit = QtGui.QLineEdit(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotFilenameLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotFilenameLineEdit.setSizePolicy(sizePolicy)
        self.screenshotFilenameLineEdit.setObjectName("screenshotFilenameLineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.screenshotFilenameLineEdit)
        self.screenshotSaveButton = QtGui.QPushButton(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotSaveButton.sizePolicy().hasHeightForWidth())
        self.screenshotSaveButton.setSizePolicy(sizePolicy)
        self.screenshotSaveButton.setObjectName("screenshotSaveButton")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.screenshotSaveButton)
        self.toolBox.addItem(self.Screenshot, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.gridLayout.addWidget(self.widget1, 0, 0, 1, 1)
        self.MayaviScene = MayaviSceneWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MayaviScene.sizePolicy().hasHeightForWidth())
        self.MayaviScene.setSizePolicy(sizePolicy)
        self.MayaviScene.setObjectName("MayaviScene")
        self.gridLayout.addWidget(self.MayaviScene, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Mesh Fitting", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Visible", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Fitting Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Distance Model:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "PCs to Fit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Surface Discretisation:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Mahalanobis Weight:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "maxfev:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "xtol:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Fit Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Landmarks:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Landmark Weights:", None, QtGui.QApplication.UnicodeUTF8))
        self.acceptButton.setText(QtGui.QApplication.translate("Dialog", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("Dialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.abortButton.setText(QtGui.QApplication.translate("Dialog", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.fitButton.setText(QtGui.QApplication.translate("Dialog", "Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.errorGroup.setTitle(QtGui.QApplication.translate("Dialog", "Fitting Errors", None, QtGui.QApplication.UnicodeUTF8))
        self.RMSELabel.setText(QtGui.QApplication.translate("Dialog", "RMS:", None, QtGui.QApplication.UnicodeUTF8))
        self.meanErrorLabel.setText(QtGui.QApplication.translate("Dialog", "Mean:", None, QtGui.QApplication.UnicodeUTF8))
        self.SDLabel.setText(QtGui.QApplication.translate("Dialog", "S.D.:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_fitting), QtGui.QApplication.translate("Dialog", "Fitting", None, QtGui.QApplication.UnicodeUTF8))
        self.pixelsXLabel.setText(QtGui.QApplication.translate("Dialog", "Pixels X:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotPixelXLineEdit.setText(QtGui.QApplication.translate("Dialog", "800", None, QtGui.QApplication.UnicodeUTF8))
        self.pixelsYLabel.setText(QtGui.QApplication.translate("Dialog", "Pixels Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotPixelYLineEdit.setText(QtGui.QApplication.translate("Dialog", "600", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotFilenameLabel.setText(QtGui.QApplication.translate("Dialog", "Filename:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotFilenameLineEdit.setText(QtGui.QApplication.translate("Dialog", "screenshot.png", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotSaveButton.setText(QtGui.QApplication.translate("Dialog", "Save Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Screenshot), QtGui.QApplication.translate("Dialog", "Screenshots", None, QtGui.QApplication.UnicodeUTF8))

from mappluginutils.mayaviviewer.mayaviscenewidget import MayaviSceneWidget
