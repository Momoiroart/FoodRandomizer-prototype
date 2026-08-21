import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from logic import FoodRecommender



class FoodApp(QWidget):
    def __init__(self):
        super().__init__()
        self.recommender = FoodRecommender('food_database.json')
        self.current_category = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("What Should I Eat? 🍜")
        self.setGeometry(100, 100, 500, 350)
        main_layout = QVBoxLayout()
        SectionLayout = QHBoxLayout()
        LeftLayout = QVBoxLayout()
        BottomLeft =QVBoxLayout()
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
        self.about_label = QLabel('About:\n"Description"')
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        self.subtitle_label.setFont(QFont("Segoe UI", 14))
        self.subtitle_label.setStyleSheet("color: #8E8E93;")
        self.category_choice = QComboBox()
        self.category_choice.addItem("All Category")
        for category in self.recommender.get_category():
            self.category_choice.addItem(category.capitalize())
        self.RightPlace = QLabel('')

        self.random_btn = QPushButton("🎲 สุ่มอาหาร!")
        self.random_btn.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.random_btn.clicked.connect(self.on_random)
    
        LeftLayout.addWidget(QLabel("เลือกหมวดหมู่:"))
        LeftLayout.addWidget(self.category_choice)
        LeftLayout.addSpacing(20)
        LeftLayout.addWidget(self.random_btn)
        LeftLayout.addStretch()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(250, 250)
        self.set_image("images/Default.jpg")
        

        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.subtitle_label)
        LeftLayout.addWidget(self.category_choice)
        RightLayout.addWidget(self.RightPlace)
        RightLayout.addWidget(self.image_label)
        BottomLeft.addWidget(self.about_label)
        LeftLayout.addLayout(BottomLeft)
        SectionLayout.addLayout(LeftLayout)
        SectionLayout.addLayout(RightLayout)
        main_layout.addLayout(SectionLayout)
        self.setLayout(main_layout)


    def set_image(self, image_path):
            """โหลดรูปจาก path และแสดงบน QLabel โดยปรับขนาดให้พอดีกรอบ"""
            if not os.path.exists(image_path):
                # ถ้าไม่มีรูป ให้แสดงข้อความแทน
                self.image_label.setText("ไม่พบรูปภาพ 📷")
                self.image_label.setPixmap(QPixmap())  # เคลียร์รูปเก่า
                return
                
            pixmap = QPixmap(image_path)
            
            # ปรับขนาดรูปให้พอดีกับ QLabel (คงสัดส่วน, ไม่เกิน 250x250)
            scaled_pixmap = pixmap.scaled(
                self.image_label.width(), 
                self.image_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            
            # แปะลง QLabel
            self.image_label.setPixmap(scaled_pixmap)
    def on_random(self):
        category = self.category_choice.currentText()
        if category == "All Category":
            category = None
        food = self.recommender.get_random_food(category)
        food_name = food["name"]
        food_image = food["image"]
        self.RightPlace.setText(f"Recoomend food: {food_name}")
        self.set_image(f"images/{food_image}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FoodApp()
    window.show()
    sys.exit(app.exec_())
