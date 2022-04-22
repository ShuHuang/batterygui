# -*- coding: utf-8 -*-
"""
myMainWindow.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Main functions for the GUI interface

"""

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QAbstractItemView,
    QMessageBox,
    QDataWidgetMapper)
from PyQt5.QtCore import (
    pyqtSlot,
    Qt,
    QItemSelectionModel,
    QModelIndex,
    QFile,
    QIODevice)
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRecord, QSqlQuery
from PyQt5.QtGui import QPixmap, QFont, QStandardItemModel, QStandardItem, QPainter, QPen
from PyQt5.QtChart import *

from ui_MainWindow import Ui_MainWindow

import matplotlib as mpl
import numpy as np
from matplotlib_venn import venn2
import itertools


class QmyMainWindow(QMainWindow):

    def __init__(self, parent=None, dbFilename='None'):
        super().__init__(parent)  # Call the parent class. Create window.
        self.ui = Ui_MainWindow()  # Create UI object
        self.ui.setupUi(self)  # Create UI interface

        self.ui.tabWidget.setVisible(True)
        self.setCentralWidget(self.ui.tabWidget)

# tableView setting
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(44)
        self.ui.tableView.horizontalHeader().setDefaultSectionSize(70)
        self.ui.tableView.setSortingEnabled(True)

# Initialize chart
        self.__iniPieChart()  # Initialize pie chart
        self.__iniStackedBar()  # Stacked bar

        # mpl.rcParams['font.sans-serif'] = ['Calibri']
        mpl.rcParams['font.size'] = 8

        # Choose the SQLITE database drive
        self.DB = QSqlDatabase.addDatabase("QSQLITE")
        self.DB.setDatabaseName(dbFilename)  # Set the name of database
        if self.DB.open():  # Open database
            self.__openTable()  # Open tables
        else:
            QMessageBox.warning(self, "Warning", "Failed to open the database.")


# ==============Self-defined Fuctions============

    def __getFieldNames(self):  # Get names of all fields.
        # Get empty records, only field name.
        emptyRec = self.tabModel.record()
        self.fldNum = {}  # Dictionary of field name and index.
        for i in range(emptyRec.count()):
            fieldName = emptyRec.fieldName(i)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName] = i

    def __openTable(self):  # Open the table of database
        self.tabModel = QSqlTableModel(self, self.DB)  # Data model
        # Set the table of database TODO: Can user insert their own tables from
        # the database?
        self.tabModel.setTable("battery")
        # Data storage，OnManualSubmit , OnRowChange
        self.tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        # self.tabModel.setSort(
        #     self.tabModel.fieldIndex("RANDOM"),
        #     Qt.DescendingOrder)  # Sorting
        if (self.tabModel.select() == False):  # Failed to query the data
            QMessageBox.critical(
                self,
                "Wrong",
                "Something wrong. Failed to open the database\n" +
                self.tabModel.lastError().text())
            return
        # self.tabModel.setFilter("NUM_RECORDS LIKE 'NONE'")
        self.__getFieldNames()  # Get the field name and index

# Field name shown
        for i in self.fldNum:
            self.tabModel.setHeaderData(
                self.fldNum[i], Qt.Horizontal, i.capitalize())

# Create mappings between interface widget and the field name of data model
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.tabModel)  # Setting data model
        self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)

# The relations between interface widget and field name of tabModel
        self.mapper.addMapping(self.ui.dbEditValue, self.fldNum["Value"])
        self.mapper.addMapping(self.ui.dbEditRunit, self.fldNum["Raw_unit"])
        self.mapper.addMapping(self.ui.dbComboProperty, self.fldNum["Property"])
        self.mapper.addMapping(self.ui.dbEditUnit, self.fldNum["Unit"])
        self.mapper.addMapping(self.ui.dbEditName, self.fldNum["Name"])
        self.mapper.addMapping(
            self.ui.dbEditEname,
            self.fldNum["Extracted_name"])
        self.mapper.addMapping(self.ui.dbEditRvalue, self.fldNum["Raw_value"])
        self.mapper.addMapping(self.ui.dbEditDOI_2, self.fldNum["DOI"])
        self.mapper.addMapping(self.ui.dbEditDOI_4, self.fldNum["Date"])
        self.mapper.addMapping(self.ui.dbEditDOI_3, self.fldNum["Title"])
        self.mapper.addMapping(self.ui.dbEditDOI, self.fldNum["Journal"])
        self.mapper.addMapping(self.ui.dbEditTag, self.fldNum["Tag"])
        self.mapper.addMapping(self.ui.dbEditInfo, self.fldNum["Info"])
        self.mapper.addMapping(self.ui.dbEditType, self.fldNum["Type"])
        self.mapper.addMapping(self.ui.dbEditWarning, self.fldNum["Warning"])
        self.mapper.addMapping(self.ui.dbEditSpecifier, self.fldNum["Specifier"])
        self.mapper.toFirst()  # Move to the first record

        self.selModel = QItemSelectionModel(self.tabModel)  # Select model
        self.selModel.currentChanged.connect(
            self.do_currentChanged)  # Trigger when the current changed
        self.selModel.currentRowChanged.connect(
            self.do_currentRowChanged)  # Trigger when the current row changed

        self.ui.tableView.setModel(self.tabModel)  # Setting the data model
        self.ui.tableView.setSelectionModel(
            self.selModel)  # Setting the selection model

