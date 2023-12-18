# Sublime virtual environment setup

all works by this point in the video

if watch and follow along

from start :

[Python Setup On Sublime Text 3 + Virtualenv | Windows 10](https://youtu.be/5UlFHn6FBxk?t=385)

- works on Win 11

____

above involves :

going to :

[docs.sublimetext.info | Build System - Basics](https://docs.sublimetext.info/en/latest/reference/build_systems/basics.html)

____

and copying in :

[Example](https://docs.sublimetext.info/en/latest/reference/build_systems/basics.html#example)

```json
{
    "cmd": ["python", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}
```

1. a

In cmd

go to .venv

go to Scripts folder

copy (as) path

add python.exe

to the end of it

then paste that path into

the above json

as the value for

"cmd"

in the list at item 0

instead of python

so both go inside double quotes "  "



2:

save as:

File name: .venv.sublime.build

Save as type: JSON

____

to run:

in Sublime Text Editor:

Tools > Build System

.venv

should be there

if build file saved correctly
