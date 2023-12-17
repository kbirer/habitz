from typing import Generic, TypeVar

T = TypeVar('T')

class MultiValueItem(Generic[T]):
    """Data class which contains key value data for end user to select through multiple choice

    Attributes:

    _id -- The generic id parameter of the selected data.
    _description -- The description to display
    """
    _id: T
    _description: str

    def __init__(self, id: T, description: str):
        """Ctor

        Parameters:

        id -- The generic id parameter of the selected data.
        description -- The description to display
        """
        self._id = id
        self._description = description
