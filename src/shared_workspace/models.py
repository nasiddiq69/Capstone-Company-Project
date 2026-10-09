"""Basic data models for the Shared Workspace System."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Reservation:
    """A reservation for a workspace over a half-open time interval."""

    workspace_id: str
    user_id: str
    start: datetime
    end: datetime

    def __post_init__(self) -> None:
        if not self.workspace_id.strip():
            raise ValueError("workspace_id must not be empty")
        if not self.user_id.strip():
            raise ValueError("user_id must not be empty")
        if self.start >= self.end:
            raise ValueError("Reservation start must be earlier than end")
        if self.start.tzinfo != self.end.tzinfo:
            raise ValueError("start and end must use compatible timezone information")
