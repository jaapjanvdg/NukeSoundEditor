import nuke
if nuke.NUKE_VERSION_MAJOR < 16: 
    from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
    from PySide2.QtCore import QUrl, QSettings
else:
    from PySide6.QtMultimedia import QMediaPlayer
    from PySide6.QtCore import QUrl, QSettings


if not hasattr(nuke, "_render_sound_player"):
    nuke._render_sound_player = QMediaPlayer()

audio_player = nuke._render_sound_player

def render_sound():
    if not is_render_sound_enabled():
        return
    
    file_path = QSettings().value("NukeRenderSound/AudioFile")
    volume = int(QSettings().value("NukeRenderSound/AudioFile/Volume"))

    if nuke.NUKE_VERSION_MAJOR < 16:
        audio_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
    else:
        audio_player.setSource(QUrl.fromLocalFile(file_path))

    audio_player.stop()
    audio_player.setPosition(0)
    audio_player.setVolume(volume)
    audio_player.play()

def initialize_settings(path=None):
    settings = QSettings()
    if not settings.contains("NukeRenderSound/AudioFile"):
        settings.setValue("NukeRenderSound/AudioFile", "C:/pipeline/nuke/NukeRenderSound/rnd_okay.wav")
    if not settings.contains("NukeRenderSound/AudioFile/Enabled"):
        settings.setValue("NukeRenderSound/AudioFile/Enabled", "True")
    if not settings.contains("NukeRenderSound/AudioFile/Volume"):
        settings.setValue("NukeRenderSound/AudioFile/Volume", "100")


def set_sound_file_path(path):
    QSettings().setValue("NukeRenderSound/AudioFile", path)

def is_render_sound_enabled():
    return QSettings().value("NukeRenderSound/AudioFile/Enabled") == "True"

def set_render_sound_enabled(enabled):
    QSettings().setValue("NukeRenderSound/AudioFile/Enabled", "True" if enabled else "False")

def set_render_sound_volume(volume):
    QSettings().setValue("NukeRenderSound/AudioFile/Volume", volume)

initialize_settings()