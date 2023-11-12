from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class CheckedOutHabit():
    HabitId: int
    HabitDescription:Optional[str]
    CreationDate: datetime