#      self.ui.tableView.setColumnHidden(self.fldNum["TAG"],   True)  #Hide columns
# self.ui.tableView.setColumnHidden(self.fldNum["INFO"],  True)  #Hide
# columns
        self.ui.tableView.setColumnHidden(self.fldNum["Extracted_name"], True)  # Hide columns
        self.ui.tableView.setColumnHidden(self.fldNum["Unit"], True)  # Hide columns
        self.ui.tableView.setColumnHidden(self.fldNum["Num_records"], True)  # Hide columns
        # self.ui.tableView.setColumnHidden(
        #     self.fldNum["RAW_VALUE"], True)  # Hide columns

# Update the conditions of actions of interface widget
        self.ui.actRecAppend.setEnabled(True)
        self.ui.actRecInsert.setEnabled(True)
        self.ui.actRecDelete.setEnabled(True)

        self.ui.btnDrawPieChart.setEnabled(True)  # Pie Chart
        self.ui.spinPieSize.setEnabled(True)
        self.ui.spinHoleSize.setEnabled(True)
        self.ui.chkBox_PieLegend.setEnabled(True)

        self.ui.generateButton_3.setEnabled(True)
        self.ui.searchButton_3.setEnabled(True)
        self.ui.clearButton_3.setEnabled(True)

        self.ui.frame_4.setEnabled(True)
        self.ui.frame_3.setEnabled(True)

        self.ui.searchInput.returnPressed.connect(self.ui.searchButton.click)
        self.ui.searchInput_3.returnPressed.connect(
            self.ui.searchButton_3.click)

    def __iniPieChart(self):  # Initialize pie chart
        chart = QChart()
        # chart.setTitle("Piechart")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTheme(QChart.ChartTheme(0))
        self.ui.chartViewPie.setChart(chart)  # Setting chart for chart view
        self.ui.chartViewPie.setRenderHint(QPainter.Antialiasing)
        self.ui.chartViewPie.setCursor(Qt.CrossCursor)  # Setting cross cursor

    def __iniStackedBar(self):  # Initialize stacked bar chart
        chart = QChart()
        # chart.setTitle("Number of property records for each chemical")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTheme(QChart.ChartTheme(0))
        self.ui.chartViewStackedBar.setChart(chart)  # Set chart
        self.ui.chartViewStackedBar.setRenderHint(QPainter.Antialiasing)
        self.ui.chartViewStackedBar.setCursor(Qt.CrossCursor)  # Set mouse


