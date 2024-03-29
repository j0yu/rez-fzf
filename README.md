# fzf

[![CI](../..//workflows/CI/badge.svg?branch=main)](../../actions?query=workflow:CI+branch:main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


[rez] package to install [fzf].

Here are some beginners instructions on how to use this repository.

## Installation

1. Install [rez] via `python install.py` method
1. Clone/download this repository
1. Ensure the folder printed by this command exists `rez config local_packages_path`
1. Open terminal in (extracted) repository folder, run `rez build --install`

fzf should now be installed as a [rez] package named `fzf`.

## Usage

To run [fzf]: `rez env fzf -- fzf`

## Maintenance

Whenever new official release come out, update the `__version__`
in `package.py` then re-run `rez build --install`.

If you decide to make another install, e.g. new `commands()` environment
setup, you can instead just update the `+local.` version number to indicate
new releases/versions of your own. See [PEP 540 local version segments].

Also, you can rename `+local.` to something more relevant to you
e.g. `+mystudio.` or  `+mygithubname.`

----

Want more rez packages? Checkout [my GitHub repositories][j0yu-rez-packages]

[rez]: https://github.com/nerdvegas/rez
[requirement]: https://github.com/nerdvegas/rez/wiki/Package-Definition-Guide#requires
[j0yu-rez-packages]: https://github.com/j0yu?tab=repositories&q=topic:rez+topic:package
[fzf]: https://github.com/junegunn/fzf
[PEP 540 local version segments]: https://www.python.org/dev/peps/pep-0440/#local-version-segments
