@echo off

REM This batch file is used to run the launcher.py script with different test files and parameters.

REM - first test file —
python launcher.py -n 64random_diameter38test.edgelist
python launcher.py -n 64random_diameter38test.edgelist -r 50
python launcher.py -n 64random_diameter38test.edgelist -r 100

REM - second test file —
python launcher.py -n 64random_diameter66test.edgelist
python launcher.py -n 64random_diameter66test.edgelist -r 50
python launcher.py -n 64random_diameter66test.edgelist -r 100

REM — third test file —
python launcher.py -n 128random_diameter104test.edgelist
python launcher.py -n 128random_diameter104test.edgelist -r 50
python launcher.py -n 128random_diameter104test.edgelist -r 100

REM — fourth test file —
python launcher.py -n 128random_diameter146test.edgelist
python launcher.py -n 128random_diameter146test.edgelist -r 50
python launcher.py -n 128random_diameter146test.edgelist -r 100

REM — fifth test file —
python launcher.py -n 256random_diameter71test.edgelist
python launcher.py -n 256random_diameter71test.edgelist -r 50
python launcher.py -n 256random_diameter71test.edgelist -r 100

REM — sixth test file —
python launcher.py -n 256random_diameter79test.edgelist
python launcher.py -n 256random_diameter79test.edgelist -r 50
python launcher.py -n 256random_diameter79test.edgelist -r 100

REM — seventh test file —
python launcher.py -n 512random_diameter43test.edgelist
python launcher.py -n 512random_diameter43test.edgelist -r 50
python launcher.py -n 512random_diameter43test.edgelist -r 100

REM — eighth test file —
python launcher.py -n 512random_diameter48test.edgelist
python launcher.py -n 512random_diameter48test.edgelist -r 50
python launcher.py -n 512random_diameter48test.edgelist -r 100

REM — ninth test file —
python launcher.py -n 1024random_diameter24test.edgelist
python launcher.py -n 1024random_diameter24test.edgelist -r 50
python launcher.py -n 1024random_diameter24test.edgelist -r 100

REM — tenth test file —
python launcher.py -n 1024random_diameter30test.edgelist
python launcher.py -n 1024random_diameter30test.edgelist -r 50
python launcher.py -n 1024random_diameter30test.edgelist -r 100