# Anki Chess
Generate Anki packages from chess PGN files using the `genanki` and `chess` modules.

`ankichess.py` is the single program file in this project. It is written in Python 3 and is called from the commandline.

#### Visual Example
<img src="https://i.imgur.com/IOUd5Cq.png" alt="Visual Example" width=500/>

#### Blindfold Example
<img src="https://i.imgur.com/IPKAPQC.png" alt="Blindfold Example" width=500/>

## Install
Currently there is no install tool. You can manually add `ankichess.py` to your path or call it from its project directory.

### Installing Dependencies
- `pip3 install genanki`
- `pip3 install chess`

## Usage
`ankichess.py [-h] [--mainline] [--blindfold] [--game NUM] PGN_FILE OUT_FILE TITLE`

| argument      | positional | optional | description                                                               |
|---------------|:----------:|:--------:|---------------------------------------------------------------------------|
| `PGN_FILE`    | x          |          | A PGN file to generate an Anki package from (mainline only)               |
| `OUT_FILE`    | x          |          | The file name of the Anki package to generate (typically ending in .apkg) |
| `TITLE`       | x          |          | The title to give the generated deck as seen in the Anki GUI              |
| `--mainline`  |            | x        | Only generate cards for the mainline moves                                |
| `--blindfold` |            | x        | Generate text notation only, no images (Implies --mainline)               |
| `--game NUM`  |            | x        | Select the Nth game from the PGN file (Default is 1)                      |

example: `ankichess.py pgn/opera_game.pgn opera_game.apkg "The Opera Game"`

Generated packages can be imported into the desktop version of Anki using the _Import File_ GUI.

## Example PGN Files
Three PGN files are included in `pgn/`. They include _The Opera Game_, _Fool's Mate_ and _Scholar's Mate_, and an _Italian Game_. These files are intended for testing purposes.
