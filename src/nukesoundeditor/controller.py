from nukesoundeditor.view import SoundEditorView
from nukesoundeditor import model
import nuke

if nuke.NUKE_VERSION_MAJOR < 16: 
    from PySide2.QtWidgets import QFileDialog
    from PySide2.QtCore import Qt, QSettings
else:
    from PySide6.QtWidgets import QFileDialog
    from PySide6.QtCore import Qt, QSettings

class SoundEditorController:
    def __init__(self):
        self._view = SoundEditorView()
        self._connect_interface()
        self._checkbox_connect()
        self.nuke_setting_sound()
        self._save_button_connect()
        self._standard_checking()
        self._slider_control()

    def open_interface(self):
        self._view.show()

    def _select_sound_file(self):
        select_sound_file_dialog = QFileDialog()
        select_sound_file_dialog.setNameFilter("select file (*.mp3 *.wav)")
        select_sound_file_dialog.exec()
        if not select_sound_file_dialog.selectedFiles():
            self._view.selection_status.setText("You did not select a file")
            return
        
        self.output = select_sound_file_dialog.selectedFiles()[0]
        model.set_sound_file_path(self.output)
        self._view.selection_status.setText("Sound has been selected")

    def _connect_interface(self):
        self._view.selection_button.clicked.connect(self._select_sound_file)

    def nuke_setting_sound(self):
        if not model.is_render_sound_enabled():
            return
        nuke.addAfterRender(model.render_sound)

    def _checkbox_connect(self):
        self._view.check.stateChanged.connect(self._checkbox_change)
    
    def _checkbox_change(self):
        if self._view.check.isChecked():
            self._view.selection_status.setText("RenderSound is enabled")
            model.set_render_sound_enabled(True)
        else:
            self._view.selection_status.setText("RenderSound is disabled")
            model.set_render_sound_enabled(False)


    def _save_button_connect(self):
        self._view.save_button.clicked.connect(self.exit_app)

    def exit_app(self):
        self._view.close()

    def _standard_checking(self):
        self._view.check.setChecked(model.is_render_sound_enabled())

    def _slider_control(self):
        self._view.slider.valueChanged.connect(self._view.changed_value)
        self._view.slider.setSliderPosition(int(QSettings().value("NukeRenderSound/AudioFile/Volume")))
        self._view.slider.valueChanged.connect(lambda v: model.set_render_sound_volume(int(v)))
        self._view.slider.sliderReleased.connect(model.render_sound)

