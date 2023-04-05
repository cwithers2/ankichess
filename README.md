# Anki Chess
Generate Anki packages from chess PGN files.

## What is Anki?
Anki is a free flashcard program. It uses a spaced repitition system (SRS) to improve flashcard memorization. Similar flashcards are stored in a 'deck', and one or more decks are stored in a 'package'.

This program successfully creates a package containing one deck where each flashcard represents a move in a game of chess. It does so by reading an inputted PGN file...

## What is a PGN file?
To start generating packages, all that is needed is a portable game notation (PGN) file. A PGN file a plain-text file-type with a well defined format used to notate chess games.

Many chess websites include options to export specific games as a PGN file. Additionally, many sites offer analysis boards, where games can be constructed to study one or more move variations. This is typically helpful when studying different openings and how to respond to different moves. The PGN file format also supports these variations. The generated PGN for those games will encode a branching heirarchy of all the moves studied. The PGN file format is created from plain-text, so it's easy to create or edit by hand if ever needed, too.

NOTE: Its also worth mentioning that a PGN file can contain more than a single game.

### Example PGN Files
Three PGN files are included in `pgn/`. They include _The Opera Game_, _Fool's Mate_ and _Scholar's Mate_, and an _Italian Game_. These files are intended for testing purposes.

For more information about PGN files, visit this [wikipedia page](https://en.wikipedia.org/wiki/Portable_Game_Notation).

## More about this program
`ankichess.py` is the single program file in this project. It is written in Python 3 and is called from the commandline. It generates a package containing one deck. The deck represents an inputted PGN file. There are many commandline options to modify how the deck is generated. For example, there is an option to generate flashcards in 'blindfold' mode. In this mode, no pictures are generated, only text describing the moves.

#### Visual Example
<figure>
  <img src="https://i.imgur.com/IOUd5Cq.png" alt="Visual Example" width=500/>
  <figcaption>Left: Question/Front of card, Right: Answer/Back of card</figcaption>
</figure>

#### Blindfold Example
<figure>
  <img src="https://i.imgur.com/IPKAPQC.png" alt="Blindfold Example" width=500/>
  <figcaption>Left: Question/Front of card, Right: Answer/Back of card</br><i>Note: Generated text is PGN format</i></figcaption>
</figure>

### Usage
`ankichess.py [-h] [--mainline] [--blindfold] [--game NUM] PGN_FILE OUT_FILE TITLE`

| argument      | positional | optional | description                                                               |
|---------------|:----------:|:--------:|---------------------------------------------------------------------------|
| `PGN_FILE`    | x          |          | A PGN file to generate an Anki package from                               |
| `OUT_FILE`    | x          |          | The file name of the Anki package to generate (typically ending in .apkg) |
| `TITLE`       | x          |          | The title to give the generated deck as seen in the Anki GUI              |
| `--mainline`  |            | x        | Only generate cards for the mainline moves                                |
| `--blindfold` |            | x        | Generate text notation only, no images (Implies --mainline)               |
| `--game NUM`  |            | x        | Select the Nth game from the PGN file (Default is 1)                      |
| `--flip`      |            | x        | Generate images from black's perspective (Does nothing if --blindfold)    |

example: `ankichess.py pgn/opera_game.pgn opera_game.apkg "The Opera Game"`

Generated packages can be imported into the desktop version of Anki using the _Import File_ GUI.

### Install
Currently there is no install tool. You can manually add `ankichess.py` to your path or call it from its project directory.

#### Installing Dependencies
- `pip3 install genanki`
- `pip3 install chess`
