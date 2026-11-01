
all: containers
.PHONY: all containers

CONTAINERS=chimera chimera-base
containers: $(foreach c,$(CONTAINERS),$c.container)

WHLNAME=atmpage_etl-0.0.1-py3-none-any.whl

dist/$(WHLNAME): atmpage/* pyproject.toml
	pyproject-build

%.container.d/$(WHLNAME): dist/$(WHLNAME)
	cp -f $< $@

chimera.container: chimera-base.container chimera.container.d/$(WHLNAME)
	podman build -t atmetl-chimera chimera.container.d --iidfile=$@ --from $(file < $<)

%.container: %.container.d/Containerfile
	podman build -t atmetl-$* $*.container.d --iidfile=$@

devcont: chimera-base.container
	podman run --rm -it --userns keep-id -v $(CURDIR)/..:/mnt -w /mnt $(file < $<) /bin/sh -c 'pip install -e /mnt/etl; exec sh -i'

clean:
	rm -f $(foreach c,$(CONTAINERS),$c.container) \
		chimera.container.d/*.whl
	rm -rf dist/
