from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QPushButton

app = QApplication([])

# Create a main window
main_window = QMainWindow()

# Create a scroll area and set its widget to a QWidget
scroll_area = QScrollArea()
widget = QWidget()
scroll_area.setWidgetResizable(True)
scroll_area.setWidget(widget)

# Create a QVBoxLayout for the QWidget
layout = QVBoxLayout(widget)
layout.setSpacing(0)

# Add some widgets to the QVBoxLayout
for i in range(10):
    button = QPushButton(f"Button {i}")
    layout.addWidget(button)

# Set the main window's central widget to the scroll area
main_window.setCentralWidget(scroll_area)

# Show the main window
main_window.show()

app.exec_()

