# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mbtool.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import os
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QFileDialog, QComboBox, QMessageBox, \
    QAbstractItemView, QDialogButtonBox, QLabel, QWidget, QPushButton, QListWidget, QProgressBar, QFrame, QFrame, \
    QProgressBar, QStatusBar


class ChooseStagePopupUI(object):
    def __init__(self):
        self._stage_select_combobox = None  # type: QComboBox
        self._dialog_button_box = None  # type: QDialogButtonBox
        self._choose_stage_label = None  # type: QLabel
        self._stage_base_names = []

    def _setup_ui(self, choose_stage_popup):
        choose_stage_popup.setObjectName("choose_stage_popupI")
        choose_stage_popup.resize(493, 108)

        self._stage_select_combobox = QComboBox(choose_stage_popup)
        self._stage_select_combobox.setGeometry(QtCore.QRect(10, 30, 471, 27))
        self._stage_select_combobox.setObjectName("stage_select_combobox")
        self._load_stages()

        self._dialog_button_box = QDialogButtonBox(choose_stage_popup)
        self._dialog_button_box.setGeometry(QtCore.QRect(150, 70, 176, 27))
        self._dialog_button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self._dialog_button_box.setObjectName("dialog_button_box")
        self._dialog_button_box.rejected.connect(self.close)

        self._choose_stage_label = QLabel(choose_stage_popup)
        self._choose_stage_label.setGeometry(QtCore.QRect(10, 10, 461, 17))
        self._choose_stage_label.setObjectName("choose_stage_label")
        self._choose_stage_label.setText("Choose monkeyball stage to replace (Challenge Mode)")

        choose_stage_popup.setWindowTitle("Choose Stage to Replace")

    def _load_stages(self):
        with open(os.path.join(get_current_dir(), 'mbtool2/resources', 'challenge_stages_list.txt'), 'r') as f:
            for line in f:
                self._stage_select_combobox.addItem(line.strip())
                self._stage_base_names.append(line.strip())

    def connect(self, callback):
        self._dialog_button_box.accepted.connect(callback)

    def get_selected_stage_index(self):
        return int(self._stage_select_combobox.currentIndex())

    def set_associated_stage(self, index, associated_stage):
        self._stage_select_combobox.setItemText(index, self._stage_base_names[index] + " [{}]".format(associated_stage))

    def get_stage_name(self, index):
        return self._stage_base_names[index].split(":")[1][1:]

    def get_stage_id(self, index):
        return self._stage_base_names[index].split(":")[0]


class ChooseStagePopup(QMainWindow, ChooseStagePopupUI):
    def __init__(self):
        QMainWindow.__init__(self)
        ChooseStagePopupUI.__init__(self)
        self._setup_ui(self)


