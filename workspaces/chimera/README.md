# Chimera workspace

These scripts are meant to be run in a chimera linux container, or a real host of the same

* `get.sh` dumps a list of all packages ending in '-man' to pkgs.list
* `fetch.sh` downloads all listed packages into `pkgs/`
* `extract.sh` extracts apks from the `pkgs/` dir into `trees/`
* `reorg.sh` makes per-package and combined mandirs at `pkgman/PKG` and `combi/`
