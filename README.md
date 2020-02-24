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

output xml file.

```
PS C:\desk\GitHub\cli_tool> coverage-2.7.exe xml
```


## Run

```
PS C:\desk\GitHub\cli_tool> python cli_tool\core.py
Start
Hello sample01
End
PS C:\desk\GitHub\cli_tool> 
```


