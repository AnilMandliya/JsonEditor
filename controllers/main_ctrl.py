import json
from pathlib import Path
import sys
import os

from PyQt5.QtCore import (
    QObject,
    Qt
)



class MainController(QObject):

    def __init__(self, model, view, *args, **kwargs):
        super(MainController, self).__init__(*args, **kwargs)
        self._model = model
        self._view = view
        pass

        self._connectJsonSignalsAndSlots()

        # Create model
        try:
            # Set model view
            self._view.tree_view.setModel(self._model)
            self._view.updateJsonView()
        except Exception as e:
            print(e)


    def _connectJsonSignalsAndSlots(self):
        # Connect Signals and slots for JSON Editor Window
        self._view.saveJsonBtn.clicked.connect(
            lambda: self.saveJson())
        self._view.cancelJsonBtn.clicked.connect(
            lambda: sys.exit(0))
    
    def saveJson(self):
        try:
            newData = self._model.to_json()
            configFileName = self._view.configType + ".json"
            newPath = Path(__file__).resolve(
            ).parents[1] / "temp" / configFileName
            os.makedirs(Path(__file__).resolve().parents[1] / "temp", exist_ok=True )
            
            with open(newPath, 'w') as fp:
                json.dump(newData, fp, indent=4)

            print(f'Saved Config at {newPath}')

        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")

        finally:
            sys.exit(0)