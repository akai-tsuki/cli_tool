# cli_tool
sample cli tool

## Prepare

### VS Code

VS Code Counter
https://marketplace.visualstudio.com/items?itemName=uctakeoff.vscode-counter

## Build


## Test and coverage

- unittest

```
PS C:\desk\GitHub\cli_tool> python -m unittest tests.test_sample01
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
PS C:\desk\GitHub\cli_tool>
```

- coverage

```
PS C:\desk\GitHub\cli_tool> coverage-2.7.exe run --source .\cli_tool\ -m unittest discover
.
Ran 1 test in 0.000s

OK
PS C:\desk\GitHub\cli_tool>
PS C:\desk\GitHub\cli_tool> coverage-2.7.exe report -m 
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
cli_tool\__init__.py       0      0   100%
cli_tool\core.py           9      9     0%   4-18
cli_tool\sample01.py       6      0   100%
----------------------------------------------------
TOTAL                     15      9    40%
PS C:\desk\GitHub\cli_tool>
```

- output xml file.

```
PS C:\desk\GitHub\cli_tool> coverage-2.7.exe xml
```


## Run by python command

```
PS C:\desk\GitHub\cli_tool> python.exe .\cli_tool\core.py -a test -b value -n 1
Check args ---
test
value
1
Start ---
Hello sample01
End ---
PS C:\desk\GitHub\cli_tool> 
```

## Package and Build

```
PS C:\desk\GitHub\cli_tool> python setup.py sdist --formats=gztar,zip

PS C:\desk\GitHub\cli_tool> ls dist


    ディレクトリ: C:\desk\GitHub\cli_tool\dist


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       2020/03/01     15:10           3504 cli_tool-0.1.0.tar.gz
-a----       2020/03/01     15:10           7254 cli_tool-0.1.0.zip


PS C:\desk\GitHub\cli_tool> 
```

create whl package

```
PS C:\desk\GitHub\cli_tool> python setup.py bdist_wheel

PS C:\desk\GitHub\cli_tool> ls dist


    ディレクトリ: C:\desk\GitHub\cli_tool\dist


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       2020/03/07     23:25           3686 cli_tool-0.1.0-py2-none-any.whl


PS C:\desk\GitHub\cli_tool>
```

## Ref

# Learn more:

  https://github.com/kennethreitz/setup.py
  https://python-packaging-user-guide-ja.readthedocs.io/ja/latest/distributing.html


## Help

python setup.py --help-commands

```
PS C:\desk\GitHub\cli_tool> python setup.py --help-commands
Standard commands:
  build             build everything needed to install
  build_py          "build" pure Python modules (copy to build directory)
  build_ext         build C/C++ extensions (compile/link to build directory)
  build_clib        build C/C++ libraries used by Python extensions
  build_scripts     "build" scripts (copy and fixup #! line)
  clean             clean up temporary files from 'build' command
  install           install everything from build directory
  install_lib       install all Python modules (extensions and pure Python)
  install_headers   install C/C++ header files
  install_scripts   install scripts (Python or otherwise)
  install_data      install data files
  sdist             create a source distribution (tarball, zip file, etc.)
  register          register the distribution with the Python package index
  bdist             create a built (binary) distribution
  bdist_dumb        create a "dumb" built distribution
  bdist_rpm         create an RPM distribution
  bdist_wininst     create an executable installer for MS Windows
  upload            upload binary package to PyPI
  check             perform some checks on the package

Extra commands:
  saveopts          save supplied options to setup.cfg or other config file
  develop           install package in 'development mode'
  upload_docs       Upload documentation to PyPI
  isort             Run isort on modules registered in setuptools
  test              run unit tests after in-place build
  flake8            Run Flake8 on modules registered in setup.py
  setopt            set an option in setup.cfg or another config file
  nosetests         Run unit tests using nosetests
  install_egg_info  Install an .egg-info directory for the package
  rotate            delete older distributions, keeping N newest files
  bdist_wheel       create a wheel distribution
  egg_info          create a distribution's .egg-info directory
  alias             define a shortcut to invoke one or more commands
  easy_install      Find/get/install Python packages
  bdist_egg         create an "egg" distribution
  dist_info         create a .dist-info directory

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help

PS C:\desk\GitHub\cli_tool>
```
