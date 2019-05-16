import time
import os
import sys
import shutil
import subprocess

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QFileDialog, QComboBox, QMessageBox, \
    QAbstractItemView, QDialogButtonBox, QLabel, QWidget, QPushButton, QListWidget, QFrame, QProgressBar, QStatusBar


class ChooseStagePopupUI:
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
        with open(os.path.join(get_mbtool_dir(), 'resources', 'challenge_stages_list.txt'), 'r') as f:
            for line in f:
                clean_line = line.strip()
                self._stage_select_combobox.addItem(clean_line)
                self._stage_base_names.append(clean_line)


class ChooseStagePopup(QMainWindow, ChooseStagePopupUI):
    def __init__(self):
        QMainWindow.__init__(self)
        ChooseStagePopupUI.__init__(self)
        self._setup_ui(self)

    def connect(self, callback):
        self._dialog_button_box.accepted.connect(callback)

    def get_selected_stage_index(self):
        return int(self._stage_select_combobox.currentIndex())

    def set_associated_stage(self, index, associated_stage):
        self._stage_select_combobox.setItemText(index, self._stage_base_names[index] + " [{}]".format(associated_stage))

    def remove_associated_stage(self, stage_index):
        self._stage_select_combobox.setItemText(stage_index, self._stage_base_names[stage_index])

    def get_stage_name(self, index):
        return self._stage_base_names[index].split(":")[1][1:]

    def get_stage_id(self, index):
        return self._stage_base_names[index].split(":")[0]

    def increment_stage_index(self):
        current_idx = self._stage_select_combobox.currentIndex()
        if current_idx == self._stage_select_combobox.count() - 1:
            current_idx = 0
        else:
            current_idx += 1
        self._stage_select_combobox.setCurrentIndex(current_idx)


