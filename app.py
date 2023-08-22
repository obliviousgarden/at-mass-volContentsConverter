from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFormLayout
import numpy as np
from utils.component import Component
from utils.element import Element
import os, sys
from utils.common_components import Co,SrF2
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

from ui.converter import Ui_MainWindow
from utils.str_splitter import split_substance_and_media


class Converter(Ui_MainWindow):
    def __init__(self):
        super(Converter, self).__init__()
        # dict for intro
        self.intro_text = {
            "en":"This is a converter that converts at.%, mass.% and col.% and estimates the diameter or intervl of the ideal spatial distribution. \n"
                 "Substance and Media will be automatically identified, and if the parameters (mass density and atomic mass) corresponding to the component or element exist in the database, \n"
                 "they will be automatically updated to the groupbox below.",
            "cn":"这是一个转换器，用来换算at.%, mass.% and col.%，并估计理想空间分布的直径或者间距。\n"
                 "Substance和Media会被自动识别，如果对应物质或元素的参数（质量密度和原子质量）是数据库中存在的，\n"
                 "那么将会被自动更新到下方的组框中。",
            "jp":"これはat.%とmass.%とcol.%とを変換し、理想的な空間分布の直径や間隔を推定するコンバータです。\n"
                 "SubstanceやMediaを自動認識し、データベースに組成や元素に対応するパラメータ(質量密度や原子質量)が存在すれば、\n"
                 "下のグループボックスに自動的に更新されます。"
        }
        self.substance_str = "Co"
        self.media_str = "SrF2"
        self.component_list = [Co,SrF2]
        self.element_list = [Element('Co',58.933194),Element('F',18.998403163),Element('Sr',87.62)]
        self.at_content = 56.58
        self.mass_content = at_mass_converter(component_list=self.component_list,element_list=self.element_list,at_content=self.at_content)
        self.vol_content = vol_mass_converter(component_list=self.component_list,mass_content=self.mass_content)
        self.recalculating_flag = False
        self.reestimating_flag = False
        self.diameter = 3.0
        self.interval = 0.5


    def setupUi(self, MainWindow):
        # Father's UI
        Ui_MainWindow.setupUi(self, MainWindow)
        # Menu
        self.actionQuit.triggered.connect(on_Action_quit)
        # Initialize the introduction part
        self.textEdit_intro.setText(self.intro_text.get("en"))
        # EN-CN-JP
        self.radioButton_intro_en.clicked.connect(self.update_textEdit_intro)
        self.radioButton_intro_cn.clicked.connect(self.update_textEdit_intro)
        self.radioButton_intro_jp.clicked.connect(self.update_textEdit_intro)
        # Set validator 只允许 Co1.5Fe3.7的写法，不允许出现括号或者空格或者逗号等符号
        regex = QRegExp("[A-Za-z0-9.]*")
        validator_substance = QRegExpValidator(regex, self.lineEdit_substance)
        validator_media = QRegExpValidator(regex, self.lineEdit_media)
        self.lineEdit_substance.setValidator(validator_substance)
        self.lineEdit_media.setValidator(validator_media)
        # Update substance or media info in 2 GroupBox
        self.lineEdit_substance.editingFinished.connect(self.update_materials)
        self.lineEdit_media.editingFinished.connect(self.update_materials)
        # fill all contents
        self.doubleSpinBox_at.setValue(self.at_content)
        self.doubleSpinBox_mass.setValue(self.mass_content)
        self.doubleSpinBox_vol.setValue(self.vol_content)
        # set recalculation for all contents
        self.doubleSpinBox_at.valueChanged.connect(self.recalculate_contents_from_at)
        self.doubleSpinBox_mass.valueChanged.connect(self.recalculate_contents_from_mass)
        self.doubleSpinBox_vol.valueChanged.connect(self.recalculate_contents_from_vol)
        # fill all atomic mass and mass density
        self.doubleSpinBox_atomicmass_1.setValue(self.element_list[0].get_atomic_mass())
        self.doubleSpinBox_atomicmass_2.setValue(self.element_list[1].get_atomic_mass())
        self.doubleSpinBox_atomicmass_3.setValue(self.element_list[2].get_atomic_mass())
        self.doubleSpinBox_massdensity_1.setValue(self.component_list[0].get_mass_density())
        self.doubleSpinBox_massdensity_2.setValue(self.component_list[1].get_mass_density())
        # estimation-ralated
        self.radioButton_estimation_fcc.clicked.connect(self.reestimate_spactial_from_diameter)
        self.radioButton_estimation_bcc.clicked.connect(self.reestimate_spactial_from_diameter)
        self.doubleSpinBox_estimation_diameter.setValue(self.diameter)
        self.doubleSpinBox_estimation_interval.setValue(self.interval)
        self.doubleSpinBox_estimation_diameter.valueChanged.connect(self.reestimate_spactial_from_diameter)
        self.doubleSpinBox_estimation_interval.valueChanged.connect(self.reestimate_spactial_from_interval)


    def update_textEdit_intro(self):
        if self.radioButton_intro_en.isChecked():
            self.textEdit_intro.setText(self.intro_text.get("en"))
        elif self.radioButton_intro_cn.isChecked():
            self.textEdit_intro.setText(self.intro_text.get("cn"))
        elif self.radioButton_intro_jp.isChecked():
            self.textEdit_intro.setText(self.intro_text.get("jp"))
        else:
            pass

    def update_materials(self):
        self.substance_str = self.lineEdit_substance.text()
        self.media_str = self.lineEdit_media.text()
        self.component_list, self.element_list = split_substance_and_media(self.substance_str,self.media_str)
        # Update Element info.
        for row in range(self.formLayout_2.rowCount(),-1,-1):
            self.formLayout_2.removeRow(row)
        for index,element in enumerate(self.element_list):
            label_widget = QtWidgets.QLabel(self.groupBox_atomicmass)
            label_widget.setText(element.get_element_str())
            label_widget.setObjectName("label_atomicmass_"+str(index))
            doubleSpinBox_widget = QtWidgets.QDoubleSpinBox(self.groupBox_atomicmass)
            doubleSpinBox_widget.setMaximum(999.9)
            doubleSpinBox_widget.setSingleStep(0.05)
            doubleSpinBox_widget.setValue(element.get_atomic_mass())
            doubleSpinBox_widget.setObjectName("doubleSpinBox_atomicmass_"+str(index))
            self.formLayout_2.addRow(label_widget,doubleSpinBox_widget)
        # Update Component info.
        for row in range(self.formLayout.rowCount(),-1,-1):
            self.formLayout.removeRow(row)
        for index,component in enumerate(self.component_list):
            label_widget = QtWidgets.QLabel(self.groupBox_massdensity)
            label_widget.setText(component.get_composition_str())
            label_widget.setObjectName("label_massdensity_"+str(index))
            doubleSpinBox_widget = QtWidgets.QDoubleSpinBox(self.groupBox_massdensity)
            doubleSpinBox_widget.setMaximum(999.9)
            doubleSpinBox_widget.setSingleStep(0.05)
            doubleSpinBox_widget.setValue(component.get_mass_density())
            doubleSpinBox_widget.setObjectName("doubleSpinBox_massdensity_"+str(index))
            self.formLayout.addRow(label_widget,doubleSpinBox_widget)
    def update_component_and_element_list(self):
        # Update Element info.
        print("Element info.:")
        for row in range(self.formLayout_2.rowCount()):
            atomic_mass_str = self.formLayout_2.itemAt(row,QFormLayout.FieldRole).widget().text()
            self.element_list[row].set_atomic_mass(float(atomic_mass_str))
            print(self.element_list[row].get_element_str(),":",self.element_list[row].get_atomic_mass(),"u")
        # Update Component info.
        print("Component info.:")
        for row in range(self.formLayout.rowCount()):
            mass_density_str = self.formLayout.itemAt(row,QFormLayout.FieldRole).widget().text()
            self.component_list[row].set_mass_density(float(mass_density_str))
            print(self.component_list[row].get_composition_str(),":",self.component_list[row].get_mass_density(),"/cm^3")

    def recalculate_contents_from_at(self):
        if self.recalculating_flag is False:
            # 计算前必须更新一次components和element内部的atomic mass和mass density的参数
            self.update_component_and_element_list()
            print('Recalculate from at.%')
            self.recalculating_flag = True
            self.at_content = self.doubleSpinBox_at.value()
            self.mass_content = at_mass_converter(component_list=self.component_list,element_list=self.element_list,at_content=self.at_content,mass_content=None)
            self.vol_content = vol_mass_converter(component_list=self.component_list,vol_content=None,mass_content=self.mass_content)
            self.doubleSpinBox_mass.setValue(self.mass_content)
            self.doubleSpinBox_vol.setValue(self.vol_content)
            self.recalculating_flag = False
            self.reestimate_spactial_from_diameter()
    def recalculate_contents_from_mass(self):
        if self.recalculating_flag is False:
            # 计算前必须更新一次components和element内部的atomic mass和mass density的参数
            self.update_component_and_element_list()
            print('Recalculate from mass.%')
            self.recalculating_flag = True
            self.mass_content = self.doubleSpinBox_mass.value()
            self.at_content = at_mass_converter(component_list=self.component_list,element_list=self.element_list,at_content=None,mass_content=self.mass_content)
            self.vol_content = vol_mass_converter(component_list=self.component_list,vol_content=None,mass_content=self.mass_content)
            self.doubleSpinBox_at.setValue(self.at_content)
            self.doubleSpinBox_vol.setValue(self.vol_content)
            self.recalculating_flag = False
            self.reestimate_spactial_from_diameter()
    def recalculate_contents_from_vol(self):
        if self.recalculating_flag is False:
            # 计算前必须更新一次components和element内部的atomic mass和mass density的参数
            self.update_component_and_element_list()
            print('Recalculate from vol.%')
            self.recalculating_flag = True
            self.vol_content = self.doubleSpinBox_vol.value()
            self.mass_content = vol_mass_converter(component_list=self.component_list,vol_content=self.vol_content,mass_content=None)
            self.at_content = at_mass_converter(component_list=self.component_list,element_list=self.element_list,at_content=None,mass_content=self.mass_content)
            self.doubleSpinBox_mass.setValue(self.mass_content)
            self.doubleSpinBox_vol.setValue(self.vol_content)
            self.recalculating_flag = False
            self.reestimate_spactial_from_diameter()
    def reestimate_spactial_from_diameter(self):
        if self.reestimating_flag is False:
            print('Reestimate from Diameter')
            self.reestimating_flag = True
            self.diameter = self.doubleSpinBox_estimation_diameter.value()
            if self.radioButton_estimation_fcc.isChecked():
                sd_ratio = np.power(np.pi/(3.0*np.sqrt(2.0)*self.vol_content/100.0),1/3)-1.0
                self.interval = self.diameter*sd_ratio
            elif self.radioButton_estimation_bcc.isChecked():
                sd_ratio = np.power((np.sqrt(3)*np.pi)/(8*self.vol_content/100.0),1/3)-1.0
                self.interval = self.diameter*sd_ratio
            else:
                print('Neither FCC nor BCC')
            self.doubleSpinBox_estimation_interval.setValue(self.interval)
            self.reestimating_flag = False

    def reestimate_spactial_from_interval(self):
        if self.reestimating_flag is False:
            print('Reestimate from Interval')
            self.reestimating_flag = True
            self.interval = self.doubleSpinBox_estimation_interval.value()
            if self.radioButton_estimation_fcc.isChecked():
                sd_ratio = np.power(np.pi/(3.0*np.sqrt(2.0)*self.vol_content/100.0),1/3)-1.0
                self.diameter = self.interval/sd_ratio
            elif self.radioButton_estimation_bcc.isChecked():
                sd_ratio = np.power((np.sqrt(3)*np.pi)/(8*self.vol_content/100.0),1/3)-1.0
                self.diameter = self.interval/sd_ratio
            else:
                print('Neither FCC nor BCC')
            self.doubleSpinBox_estimation_diameter.setValue(self.diameter)
            self.reestimating_flag = False

