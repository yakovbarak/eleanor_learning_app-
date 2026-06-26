import random

import pytest

from eleanor_learning_app.games.numbers.logic import NumberGame, all_choices_in_range


def test_generated_target_is_between_1_and_10() -> None:
    game = NumberGame(rng=random.Random(1))

    for _ in range(50):
        round_ = game.new_round()
        assert 1 <= round_.target <= 10


def test_answer_choices_contain_three_unique_choices_and_target() -> None:
    game = NumberGame(rng=random.Random(2))

    round_ = game.new_round()

    assert len(round_.choices) == 3
    assert len(set(round_.choices)) == 3
    assert round_.target in round_.choices


def test_incorrect_answers_are_within_range() -> None:
    game = NumberGame(rng=random.Random(3))

    round_ = game.new_round()
    incorrect = [choice for choice in round_.choices if choice != round_.target]

    assert all_choices_in_range(incorrect)


def test_correctness_checking_works() -> None:
    game = NumberGame()

    assert game.is_correct(7, 7)
    assert not game.is_correct(3, 7)


def test_generate_choices_rejects_out_of_range_target() -> None:
    game = NumberGame()

    with pytest.raises(ValueError):
        game.generate_choices(11)
