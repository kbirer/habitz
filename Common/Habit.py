from dataclasses import dataclass
from Common.Periodicity import Periodicity

@dataclass
class Habit():
    """Data class for habit information. 
        
    Attributes:
        
    Id -- Storage id of habit
    Description -- Description of habit
    Periodicity -- Periodicity of habit
    Times -- Times that the habit must be completed within a given period"""
    Id: int
    Description: str
    Periodicity: Periodicity
    Times: int
