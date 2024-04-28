# INSAlgo 2024 Code Golf Contest

My different solutions for [INSAlgo 2024 Code Golf Contest](https://github.com/INSAlgo/Code-Golf-2024).

## 05AB1E

I mostly used [05AB1E](https://github.com/Adriandmen/05AB1E) golfing language with the legacy [python version](https://github.com/Adriandmen/05AB1E/tree/fb4a2ce2bce6660e1a680a74dd61b72c945e6c3b).

For the 05AB1E solutions :

- `[DAY].abe` is the base code.

- `[DAY]_commented.abe` is the commented version.

- `[DAY].05AB1E` is the submitted code.

    It is encoded in [`osabie encoding`](https://github.com/Adriandmen/05AB1E/blob/fb4a2ce2bce6660e1a680a74dd61b72c945e6c3b/docs/code-page.md) to reduce file size.
    
    Encoded from `[DAY].abe` using [osabie-encode](./nix/05AB1E-encode/osabie-encode.py).
    
    Needs osabie `-c` flag to run.

## Flake

The flake provides a nix shell with the dependencies needed to run the different programs :

- python3: for python solutions.

- [osabie](./nix/05AB1E/default.nix) : 05AB1E interpreter.

- [osabie-encode](./nix/05AB1E-encode/default.nix) : wrapper for [osabie-encode.py](./nix/05AB1E-encode/osabie-encode.py).
