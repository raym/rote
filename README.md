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
