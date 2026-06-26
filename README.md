# Eleanor Learning App

A local/private Python pygame learning app for a young child. Sprint 1 is a playable "Find the Number" MVP for numbers 1 to 10.

## Install

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e ".[dev]"
```

## Run

```bash
python -m eleanor_learning_app
```

The app opens a normal resizable 1024 x 768 pygame window.

## Test

```bash
pytest
```

## Add Number Sounds

Number sounds are optional. Add `.wav` files named after each number:

```text
assets/sounds/numbers/he/1.wav
assets/sounds/numbers/he/2.wav
...
assets/sounds/numbers/he/10.wav
```

Russian sounds use:

```text
assets/sounds/numbers/ru/
```

If a sound file is missing, the app continues silently.

## Add Another Language

1. Create a new sound folder, for example `assets/sounds/numbers/en`.
2. Add a language entry to `config/languages.json`.
3. Use the new language id in `number_sound_path`.

Example:

```json
{
  "id": "en",
  "display_name": "English",
  "number_sound_path": "assets/sounds/numbers/en"
}
```

No number game code changes are needed.
