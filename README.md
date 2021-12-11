# MuscleFuck

Run this program on Raspberry Pi. I do not support other platforms.

- [Design Doc](https://esotech.notion.site/BDM-Musclefuck-0483b0cdfb0542ef92df9975ef1ec8f3)
- [Presentation](https://docs.google.com/presentation/d/1rN5PLomJHd9JZrjKUzma4-PGZXhdor9di5YT2XHEMSU/edit)

## deps

You must install them before running this program.

- [pyenv](https://pypi.org/project/poetry/)
- [poetry](https://github.com/pyenv/pyenv#automatic-installer)

## setup

Install required packages.

```bash
pyenv install
poetry install
```

## format/lint/test

Check if there is a cause of bugs.

```bash
poetry run pysen run format lint
poetry run pytest
```

## execute

Run the program. MuscleFuck interpreter will be executed and send inputs by tact buttons.

```bash
poetry run python src/main.py
```