class MBToolUI(object):
    def __init__(self):
        self._central_widget = None  # type: QWidget
        self._import_multiple_stages_btn = None  # type: QPushButton
        self._import_root_btn = None  # type: QPushButton
        self._imported_stages_list = None  # type: QListWidget
        self._imported_stages_label = None  # type: QLabel
        self._replace_queue_list = None  # type: QListWidget
        self._stages_to_be_replaced_label = None  # type: QLabel
        self._replace_btn = None  # type: QPushButton
        self._add_to_replace_btn = None  # type: QPushButton
        self._remove_from_replace_btn = None  # type: QPushButton
        self._progress_bar = None  # type: QProgressBar
        self._line = None  # type: QFrame
        self._add_single_stage_btn = None  # type: QPushButton
        self._remove_single_stage_btn = None  # type: QPushButton
        self._status_bar = None  # type: QStatusBar

    def _setup_ui(self, mbtool):
        mbtool.setObjectName("mbtool")
        mbtool.resize(582, 582)

        self._central_widget = QWidget(mbtool)
        self._central_widget.setObjectName("centralWidget")

        self._import_multiple_stages_btn = QPushButton(self._central_widget)
        self._import_multiple_stages_btn.setGeometry(QtCore.QRect(60, 490, 151, 27))
        self._import_multiple_stages_btn.setObjectName("import_multiple_stages_btn")
        self._import_multiple_stages_btn.setText("import stages folder")

        self._import_root_btn = QPushButton(self._central_widget)
        self._import_root_btn.setGeometry(QtCore.QRect(40, 10, 161, 31))
        self._import_root_btn.setObjectName("import_root_btn")
        self._import_root_btn.setText("import root folder")

        self.root_folder_label = QLabel(self._central_widget)
        self.root_folder_label.setGeometry(QtCore.QRect(220, 16, 341, 21))
        self.root_folder_label.setObjectName("root_folder_label")

        self._imported_stages_list = QListWidget(self._central_widget)
        self._imported_stages_list.setGeometry(QtCore.QRect(10, 80, 251, 401))
        self._imported_stages_list.setObjectName("imported_stages_list")
        self._imported_stages_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self._imported_stages_label = QLabel(self._central_widget)
        self._imported_stages_label.setGeometry(QtCore.QRect(70, 50, 111, 31))
        self._imported_stages_label.setObjectName("imported_stages_label")
        self._imported_stages_label.setText("imported stages")

        self._replace_queue_list = QListWidget(self._central_widget)
        self._replace_queue_list.setGeometry(QtCore.QRect(320, 80, 251, 401))
        self._replace_queue_list.setObjectName("replace_queue_list")
        self._replace_queue_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self._stages_to_be_replaced_label = QLabel(self._central_widget)
        self._stages_to_be_replaced_label.setGeometry(QtCore.QRect(370, 50, 151, 31))
        self._stages_to_be_replaced_label.setObjectName("stages_to_be_replaced_label")
        self._stages_to_be_replaced_label.setText("stages to be replaced")

        self._replace_btn = QPushButton(self._central_widget)
        self._replace_btn.setGeometry(QtCore.QRect(380, 490, 131, 31))
        self._replace_btn.setObjectName("replace_btn")
        self._replace_btn.setText("replace!")

        self._add_to_replace_btn = QPushButton(self._central_widget)
        self._add_to_replace_btn.setGeometry(QtCore.QRect(270, 240, 41, 27))
        self._add_to_replace_btn.setObjectName("add_to_replace_btn")
        self._add_to_replace_btn.setText("->")

        self._remove_from_replace_btn = QPushButton(self._central_widget)
        self._remove_from_replace_btn.setGeometry(QtCore.QRect(270, 290, 41, 27))
        self._remove_from_replace_btn.setObjectName("remove_from_replace_btn")
        self._remove_from_replace_btn.setText("<-")

        self._progress_bar = QProgressBar(self._central_widget)
        self._progress_bar.setGeometry(QtCore.QRect(0, 530, 581, 23))
        self._progress_bar.setProperty("value", 0)
        self._progress_bar.setObjectName("progress_bar")

        self._line = QFrame(self._central_widget)
        self._line.setGeometry(QtCore.QRect(0, 40, 571, 20))
        self._line.setFrameShape(QFrame.HLine)
        self._line.setFrameShadow(QFrame.Sunken)
        self._line.setObjectName("line")

        self._add_single_stage_btn = QPushButton(self._central_widget)
        self._add_single_stage_btn.setGeometry(QtCore.QRect(230, 490, 31, 27))
        self._add_single_stage_btn.setObjectName("add_single_stage_btn")
        self._add_single_stage_btn.setText("+")

        self._remove_single_stage_btn = QPushButton(self._central_widget)
        self._remove_single_stage_btn.setGeometry(QtCore.QRect(10, 490, 31, 27))
        self._remove_single_stage_btn.setObjectName("remove_single_stage_btn")
        self._remove_single_stage_btn.setText("-")

        mbtool.setCentralWidget(self._central_widget)

        self._status_bar = QStatusBar(mbtool)
        self._status_bar.setObjectName("statusBar")
        mbtool.setStatusBar(self._status_bar)

        mbtool.setWindowTitle("mbtool")

