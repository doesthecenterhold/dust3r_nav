import numpy as np
from pathlib import Path
import json
import os

class DroneLoc:
    def __init__(self, dataset_path):

        self.path = Path(dataset_path)
        dataset_name = self.path.name

        self.images_path = self.path / "footage"
        self.anno_path = self.path / dataset_name

    def load_images():
        pass

if __name__ == "__main__":
    pass

