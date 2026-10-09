"""Reservation rules. This starter version stores reservations in memory."""

from shared_workspace.models import Reservation


class ReservationConflictError(ValueError):
    """Raised when a reservation overlaps an existing booking."""


def overlaps(first: Reservation, second: Reservation) -> bool:
    """Return True when two half-open intervals overlap."""
    return (
        first.workspace_id == second.workspace_id
        and first.start < second.end
        and second.start < first.end
    )


class ReservationService:
    """Small in-memory service to demonstrate conflict detection."""

    def __init__(self) -> None:
        self._reservations: list[Reservation] = []

    def list_reservations(self) -> list[Reservation]:
        return list(self._reservations)

    def create_reservation(self, reservation: Reservation) -> Reservation:
        if any(overlaps(existing, reservation) for existing in self._reservations):
            raise ReservationConflictError(
                "This workspace already has a reservation during that time."
            )
        self._reservations.append(reservation)
        return reservation
