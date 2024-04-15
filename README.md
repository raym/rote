# rote

Use the commands below to setup and run `rote` for the first time (and get back to your original shell). This does assume you have `nix` installed on your machine. `nix` is a [single command install](https://nixos.org/download/) and it's non-invasive to your environment. Give it a try or read up on `nix` if you haven't!

```
nix-shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python rote.py
deactivate
<Ctrl+D>
```

And after you've setup the first time with the above commands, you'll only need the subset below to run `rote` again (and get back to your original shell).

```
nix-shell
source venv/bin/activate
python rote.py
deactivate
<Ctrl+D>
```

There are a few sample flashcard decks in this repository, for now:
- `./decks/git`
- `./decks/python-cli`
- `./decks/python-language`

However, I believe it's more helpful for each individual to create and curate their own decks. I plan to curate the sample decks some more and then add the `decks` directory to `.gitignore`. Until then, `my_decks` is present in `.gitignore`, so that is available for each individual's decks.

You can specify a deck at the terminal. If left unspecified, it will default to `./decks/git`.

```
python rote.py ./decks/python-cli
```

To add your own flashcard decks, create a directory with one or more `.yaml` files in them, where the YAML is a top-level array of objects with keys `front` and `back`, like so:

```yaml
# ./decks/example/fox.yaml
-
  front: what is the only thing with which one can see rightly?
  back: the heart
-
  front: what is invisible to the eye?
  back: the essential
```
```yaml
# ./decks/example/md5-cli.yaml
-
  front: get the md5 hash of the string "wonder" using the here-string operator
  back: md5sum <<< "wonder"
```

Then specify the deck directory and all flashcards found in all `.yaml` files will be shuffled and, one by one, presented at the terminal:

```
python rote.py ./decks/example/
```

To continue, the user must type the value of the flashcard's `back` verbatim.
