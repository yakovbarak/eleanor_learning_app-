from __future__ import annotations

from dataclasses import dataclass
import random
from collections.abc import Sequence
from typing import cast


@dataclass(frozen=True)
class NumberRound:
    target: int
    choices: tuple[int, int, int]


class NumberGame:
    def __init__(
        self,
        minimum: int = 1,
        maximum: int = 10,
        choice_count: int = 3,
        rng: random.Random | None = None,
    ) -> None:
        if minimum >= maximum:
            raise ValueError("minimum must be less than maximum")
        if choice_count < 2:
            raise ValueError("choice_count must be at least 2")
        if maximum - minimum + 1 < choice_count:
            raise ValueError("number range must contain enough unique choices")

        self.minimum = minimum
        self.maximum = maximum
        self.choice_count = choice_count
        self._rng = rng or random.Random()

    def new_round(self) -> NumberRound:
        target = self._rng.randint(self.minimum, self.maximum)
        choices = self.generate_choices(target)
        return NumberRound(target=target, choices=choices)

    def generate_choices(self, target: int) -> tuple[int, int, int]:
        self._validate_number(target)
        incorrect_pool = [
            number
            for number in range(self.minimum, self.maximum + 1)
            if number != target
        ]
        incorrect = self._rng.sample(incorrect_pool, self.choice_count - 1)
        choices: list[int] = [target, *incorrect]
        self._rng.shuffle(choices)
        return cast(tuple[int, int, int], tuple(choices))

    def is_correct(self, answer: int, target: int) -> bool:
        self._validate_number(target)
        return answer == target

    def _validate_number(self, number: int) -> None:
        if number < self.minimum or number > self.maximum:
            raise ValueError(f"number must be between {self.minimum} and {self.maximum}")


def all_choices_in_range(choices: Sequence[int], minimum: int = 1, maximum: int = 10) -> bool:
    return all(minimum <= choice <= maximum for choice in choices)
