# Stubs for xlwt.Column (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Column:
    width: int = ...
    hidden: int = ...
    level: int = ...
    collapse: int = ...
    user_set: int = ...
    best_fit: int = ...
    unused: int = ...
    def __init__(self, colx: Any, parent_sheet: Any) -> None: ...
    def set_width(self, width: Any) -> None: ...
    def get_width(self): ...
    def set_style(self, style: Any) -> None: ...
    def width_in_pixels(self): ...
    def get_biff_record(self): ...