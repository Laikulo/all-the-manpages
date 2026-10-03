This DB is for use by the infra used to extract and catalouge repos.

Some of its schema may be re-used by end-user artifacts, but it is not intended
as a deliverable.

sources

distro = string representing the distribution this source is from
version = distro version of the repo, stub strings used for rolling distros (e.g. current, 8, 16.04)
bundle = an identifier for this repo within the distro/release (e.g. main, baseos, appstream)

last_checked = The last time the upstream was checked for a new release. Null means never cheked
last_processed = The last time a new release was processed. Null means never processed
last_ref = The upstream 'reference' that was most recently processed. Used to determine if a release should be reprocessed. Some types may not support this, so they have to be checked package-by-package.

