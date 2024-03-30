from dataclasses import dataclass
from typing import List
import os

@dataclass
class TranscriptionTask:
    folder: str
    file: str
    speaker: str
    model: str

    def validate_paths(self):
        if not os.path.isdir(self.folder):
            raise ValueError(f"Folder does not exist: {self.folder}")
        full_path: str = os.path.join(self.folder, self.file)
        if not os.path.isfile(full_path):
            raise FileNotFoundError(f"File does not exist: {full_path}")


@dataclass
class TranslationRequest:
    tasks: List[TranscriptionTask]
