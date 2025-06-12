import sys
import json
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt

PERSISTENCE_FILE = 'app_state.json'

class McuClientUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('McuClientUI')
        self.resize(800, 600)
        self.state = {
            'current_position': '0,0,0',
            'coordinate_mode': 'absolute',
            'current_gcode_line': 0,
            'gcode_lines': []
        }
        self.load_state()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        # UART config and position
        info_layout = QHBoxLayout()
        self.uart_label = QLabel('UART: /dev/ttyUSB0, 115200')
        self.position_label = QLabel(f'Position: {self.state["current_position"]}')
        info_layout.addWidget(self.uart_label)
        info_layout.addWidget(self.position_label)
        layout.addLayout(info_layout)
        # G-Code list
        self.gcode_list = QListWidget()
        for line in self.state['gcode_lines']:
            self.gcode_list.addItem(line)
        self.gcode_list.setCurrentRow(self.state['current_gcode_line'])
        layout.addWidget(self.gcode_list)
        # Text box for G-Code input
        self.gcode_text = QTextEdit()
        self.gcode_text.setPlaceholderText('Enter G-Code commands here...')
        self.gcode_text.setPlainText('\n'.join(self.state['gcode_lines']))
        layout.addWidget(self.gcode_text)
        # Buttons
        btn_layout = QHBoxLayout()
        self.play_btn = QPushButton('Play')
        self.pause_btn = QPushButton('Pause')
        self.stop_btn = QPushButton('Stop')
        btn_layout.addWidget(self.play_btn)
        btn_layout.addWidget(self.pause_btn)
        btn_layout.addWidget(self.stop_btn)
        layout.addLayout(btn_layout)
        self.setLayout(layout)
        # Connect signals
        self.play_btn.clicked.connect(self.on_play)
        self.pause_btn.clicked.connect(self.on_pause)
        self.stop_btn.clicked.connect(self.on_stop)

    def on_play(self):
        # Placeholder for play logic
        self.save_state()

    def on_pause(self):
        # Placeholder for pause logic
        self.save_state()

    def on_stop(self):
        # Placeholder for stop logic
        self.save_state()

    def save_state(self):
        self.state['gcode_lines'] = self.gcode_text.toPlainText().splitlines()
        self.state['current_gcode_line'] = self.gcode_list.currentRow()
        with open(PERSISTENCE_FILE, 'w') as f:
            json.dump(self.state, f)

    def load_state(self):
        if os.path.exists(PERSISTENCE_FILE):
            with open(PERSISTENCE_FILE, 'r') as f:
                self.state = json.load(f)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = McuClientUI()
    window.show()
    sys.exit(app.exec_())
