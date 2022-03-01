from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Movie:
    id: int
    type: str
    primary_title: str
    original_title: str
    release_year: int
    runtime: Optional[int] = None
    end_year: Optional[int] = None
    genres: List[str] = field(default_factory=list)  # creaza de fiecare data o lista goala

