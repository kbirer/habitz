from dataclasses import dataclass
from typing import Optional


@dataclass
class ActionResult:
    Success: bool
    ErrorMessage: Optional[str]
