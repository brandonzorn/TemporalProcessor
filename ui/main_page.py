# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDockWidget,
    QFrame, QGraphicsView, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(724, 593)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_button = QPushButton(Form)
        self.start_button.setObjectName(u"start_button")

        self.verticalLayout.addWidget(self.start_button)

        self.stop_button = QPushButton(Form)
        self.stop_button.setObjectName(u"stop_button")

        self.verticalLayout.addWidget(self.stop_button)

        self.update_button = QPushButton(Form)
        self.update_button.setObjectName(u"update_button")

        self.verticalLayout.addWidget(self.update_button)

        self.time_label = QLabel(Form)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.time_label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setFrameShape(QFrame.Shape.NoFrame)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsView.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.graphicsView.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dockWidget = QDockWidget(Form)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.relationships_table = QTableWidget(self.dockWidgetContents)
        self.relationships_table.setObjectName(u"relationships_table")
        self.relationships_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_4.addWidget(self.relationships_table)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.verticalLayout_3.addWidget(self.dockWidget)

        self.dockWidget_2 = QDockWidget(Form)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidget_2.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textBrowser = QTextBrowser(self.dockWidgetContents_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_5.addWidget(self.textBrowser)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)

        self.verticalLayout_3.addWidget(self.dockWidget_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.start_button.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.stop_button.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u043f", None))
        self.update_button.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.time_label.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f: 0", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("Form", u"\u0422\u0435\u043c\u043f\u043e\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f", None))
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("Form", u"\u0422\u0438\u043f\u044b \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0439", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rts1</span> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441 1 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0434\u043e \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430 2 (\u0441 \u043f\u0430\u0443\u0437\u043e\u0439)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rts2</span> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441 2 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0434\u043e \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430 1 (\u0441 \u043f\u0430\u0443\u0437\u043e\u0439)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rtsn1</span> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441 1 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0432 \u043c\u043e\u043c\u0435\u043d\u0442 \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430 2 (\u0431\u0435\u0437 \u043f\u0430\u0443\u0437\u044b)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rtsn2</span> "
                        "- \u041f\u0440\u043e\u0446\u0435\u0441\u0441 2 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0432 \u043c\u043e\u043c\u0435\u043d\u0442 \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430 1 (\u0431\u0435\u0437 \u043f\u0430\u0443\u0437\u044b)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rtel1</span> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441 1 \u0432\u043b\u043e\u0436\u0435\u043d \u0432 \u043f\u0440\u043e\u0446\u0435\u0441\u0441 2 \u0438 \u043f\u0440\u0438\u043c\u044b\u043a\u0430\u0435\u0442 \u043a \u0435\u0433\u043e \u043d\u0430\u0447\u0430\u043b\u0443</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rtel2</span> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441 2 \u0432\u043b\u043e\u0436\u0435\u043d \u0432 \u043f\u0440"
                        "\u043e\u0446\u0435\u0441\u0441 1 \u0438 \u043f\u0440\u0438\u043c\u044b\u043a\u0430\u0435\u0442 \u043a \u0435\u0433\u043e \u043d\u0430\u0447\u0430\u043b\u0443</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rter1</span> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441 1 \u0432\u043b\u043e\u0436\u0435\u043d \u0432 \u043f\u0440\u043e\u0446\u0435\u0441\u0441 2 \u0438 \u043f\u0440\u0438\u043c\u044b\u043a\u0430\u0435\u0442 \u043a \u0435\u0433\u043e \u043a\u043e\u043d\u0446\u0443</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rter2</span> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441 2 \u0432\u043b\u043e\u0436\u0435\u043d \u0432 \u043f\u0440\u043e\u0446\u0435\u0441\u0441 1 \u0438 \u043f\u0440\u0438\u043c\u044b\u043a\u0430\u0435\u0442 \u043a \u0435\u0433\u043e \u043a\u043e\u043d\u0446\u0443</p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rte1</span> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441 1 \u0432\u043b\u043e\u0436\u0435\u043d \u0432 \u043f\u0440\u043e\u0446\u0435\u0441\u0441 2 \u0431\u0435\u0437 \u043f\u0440\u0438\u043c\u044b\u043a\u0430\u043d\u0438\u044f</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rte2</span> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441 2 \u0432\u043b\u043e\u0436\u0435\u043d \u0432 \u043f\u0440\u043e\u0446\u0435\u0441\u0441 1 \u0431\u0435\u0437 \u043f\u0440\u0438\u043c\u044b\u043a\u0430\u043d\u0438\u044f</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">rtes</span> - \u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b \u043f\u0435\u0440\u0435\u0441"
                        "\u0435\u043a\u0430\u044e\u0442\u0441\u044f</p></body></html>", None))
    # retranslateUi

