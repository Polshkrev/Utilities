from typing import Any, Optional

import json

def make_database(file: str, data: Any, indent: Optional[int] = None) -> None:

    with open(file, "w", encoding='utf-8') as f:
        if "json" not in file:
            raise NotImplementedError()
        json.dump(data, f, indent=indent, ensure_ascii=False)