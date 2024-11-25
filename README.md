"Build System" for C / C++ created while ago because I didn't want to deal with real build systems for build systems for b...

<br>

**Functionality Level:** 93.253% chance to build simple Hello World program

<br>

**Commands**
- init
- clean
- build
<br>

**IMPORTANT**
- Requires Python 3.11 or later
- Works only on Linux
<br>

**Config Example**
  ```toml
main = "main.c"
output_path = "."
cpp = false

[Include]
paths  = [
    "./src"
]

[Libraries]
include = [
    # specify the library name either as is or with the 'lib' or 'l' prefix 

    "libm",
    "lstdc++",
    "custom_library"
]

[Other]
other = "" # anything else to pass to the compiler
  ```