def at_mass_converter(component_list,element_list,at_content:float=None,mass_content:float=None)->float:
    # (a+b+d)/(aA+bB+dD) term
    # TODO:以后可能会出现多组分的substance或者media，这里则需要改写
    substance_compoennt = component_list[0]
    media_compoennt = component_list[1]
    term_substance_top = 0.0
    term_substance_bot = 0.0
    for index, element_str in enumerate(substance_compoennt.get_element_list()):
        subscript = substance_compoennt.get_subscript_list()[index]
        term_substance_top += subscript
        for element in element_list:
            if element_str == element.get_element_str():
                term_substance_bot += subscript*element.get_atomic_mass()
                break
    term_substance = term_substance_top/term_substance_bot
    term_media_top = 0.0
    term_media_bot = 0.0
    for index, element_str in enumerate(media_compoennt.get_element_list()):
        subscript = media_compoennt.get_subscript_list()[index]
        term_media_top += subscript
        for element in element_list:
            if element_str == element.get_element_str():
                term_media_bot += subscript*element.get_atomic_mass()
                break
    term_media=term_media_top/term_media_bot
    print("Substance term:",term_substance_top,term_substance_bot,term_substance)
    print("Media term:",term_media_top,term_media_bot,term_media)

    if at_content is not None:
        # at计算mass
        mass_content = (at_content/term_substance)/(at_content/term_substance+(100-at_content)/term_media)*100
        return mass_content
    else:
        # mass计算at
        at_content = (mass_content*term_substance)/(mass_content*term_substance+(100-mass_content)*term_media)*100
        return at_content

def vol_mass_converter(component_list,vol_content:float=None,mass_content:float=None)->float:
    # TODO:以后可能会出现多组分的substance或者media，这里则需要改写
    mass_density_substance = component_list[0].get_mass_density()
    mass_density_media = component_list[1].get_mass_density()
    if vol_content is not None:
        # vol计算mass
        mass_content = (vol_content*mass_density_substance)/(vol_content*mass_density_substance+(100-vol_content)*mass_density_media)*100
        return mass_content
    else:
        # mass计算vol
        vol_content = (mass_content/mass_density_substance)/(mass_content/mass_density_substance+(100-mass_content)/mass_density_media)*100
        return vol_content

def on_Action_quit():
    sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    converter = Converter()
    converter.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())