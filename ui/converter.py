# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/ユウカ.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_intro = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_intro.setObjectName("groupBox_intro")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_intro)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_intro_en = QtWidgets.QRadioButton(self.groupBox_intro)
        self.radioButton_intro_en.setChecked(True)
        self.radioButton_intro_en.setObjectName("radioButton_intro_en")
        self.horizontalLayout.addWidget(self.radioButton_intro_en)
        self.radioButton_intro_cn = QtWidgets.QRadioButton(self.groupBox_intro)
        self.radioButton_intro_cn.setObjectName("radioButton_intro_cn")
        self.horizontalLayout.addWidget(self.radioButton_intro_cn)
        self.radioButton_intro_jp = QtWidgets.QRadioButton(self.groupBox_intro)
        self.radioButton_intro_jp.setObjectName("radioButton_intro_jp")
        self.horizontalLayout.addWidget(self.radioButton_intro_jp)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.textEdit_intro = QtWidgets.QTextEdit(self.groupBox_intro)
        self.textEdit_intro.setEnabled(True)
        self.textEdit_intro.setReadOnly(True)
        self.textEdit_intro.setObjectName("textEdit_intro")
        self.verticalLayout_4.addWidget(self.textEdit_intro)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout.addWidget(self.groupBox_intro)
        self.horizontalLayout_setting = QtWidgets.QHBoxLayout()
        self.horizontalLayout_setting.setObjectName("horizontalLayout_setting")
        self.label_substance = QtWidgets.QLabel(self.centralwidget)
        self.label_substance.setObjectName("label_substance")
        self.horizontalLayout_setting.addWidget(self.label_substance)
        self.lineEdit_substance = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_substance.setInputMask("")
        self.lineEdit_substance.setObjectName("lineEdit_substance")
        self.horizontalLayout_setting.addWidget(self.lineEdit_substance)
        self.label_media = QtWidgets.QLabel(self.centralwidget)
        self.label_media.setObjectName("label_media")
        self.horizontalLayout_setting.addWidget(self.label_media)
        self.lineEdit_media = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_media.setObjectName("lineEdit_media")
        self.horizontalLayout_setting.addWidget(self.lineEdit_media)
        self.verticalLayout.addLayout(self.horizontalLayout_setting)
        self.horizontalLayout_at = QtWidgets.QHBoxLayout()
        self.horizontalLayout_at.setObjectName("horizontalLayout_at")
        self.label_at = QtWidgets.QLabel(self.centralwidget)
        self.label_at.setObjectName("label_at")
        self.horizontalLayout_at.addWidget(self.label_at)
        self.doubleSpinBox_at = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_at.setSingleStep(0.5)
        self.doubleSpinBox_at.setObjectName("doubleSpinBox_at")
        self.horizontalLayout_at.addWidget(self.doubleSpinBox_at)
        self.horizontalLayout_at.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_at)
        self.groupBox_atomicmass = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_atomicmass.setObjectName("groupBox_atomicmass")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_atomicmass)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_atomicmass_1 = QtWidgets.QLabel(self.groupBox_atomicmass)
        self.label_atomicmass_1.setObjectName("label_atomicmass_1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_atomicmass_1)
        self.doubleSpinBox_atomicmass_1 = QtWidgets.QDoubleSpinBox(self.groupBox_atomicmass)
        self.doubleSpinBox_atomicmass_1.setReadOnly(False)
        self.doubleSpinBox_atomicmass_1.setMaximum(999.99)
        self.doubleSpinBox_atomicmass_1.setObjectName("doubleSpinBox_atomicmass_1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_atomicmass_1)
        self.label_atomicmass_2 = QtWidgets.QLabel(self.groupBox_atomicmass)
        self.label_atomicmass_2.setObjectName("label_atomicmass_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_atomicmass_2)
        self.doubleSpinBox_atomicmass_2 = QtWidgets.QDoubleSpinBox(self.groupBox_atomicmass)
        self.doubleSpinBox_atomicmass_2.setReadOnly(False)
        self.doubleSpinBox_atomicmass_2.setMaximum(999.99)
        self.doubleSpinBox_atomicmass_2.setObjectName("doubleSpinBox_atomicmass_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_atomicmass_2)
        self.label_atomicmass_3 = QtWidgets.QLabel(self.groupBox_atomicmass)
        self.label_atomicmass_3.setObjectName("label_atomicmass_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_atomicmass_3)
        self.doubleSpinBox_atomicmass_3 = QtWidgets.QDoubleSpinBox(self.groupBox_atomicmass)
        self.doubleSpinBox_atomicmass_3.setReadOnly(False)
        self.doubleSpinBox_atomicmass_3.setMaximum(999.99)
        self.doubleSpinBox_atomicmass_3.setObjectName("doubleSpinBox_atomicmass_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_atomicmass_3)
        self.verticalLayout.addWidget(self.groupBox_atomicmass)
        self.horizontalLayout_mass = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mass.setObjectName("horizontalLayout_mass")
        self.label_mass = QtWidgets.QLabel(self.centralwidget)
        self.label_mass.setObjectName("label_mass")
        self.horizontalLayout_mass.addWidget(self.label_mass)
        self.doubleSpinBox_mass = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_mass.setSingleStep(0.5)
        self.doubleSpinBox_mass.setObjectName("doubleSpinBox_mass")
        self.horizontalLayout_mass.addWidget(self.doubleSpinBox_mass)
        self.horizontalLayout_mass.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_mass)
        self.groupBox_massdensity = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_massdensity.setObjectName("groupBox_massdensity")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_massdensity)
        self.formLayout.setObjectName("formLayout")
        self.label_massdensity_1 = QtWidgets.QLabel(self.groupBox_massdensity)
        self.label_massdensity_1.setObjectName("label_massdensity_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_massdensity_1)
        self.doubleSpinBox_massdensity_1 = QtWidgets.QDoubleSpinBox(self.groupBox_massdensity)
        self.doubleSpinBox_massdensity_1.setMaximum(999.99)
        self.doubleSpinBox_massdensity_1.setSingleStep(0.05)
        self.doubleSpinBox_massdensity_1.setObjectName("doubleSpinBox_massdensity_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_massdensity_1)
        self.label_massdensity_2 = QtWidgets.QLabel(self.groupBox_massdensity)
        self.label_massdensity_2.setObjectName("label_massdensity_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_massdensity_2)
        self.doubleSpinBox_massdensity_2 = QtWidgets.QDoubleSpinBox(self.groupBox_massdensity)
        self.doubleSpinBox_massdensity_2.setMaximum(999.99)
        self.doubleSpinBox_massdensity_2.setSingleStep(0.05)
        self.doubleSpinBox_massdensity_2.setObjectName("doubleSpinBox_massdensity_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_massdensity_2)
        self.verticalLayout.addWidget(self.groupBox_massdensity)
        self.horizontalLayout_vol = QtWidgets.QHBoxLayout()
        self.horizontalLayout_vol.setObjectName("horizontalLayout_vol")
        self.label_vol = QtWidgets.QLabel(self.centralwidget)
        self.label_vol.setObjectName("label_vol")
        self.horizontalLayout_vol.addWidget(self.label_vol)
        self.doubleSpinBox_vol = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_vol.setSingleStep(0.5)
        self.doubleSpinBox_vol.setObjectName("doubleSpinBox_vol")
        self.horizontalLayout_vol.addWidget(self.doubleSpinBox_vol)
        self.horizontalLayout_vol.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_vol)
        self.groupBox_estimation = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_estimation.setObjectName("groupBox_estimation")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_estimation)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_estimation_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_estimation_1.setObjectName("horizontalLayout_estimation_1")
        self.radioButton_estimation_fcc = QtWidgets.QRadioButton(self.groupBox_estimation)
        self.radioButton_estimation_fcc.setChecked(True)
        self.radioButton_estimation_fcc.setObjectName("radioButton_estimation_fcc")
        self.horizontalLayout_estimation_1.addWidget(self.radioButton_estimation_fcc)
        self.radioButton_estimation_bcc = QtWidgets.QRadioButton(self.groupBox_estimation)
        self.radioButton_estimation_bcc.setObjectName("radioButton_estimation_bcc")
        self.horizontalLayout_estimation_1.addWidget(self.radioButton_estimation_bcc)
        self.verticalLayout_2.addLayout(self.horizontalLayout_estimation_1)
        self.horizontalLayout_estimation_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_estimation_2.setObjectName("horizontalLayout_estimation_2")
        self.label_estimation_diameter = QtWidgets.QLabel(self.groupBox_estimation)
        self.label_estimation_diameter.setObjectName("label_estimation_diameter")
        self.horizontalLayout_estimation_2.addWidget(self.label_estimation_diameter)
        self.doubleSpinBox_estimation_diameter = QtWidgets.QDoubleSpinBox(self.groupBox_estimation)
        self.doubleSpinBox_estimation_diameter.setSingleStep(0.1)
        self.doubleSpinBox_estimation_diameter.setObjectName("doubleSpinBox_estimation_diameter")
        self.horizontalLayout_estimation_2.addWidget(self.doubleSpinBox_estimation_diameter)
        self.label_estimation_interval = QtWidgets.QLabel(self.groupBox_estimation)
        self.label_estimation_interval.setObjectName("label_estimation_interval")
        self.horizontalLayout_estimation_2.addWidget(self.label_estimation_interval)
        self.doubleSpinBox_estimation_interval = QtWidgets.QDoubleSpinBox(self.groupBox_estimation)
        self.doubleSpinBox_estimation_interval.setSingleStep(0.1)
        self.doubleSpinBox_estimation_interval.setObjectName("doubleSpinBox_estimation_interval")
        self.horizontalLayout_estimation_2.addWidget(self.doubleSpinBox_estimation_interval)
        self.verticalLayout_2.addLayout(self.horizontalLayout_estimation_2)
        self.verticalLayout.addWidget(self.groupBox_estimation)
        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionComponent_Manegement = QtWidgets.QAction(MainWindow)
        self.actionComponent_Manegement.setObjectName("actionComponent_Manegement")
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionComponent_Manegement)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "at.%-mass.%-vol.% Converter by 誠"))
        self.groupBox_intro.setTitle(_translate("MainWindow", "What am I?"))
        self.radioButton_intro_en.setText(_translate("MainWindow", "English"))
        self.radioButton_intro_cn.setText(_translate("MainWindow", "汉语"))
        self.radioButton_intro_jp.setText(_translate("MainWindow", "日本語"))
        self.textEdit_intro.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.label_substance.setText(_translate("MainWindow", "Substance"))
        self.lineEdit_substance.setText(_translate("MainWindow", "Co"))
        self.label_media.setText(_translate("MainWindow", "in Media"))
        self.lineEdit_media.setText(_translate("MainWindow", "SrF2"))
        self.label_at.setText(_translate("MainWindow", "X(at.%) = "))
        self.groupBox_atomicmass.setTitle(_translate("MainWindow", "Atomic mass(u)"))
        self.label_atomicmass_1.setText(_translate("MainWindow", "Co"))
        self.label_atomicmass_2.setText(_translate("MainWindow", "F"))
        self.label_atomicmass_3.setText(_translate("MainWindow", "Sr"))
        self.label_mass.setText(_translate("MainWindow", "X(mass.%) = "))
        self.groupBox_massdensity.setTitle(_translate("MainWindow", "Mass density(g/cm^3)"))
        self.label_massdensity_1.setText(_translate("MainWindow", "Co"))
        self.label_massdensity_2.setText(_translate("MainWindow", "SrF2"))
        self.label_vol.setText(_translate("MainWindow", "X(vol.%) = "))
        self.groupBox_estimation.setTitle(_translate("MainWindow", "ideal spactial estimation(nm)"))
        self.radioButton_estimation_fcc.setText(_translate("MainWindow", "FCC-like"))
        self.radioButton_estimation_bcc.setText(_translate("MainWindow", "BCC-like"))
        self.label_estimation_diameter.setText(_translate("MainWindow", "Diameter"))
        self.label_estimation_interval.setText(_translate("MainWindow", "Interval"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Settings"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionComponent_Manegement.setText(_translate("MainWindow", "Component Manegement"))
import ui.converter_rc
