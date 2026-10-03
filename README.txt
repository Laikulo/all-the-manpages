This is an effort to collect manpages from various distros, for use in offline environments,
  or as the baseline for other services.

Assumptions:
* Distros publish manpages in packaged format alongside their packaged applications
* Manpages are the same for a given DISTRO/REVSION pair, regardless of arch
  * Therefore, a 'canonical' arch may be used for a given DISTRO/REVISION
* Distros will not publish version-identical packages wtih different manpages
* Packages may modify their generated manpage based on build-time options
* Distros may modify manpages

As such:
* A manpage for a given package and version from one source is not interchangable with others.

Expected flow (for each DISTRO/REVISION/REPO tuple)

Check revision date if available, if date has alread been processed (or is older):
  CONTINUE
Download repo metadata, and filelists if available.

If filelists are available,
  reduce the working set to just packages with contents in /usr/share/man or distro equivlen
Otherwise
  continue with all packages

For each package, determine if it has already been extracted based on NEVRA or equivelant.
  If so
    NOP
  If not
    Download, extract only contents below /usr/share/man if possible, or extract into scratch dir and discard all else

Add this package to the list of pacakges associated with this "release" of the parent DISTRO/VERSION/REPO

--- TODO process of handling the files themselves

--- TODO This will need some makewhatis equivelant, preferably in a distro-agnostic format (sqlite?)

--- TODO How to handle locales


In order to be nice to upstreams, repos w/o filelists, or with a large number of pacakges should be done from a local mirror. Pulp in pull-through would be a happy medium to prevent needing to mirror __EVERYTING__


Side goals:
Static site generator
