# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\development\Ui\BSM\BSM_13.ui'
#
# Created: Thu Feb 04 18:20:33 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(549, 450)
        Dialog.setMinimumSize(QtCore.QSize(0, 450))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 450))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 9, 225, 432))
        self.groupBox_2.setMinimumSize(QtCore.QSize(225, 385))
        self.groupBox_2.setMaximumSize(QtCore.QSize(3000, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.bs_node_menu = QtGui.QComboBox(self.groupBox_2)
        self.bs_node_menu.setMinimumSize(QtCore.QSize(140, 35))
        self.bs_node_menu.setMaximumSize(QtCore.QSize(3000, 35))
        self.bs_node_menu.setEditable(False)
        self.bs_node_menu.setObjectName("bs_node_menu")
        self.gridLayout_4.addWidget(self.bs_node_menu, 0, 0, 1, 1)
        self.bs_targets_list = QtGui.QListWidget(self.groupBox_2)
        self.bs_targets_list.setMinimumSize(QtCore.QSize(200, 0))
        self.bs_targets_list.setMaximumSize(QtCore.QSize(3000, 16777215))
        self.bs_targets_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.bs_targets_list.setObjectName("bs_targets_list")
        self.gridLayout_4.addWidget(self.bs_targets_list, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(240, 9, 300, 434))
        self.groupBox_4.setMinimumSize(QtCore.QSize(300, 385))
        self.groupBox_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.reset_all_ctrl = QtGui.QPushButton(self.groupBox_4)
        self.reset_all_ctrl.setMinimumSize(QtCore.QSize(131, 35))
        self.reset_all_ctrl.setMaximumSize(QtCore.QSize(131, 35))
        self.reset_all_ctrl.setAutoDefault(False)
        self.reset_all_ctrl.setDefault(False)
        self.reset_all_ctrl.setFlat(False)
        self.reset_all_ctrl.setObjectName("reset_all_ctrl")
        self.gridLayout_3.addWidget(self.reset_all_ctrl, 0, 2, 1, 1)
        self.refresh_button = QtGui.QPushButton(self.groupBox_4)
        self.refresh_button.setMinimumSize(QtCore.QSize(131, 35))
        self.refresh_button.setMaximumSize(QtCore.QSize(131, 35))
        self.refresh_button.setAutoDefault(False)
        self.refresh_button.setDefault(False)
        self.refresh_button.setFlat(False)
        self.refresh_button.setObjectName("refresh_button")
        self.gridLayout_3.addWidget(self.refresh_button, 0, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.groupBox_4)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 360))
        self.tabWidget.setMaximumSize(QtCore.QSize(280, 360))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.create_bs_button = QtGui.QPushButton(self.tab_2)
        self.create_bs_button.setMinimumSize(QtCore.QSize(200, 35))
        self.create_bs_button.setMaximumSize(QtCore.QSize(250, 35))
        self.create_bs_button.setAutoDefault(False)
        self.create_bs_button.setObjectName("create_bs_button")
        self.gridLayout.addWidget(self.create_bs_button, 0, 0, 1, 2)
        self.add_targets_button = QtGui.QPushButton(self.tab_2)
        self.add_targets_button.setMinimumSize(QtCore.QSize(200, 35))
        self.add_targets_button.setMaximumSize(QtCore.QSize(250, 35))
        self.add_targets_button.setAutoDefault(False)
        self.add_targets_button.setObjectName("add_targets_button")
        self.gridLayout.addWidget(self.add_targets_button, 1, 0, 1, 2)
        self.extract_targets_button = QtGui.QPushButton(self.tab_2)
        self.extract_targets_button.setMinimumSize(QtCore.QSize(200, 35))
        self.extract_targets_button.setMaximumSize(QtCore.QSize(250, 35))
        self.extract_targets_button.setAutoDefault(False)
        self.extract_targets_button.setObjectName("extract_targets_button")
        self.gridLayout.addWidget(self.extract_targets_button, 2, 0, 1, 2)
        self.delete_bs_button = QtGui.QPushButton(self.tab_2)
        self.delete_bs_button.setMinimumSize(QtCore.QSize(200, 35))
        self.delete_bs_button.setMaximumSize(QtCore.QSize(250, 35))
        self.delete_bs_button.setAutoDefault(False)
        self.delete_bs_button.setObjectName("delete_bs_button")
        self.gridLayout.addWidget(self.delete_bs_button, 3, 0, 1, 2)
        self.remove_targets_button = QtGui.QPushButton(self.tab_2)
        self.remove_targets_button.setMinimumSize(QtCore.QSize(200, 35))
        self.remove_targets_button.setMaximumSize(QtCore.QSize(250, 35))
        self.remove_targets_button.setAutoDefault(False)
        self.remove_targets_button.setObjectName("remove_targets_button")
        self.gridLayout.addWidget(self.remove_targets_button, 4, 0, 1, 2)
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setMinimumSize(QtCore.QSize(90, 35))
        self.label.setMaximumSize(QtCore.QSize(122, 35))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.inbetween_value = QtGui.QDoubleSpinBox(self.tab_2)
        self.inbetween_value.setMinimumSize(QtCore.QSize(123, 35))
        self.inbetween_value.setMaximumSize(QtCore.QSize(123, 35))
        self.inbetween_value.setMinimum(-99.99)
        self.inbetween_value.setSingleStep(0.1)
        self.inbetween_value.setProperty("value", 0.5)
        self.inbetween_value.setObjectName("inbetween_value")
        self.gridLayout.addWidget(self.inbetween_value, 5, 1, 1, 1)
        self.add_inbetween_button = QtGui.QPushButton(self.tab_2)
        self.add_inbetween_button.setMinimumSize(QtCore.QSize(200, 35))
        self.add_inbetween_button.setMaximumSize(QtCore.QSize(250, 35))
        self.add_inbetween_button.setAutoDefault(False)
        self.add_inbetween_button.setObjectName("add_inbetween_button")
        self.gridLayout.addWidget(self.add_inbetween_button, 6, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtGui.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setMinimumSize(QtCore.QSize(95, 35))
        self.label_6.setMaximumSize(QtCore.QSize(122, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 2)
        self.controllers_menu = QtGui.QComboBox(self.tab)
        self.controllers_menu.setMinimumSize(QtCore.QSize(95, 35))
        self.controllers_menu.setMaximumSize(QtCore.QSize(122, 16777215))
        self.controllers_menu.setEditable(False)
        self.controllers_menu.setObjectName("controllers_menu")
        self.gridLayout_5.addWidget(self.controllers_menu, 0, 2, 1, 2)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setMinimumSize(QtCore.QSize(95, 35))
        self.label_7.setMaximumSize(QtCore.QSize(122, 16777215))
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 2)
        self.attributes_menu = QtGui.QComboBox(self.tab)
        self.attributes_menu.setMinimumSize(QtCore.QSize(95, 35))
        self.attributes_menu.setMaximumSize(QtCore.QSize(122, 16777215))
        self.attributes_menu.setEditable(False)
        self.attributes_menu.setObjectName("attributes_menu")
        self.gridLayout_5.addWidget(self.attributes_menu, 1, 2, 1, 2)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(50, 35))
        self.label_2.setMaximumSize(QtCore.QSize(60, 35))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        self.min_value = QtGui.QDoubleSpinBox(self.tab)
        self.min_value.setMinimumSize(QtCore.QSize(50, 35))
        self.min_value.setMaximumSize(QtCore.QSize(60, 16777215))
        self.min_value.setMinimum(-99.99)
        self.min_value.setSingleStep(0.1)
        self.min_value.setObjectName("min_value")
        self.gridLayout_5.addWidget(self.min_value, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setMinimumSize(QtCore.QSize(50, 35))
        self.label_3.setMaximumSize(QtCore.QSize(60, 35))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 2, 1, 1)
        self.max_value = QtGui.QDoubleSpinBox(self.tab)
        self.max_value.setMinimumSize(QtCore.QSize(50, 35))
        self.max_value.setMaximumSize(QtCore.QSize(60, 16777215))
        self.max_value.setMinimum(-99.99)
        self.max_value.setSingleStep(0.1)
        self.max_value.setObjectName("max_value")
        self.gridLayout_5.addWidget(self.max_value, 2, 3, 1, 1)
        self.negative = QtGui.QCheckBox(self.tab)
        self.negative.setMinimumSize(QtCore.QSize(95, 35))
        self.negative.setMaximumSize(QtCore.QSize(122, 16777215))
        self.negative.setObjectName("negative")
        self.gridLayout_5.addWidget(self.negative, 3, 0, 1, 2)
        self.new_attr_name = QtGui.QLineEdit(self.tab)
        self.new_attr_name.setMinimumSize(QtCore.QSize(95, 35))
        self.new_attr_name.setMaximumSize(QtCore.QSize(122, 16777215))
        self.new_attr_name.setObjectName("new_attr_name")
        self.gridLayout_5.addWidget(self.new_attr_name, 3, 2, 1, 2)
        self.connect_button = QtGui.QPushButton(self.tab)
        self.connect_button.setMinimumSize(QtCore.QSize(95, 35))
        self.connect_button.setMaximumSize(QtCore.QSize(122, 16777215))
        self.connect_button.setAutoDefault(False)
        self.connect_button.setObjectName("connect_button")
        self.gridLayout_5.addWidget(self.connect_button, 4, 0, 1, 2)
        self.create_attr_button = QtGui.QPushButton(self.tab)
        self.create_attr_button.setMinimumSize(QtCore.QSize(95, 35))
        self.create_attr_button.setMaximumSize(QtCore.QSize(122, 16777215))
        self.create_attr_button.setAutoDefault(False)
        self.create_attr_button.setObjectName("create_attr_button")
        self.gridLayout_5.addWidget(self.create_attr_button, 4, 2, 1, 2)
        self.disconnect_button = QtGui.QPushButton(self.tab)
        self.disconnect_button.setMinimumSize(QtCore.QSize(95, 35))
        self.disconnect_button.setMaximumSize(QtCore.QSize(122, 16777215))
        self.disconnect_button.setAutoDefault(False)
        self.disconnect_button.setObjectName("disconnect_button")
        self.gridLayout_5.addWidget(self.disconnect_button, 5, 0, 1, 2)
        self.delete_attr_button = QtGui.QPushButton(self.tab)
        self.delete_attr_button.setMinimumSize(QtCore.QSize(95, 35))
        self.delete_attr_button.setMaximumSize(QtCore.QSize(122, 16777215))
        self.delete_attr_button.setAutoDefault(False)
        self.delete_attr_button.setObjectName("delete_attr_button")
        self.gridLayout_5.addWidget(self.delete_attr_button, 5, 2, 1, 2)
        self.export_connections_button = QtGui.QPushButton(self.tab)
        self.export_connections_button.setMinimumSize(QtCore.QSize(95, 35))
        self.export_connections_button.setMaximumSize(QtCore.QSize(122, 16777215))
        self.export_connections_button.setAutoDefault(False)
        self.export_connections_button.setObjectName("export_connections_button")
        self.gridLayout_5.addWidget(self.export_connections_button, 6, 0, 1, 2)
        self.import_connections_button = QtGui.QPushButton(self.tab)
        self.import_connections_button.setMinimumSize(QtCore.QSize(95, 35))
        self.import_connections_button.setMaximumSize(QtCore.QSize(122, 16777215))
        self.import_connections_button.setAutoDefault(False)
        self.import_connections_button.setObjectName("import_connections_button")
        self.gridLayout_5.addWidget(self.import_connections_button, 6, 2, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setEnabled(True)
        font = QtGui.QFont()
        self.groupBox.setFont(font)
        self.groupBox.setStatusTip("")
        self.groupBox.setAccessibleName("")
        self.groupBox.setAccessibleDescription("")
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.use_active_selection_radiobutton = QtGui.QRadioButton(self.groupBox)
        self.use_active_selection_radiobutton.setChecked(True)
        self.use_active_selection_radiobutton.setObjectName("use_active_selection_radiobutton")
        self.gridLayout_2.addWidget(self.use_active_selection_radiobutton, 0, 0, 1, 1)
        self.use_ui_selection_radiobutton = QtGui.QRadioButton(self.groupBox)
        self.use_ui_selection_radiobutton.setObjectName("use_ui_selection_radiobutton")
        self.gridLayout_2.addWidget(self.use_ui_selection_radiobutton, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_3 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.yz_orientation_radiobutton = QtGui.QRadioButton(self.groupBox_3)
        self.yz_orientation_radiobutton.setChecked(True)
        self.yz_orientation_radiobutton.setObjectName("yz_orientation_radiobutton")
        self.gridLayout_7.addWidget(self.yz_orientation_radiobutton, 0, 0, 1, 1)
        self.xz_orientation_radiobutton = QtGui.QRadioButton(self.groupBox_3)
        self.xz_orientation_radiobutton.setObjectName("xz_orientation_radiobutton")
        self.gridLayout_7.addWidget(self.xz_orientation_radiobutton, 0, 1, 1, 1)
        self.xy_orientation_radiobutton = QtGui.QRadioButton(self.groupBox_3)
        self.xy_orientation_radiobutton.setChecked(False)
        self.xy_orientation_radiobutton.setObjectName("xy_orientation_radiobutton")
        self.gridLayout_7.addWidget(self.xy_orientation_radiobutton, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 1, 0, 1, 2)
        self.select_base_geometry_button = QtGui.QPushButton(self.tab_3)
        self.select_base_geometry_button.setMinimumSize(QtCore.QSize(0, 20))
        self.select_base_geometry_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_base_geometry_button.setAutoDefault(False)
        self.select_base_geometry_button.setDefault(False)
        self.select_base_geometry_button.setFlat(False)
        self.select_base_geometry_button.setObjectName("select_base_geometry_button")
        self.gridLayout_6.addWidget(self.select_base_geometry_button, 2, 0, 1, 2)
        self.base_geometry_lineedit = QtGui.QLineEdit(self.tab_3)
        self.base_geometry_lineedit.setEnabled(False)
        self.base_geometry_lineedit.setMinimumSize(QtCore.QSize(0, 20))
        self.base_geometry_lineedit.setObjectName("base_geometry_lineedit")
        self.gridLayout_6.addWidget(self.base_geometry_lineedit, 3, 0, 1, 2)
        self.check_sym_button = QtGui.QPushButton(self.tab_3)
        self.check_sym_button.setMinimumSize(QtCore.QSize(0, 20))
        self.check_sym_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.check_sym_button.setAutoDefault(False)
        self.check_sym_button.setDefault(False)
        self.check_sym_button.setFlat(False)
        self.check_sym_button.setObjectName("check_sym_button")
        self.gridLayout_6.addWidget(self.check_sym_button, 4, 0, 1, 2)
        self.select_mirror_button = QtGui.QPushButton(self.tab_3)
        self.select_mirror_button.setMinimumSize(QtCore.QSize(0, 20))
        self.select_mirror_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_mirror_button.setAutoDefault(False)
        self.select_mirror_button.setDefault(False)
        self.select_mirror_button.setFlat(False)
        self.select_mirror_button.setObjectName("select_mirror_button")
        self.gridLayout_6.addWidget(self.select_mirror_button, 5, 0, 1, 2)
        self.select_moved_verts_button = QtGui.QPushButton(self.tab_3)
        self.select_moved_verts_button.setMinimumSize(QtCore.QSize(0, 20))
        self.select_moved_verts_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_moved_verts_button.setAutoDefault(False)
        self.select_moved_verts_button.setDefault(False)
        self.select_moved_verts_button.setFlat(False)
        self.select_moved_verts_button.setObjectName("select_moved_verts_button")
        self.gridLayout_6.addWidget(self.select_moved_verts_button, 6, 0, 1, 2)
        self.mirror_selected_button = QtGui.QPushButton(self.tab_3)
        self.mirror_selected_button.setMinimumSize(QtCore.QSize(0, 20))
        self.mirror_selected_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mirror_selected_button.setAutoDefault(False)
        self.mirror_selected_button.setDefault(False)
        self.mirror_selected_button.setFlat(False)
        self.mirror_selected_button.setObjectName("mirror_selected_button")
        self.gridLayout_6.addWidget(self.mirror_selected_button, 7, 0, 1, 2)
        self.flip_selected_button = QtGui.QPushButton(self.tab_3)
        self.flip_selected_button.setMinimumSize(QtCore.QSize(0, 20))
        self.flip_selected_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.flip_selected_button.setAutoDefault(False)
        self.flip_selected_button.setDefault(False)
        self.flip_selected_button.setFlat(False)
        self.flip_selected_button.setObjectName("flip_selected_button")
        self.gridLayout_6.addWidget(self.flip_selected_button, 8, 0, 1, 2)
        self.revert_selected_button = QtGui.QPushButton(self.tab_3)
        self.revert_selected_button.setMinimumSize(QtCore.QSize(0, 20))
        self.revert_selected_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.revert_selected_button.setAutoDefault(False)
        self.revert_selected_button.setDefault(False)
        self.revert_selected_button.setFlat(False)
        self.revert_selected_button.setObjectName("revert_selected_button")
        self.gridLayout_6.addWidget(self.revert_selected_button, 9, 0, 1, 2)
        self.revert_selected_slider = QtGui.QSlider(self.tab_3)
        self.revert_selected_slider.setOrientation(QtCore.Qt.Horizontal)
        self.revert_selected_slider.setObjectName("revert_selected_slider")
        self.gridLayout_6.addWidget(self.revert_selected_slider, 10, 0, 1, 1)
        self.revert_selected_doublespinbox = QtGui.QSpinBox(self.tab_3)
        self.revert_selected_doublespinbox.setWrapping(False)
        self.revert_selected_doublespinbox.setAccelerated(True)
        self.revert_selected_doublespinbox.setMaximum(100)
        self.revert_selected_doublespinbox.setObjectName("revert_selected_doublespinbox")
        self.gridLayout_6.addWidget(self.revert_selected_doublespinbox, 10, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.operate_negative_direction_checkbox = QtGui.QCheckBox(self.tab_3)
        self.operate_negative_direction_checkbox.setObjectName("operate_negative_direction_checkbox")
        self.horizontalLayout_3.addWidget(self.operate_negative_direction_checkbox)
        self.use_pivot_as_origin_checkbox = QtGui.QCheckBox(self.tab_3)
        self.use_pivot_as_origin_checkbox.setChecked(True)
        self.use_pivot_as_origin_checkbox.setObjectName("use_pivot_as_origin_checkbox")
        self.horizontalLayout_3.addWidget(self.use_pivot_as_origin_checkbox)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 11, 0, 1, 2)
        self.select_old_geometry_button = QtGui.QPushButton(self.tab_3)
        self.select_old_geometry_button.setEnabled(True)
        self.select_old_geometry_button.setMinimumSize(QtCore.QSize(0, 20))
        self.select_old_geometry_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_old_geometry_button.setAutoDefault(False)
        self.select_old_geometry_button.setDefault(False)
        self.select_old_geometry_button.setFlat(False)
        self.select_old_geometry_button.setObjectName("select_old_geometry_button")
        self.gridLayout_6.addWidget(self.select_old_geometry_button, 12, 0, 1, 2)
        self.old_geometry_lineedit = QtGui.QLineEdit(self.tab_3)
        self.old_geometry_lineedit.setEnabled(False)
        self.old_geometry_lineedit.setMinimumSize(QtCore.QSize(0, 20))
        self.old_geometry_lineedit.setObjectName("old_geometry_lineedit")
        self.gridLayout_6.addWidget(self.old_geometry_lineedit, 13, 0, 1, 2)
        self.bake_geometry_modification_button = QtGui.QPushButton(self.tab_3)
        self.bake_geometry_modification_button.setMinimumSize(QtCore.QSize(0, 20))
        self.bake_geometry_modification_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bake_geometry_modification_button.setAutoDefault(False)
        self.bake_geometry_modification_button.setDefault(False)
        self.bake_geometry_modification_button.setFlat(False)
        self.bake_geometry_modification_button.setObjectName("bake_geometry_modification_button")
        self.gridLayout_6.addWidget(self.bake_geometry_modification_button, 14, 0, 1, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 3)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Blendshape targets", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_all_ctrl.setText(QtGui.QApplication.translate("Dialog", "Reset controllers", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_button.setText(QtGui.QApplication.translate("Dialog", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.create_bs_button.setText(QtGui.QApplication.translate("Dialog", "Create blendshape", None, QtGui.QApplication.UnicodeUTF8))
        self.add_targets_button.setText(QtGui.QApplication.translate("Dialog", "Add target(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.extract_targets_button.setText(QtGui.QApplication.translate("Dialog", "Extract target(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_bs_button.setText(QtGui.QApplication.translate("Dialog", "Delete blendshape node", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_targets_button.setText(QtGui.QApplication.translate("Dialog", "Remove target(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "In-between value", None, QtGui.QApplication.UnicodeUTF8))
        self.add_inbetween_button.setText(QtGui.QApplication.translate("Dialog", "Add in-between", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Blendshapes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.negative.setText(QtGui.QApplication.translate("Dialog", "Negative", None, QtGui.QApplication.UnicodeUTF8))
        self.new_attr_name.setText(QtGui.QApplication.translate("Dialog", "New Attribute name", None, QtGui.QApplication.UnicodeUTF8))
        self.connect_button.setText(QtGui.QApplication.translate("Dialog", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.create_attr_button.setText(QtGui.QApplication.translate("Dialog", "Create attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.disconnect_button.setText(QtGui.QApplication.translate("Dialog", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_attr_button.setText(QtGui.QApplication.translate("Dialog", "Delete attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.export_connections_button.setText(QtGui.QApplication.translate("Dialog", "Export connections", None, QtGui.QApplication.UnicodeUTF8))
        self.import_connections_button.setText(QtGui.QApplication.translate("Dialog", "Import connections", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Controllers", None, QtGui.QApplication.UnicodeUTF8))
        self.use_active_selection_radiobutton.setText(QtGui.QApplication.translate("Dialog", "Use Active Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.use_ui_selection_radiobutton.setText(QtGui.QApplication.translate("Dialog", "Use Ui Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.yz_orientation_radiobutton.setText(QtGui.QApplication.translate("Dialog", "YZ", None, QtGui.QApplication.UnicodeUTF8))
        self.xz_orientation_radiobutton.setText(QtGui.QApplication.translate("Dialog", "XZ", None, QtGui.QApplication.UnicodeUTF8))
        self.xy_orientation_radiobutton.setText(QtGui.QApplication.translate("Dialog", "XY", None, QtGui.QApplication.UnicodeUTF8))
        self.select_base_geometry_button.setText(QtGui.QApplication.translate("Dialog", "Select Base Geometry", None, QtGui.QApplication.UnicodeUTF8))
        self.check_sym_button.setText(QtGui.QApplication.translate("Dialog", "Check Symmetry", None, QtGui.QApplication.UnicodeUTF8))
        self.select_mirror_button.setText(QtGui.QApplication.translate("Dialog", "Select Mirror", None, QtGui.QApplication.UnicodeUTF8))
        self.select_moved_verts_button.setText(QtGui.QApplication.translate("Dialog", "Select Moved Vertices", None, QtGui.QApplication.UnicodeUTF8))
        self.mirror_selected_button.setText(QtGui.QApplication.translate("Dialog", "Mirror Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.flip_selected_button.setText(QtGui.QApplication.translate("Dialog", "Flip Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.revert_selected_button.setText(QtGui.QApplication.translate("Dialog", "Revert Selected To base", None, QtGui.QApplication.UnicodeUTF8))
        self.operate_negative_direction_checkbox.setText(QtGui.QApplication.translate("Dialog", "Operate -X to +X", None, QtGui.QApplication.UnicodeUTF8))
        self.use_pivot_as_origin_checkbox.setText(QtGui.QApplication.translate("Dialog", "Use Pivot as Origin", None, QtGui.QApplication.UnicodeUTF8))
        self.select_old_geometry_button.setText(QtGui.QApplication.translate("Dialog", "Select Old Geometry", None, QtGui.QApplication.UnicodeUTF8))
        self.bake_geometry_modification_button.setText(QtGui.QApplication.translate("Dialog", "Bake Geometry Modification", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Dialog", "Symetry Tools", None, QtGui.QApplication.UnicodeUTF8))

