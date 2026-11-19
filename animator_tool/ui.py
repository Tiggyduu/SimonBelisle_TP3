from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGroupBox,
    QLabel,
    QSpinBox,
    QPushButton,
    QGridLayout,
)

class RandomAnimationGenerator(QWidget):
    
    def __init__(self):
        super().__init__()

    def build_ui(self):

        self.setWindowTitle("Random Animation Generator")
        self.setMinimumWidth(400)
        self.layout = QVBoxLayout(self)
        self.animation_timing()
        self.translate_parameters()
        self.rotate_parameters()
        self.scale_parameters()
        self.generate_button()

    ### Animation Timing ###
    def animation_timing(self):
        # Crée le rectangle gris qui contient les paramètres et le label de la section
        animation_timing = QGroupBox("Animation Timing")
        animation_timing_layout = QGridLayout(animation_timing)
        # Pour la duration
        self.duration = QSpinBox()
        self.duration.setRange(0, 10000) # Range du "QSpinBox" (entre 0 et 10000 frames)
        self.duration.setValue(100) # Valeur par défaut
        # Pour le step
        self.step = QSpinBox()
        self.step.setRange(0, 10000)
        self.step.setValue(10)
        # Ajoute les "QSpinBox" dans le layout avec des labels
        # (*QLabel*, 0, 0) controle l'emplacement du widget dans le layout (0, 0 = à gauche sur la première ligne)
        animation_timing_layout.addWidget(QLabel("Durations (Frames):"), 0, 0)
        animation_timing_layout.addWidget(self.duration, 0, 1)
        animation_timing_layout.addWidget(QLabel("Step (Frames):"), 0, 2)
        animation_timing_layout.addWidget(self.step, 0, 3)
        # Ajoute le "QGroupBox" dans le layout de la fenêtre
        self.layout.addWidget(animation_timing)

    ### Translate Parameters ###
    def translate_parameters(self):
        # Voir commentaires dans "animation_timing()" pour comprendre le fonctionnement
        translate_parameters = QGroupBox("Translate Parameters")
        translate_layout = QGridLayout(translate_parameters)

        # Min x
        self.min_x = QSpinBox()
        self.min_x.setRange(-10000, 10000)
        self.min_x.setValue(0)
        # Min y
        self.min_y = QSpinBox()
        self.min_y.setRange(-10000, 10000)
        self.min_y.setValue(0)
        # Min z
        self.min_z = QSpinBox()
        self.min_z.setRange(-10000, 10000)
        self.min_z.setValue(0)

        # Max x
        self.max_x = QSpinBox()
        self.max_x.setRange(-10000, 10000)
        self.max_x.setValue(0)
        # Max y
        self.max_y = QSpinBox()
        self.max_y.setRange(-10000, 10000)
        self.max_y.setValue(0)
        # Max z
        self.max_z = QSpinBox()
        self.max_z.setRange(-10000, 10000)
        self.max_z.setValue(0)

        # Min
        translate_layout.addWidget(QLabel("Min X:"), 0, 0)
        translate_layout.addWidget(self.min_x, 0, 1)
        translate_layout.addWidget(QLabel("Min Y:"), 0, 2)
        translate_layout.addWidget(self.min_y, 0, 3)
        translate_layout.addWidget(QLabel("Min Z:"), 0, 4)
        translate_layout.addWidget(self.min_z, 0, 5)
        # Max
        translate_layout.addWidget(QLabel("Max X:"), 1, 0)
        translate_layout.addWidget(self.max_x, 1, 1)
        translate_layout.addWidget(QLabel("Max Y:"), 1, 2)
        translate_layout.addWidget(self.max_y, 1, 3)
        translate_layout.addWidget(QLabel("Max Z:"), 1, 4)
        translate_layout.addWidget(self.max_z, 1, 5)
        # Ajoute dans le main layout
        self.layout.addWidget(translate_parameters)

    ### Rotate Parameters ###
    def rotate_parameters(self):
        # Voir commentaires dans "animation_timing()" pour comprendre le fonctionnement
        rotate_parameters = QGroupBox("Rotate Parameters")
        rotate_layout = QGridLayout(rotate_parameters)

        # Min x
        self.min_x = QSpinBox()
        self.min_x.setRange(-10000, 10000)
        self.min_x.setValue(0)
        # Min y
        self.min_y = QSpinBox()
        self.min_y.setRange(-10000, 10000)
        self.min_y.setValue(0)
        # Min z
        self.min_z = QSpinBox()
        self.min_z.setRange(-10000, 10000)
        self.min_z.setValue(0)

        # Max x
        self.max_x = QSpinBox()
        self.max_x.setRange(-10000, 10000)
        self.max_x.setValue(0)
        # Max y
        self.max_y = QSpinBox()
        self.max_y.setRange(-10000, 10000)
        self.max_y.setValue(0)
        # Max z
        self.max_z = QSpinBox()
        self.max_z.setRange(-10000, 10000)
        self.max_z.setValue(0)

        # Min
        rotate_layout.addWidget(QLabel("Min X:"), 0, 0)
        rotate_layout.addWidget(self.min_x, 0, 1)
        rotate_layout.addWidget(QLabel("Min Y:"), 0, 2)
        rotate_layout.addWidget(self.min_y, 0, 3)
        rotate_layout.addWidget(QLabel("Min Z:"), 0, 4)
        rotate_layout.addWidget(self.min_z, 0, 5)
        # Max
        rotate_layout.addWidget(QLabel("Max X:"), 1, 0)
        rotate_layout.addWidget(self.max_x, 1, 1)
        rotate_layout.addWidget(QLabel("Max Y:"), 1, 2)
        rotate_layout.addWidget(self.max_y, 1, 3)
        rotate_layout.addWidget(QLabel("Max Z:"), 1, 4)
        rotate_layout.addWidget(self.max_z, 1, 5)
        # Ajoute dans le main layout
        self.layout.addWidget(rotate_parameters)

    ### Scale Parameters ###
    def scale_parameters(self):
        # Voir commentaires dans "animation_timing()" pour comprendre le fonctionnement
        scale_parameters = QGroupBox("Scale Parameters")
        scale_layout = QGridLayout(scale_parameters)

        # Min x
        self.min_x = QSpinBox()
        self.min_x.setRange(-10000, 10000)
        self.min_x.setValue(0)
        # Min y
        self.min_y = QSpinBox()
        self.min_y.setRange(-10000, 10000)
        self.min_y.setValue(0)
        # Min z
        self.min_z = QSpinBox()
        self.min_z.setRange(-10000, 10000)
        self.min_z.setValue(0)

        # Max x
        self.max_x = QSpinBox()
        self.max_x.setRange(-10000, 10000)
        self.max_x.setValue(0)
        # Max y
        self.max_y = QSpinBox()
        self.max_y.setRange(-10000, 10000)
        self.max_y.setValue(0)
        # Max z
        self.max_z = QSpinBox()
        self.max_z.setRange(-10000, 10000)
        self.max_z.setValue(0)

        # Min
        scale_layout.addWidget(QLabel("Min X:"), 0, 0)
        scale_layout.addWidget(self.min_x, 0, 1)
        scale_layout.addWidget(QLabel("Min Y:"), 0, 2)
        scale_layout.addWidget(self.min_y, 0, 3)
        scale_layout.addWidget(QLabel("Min Z:"), 0, 4)
        scale_layout.addWidget(self.min_z, 0, 5)
        # Max
        scale_layout.addWidget(QLabel("Max X:"), 1, 0)
        scale_layout.addWidget(self.max_x, 1, 1)
        scale_layout.addWidget(QLabel("Max Y:"), 1, 2)
        scale_layout.addWidget(self.max_y, 1, 3)
        scale_layout.addWidget(QLabel("Max Z:"), 1, 4)
        scale_layout.addWidget(self.max_z, 1, 5)
        # Ajoute dans le main layout
        self.layout.addWidget(scale_parameters)

    ### Generate Button ###
    def generate_button(self):
        self.generate = QPushButton("Generate")
        self.layout.addWidget(self.generate)
