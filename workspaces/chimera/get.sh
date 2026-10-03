#!/usr/bin/env sh
apk list | cut -f1 -d' ' | rev | cut -f3- -d- | rev | grep -- '-man$' > pkgs.list