# ==========Table tab slot function==================
    @pyqtSlot()  # Save changes
    def on_actSubmit_triggered(self):
        res = self.tabModel.submitAll()
        if (res == False):
            QMessageBox.information(
                self,
                "Information",
                "Failed to store the changes. Wrong information. \n" +
                self.tabModel.lastError().text())
        else:
            self.ui.actSubmit.setEnabled(False)
            self.ui.actRevert.setEnabled(False)

    @pyqtSlot()  # Cancel changes
    def on_actRevert_triggered(self):
        self.tabModel.revertAll()
        self.ui.actSubmit.setEnabled(False)
        self.ui.actRevert.setEnabled(False)

    @pyqtSlot()  # Add records
    def on_actRecAppend_triggered(self):
        self.tabModel.insertRow(
            self.tabModel.rowCount(),
            QModelIndex())  # Add one record in the last row
        curIndex = self.tabModel.index(
            self.tabModel.rowCount() - 1,
            1)  # Create ModelIndex of the last row
        self.selModel.clearSelection()  # Clear selections
        # Choosing the current row when selection.
        self.selModel.setCurrentIndex(curIndex, QItemSelectionModel.Select)

        currow = curIndex.row()  # Get current row

    @pyqtSlot()  # Insert records
    def on_actRecInsert_triggered(self):
        curIndex = self.ui.tableView.currentIndex()  # QModelIndex
        self.tabModel.insertRow(curIndex.row(), QModelIndex())
        self.selModel.clearSelection()  # Clear selections
        self.selModel.setCurrentIndex(curIndex, QItemSelectionModel.Select)

    @pyqtSlot()  # Delete records
    def on_actRecDelete_triggered(self):
        # Get the current index of current model
        curIndex = self.selModel.currentIndex()
        self.tabModel.removeRow(curIndex.row(),
                                QModelIndex())  # Delete the current row
        self.tabModel.submit()

    @pyqtSlot()  # Help message box
    def on_actHelp_triggered(self):
        msg = QMessageBox()
        msg.about(
            self, "Help", '<div>'
            '<h3>Table:&nbsp;Query&nbsp;the&nbsp;database&nbsp;according&nbsp;to&nbsp;data&nbsp;types&nbsp;and&nbsp;name&nbsp;or&nbsp;DOI.</h3>'
            '<ul>'
            '<li>Search&nbsp;the&nbsp;exact&nbsp;compound&nbsp;name&nbsp;in&nbsp;"<em>Exact&nbsp;Match</em>". Search&nbsp;the&nbsp;element&nbsp;or&nbsp;part&nbsp;of&nbsp;compound&nbsp;name&nbsp;in&nbsp;"<em>Generic&nbsp;Match</em>".&nbsp;</li>'
            '<li>Click the "<em>Home</em>" or "<em>All</em>" button to view the full database</li>'
            '<li>Refer&nbsp;to&nbsp;"<em>Correctness</em>"&nbsp;column&nbsp;for&nbsp;database&nbsp;evaluation&nbsp;details.&nbsp;</li>'
            '<li>You can add your own database entries using the "<em>Insert</em>" tab; click "<em>Save</em>" to save the changes.</li>'
            '</ul>'
            '<h3>Figure:&nbsp;Statistical&nbsp;analysis&nbsp;of&nbsp;the&nbsp;database.</h3>'
            '<ul>'
            '<li><em>Pie&nbsp;chart</em>&nbsp;shows&nbsp;the&nbsp;proportion&nbsp;of&nbsp;data&nbsp;records.</li>'
            '<li><em>Stacked&nbsp;bar&nbsp;chart</em>&nbsp;shows&nbsp;the&nbsp;data&nbsp;types&nbsp;for&nbsp;each&nbsp;compound. First&nbsp;input&nbsp;the&nbsp;compound&nbsp;name,&nbsp;click&nbsp;"<em>Add</em>"&nbsp;and&nbsp;then&nbsp;"<em>Generate</em>"&nbsp;data&nbsp;for&nbsp;overview.&nbsp;</li>'
            '<li><em>Histogram&nbsp;</em>shows&nbsp;the&nbsp;distribution&nbsp;of&nbsp;each&nbsp;data&nbsp;type.</li>'
            '<li><em>Venn&nbsp;diagram</em>&nbsp;shows&nbsp;the&nbsp;correlation&nbsp;of&nbsp;each&nbsp;data&nbsp;type.</li>'
            '</ul>'
            '</div>')

    @pyqtSlot()  # Filtering
    def on_radioBtnVoltage_clicked(self):
        flag, sqlmerge = self.merged_or_not()
        print(sqlmerge)
        self.tabModel.setFilter("PROPERTY LIKE 'Voltage' AND %s"% sqlmerge)

    @pyqtSlot()  # Filtering
    def on_radioBtnCoulombic_clicked(self):
        flag, sqlmerge = self.merged_or_not()
        self.tabModel.setFilter("PROPERTY LIKE 'Coulombic Efficiency' AND %s"% sqlmerge)

    @pyqtSlot()  # Filtering
    def on_radioBtnConductivity_clicked(self):
        flag, sqlmerge = self.merged_or_not()
        self.tabModel.setFilter("PROPERTY LIKE 'Conductivity' AND %s"% sqlmerge)

    @pyqtSlot()  # Filetering
    def on_radioBtnCapacity_clicked(self):
        flag, sqlmerge = self.merged_or_not()
        self.tabModel.setFilter("PROPERTY LIKE 'Capacity' AND %s"% sqlmerge)

    @pyqtSlot()  # Filtering
    def on_radioBtnEnergy_clicked(self):
        flag, sqlmerge = self.merged_or_not()
        self.tabModel.setFilter("PROPERTY LIKE 'Energy' AND %s"% sqlmerge)

    @pyqtSlot()  # Cancel Filetering
    def on_radioBtnAll_clicked(self):
        flag, sqlmerge = self.merged_or_not()
        self.tabModel.setFilter("%s"% sqlmerge)
    # print(self.tabModel.filter())
    # self.tabModel.select()

    def get_elements(self):
        element_dic = {
            "Hydrogen": "H",
            "Helium": "He",
            "Lithium": "Li",
            "Beryllium": "Be",
            "Boron": "B",
            "Carbon": "C",
            "Nitrogen": "N",
            "Oxygen": "O",
            "Fluorine": "F",
            "Neon": "Ne",
            "Sodium": "Na",
            "Magnesium": "Mg",
            "Aluminum": "Al",
            "Silicon": "Si",
            "Phosphorus": "P",
            "Sulfur": "S",
            "Chlorine": "Cl",
            "Argon": "Ar",
            "Potassium": "K",
            "Calcium": "Ca",
            "Scandium": "Sc",
            "Titanium": "Ti",
            "Vanadium": "V",
            "Chromium": "Cr",
            "Manganese": "Mn",
            "Iron": "Fe",
            "Cobalt": "Co",
            "Nickel": "Ni",
            "Copper": "Cu",
            "Zinc": "Zn",
            "Gallium": "Ga",
            "Germanium": "Ge",
            "Arsenic": "As",
            "Selenium": "Se",
            "Bromine": "Br",
            "Krypton": "Kr",
            "Rubidium": "Rb",
            "Strontium": "Sr",
            "Yttrium": "Y",
            "Zirconium": "Zr",
            "Niobium": "Nb",
            "Molybdenum": "Mo",
            "Technetium": "Tc",
            "Ruthenium": "Ru",
            "Rhodium": "Rh",
            "Palladium": "Pd",
            "Silver": "Ag",
            "Cadmium": "Cd",
            "Indium": "In",
            "Tin": "Sn",
            "Antimony": "Sb",
            "Tellurium": "Te",
            "Iodine": "I",
            "Xenon": "Xe",
            "Cesium": "Cs",
            "Barium": "Ba",
            "Lanthanum": "La",
            "Cerium": "Ce",
            "Praseodymium": "Pr",
            "Neodymium": "Nd",
            "Promethium": "Pm",
            "Samarium": "Sm",
            "Europium": "Eu",
            "Gadolinium": "Gd",
            "Terbium": "Tb",
            "Dysprosium": "Dy",
            "Holmium": "Ho",
            "Erbium": "Er",
            "Thulium": "Tm",
            "Ytterbium": "Yb",
            "Lutetium": "Lu",
            "Hafnium": "Hf",
            "Tantalum": "Ta",
            "Tungsten": "W",
            "Rhenium": "Re",
            "Osmium": "Os",
            "Iridium": "Ir",
            "Platinum": "Pt",
            "Gold": "Au",
            "Mercury": "Hg",
            "Thallium": "Tl",
            "Lead": "Pb",
            "Bismuth": "Bi",
            "Polonium": "Po",
            "Astatine": "At",
            "Radon": "Rn",
            "Francium": "Fr",
            "Radium": "Ra",
            "Actinium": "Ac",
            "Thorium": "Th",
            "Protactinium": "Pa",
            "Uranium": "U",
            "Neptunium": "Np",
            "Plutonium": "Pu",
            "Americium": "Am",
            "Curium": "Cm",
            "Berkelium": "Bk",
            "Californium": "Cf",
            "Einsteinium": "Es",
            "Fermium": "Fm",
            "Mendelevium": "Md",
            "Nobelium": "No",
            "Lawrencium": "Lr",
            "Rutherfordium": "Rf",
            "Dubnium": "Db",
            "Seaborgium": "Sg",
            "Bohrium": "Bh",
            "Hassium": "Hs",
            "Meitnerium": "Mt",
            "Darmstadtium": "Ds",
            "Roentgenium": "Rg",
            "Copernicium": "Cn",
            "Nihonium": "Nh",
            "Flerovium": "Fl",
            "Moscovium": "Mc",
            "Livermorium": "Lv",
            "Tennessine": "Ts",
            "Oganesson": "Og"}
        return element_dic

    def merged_or_not(self):
        flag = self.ui.mergeBox.isChecked()
        if flag:
            sqlmerge = "NUM_RECORDS NOT LIKE 'NONE'"
        else:
            sqlmerge = "NUM_RECORDS LIKE 'NONE'"
        return flag, sqlmerge 


    @pyqtSlot()
    def on_homeButton_clicked(self):
        self.tabModel.setFilter("NUM_RECORDS LIKE 'NONE'")
        self.ui.mergeBox.setChecked(False)

    @pyqtSlot()
    def on_mergeButton_clicked(self):
        self.tabModel.setFilter("NUM_RECORDS NOT LIKE 'NONE'")
        self.ui.mergeBox.setChecked(True)

    @pyqtSlot()
    def on_searchButton_clicked(self):
        searchtext = self.ui.searchInput.text()
        searchclass = self.ui.searchClass.currentText()
        matchtype = self.ui.matchType.currentText()
        flag, sqlmerge = self.merged_or_not()

        if searchclass == "DOI":
            if matchtype == "Exact Match":
                self.tabModel.setFilter("DOI LIKE '%s' AND %s" % (searchtext, sqlmerge))
            elif matchtype == "Generic Match":
                self.tabModel.setFilter("DOI LIKE '%%%s%%' AND %s" % (searchtext, sqlmerge))

            if self.tabModel.rowCount() == 0:
                self.tabModel.setFilter("")
                QMessageBox.warning(
                    self, "Warning", "No such DOIs in the database. Please search new DOI.")

        elif searchclass == "Warning":
            if matchtype == "Exact Match":
                self.tabModel.setFilter("WARNING LIKE '%s' AND %s" % (searchtext, sqlmerge))
            elif matchtype == "Generic Match":
                self.tabModel.setFilter("WARNING LIKE '%%%s%%' AND %s" % (searchtext, sqlmerge))

            if self.tabModel.rowCount() == 0:
                self.tabModel.setFilter("")
                QMessageBox.warning(
                    self, "Warning", "No such DOIs in the database. Please search new DOI.")

        elif searchclass == 'Name':
            try:
                searchtext = self.get_elements()[searchtext.capitalize()]
            except BaseException:
                pass
            if matchtype == "Exact Match":
                if self.ui.radioBtnAll.isChecked():
                    self.tabModel.setFilter(
                        "%s LIKE '%s' " %
                        (searchclass, searchtext))
                elif self.ui.radioBtnVoltage.isChecked():
                    self.tabModel.setFilter(
                        "%s LIKE '%s' AND PROPERTY LIKE 'VOLTAGE' AND %s" %
                        (searchclass, searchtext, sqlmerge))
                elif self.ui.radioBtnCapacity.isChecked():
                    self.tabModel.setFilter(
                        "%s LIKE '%s' AND PROPERTY LIKE 'CAPACITY' AND %s" %
                        (searchclass, searchtext, sqlmerge))
                elif self.ui.radioBtnConductivity.isChecked():
                    self.tabModel.setFilter(
                        "%s LIKE '%s' AND PROPERTY LIKE 'CONDUCTIVITY' AND %s" %
                        (searchclass, searchtext, sqlmerge))
                elif self.ui.radioBtnCoulombic.isChecked():
                    self.tabModel.setFilter(
                        "%s LIKE '%s' AND PROPERTY LIKE 'COULOMBIC EFFICIENCY' AND %s " %
                        (searchclass, searchtext, sqlmerge))
                elif self.ui.radioBtnEnergy.isChecked():
                    self.tabModel.setFilter(
                        "%s LIKE '%s' AND PROPERTY LIKE 'ENERGY'AND %s " %
                        (searchclass, searchtext, sqlmerge))

            elif matchtype == "Generic Match":
                if self.ui.radioBtnAll.isChecked():
                    self.tabModel.setFilter(
                        "(EXTRACTED_NAME LIKE '%%''%s''%%' OR NAME LIKE '%s') AND %s" %
                        (searchtext, searchtext, sqlmerge))
                elif self.ui.radioBtnVoltage.isChecked():
                    self.tabModel.setFilter(
                        "EXTRACTED_NAME LIKE '%%''%s''%%' OR NAME LIKE '%s' AND %s" %
                        (searchtext, searchtext, sqlmerge))
                elif self.ui.radioBtnCapacity.isChecked():
                    self.tabModel.setFilter(
                        "EXTRACTED_NAME LIKE '%%''%s''%%' OR NAME LIKE '%s' AND %s" %
                        (searchtext, searchtext, sqlmerge))
                elif self.ui.radioBtnConductivity.isChecked():
                    self.tabModel.setFilter(
                        "EXTRACTED_NAME LIKE '%%''%s''%%' OR NAME LIKE '%s' AND %s" %
                        (searchtext, searchtext, sqlmerge))
                elif self.ui.radioBtnCoulombic.isChecked():
                    self.tabModel.setFilter(
                        "EXTRACTED_NAME LIKE '%%''%s''%%' OR NAME LIKE '%s' AND %s" %
                        (searchtext, searchtext, sqlmerge))
                elif self.ui.radioBtnEnergy.isChecked():
                    self.tabModel.setFilter(
                        "EXTRACTED_NAME LIKE '%%''%s''%%' OR NAME LIKE '%s' AND %s" %
                        (searchtext, searchtext, sqlmerge))

            if self.tabModel.rowCount() == 0:
                self.tabModel.setFilter("")
                QMessageBox.warning(
                    self,
                    "Warning",
                    "No such compounds in the database. Please search new compounds.")


