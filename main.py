import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from logic import FoodRecommender



class FoodApp(QWidget):
    def __init__(self):
        super().__init__()
        self.recommender = FoodRecommender()
        self.current_category = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("What Should I Eat? 🍜")
        self.setGeometry(100, 100, 500, 350)
        main_layout = QVBoxLayout()
        SectionLayout = QHBoxLayout()
        LeftLayout = QVBoxLayout()
        RightLayout= QVBoxLayout()
        main_layout.setContentsMargins(50, 40, 50, 40)
        main_layout.setSpacing(25)
        self.title_label = QLabel("Random Meal Picker")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Segoe UI", 36, QFont.Bold))
        self.title_label.setStyleSheet("color: #1C1C1E;")

        self.subtitle_label = QLabel("can't decide what to eat?")
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        self.subtitle_label.setFont(QFont("Segoe UI", 14))
        self.subtitle_label.setStyleSheet("color: #8E8E93;")






        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.subtitle_label)
        SectionLayout.addLayout(LeftLayout)
        SectionLayout.addLayout(RightLayout)
        main_layout.addLayout(SectionLayout)
        self.setLayout(main_layout)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FoodApp()
    window.show()
    sys.exit(app.exec_())