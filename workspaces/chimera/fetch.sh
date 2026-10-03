#!/usr/bin/env sh
xargs < pkgs.list apk fetch -o pkgs