# ============Picture Tab 1, Pie Chart=====================

    @pyqtSlot()  # Draw the pie chart
    def on_btnDrawPieChart_clicked(self):
        self.draw_pieChart()

    @pyqtSlot(float)  # Set holeSize
    def on_spinHoleSize_valueChanged(self, arg1):
        seriesPie = self.ui.chartViewPie.chart().series()[0]
        seriesPie.setHoleSize(arg1)

    @pyqtSlot(float)  # Set pieSize
    def on_spinPieSize_valueChanged(self, arg1):
        seriesPie = self.ui.chartViewPie.chart().series()[0]
        seriesPie.setPieSize(arg1)

    @pyqtSlot(bool)  # Set legend checkbox
    def on_chkBox_PieLegend_clicked(self, checked):
        self.ui.chartViewPie.chart().legend().setVisible(checked)

    def pie_data(self):  # Return a list of property name and the number of property
        num_list = []
        pro_list = [
            "CAPACITY",
            "CONDUCTIVITY",
            "COULOMBIC EFFICIENCY",
            "ENERGY",
            "VOLTAGE"]
        for i in range(len(pro_list)):
            query = QSqlQuery(
                db=self.DB,
                query="SELECT COUNT(NAME) FROM BATTERY WHERE PROPERTY LIKE '%s'" %
                pro_list[i])  # Query database
            while query.next():
                num_value = query.value(0)  # Returned value for each query

                item = self.ui.treeWidget_2.topLevelItem(i)  # The ith row
                # The 2nd column
                item.setText(1, str(num_value))
                item.setTextAlignment(1, Qt.AlignHCenter)

                num_list.append(num_value)
        return pro_list, num_list

    def draw_pieChart(self):  # Draw the pie chart
        chart = self.ui.chartViewPie.chart()

        chart.legend().setAlignment(Qt.AlignRight)  # AlignRight,AlignBottom
        chart.removeAllSeries()  # Delete all series

        seriesPie = QPieSeries()  # Pie chart series
        seriesPie.setHoleSize(self.ui.spinHoleSize.value())  # Hole size
        seriesPie.setPieSize(self.ui.spinPieSize.value())  # Pie size
        sec_count = 5  # Number of properties
        seriesPie.setLabelsVisible(True)  # Label

        pro, num = self.pie_data()
        for i in range(sec_count):
            seriesPie.append(pro[i], num[i])

        seriesPie.setLabelsVisible(True)  # Label

        # Pie hoverd when mouse selected
        seriesPie.hovered.connect(self.do_pieHovered)
        chart.addSeries(seriesPie)
        chart.setTitle("Proportion of data records for each property")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(75)
        chart.setTitleFont(font)

        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(35)
        legend = chart.legend()
        legend.setFont(font)


