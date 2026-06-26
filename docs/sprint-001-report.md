Sprint: 1 - Playable Numbers MVP
Branch: feature/sprint-1-numbers-mvp
Summary: Created the first playable local pygame MVP for finding numbers 1 to 10.
Implemented:
- src layout Python package
- resizable pygame app launched with python -m eleanor_learning_app
- main menu with Start button
- config-driven Hebrew/Russian language menu
- playable Find the Number game with 3 large answer buttons
- optional number sound playback with graceful missing-file fallback
- pure number game logic separated from pygame screens
- empty sound folders for Hebrew and Russian
- README setup/run/test/language instructions
Tests:
- Pure number game logic tests for target range, choices, uniqueness, range, and correctness
How to run:
- python -m pip install -e ".[dev]"
- python -m eleanor_learning_app
- pytest
Known issues:
- Sprint 1 does not include real sound files or polished visual assets.
- Pygame rendering is intentionally not heavily tested.
Questions for Architect/User:
- Should the next sprint prioritize audio recording, more visual reward feedback, or another learning area?
Suggested backlog items:
- Add recorded Hebrew and Russian number sounds.
- Add parent-only settings for language and game selection.
- Add more games using the same screen/navigation pattern.
- Add basic packaged app instructions for the family machine.
Commits:
- Add Sprint 1 playable numbers MVP
