import random

from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor, QBrush, Qt, QPen
from PySide6.QtWidgets import (
    QWidget,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsTextItem,
    QGraphicsLineItem,
    QTableWidgetItem,
)

from models import Event, EventStatus
from ui.main_page import Ui_Form


class MainPage(QWidget):
    def __init__(self, /):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(100)
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider.valueChanged.connect(self.update_observer_position)

        self.ui.start_button.clicked.connect(self.start_simulation)
        self.ui.stop_button.clicked.connect(self.stop_simulation)
        self.ui.update_button.clicked.connect(self.build_scene)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.resizeEvent = self.graphics_view_resize_event

        self.observer_line = QGraphicsLineItem(0, 0, 0, 500)
        self.observer_line.setPen(QPen(QColor(255, 0, 0), 2))

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_events)

        self.events: list[Event] = []

        self.build_scene()

    def graphics_view_resize_event(self, event):
        super().resizeEvent(event)
        self.ui.graphicsView.fitInView(
            self.scene.sceneRect(),
            Qt.AspectRatioMode.KeepAspectRatio,
        )
        view_rect = self.ui.graphicsView.mapFromScene(self.scene.sceneRect()).boundingRect()
        self.ui.horizontalSlider.setMaximumWidth(view_rect.width())

    def update_observer_position(self):
        position = self.ui.horizontalSlider.value()
        self.ui.time_label.setText(f"Время: {position}")
        self.check_events_status(position)
        self.update_observer_line(position)

    def start_simulation(self):
        self.timer.start(1000)

    def stop_simulation(self):
        self.timer.stop()

    def build_scene(self):
        self.events.clear()
        self.scene.clear()

        self.generate_processes()
        self.add_time_labels()
        self.observer_line = QGraphicsLineItem(0, 0, 0, 500)
        self.observer_line.setPen(QPen(QColor(255, 0, 0), 2))
        self.scene.addItem(self.observer_line)

        self.update_observer_position()

    def generate_processes(self):
        colors = [
            QColor("#8A2BE2"),
            QColor("#1E90FF"),
            QColor("#8B0000"),
            QColor("#228B22"),
            QColor("#FFA07A"),
        ]

        for i in range(8):
            start = random.randint(0, 50)
            end = start + random.randint(20, 50)

            rect = QGraphicsRectItem(
                start * 5,
                i * 40,
                (end - start) * 5,
                40,
            )
            rect.setBrush(QBrush(colors[i % len(colors)]))
            self.scene.addItem(rect)

            event = Event(i + 1, start, end, rect)
            self.scene.addItem(event.label)

            self.events.append(event)

        self.generate_process_relationships()

    def update_observer_line(self, position):
        x_position = position * 5
        self.observer_line.setLine(x_position, 0, x_position, 500)

    def add_time_labels(self):
        step = 10
        for i in range(0, 110, step):
            label = QGraphicsTextItem(str(i))
            label.setPos(i * 5 - step, 500)
            self.scene.addItem(label)

    def update_events(self):
        self.ui.horizontalSlider.setValue(
            (self.ui.horizontalSlider.value() + 1) % 101,
        )

    def check_events_status(self, position):
        for event in self.events:
            if position < event.start:
                status = EventStatus.NOT_STARTED
            elif event.start <= position <= event.end:
                status = EventStatus.IN_PROGRESS
            else:
                status = EventStatus.COMPLETED
            event.set_status(status)
            event.rect.setOpacity(1.0 if event.status == EventStatus.IN_PROGRESS else 0.5)

    def generate_process_relationships(self):
        self.ui.relationships_table.setColumnCount(len(self.events))
        self.ui.relationships_table.setRowCount(len(self.events))

        column_count = self.ui.relationships_table.columnCount()
        for col in range(column_count):
            self.ui.relationships_table.setColumnWidth(col, 50)

        event_names = [str(event.number) for event in self.events]
        self.ui.relationships_table.setHorizontalHeaderLabels(event_names)
        self.ui.relationships_table.setVerticalHeaderLabels(event_names)

        for i, eventi in enumerate(self.events):
            for j, eventj in enumerate(self.events):
                if i != j:
                    relationship = eventi.get_relationship(eventj)
                    self.ui.relationships_table.setItem(i, j, QTableWidgetItem(relationship))
                    self.ui.relationships_table.setItem(j, i, QTableWidgetItem(relationship))