# =========Picture tab 2. StackedBar=========
    @pyqtSlot()  # Draw StackedBar
    def on_btnStackedBar_clicked(self):
        self.draw_stackedBar()

    @pyqtSlot()  # Draw horizontal StackedBar
    def on_btnStackedBarH_clicked(self):
        self.draw_stackedBar(False)

    # Search button in the Stacked bar chart tab. Add name to the first column
    # of the table.
    @pyqtSlot()
    def on_searchButton_3_clicked(self):
        searchtext = self.ui.searchInput_3.text()

        current_index = self.ui.stackedWidget.topLevelItemCount()
        item_0 = QtWidgets.QTreeWidgetItem(self.ui.stackedWidget)
        item_0.setText(0, searchtext)

    @pyqtSlot()  # Generate data using the input chemical names
    def on_generateButton_3_clicked(self):
        self.ui.zoominButton.setEnabled(True)
        self.ui.zoomoutButton.setEnabled(True)
        self.ui.originalButton.setEnabled(True)
        self.ui.btnStackedBar.setEnabled(True)  # Stacked bar chart
        self.ui.btnStackedBarH.setEnabled(True)

        current_index = self.ui.stackedWidget.topLevelItemCount()
        chemical_list = [self.ui.stackedWidget.topLevelItem(index).text(
            0) for index in range(current_index)]  # Get a list of the inputed chemical name
        pro_list = [
            "CAPACITY",
            "CONDUCTIVITY",
            "COULOMBIC EFFICIENCY",
            "ENERGY",
            "VOLTAGE"]
        for row, chemical in enumerate(chemical_list):
            for index, pro in enumerate(pro_list):
                query = QSqlQuery(
                    db=self.DB,
                    query="SELECT SUM(NUM_RECORDS) FROM BATTERY WHERE PROPERTY LIKE '%s' AND NAME LIKE '%s' " %
                    (pro,
                     chemical))
                while query.next():
                    num_value = query.value(0)
                    print(num_value)
                    if num_value == "":
                        num_value = 0
                    item = self.ui.stackedWidget.topLevelItem(
                        row)  # The row'th row
                    item.setText(index + 1, str(num_value))
                    item.setTextAlignment(index + 1, Qt.AlignHCenter)

    @pyqtSlot()  # Clear button
    def on_clearButton_3_clicked(self):
        self.ui.stackedWidget.clear()

    @pyqtSlot()  # Zoom in
    def on_zoominButton_clicked(self):
        self.ui.chartViewStackedBar.chart().zoom(1.2)

    @pyqtSlot()  # Zoom out
    def on_zoomoutButton_clicked(self):
        self.ui.chartViewStackedBar.chart().zoom(0.8)

    @pyqtSlot()  # Reset original size
    def on_originalButton_clicked(self):
        self.ui.chartViewStackedBar.chart().zoomReset()

    def draw_stackedBar(self, isVertical=True):  # Stacked bar chart
        chart = self.ui.chartViewStackedBar.chart()
        chart.removeAllSeries()  # Remove all series
        chart.removeAxis(chart.axisX())  # remove axis
        chart.removeAxis(chart.axisY())
        if isVertical:  # Vertical
            chart.setTitle("Number of property records for each chemical ")
            chart.legend().setAlignment(Qt.AlignBottom)
        else:  # Horizontal
            chart.setTitle("Number of property records for each chemical")
            chart.legend().setAlignment(Qt.AlignRight)

        # Create data sets
        setCapacity = QBarSet("Capacity")
        setConductivity = QBarSet("Conductivity")
        setCoulombic = QBarSet("Coulombic")
        setEnergy = QBarSet("Energy")
        setVoltage = QBarSet("Voltage")

        chemical_Count = self.ui.stackedWidget.topLevelItemCount()
        nameList = []  # Chemical lists
        for i in range(chemical_Count):
            item = self.ui.stackedWidget.topLevelItem(i)
            # print(item.text(1))
            nameList.append(item.text(0))
            setCapacity.append(float(item.text(1)))
            setConductivity.append(float(item.text(2)))
            setCoulombic.append(float(item.text(3)))
            setEnergy.append(float(item.text(4)))
            setVoltage.append(float(item.text(5)))

        # Create series
        if isVertical:
            seriesBar = QStackedBarSeries()
        else:
            seriesBar = QHorizontalStackedBarSeries()

        seriesBar.append(setCapacity)
        seriesBar.append(setConductivity)
        seriesBar.append(setCoulombic)
        seriesBar.append(setEnergy)
        seriesBar.append(setVoltage)

        seriesBar.setLabelsVisible(True)  # Show labels for each bar
        seriesBar.setLabelsFormat("@value")
        seriesBar.setLabelsPosition(QAbstractBarSeries.LabelsCenter)

        seriesBar.setBarWidth(0.3)

        chart.addSeries(seriesBar)

        axisStud = QBarCategoryAxis()  # Category axis
        axisStud.append(nameList)
        axisStud.setRange(nameList[0], nameList[chemical_Count - 1])

        axisValue = QValueAxis()  # Value axis
        # axisValue.setRange(0, 300)
        axisValue.setTitleText("Number of records")
        # axisValue.setTickCount(6)
        axisValue.applyNiceNumbers()

        if isVertical:
            chart.setAxisX(axisStud, seriesBar)
            chart.setAxisY(axisValue, seriesBar)
        else:
            chart.setAxisY(axisStud, seriesBar)
            chart.setAxisX(axisValue, seriesBar)

        for marker in chart.legend().markers():  # QLegendMarker lists
            marker.clicked.connect(self.do_LegendMarkerClicked)


