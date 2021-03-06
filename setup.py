from distutils.core import setup

# TODO: How do we express the dependency on the requests library?
setup(
	name = "libraryh3lp-sdk",
	version = "0.1.0",
	description = "Convenience wrappers for the LibraryH3lp REST API.",
	author = "Mike McCarty",
	author_email = "mike@nubgames.com",
	url = "https://github.com/nubgames/libraryh3lp-sdk-python",
	packages = ["libraryh3lp"]
	)
