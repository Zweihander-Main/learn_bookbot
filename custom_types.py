from typing import TypedDict

type CharDict = dict[str, int]

class CharDataForSortedList(TypedDict):
    char: str
    num: int
type CharDataSortedList = list[CharDataForSortedList]