# =========Picture tab 3. Histogram=========
    @pyqtSlot(bool)  # Show toolbar
    def on_gBoxHist_toolbar_2_clicked(self, checked):
        self.ui.widgetHist_2.setToolbarVisible(checked)

    @pyqtSlot()  # Draw
    def on_histButton_clicked(self):
        self.__drawHist()

    def hist_data(self, pro):
        query = QSqlQuery(
            db=self.DB,
            query="SELECT VALUE FROM BATTERY WHERE PROPERTY LIKE '%s'" %
            pro)
        data = []
        while query.next():
            num_value = query.value(0)
            data.append(num_value)
        return data

    def __drawHist(self):  # Histogram
        pro = self.ui.propertycomboBox_2.currentText()
        data = self.hist_data(pro)
        self.ui.widgetHist_2.figure.clear()  # Clear figure

        ax = self.ui.widgetHist_2.figure.add_subplot(1, 1, 1)

        if pro == 'Capacity':
            M, bins, patches = ax.hist(
                [5000 if float(i) > 4999 else float(i) for i in data], bins='auto', color='darkgreen', alpha=0.5, rwidth=1)
            ax.set_xlim(0, 5001)
            # ax.set_ylim(0,15000)
            ax.tick_params(labelsize=12)
            ax.set_xticklabels(['0', '1000', '2000', '3000', '4000', '5000+'])
            ax.set_xlabel('Capacity (mAh/g)', fontsize=14)
            ax.set_ylabel('Frequency', fontsize=14)
            ax.set_title('Battery Capacity Distrbution', fontsize=14)
            ax.figure.canvas.draw()

        elif pro == "Voltage":
            count1 = []
            for i in data:
                count1.append(float(i))

            n, bins, patches = ax.hist(
                x=count1, bins='auto', range=(
                    0, 8), color='r', alpha=0.5, rwidth=1)
            ax.set_xticklabels(['0', '1', '2', '3', '4', '5', '6', '7', '8+'])

            ax.set_xlim(0, 8)
            ax.tick_params(labelsize=12)
            ax.set_xlabel('Voltage (V)', fontsize=14)
            ax.set_ylabel('Frequency', fontsize=14)
            ax.set_title('Battery Voltage Distrbution', fontsize=14)
            ax.figure.canvas.draw()

        elif pro == "Energy":
            n, bins, patches = ax.hist(
                [3000 if float(i) > 2999 else float(i) for i in data], bins='auto', color='y', alpha=0.5, rwidth=1)
            ax.set_xticklabels(
                ['0', '500', '1000', '1500', '2000', '2500', '3000+'])
            ax.set_xlim(0, 3001)
            ax.tick_params(labelsize=12)
            ax.set_xlabel('Energy (Wh/kg)', fontsize=14)
            ax.set_ylabel('Frequency', fontsize=14)
            ax.set_title('Battery Energy Distrbution', fontsize=14)
            ax.figure.canvas.draw()

        elif pro == "Coulombic Efficiency":
            dataplot = [float(i) for i in data]
            n, bins, patches = ax.hist(x=dataplot, bins='auto', color='c',
                                       alpha=0.5, rwidth=1)
            ax.set_xlim(0, 100)
            ax.tick_params(labelsize=12)
            ax.set_xlabel('Coulombic Effciency (%)', fontsize=14)
            ax.set_ylabel('Frequency', fontsize=14)
            ax.set_title(
                'Battery Coulombic Effciency Distrbution',
                fontsize=14)
            ax.figure.canvas.draw()

        elif pro == "Conductivity":
            dataplot = [float(i) for i in data]
            n, bins, patches = ax.hist(x=dataplot, bins=np.logspace(
                np.log10(1e-15), np.log10(1)), color='k', alpha=0.5, rwidth=1)
            ax.set_xlim(1e-20, 10)
            ax.set_xscale('log')
            ax.tick_params(labelsize=12)
            ax.set_xlabel('log10 (Conductivity (S/cm))', fontsize=14)
            ax.set_ylabel('Frequency', fontsize=14)
            ax.set_title('Battery Conductivity Distrbution', fontsize=14)
            ax.figure.canvas.draw()

