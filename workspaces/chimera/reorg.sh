#!/usr/bin/env sh
combidir="combi"
[ -d "$combidir" ] || mkdir "$combidir"
for pkgman in trees/*/usr/share/man; do
	pkgbase="${pkgman#trees/}"
	pkgbase="${pkgbase%/usr/share/man}"
	pkgbase="$(echo "$pkgbase" | rev | cut -f 4- -d- | rev)"
	echo "$pkgbase"
	pkgdir="pkgman/$pkgbase"
	[ -d "$pkgdir" ] || mkdir -p "$pkgdir"
	cp -rv "$pkgman/"* "$pkgdir"
	cp -rv "$pkgman/"* "$combidir"
done