class MBTool(QMainWindow, MBToolUI):
    def __init__(self):
        QMainWindow.__init__(self)
        MBToolUI.__init__(self)
        self._setup_ui(self)

        self._import_multiple_stages_btn.clicked.connect(self._import_multiple_stages_btn_clicked)
        self._import_root_btn.clicked.connect(self._import_root_btn_clicked)
        self._add_to_replace_btn.clicked.connect(self._add_to_replace_btn_clicked)
        self._remove_from_replace_btn.clicked.connect(self._remove_from_replace_btn_clicked)
        self._replace_btn.clicked.connect(self._replace_btn_clicked)
        self._add_single_stage_btn.clicked.connect(self._add_single_stage_btn_clicked)
        self._remove_single_stage_btn.clicked.connect(self._remove_single_stage_btn_clicked)

        self._root_folder_path = None
        self._imported_stages = []
        self._stages_to_be_replaced = []
        self._choose_stage_popup = ChooseStagePopup()

        self._input_filenames_key = QtCore.Qt.UserRole
        self._output_stage_id_key = QtCore.Qt.DisplayRole
        self._is_valid_input_key = QtCore.Qt.BackgroundRole
        self._required_extensions = ["mtl", "obj", "xml"]
        self._replace_queue = []

    # button callbacks:
    def _add_single_stage(self, obj_filepath):
        has_ext = dict(zip(self._required_extensions, [False]*len(self._required_extensions)))

        stage_base_name = str(os.path.basename(obj_filepath).split(".")[0])
        required_filenames = [stage_base_name + "." + required_extension for required_extension in self._required_extensions]
        stage_directory = os.path.dirname(obj_filepath)

        collected_filenames = []
        for filename in os.listdir(stage_directory):
            if filename in required_filenames:
                collected_filenames.append(filename)
                has_ext[filename.split(".")[-1]] = True
        item_string = stage_base_name + " | ["
        for required_extension in self._required_extensions:
            if has_ext[required_extension]:
                item_string += required_extension + ", "
        item_string = item_string[:-2] + "]"

        collected_filepaths = []
        for collected_filename in collected_filenames:
            collected_filepaths.append(os.path.join(stage_directory, collected_filename))

        item = QListWidgetItem()
        item.setData(self._input_filenames_key, ", ".join(collected_filepaths))
        item.setData(self._is_valid_input_key, sum(has_ext.values()) == len(self._required_extensions))
        item.setText(item_string)
        item.setIcon(QIcon("resources/green_checkmark.png")
                     if sum(has_ext.values()) == len(self._required_extensions)
                     else QIcon("resources/red_xmark.png"))

        self._imported_stages_list.addItem(item)

    def _add_single_stage_btn_clicked(self):
        file_dialog = QFileDialog()
        obj_filepath = QFileDialog.getOpenFileName(file_dialog,
                                                   "import stage .obj file",
                                                   os.path.join(get_current_dir(), "mbtool"),
                                                   "*.obj")[0]
        if obj_filepath:
            self._add_single_stage(obj_filepath)
        self._imported_stages_list.sortItems()

    def _remove_single_stage_btn_clicked(self):
        selected_items = self._imported_stages_list.selectedItems()
        for selected_item in selected_items:
            self._imported_stages_list.takeItem(self._imported_stages_list.row(selected_item))

    def _import_multiple_stages_btn_clicked(self):
        file_dialog = QFileDialog()
        file_dialog.setParent(self.sender())
        stages_folder_path = QFileDialog.getExistingDirectory(file_dialog,
                                                              "import folder with multiple objs/mtls/configs",
                                                              os.path.join(get_current_dir(), "mbtool2"))
        obj_filepaths = [os.path.join(dp, f)
                         for dp, dn, filenames in os.walk(stages_folder_path)
                         for f in filenames if os.path.splitext(f)[1] == '.obj']

        for obj_filepath in obj_filepaths:
            self._add_single_stage(obj_filepath)
        self._imported_stages_list.sortItems()

    def _import_root_btn_clicked(self):
        file_dialog = QFileDialog()
        file_dialog.setParent(self.sender())
        self._root_folder_path = QFileDialog.getExistingDirectory(file_dialog,
                                                                  "import root folder extracted from .iso",
                                                                  os.path.join(get_current_dir(), "mbtool2"))
        self.root_folder_label.setText(self._root_folder_path)

    def _add_to_replace_btn_clicked(self):
        selected_items = self._imported_stages_list.selectedItems()

        if not selected_items:
            pass
        elif len(selected_items) > 1:
            self._give_error_message("Please only select one stage at a time for replacement!")
        elif not selected_items[0].data(self._is_valid_input_key):
            self._give_error_message("Could not find all required files for the selected stage!\n"
                                     "Required Extensions: [" + ", ".join(self._required_extensions) + "]\n\n"
                                     "Please sure the required files are in the same directory as the .obj,\n"
                                     "then reimport the stage!")
        else:
            self._choose_stage_popup.setWindowModality(QtCore.Qt.WindowModal)
            self._choose_stage_popup.connect(self._on_choose_stage)
            self._choose_stage_popup.show()

    def _remove_from_replace_btn_clicked(self):
        selected_items = self._replace_queue_list.selectedItems()
        for selected_item in selected_items:
            self._replace_queue_list.takeItem(self._replace_queue_list.row(selected_item))

    def _replace_btn_clicked(self):
        pass

    def _on_choose_stage(self):
        if not self._choose_stage_popup.isActiveWindow():
            return

        self._choose_stage_popup.close()
        stage_index = self._choose_stage_popup.get_selected_stage_index()

        selected_items = self._imported_stages_list.selectedItems()
        if len(selected_items) != 1:
            self._give_error_message("Please only select one stage at a time for replacement!")
            return

        replacement_stage_name = selected_items[0].text().split("|")[0][:-1]

        # if theres a conflict or duplicate, remove it
        if self._replace_queue:
            stage_indices = list(zip(*self._replace_queue))[1]
            # conflict
            if stage_index in stage_indices:
                conflict_index = stage_indices.index(stage_index)
                conflict_item = self._replace_queue_list.item(conflict_index)
                self._replace_queue_list.takeItem(self._replace_queue_list.row(conflict_item))
                del self._replace_queue[conflict_index]

            # duplicate
            if (replacement_stage_name, stage_index) in self._replace_queue:
                return

        self._choose_stage_popup.set_associated_stage(stage_index, replacement_stage_name)

        input_filenames = selected_items[0].data(self._input_filenames_key).split(",")

        item = QListWidgetItem()
        item.setData(self._output_stage_id_key, self._choose_stage_popup.get_stage_id(stage_index))
        item.setData(self._input_filenames_key, input_filenames)
        item_text = replacement_stage_name + " -> " + self._choose_stage_popup.get_stage_name(stage_index)
        item.setText(item_text)

        self._replace_queue_list.addItem(item)
        self._replace_queue.append((replacement_stage_name, stage_index))

    def _give_error_message(self, message):
        error_message = QMessageBox()
        error_message.setParent(self.sender())
        error_message.setWindowTitle("ERROR")
        error_message.setText(message)
        error_message.setWindowModality(QtCore.Qt.WindowModal)
        error_message.exec_()


def get_current_dir():
    """
    Get the current dir
    :return str: mbtool root dir
    """
    return os.path.dirname(os.path.dirname(__file__))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MBTool()
    window.show()
    sys.exit(app.exec_())
