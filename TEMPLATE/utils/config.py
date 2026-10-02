from typing import Any

class Config:
    def __init__(self, file_path: Optional[str] = None) -> None:
        if file_path is not None: 
            settings = self.load_config(file_path)
        else: 
            settings = {}
        ...

    def load_config(self, file_path: str) -> dict[str, Any]:
        raise NotImplementedError