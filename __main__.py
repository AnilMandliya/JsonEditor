import json
import sys
from pathlib import Path
import ctypes
import platform
import asyncio
import faulthandler

from PyQt5.QtWidgets import (
    QTreeView,
    QApplication,
    QHeaderView,
    QApplication,
    QStyleFactory,
)


from PyQt5.QtCore import QCoreApplication

from controllers import MainController

from views import JsonEditorWindow
from models import JsonModel

#CONSTANTS
WINDOWS = sys.platform.startswith("win")

faulthandler.enable()



# Workaround for plot axes issue with multi-screen
def make_dpi_aware():
    if WINDOWS and int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)

if __name__ == "__main__":        
        # Multi-screen
        make_dpi_aware()

        print("[PID]:", QCoreApplication.applicationPid())
        
        app = QApplication(sys.argv)
        QApplication.setStyle(QStyleFactory.create("fusion"))
       
        json_path = Path(__file__).resolve().parents[0] /"ExampleJson.json"

        with open(json_path) as file:
            document = json.load(file)
        
        
        model = JsonModel(document)
        view = JsonEditorWindow(json_path)

        MainController(model, view)
        view.show()
        sys.exit(app.exec_())