class MBToolUI:
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
        self._progress_bar.setGeometry(QtCore.QRect(0, 530, 617, 23))
        self._progress_bar.setValue(0)
        self._progress_bar.setMaximum(100)
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
        self._output_stage_id_key = QtCore.Qt.DecorationRole
        self._is_valid_input_key = QtCore.Qt.BackgroundRole

        # the tuple allows for replacement files for the given element. obj and mtl are required and have no replacement
        # but for config we can take xml lz or lz.raw. let the order of the tuple denote priority (we want xml over all)
        self._required_extensions = [("obj",), ("mtl",), ("xml", "lz", "lz.raw")]
        self._required_tools = ['GxModelViewer.exe', 'ws2lzfrontend.exe', 'SMB_LZ_Tool.exe']
        self._tool_filepaths = self.find_required_tools()
        self._imported_obj_filepaths = []
        self._replace_queue = []
        self._temp_dir = os.path.join(get_mbtool_dir(), 'temp')

    def find_required_tools(self):
        tool_filepaths = {}
        [tool_filepaths.update({f: os.path.join(dp, f)})
         for dp, dn, filenames in os.walk(get_mbtool_dir())
         for f in filenames if f in self._required_tools]

        return tool_filepaths

    # button callbacks:
    def _add_single_stage(self, obj_filepath):
        import_stage_directory = os.path.dirname(obj_filepath)
        import_stage_base_name = str(os.path.basename(obj_filepath).split(".")[0])
        all_filenames = os.listdir(import_stage_directory)

        collected_filepaths = {}
        item_string = import_stage_base_name + " | has: ["
        for required_extension in self._required_extensions:
            for extension in required_extension:
                filename = import_stage_base_name + "." + extension
                if filename in all_filenames:
                    collected_filepaths[os.path.splitext(filename)[1][1:]] = os.path.join(import_stage_directory, filename)
                    item_string += extension + ", "
                    break
        item_string = item_string[:-2] + "]"

        all_inputs_met = len(collected_filepaths.keys()) == len(self._required_extensions)

        item = QListWidgetItem()
        item.setData(self._input_filenames_key, collected_filepaths)
        item.setData(self._is_valid_input_key, all_inputs_met)
        item.setText(item_string)
        item.setIcon(QIcon("resources/green_checkmark.png") if all_inputs_met else QIcon("resources/red_xmark.png"))

        self._imported_stages_list.addItem(item)

    def _add_single_stage_btn_clicked(self):
        file_dialog = QFileDialog()
        obj_filepath = QFileDialog.getOpenFileName(file_dialog,
                                                   "import stage .obj file",
                                                   get_mbtool_dir(),
                                                   "*.obj")[0]

        if obj_filepath in self._imported_obj_filepaths:
            duplicate_idx = self._imported_obj_filepaths.index(obj_filepath)
            duplicate_item = self._imported_stages_list.item(duplicate_idx)
            self._imported_stages_list.takeItem(self._imported_stages_list.row(duplicate_item))
            del self._imported_obj_filepaths[duplicate_idx]

        if obj_filepath:
            self._add_single_stage(obj_filepath)
            self._imported_obj_filepaths.append(obj_filepath)
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
                                                              get_mbtool_dir())
        stages_folder_path = QtCore.QDir.toNativeSeparators(stages_folder_path)

        obj_filepaths = [os.path.join(dp, f)
                         for dp, dn, filenames in os.walk(stages_folder_path)
                         for f in filenames if os.path.splitext(f)[1] == '.obj']

        for obj_filepath in obj_filepaths:
            if obj_filepath in self._imported_obj_filepaths:
                duplicate_idx = self._imported_obj_filepaths.index(obj_filepath)
                duplicate_item = self._imported_stages_list.item(duplicate_idx)
                self._imported_stages_list.takeItem(self._imported_stages_list.row(duplicate_item))
                del self._imported_obj_filepaths[duplicate_idx]

            self._add_single_stage(obj_filepath)
            self._imported_obj_filepaths.append(obj_filepath)

        if obj_filepaths:
            self._imported_stages_list.sortItems()

    def _import_root_btn_clicked(self):
        file_dialog = QFileDialog()
        file_dialog.setParent(self.sender())
        self._root_folder_path = QFileDialog.getExistingDirectory(file_dialog,
                                                                  "import root folder extracted from .iso",
                                                                  get_mbtool_dir())
        self._root_folder_path = QtCore.QDir.toNativeSeparators(self._root_folder_path)

        if not os.path.exists(os.path.join(self._root_folder_path, 'stage')):
            self._root_folder_path = None
            self._give_error_message("root folder seems to be invalid, no 'stage' folder found")
            return

        self.root_folder_label.setText(self._root_folder_path)

    def _add_to_replace_btn_clicked(self):
        selected_items = self._imported_stages_list.selectedItems()

        if not selected_items:
            pass
        elif not all([selected_item.data(self._is_valid_input_key) for selected_item in selected_items]):
            required = [', or '.join(required_extension) for required_extension in self._required_extensions]
            self._give_error_message("Could not find all required files for one of the selected stages!\n"
                                     "Required Extensions: " + str(required) + "\n\n"
                                     "Please sure the required files are in the same directory as the .obj,\n"
                                     "then reimport the stage!")
        else:
            self._choose_stage_popup.setWindowModality(QtCore.Qt.WindowModal)
            self._choose_stage_popup.connect(self._on_choose_stage)
            self._choose_stage_popup.show()

    def _remove_from_replace_btn_clicked(self):
        selected_items = self._replace_queue_list.selectedItems()
        for i, selected_item in enumerate(selected_items):
            self._replace_queue_list.takeItem(self._replace_queue_list.row(selected_item))
            self._choose_stage_popup.remove_associated_stage(self._replace_queue[i][1])

    def _replace_stage_in_root(self, obj_filepath, config_filepath, stage_id):
        config_ext = os.path.splitext(config_filepath)[1]
        base_filepath = os.path.splitext(obj_filepath)[0]
        gma_filepath = base_filepath + ".gma"
        tpl_filepath = base_filepath + ".tpl"
        lz_raw_filepath = base_filepath + ".lz.raw"
        lz_filepath = os.path.splitext(lz_raw_filepath)[0]

        needs_lz_raw_creation = config_ext == "xml"
        needs_lz_compression = config_ext == "xml" or config_ext == "lz.raw"

        if not needs_lz_compression and not needs_lz_raw_creation and not os.path.exists(lz_filepath):
            self._give_error_message(".lz file promised not found", raise_exception=True)
            return

        # make gma and tpl in another thread while we do other things
        gx_process = subprocess.Popen([self._tool_filepaths['GxModelViewer.exe'], obj_filepath])

        # make .lz.raw
        if needs_lz_raw_creation:
            tool_id = 'ws2lzfrontend.exe'
            if tool_id not in self._tool_filepaths:
                self._give_error_message("Cannot find tool: " + tool_id +
                                         "\n\nPlease make sure the tool with this exact name "
                                         "is somewhere in the mbtool directory", raise_exception=True)
                return

            subprocess.call([self._tool_filepaths[tool_id], '-c', config_filepath, '-o', lz_raw_filepath, "-g", '2'])

        if needs_lz_compression and not os.path.exists(lz_raw_filepath):
            self._give_error_message("Failure to create .lz.raw file, ensure the config/obj/mtl files are valid, " \
                                     "as well as the ws2lzfrontend.exe tool", raise_exception=True)
            return

        # make .lz
        if needs_lz_compression:
            tool_id = 'SMB_LZ_Tool.exe'
            if tool_id not in self._tool_filepaths:
                self._give_error_message("Cannot find tool: " + tool_id +
                                         "\n\nPlease make sure the tool with this exact name "
                                         "is somewhere in the mbtool directory", raise_exception=True)
                return

            subprocess.call([self._tool_filepaths[tool_id], lz_raw_filepath])

        if needs_lz_compression and not os.path.exists(lz_raw_filepath + '.lz'):
            self._give_error_message("Failure to create .lz.raw file, ensure the config/obj/mtl files are valid, "
                                     "as well as the ws2lzfrontend.exe tool", raise_exception=True)
            return

        if needs_lz_compression:
            os.remove(lz_filepath)
            os.rename(lz_raw_filepath + '.lz', lz_filepath)
            os.remove(lz_raw_filepath)

        # wait for the gx process to finish
        gx_process.wait()
        if not os.path.exists(gma_filepath) or not os.path.exists(tpl_filepath):
            self._give_error_message("Failure to create gma and tpl files, ensure these files are correct, "
                                     "as well as the GxModelViewer.exe (No GUI) tool", raise_exception=True)
            return

        stage_gma_filepath = os.path.join(self._root_folder_path, 'stage', 'st' + stage_id + '.gma')
        stage_tpl_filepath = os.path.join(self._root_folder_path, 'stage', 'st' + stage_id + '.tpl')
        stage_lz_filepath = os.path.join(self._root_folder_path, 'stage', 'STAGE' + stage_id + '.lz')

        shutil.copy(gma_filepath, stage_gma_filepath)
        shutil.copy(tpl_filepath, stage_tpl_filepath)
        shutil.copy(lz_filepath, stage_lz_filepath)

    def _replace_btn_clicked(self, mock_replace=True):
        if self._root_folder_path is None:
            self._give_error_message("Please import your monkeyball root folder created by gamecube rebuilder")
            return

        self._tool_filepaths = self.find_required_tools()

        self._progress_bar.setMaximum(100)
        progress_increment = 100 / self._replace_queue_list.count()
        for i in range(self._replace_queue_list.count()):
            item = self._replace_queue_list.item(i)
            input_filepaths = item.data(self._input_filenames_key)
            obj_filepath = input_filepaths['obj']
            config_filepath = [value for key, value in input_filepaths.items() if key != 'obj' and key != 'mtl'][0]

            stage_id = item.data(self._output_stage_id_key)
            if mock_replace:
                time.sleep(0.25)
            else:
                self._replace_stage_in_root(obj_filepath, config_filepath, stage_id)

            self._status_bar.setStatusTip("written " + os.path.basename(os.path.splitext(obj_filepath)[0]) + " to root")
            self._progress_bar.setValue(int((i + 1) * progress_increment))

    def _on_choose_stage(self):
        if not self._choose_stage_popup.isActiveWindow():
            return

        self._choose_stage_popup.close()

        selected_items = self._imported_stages_list.selectedItems()
        for selected_item in selected_items:
            stage_index = self._choose_stage_popup.get_selected_stage_index()
            replacement_stage_name = selected_item.text().split("|")[0][:-1]

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

            item = QListWidgetItem()
            item.setData(self._output_stage_id_key, self._choose_stage_popup.get_stage_id(stage_index))
            item.setData(self._input_filenames_key, selected_item.data(self._input_filenames_key))
            item_text = replacement_stage_name + " -> " + self._choose_stage_popup.get_stage_name(stage_index)
            item.setText(item_text)

            self._replace_queue_list.addItem(item)
            self._replace_queue.append((replacement_stage_name, stage_index))
            self._choose_stage_popup.increment_stage_index()

    def _give_error_message(self, message, raise_exception=False):
        error_message = QMessageBox()
        error_message.setParent(self.sender())
        error_message.setWindowTitle("ERROR")
        error_message.setText(message)
        error_message.setWindowModality(QtCore.Qt.WindowModal)
        error_message.exec_()
        if raise_exception:
            raise Exception(message)


def get_mbtool_dir():
    """
    Get the mbtool dir
    :return str: mbtool root dir
    """
    return os.getcwd()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MBTool()
    window.show()
    sys.exit(app.exec_())
