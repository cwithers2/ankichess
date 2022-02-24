from setup tools import setup

setup(
	name="ankichess",
	version="2.0",
	description="Genrate Anki packages from chess PGN files",
	license="MIT",
	author="Colin Withers",
	author_email="cwithers.dev@gmail.com",
	packages=["ankichess"],
	install_requires=["chess", "genanki"],
	scripts=["ankichess"]
)
