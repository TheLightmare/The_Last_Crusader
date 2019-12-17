from cx_Freeze import setup, Executable
base = None
executables = [Executable("the_last_crusader.py", base=base)]

packages = ["idna", "tilemaps.py", "sprites.py", "settings.py", "pygame"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}

setup(
    name = "The Last Crusader",
    options = options,
    version = "1.0",
    description = 'Voici mon programme',
    executables = executables
)
