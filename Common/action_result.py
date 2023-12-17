from dataclasses import dataclass
from typing import Optional


@dataclass
class ActionResult:
    """Base class for all backend functions. 
        
    Attributes:
        
    Success -- Indicated backend operation is successful
    ErrorMessage -- Contains error message if backend operation is unsuccessfull"""
    success: bool
    error_message: Optional[str]
