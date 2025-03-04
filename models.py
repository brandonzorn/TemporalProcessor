from enum import Enum

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem


class EventStatus(Enum):
    NOT_STARTED = "Не началось"
    IN_PROGRESS = "Идет"
    COMPLETED = "Завершено"


class Event:
    def __init__(self, number: int, start: int, end: int, rect: QGraphicsRectItem):
        self.number = number
        self.start = start
        self.end = end
        self.rect = rect

        self.status: EventStatus = EventStatus.NOT_STARTED

        self.label = QGraphicsTextItem(f"{self.get_name()} {self.status.value}")
        self.label.setPos(
            start * 5 + (end - start) * 5 / 2 - self.label.boundingRect().width() / 2, (number - 1) * 40 + 10,
        )
        self.label.setDefaultTextColor(Qt.GlobalColor.white)

    def set_status(self, status: EventStatus):
        self.status = status
        self.label.setPlainText(f"{self.get_name()} {self.status.value}")

    def get_name(self):
        return f"Событие: {self.number}"

    def get_relationship(self, other):
        if self.end <= other.start:
            return "rts1"  # Процесс 1 заканчивается до начала процесса 2 (с паузой)
        elif other.end <= self.start:
            return "rts2"  # Процесс 2 заканчивается до начала процесса 1 (с паузой)
        elif self.end == other.start:
            return "rtsn1"  # Процесс 1 заканчивается в момент начала процесса 2 (без паузы)
        elif other.end == self.start:
            return "rtsn2"  # Процесс 2 заканчивается в момент начала процесса 1 (без паузы)
        elif self.start == other.start and self.end <= other.end:
            return "rtel1"  # Процесс 1 вложен в процесс 2 и примыкает к его началу
        elif other.start == self.start and other.end <= self.end:
            return "rtel2"  # Процесс 2 вложен в процесс 1 и примыкает к его началу
        elif self.start >= other.start and self.end == other.end:
            return "rter1"  # Процесс 1 вложен в процесс 2 и примыкает к его концу
        elif other.start >= self.start and other.end == self.end:
            return "rter2"  # Процесс 2 вложен в процесс 1 и примыкает к его концу
        elif self.start > other.start and self.end < other.end:
            return "rte1"  # Процесс 1 вложен в процесс 2 без примыкания
        elif other.start > self.start and other.end < self.end:
            return "rte2"  # Процесс 2 вложен в процесс 1 без примыкания
        elif self.start < other.end and other.start < self.end:
            return "rtes"  # Процессы пересекаются
        else:
            return "Не определено"
