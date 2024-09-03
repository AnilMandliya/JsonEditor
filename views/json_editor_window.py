from pathlib import Path
import os
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QTreeView,
    QDialog,
    QHBoxLayout,
    QHeaderView
)

class JsonEditorWindow(QDialog):
    
    def __init__(self, config):
        QDialog.__init__(self)
        
        self.configType = "_".join(os.path.splitext(os.path.basename(str(config)))[0].split("_")[:2])
        self.setWindowTitle("JSON Editor")
    
        # Create the Widgets for JSON Editor window
        self.tree_view = QTreeView()
        self.saveJsonBtn = QPushButton("Save")
        self.cancelJsonBtn = QPushButton("Cancel")

        

        # Create a layout and set the QTreeView as its widget
        self.layout = QVBoxLayout()
        
        self.vLayout1 = QVBoxLayout()
        self.vLayout1.addWidget(self.tree_view)
        
        self.layout.addLayout(self.vLayout1)
        
        
        
        self.hLayout1 =  QHBoxLayout()
        self.hLayout1.addWidget(self.saveJsonBtn)
        self.hLayout1.addWidget(self.cancelJsonBtn)
        
        self.layout.addLayout(self.hLayout1)
        
        self.setLayout(self.layout)

        
        self.resize(600, 500)

    def updateJsonView(self):
        # Customize the window size and other properties as needed
        self.tree_view.setAlternatingRowColors(True)
        self.tree_view.header().setSectionResizeMode(0, QHeaderView.Stretch)
    
    def updateConfigType(self, configType):
        self.configType =configType
