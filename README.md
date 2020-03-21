[![Maintainability](https://api.codeclimate.com/v1/badges/e6339a90f3ecab80960b/maintainability)](https://codeclimate.com/github/akai-tsuki/cli_tool/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e6339a90f3ecab80960b/test_coverage)](https://codeclimate.com/github/akai-tsuki/cli_tool/test_coverage)

# cli_tool

sample cli tool



## Prepare

### VS Code

VS Code Counter
https://marketplace.visualstudio.com/items?itemName=uctakeoff.vscode-counter


## Test and coverage

### unittest

```
PS C:\desk\GitHub\cli_tool> python -m unittest tests.test_sample01
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
PS C:\desk\GitHub\cli_tool>
```

### coverage

```
PS C:\desk\GitHub\cli_tool> coverage-3.8.exe run --source .\cli_tool\ -m unittest discover
.
Ran 1 test in 0.000s

OK
PS C:\desk\GitHub\cli_tool>
PS C:\desk\GitHub\cli_tool> coverage-3.8.exe report -m 
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
cli_tool\__init__.py       0      0   100%
cli_tool\core.py           9      9     0%   4-18
cli_tool\sample01.py       6      0   100%
----------------------------------------------------
TOTAL                     15      9    40%
PS C:\desk\GitHub\cli_tool>
```

output xml file.

```
PS C:\desk\GitHub\cli_tool> coverage-3.8.exe xml
```

### flake8

execute flake8 command
```
PS C:\desk\GitHub\cli_tool> flake8.exe .\cli_tool\
.\cli_tool\rest_client.py:4:1: E302 expected 2 blank lines, found 1
.\cli_tool\rest_client.py:26:1: W391 blank line at end of file
.\cli_tool\sample01.py:4:1: E302 expected 2 blank lines, found 1
.\cli_tool\sample01.py:41:1: W391 blank line at end of file
.\cli_tool\__init__.py:1:11: W292 no newline at end of file
PS C:\desk\GitHub\cli_tool>
```

## Run by python command

```
PS C:\desk\GitHub\cli_tool> python.exe -m cli_tool -a test -b value -n 1

Check args ---
test
value
1
Start ---
name:cli_tool.core
name:cli_tool.sample01
msg: Hello sample01
value: 3
output data: bbb
End ---
PS C:\desk\GitHub\cli_tool> 
```

## Package and Build

```
PS C:\desk\GitHub\cli_tool> python setup.py sdist --formats=gztar,zip

PS C:\desk\GitHub\cli_tool> ls dist


    ディレクトリ: C:\desk\GitHub\cli_tool\dist


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          2020/03/22     2:56           5364 cli_tool-0.1.0.tar.gz
-a---          2020/03/22     2:56           9462 cli_tool-0.1.0.zip


PS C:\desk\GitHub\cli_tool> 
```

create whl package

```
PS C:\desk\GitHub\cli_tool> python setup.py bdist_wheel

PS C:\desk\GitHub\cli_tool> ls dist


    ディレクトリ: C:\desk\GitHub\cli_tool\dist


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          2020/03/22     2:57           5431 cli_tool-0.1.0-py3-none-any.whl


PS C:\desk\GitHub\cli_tool>
```

## Ref

  https://github.com/kennethreitz/setup.py  
  https://python-packaging-user-guide-ja.readthedocs.io/ja/latest/distributing.html
  https://techblog.asahi-net.co.jp/entry/2018/06/15/162951#setuppy


## Help of setup.py

`python setup.py --help-commands`

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
