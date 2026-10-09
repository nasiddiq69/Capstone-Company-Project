"""Tests for basic reservation conflict detection."""

import unittest
from datetime import datetime

from shared_workspace.models import Reservation
from shared_workspace.reservation_service import (
    ReservationConflictError,
    ReservationService,
)


def dt(hour: int, minute: int = 0) -> datetime:
    return datetime(2026, 10, 10, hour, minute)


class ReservationServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.service = ReservationService()

    def test_accepts_first_reservation(self) -> None:
        booking = Reservation("room-a", "user-1", dt(9), dt(10))
        self.service.create_reservation(booking)
        self.assertEqual(self.service.list_reservations(), [booking])

    def test_rejects_overlapping_reservation_for_same_workspace(self) -> None:
        self.service.create_reservation(Reservation("room-a", "user-1", dt(9), dt(10)))
        overlapping = Reservation("room-a", "user-2", dt(9, 30), dt(10, 30))
        with self.assertRaises(ReservationConflictError):
            self.service.create_reservation(overlapping)

    def test_allows_back_to_back_reservations(self) -> None:
        self.service.create_reservation(Reservation("room-a", "user-1", dt(9), dt(10)))
        next_booking = Reservation("room-a", "user-2", dt(10), dt(11))
        self.service.create_reservation(next_booking)
        self.assertEqual(len(self.service.list_reservations()), 2)

    def test_allows_same_time_for_different_workspaces(self) -> None:
        self.service.create_reservation(Reservation("room-a", "user-1", dt(9), dt(10)))
        other_room = Reservation("room-b", "user-2", dt(9), dt(10))
        self.service.create_reservation(other_room)
        self.assertEqual(len(self.service.list_reservations()), 2)

    def test_rejects_invalid_time_range(self) -> None:
        with self.assertRaises(ValueError):
            Reservation("room-a", "user-1", dt(10), dt(9))


if __name__ == "__main__":
    unittest.main()
