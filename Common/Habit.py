from dataclasses import dataclass
from Common.Periodicity import Periodicity

@dataclass
class Habit():
    Id: int
    Description: str
    Periodicity: Periodicity
    Times: int