# =========Picture tab 4. Venn diagram=========
    @pyqtSlot()  # Draw
    def on_btnVenn_clicked(self):
        self.__drawVenn()

    @pyqtSlot(bool)  # Show toolbar
    def on_gBoxHist_toolbar_3_clicked(self, checked):
        self.ui.widgetVenn.setToolbarVisible(checked)

    def __drawVenn(self):
        self.ui.widgetVenn.figure.clear()  # Clear figure

        pro_list = [
            "Capacity",
            "Conductivity",
            "Coulombic Efficiency",
            "Energy",
            "Voltage"]
        data_dic = {}
        color_dic = dict(zip(pro_list, ['C0', 'C2', 'C6', 'C8', 'C9']))

        for i in pro_list:
            query = QSqlQuery(
                db=self.DB,
                query="SELECT COUNT(DISTINCT NAME) FROM BATTERY WHERE PROPERTY LIKE '%s'" %
                i)
            while query.next():
                num_value = query.value(0)
                data_dic[i] = num_value

        for i, combo in enumerate(itertools.combinations(pro_list, 2)):

            query = QSqlQuery(
                db=self.DB,
                query="SELECT COUNT() FROM (SELECT DISTINCT NAME AS PRO1 FROM BATTERY WHERE PROPERTY LIKE '%s')"
                      " INNER JOIN (SELECT DISTINCT NAME AS PRO2 FROM BATTERY WHERE PROPERTY "
                      "LIKE '%s') ON PRO1 = PRO2" %
                combo)
            while query.next():
                num = query.value(0)
            x3 = num
            x1 = data_dic[combo[0]] - x3
            x2 = data_dic[combo[1]] - x3

            hf = self.ui.widgetVenn.figure
            # hf.set_figheight(30)
            # hf.set_figwidth(30)
            # print(dir(hf))

            hf.set_size_inches((10, 10))
            ax1 = hf.add_subplot(5, 2, i + 1)
            v = venn2(
                subsets=(
                    x1, x2, x3), set_labels=(
                    combo[0], combo[1]), ax=ax1)

            v.get_patch_by_id('A').set_alpha(1)
            v.get_patch_by_id('A').set_color(color_dic[combo[0]])
            v.get_patch_by_id('B').set_color(color_dic[combo[1]])

            ax1.figure.canvas.draw()


