from typing import Generic, TypeVar

T = TypeVar('T')

class MultiValueItem(Generic[T]):
    id: T
    description: str

    def __init__(self, id: T, description: str):
        self.id = id
        self.description = description
