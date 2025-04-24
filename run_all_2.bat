@echo off

REM This batch file is used to run the launcher.py script with different test files and parameters.

REM - first test file —
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 1.3333333333333333
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 2
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 4
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 8
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 16
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 32
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c inf

REM — third test file —
python launcher.py -n 128random_diameter104test.edgelist -r 50 -c 1.3333333333333333
python launcher.py -n 128random_diameter104test.edgelist -r 50 -c 2
python launcher.py -n 128random_diameter104test.edgelist -r 50 -c 4
python launcher.py -n 128random_diameter104test.edgelist -r 50 -c 8
python launcher.py -n 128random_diameter104test.edgelist -r 50 -c 16
python launcher.py -n 128random_diameter104test.edgelist -r 50 -c 32
python launcher.py -n 128random_diameter104test.edgelist -r 50 -c inf


REM — sixth test file —
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 1.3333333333333333
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 2
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 4
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 8
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 16
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 32
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c inf


REM — eighth test file —
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 1.3333333333333333
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 2
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 4
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 8
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 16
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 32
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c inf


REM — tenth test file —
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 1.3333333333333333
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 2
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 4
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 8
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 16
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 32
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c inf