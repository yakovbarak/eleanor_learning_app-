# Sprint 001 Architect Report

## Sprint

Sprint 1 - Playable Numbers MVP

## Branch

`feature/sprint-1-numbers-mvp`

## Purpose

Create the first playable local/private Python pygame MVP for teaching numbers 1 to 10 to a 3-year-old child.

## Implementation Summary

Sprint 1 introduced a small `src/` layout pygame application with:

- `python -m eleanor_learning_app` startup through `__main__.py`
- resizable 1024 x 768 pygame window
- colorful main menu with a large `Start` button
- language selection loaded from `config/languages.json`
- initial Hebrew and Russian language entries
- playable "Find the Number" game for digits 1 to 10
- 3 large answer buttons per round
- correct-answer cheerful feedback with short automatic advance
- incorrect-answer retry feedback without punishment
- optional `.wav` number sound playback with missing-file fallback
- empty sound directories for Hebrew and Russian
- pure number-game logic separated from pygame rendering

## Architecture

The implementation follows the requested simple architecture:

- `src/eleanor_learning_app/app.py` owns pygame initialization, the window, the main loop, and screen transitions.
- `src/eleanor_learning_app/screens/` owns pygame drawing and click handling.
- `src/eleanor_learning_app/games/numbers/logic.py` owns pure number-game rules and is testable without pygame.
- `src/eleanor_learning_app/config.py` loads language definitions from JSON.
- `src/eleanor_learning_app/assets.py` resolves and plays optional sounds safely.

Language additions should require:

1. Adding a sound folder under `assets/sounds/numbers/<language_id>`.
2. Adding a language entry to `config/languages.json`.
3. No game-code changes.

## Verification

Commands run:

```bash
pytest
python -m compileall src tests
```

Result:

- `pytest`: 5 tests passed
- `compileall`: succeeded

Coverage focus:

- target number stays within 1 to 10
- answer choices contain exactly 3 values
- answer choices include the correct answer
- answer choices are unique
- incorrect choices stay within range
- correctness checking works

Pygame rendering was not heavily tested in Sprint 1, per sprint constraints.

## Known Limitations

- No real Hebrew or Russian sound files are included.
- Visual design uses simple pygame shapes, colors, and text only.
- No packaged executable or installer exists yet.
- No parent settings, progress tracking, or child profile exists yet.
- No automated UI test opens the pygame window.

## Architect Review Notes

Please review:

- Whether the screen-transition approach is sufficient for Sprint 2 scale.
- Whether `Language.number_sound_path` should stay as a filesystem path or become an asset id if packaging is planned soon.
- Whether number game configuration should remain fixed in code for now or move to config in a future sprint.
- Whether the app should introduce a shared base screen protocol/interface before adding more games.

## Suggested Next Sprint Options

- Add real number sounds for Hebrew and Russian.
- Add richer correct-answer visual reward feedback.
- Add a parent-facing language/game selection guard.
- Add another learning mode, such as Hebrew letters.
- Add a simple app packaging plan for the target family computer.

## Commit

`3341465 Add Sprint 1 playable numbers MVP`
