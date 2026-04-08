import nuke
if nuke.NUKE_VERSION_MAJOR < 16: 
    from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QCheckBox, QSlider
    from PySide2.QtCore import Qt
else:
    from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QCheckBox, QSlider
    from PySide6.QtCore import Qt


class SoundEditorView(QWidget):
    def __init__(self, ):
        super().__init__()

        self.setWindowTitle("Settings")
        self.setGeometry(300,300,200,200)
        self.layout = self._create_layout()
        self.setLayout(self.layout)

    def _create_layout(self):
        self._create_button()
        self._create_checkbox()
        self._create_volume_bar()
        self._create_save_button()

        editor_layout = QVBoxLayout()
        editor_layout.addWidget(self.selection_button)
        editor_layout.addWidget(self.slider)
        editor_layout.addWidget(self.sound_volume_label)
        editor_layout.addWidget(self.check)
        editor_layout.addWidget(self.selection_status)
        editor_layout.addWidget(self.save_button)
        return editor_layout

    def _create_button(self):
        self.selection_button = QPushButton("Select Audio File", self)

    def _create_checkbox(self):
        self.selection_status = QLabel()
        self.check = QCheckBox("RenderSound", self)

    def _create_save_button(self):
        self.save_button = QPushButton("Save and Quit", self)

    def _create_volume_bar(self):
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.sound_volume_label = QLabel()

    def changed_value(self, slider_value):
        self.sound_volume_label.setText(str(slider_value))

