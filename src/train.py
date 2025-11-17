"""Train class for managing train routes and pricing."""

from decimal import Decimal

from src.pricing_strategies import PricingStrategy
from src.types import CoachType, TicketType


class Train:
    def __init__(
        self,
        train_number: str,
        stations: list[str],
        pricing_strategy: PricingStrategy,
    ):
        self.train_number = train_number
        self.stations = stations                # FIX
        self.pricing_strategy = pricing_strategy

    def calculate_ticket_price(
        self,
        ticket_type: TicketType,
        coach_type: CoachType,
        number_of_passengers: int,
        from_station: str,
        to_station: str,
    ) -> Decimal:
        """
        Calculate ticket price for this train.
        """

        # --- VALIDATION ---
        if from_station not in self.stations:
            raise ValueError(f"Station not found in route: {from_station}")
        if to_station not in self.stations:
            raise ValueError(f"Station not found in route: {to_station}")
        if from_station == to_station:
            raise ValueError("From and To stations cannot be the same")

        # --- PRICE CALCULATION USING STRATEGY ---
        return self.pricing_strategy.calculate_price(
            ticket_type=ticket_type,
            coach_type=coach_type,
            number_of_passengers=number_of_passengers,
            from_station=from_station,
            to_station=to_station,
            stations=self.stations,   # FIX — must pass stations list
        )