# =============Self-defined slot function===============================

    # Update the conditions of actPost and actCancel

    def do_currentChanged(self, current, previous):
        self.ui.actSubmit.setEnabled(
            self.tabModel.isDirty())  # Use when not saving changes
        self.ui.actRevert.setEnabled(self.tabModel.isDirty())

    def do_currentRowChanged(self, current, previous):  # Control during row changes
        self.ui.actRecDelete.setEnabled(current.isValid())

        # Update current row index of mapping
        self.mapper.setCurrentIndex(current.row())
        # Get current record,QSqlRecord
        curRec = self.tabModel.record(current.row())

    def do_pieHovered(self, pieSlice, state):  # Mouse move in and out in the pie chart
        pieSlice.setExploded(state)  # Pop-up animation
        if state:  # Show the tab of percentages
            self.__oldLabel = pieSlice.label()  # Save original labels
            pieSlice.setLabel(self.__oldLabel + ": %.1f%%"
                              % (pieSlice.percentage() * 100))
            font = QFont()
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(25)
            pieSlice.setLabelFont(font)
        else:  # show original labels
            pieSlice.setLabel(self.__oldLabel)
            font = QFont()
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(25)
            pieSlice.setLabelFont(font)

    def do_LegendMarkerClicked(self):  # Click legend marker
        marker = self.sender()  # QLegendMarker

        marker.series().setVisible(not marker.series().isVisible())
        marker.setVisible(True)
        alpha = 1.0
        if not marker.series().isVisible():
            alpha = 0.5

        brush = marker.labelBrush()  # QBrush
        color = brush.color()  # QColor
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)

        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)

        pen = marker.pen()  # QPen
        color = pen.color()
        color.setAlphaF(alpha)
        pen.setColor(color)
        marker.setPen(pen)


# ##  ============Testing ================================
# if  __name__ == "__main__":
#    appctxt = ApplicationContext()    #Create GUI Application
#    db = appctxt.get_resource('battery_v3_aug2.db')
#    form=QmyMainWindow(dbFilename=db)            #Create Window
#    form.show()
#    sys.exit(appctxt.app.exec_())
