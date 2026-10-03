#!/usr/bin/env sh
for pkgpath in pkgs/*.apk; do
	pkgbase="$(basename "$pkgpath")"
	pkgbase="${pkgbase%.apk}"
	echo "$pkgbase"
	pkgtree="trees/$pkgbase"
	[ -d "$pkgtree" ] || mkdir -p "$pkgtree"
	apk extract --destination "$pkgtree" --no-chown "$pkgpath"
done
