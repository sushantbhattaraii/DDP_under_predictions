@echo off

@REM REM This batch file is used to run the launcher.py script with different test files and parameters.

@REM REM - 64 node graph —
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 2 -o 25
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 2.5 -o 25
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 3.333333333333333333333333 -o 25
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 5 -o 25
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 10 -o 25
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c inf -o 25

python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 2 -o 50
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 2.5 -o 50
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 3.333333333333333333333333 -o 50
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 5 -o 50
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c 10 -o 50
python launcher.py -n 64random_diameter38test.edgelist -r 50 -c inf -o 50


@REM REM - 128 node graph —
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c 2 -o 25
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c 2.5 -o 25
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c 3.333333333333333333333333 -o 25
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c 5 -o 25
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c 10 -o 25
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c inf -o 25

python launcher.py -n 128random_diameter146test.edgelist -r 50 -c 2 -o 50
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c 2.5 -o 50
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c 3.333333333333333333333333 -o 50
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c 5 -o 50
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c 10 -o 50
python launcher.py -n 128random_diameter146test.edgelist -r 50 -c inf -o 50

@REM REM - 256 node graph —
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 2 -o 25
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 2.5 -o 25
python launcher.py -n 256random_diameter79test.edgelist -r 5500 -c 3.333333333333333333333333 -o 25
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 5 -o 25
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 10 -o 25
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c inf -o 25

python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 2 -o 50
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 2.5 -o 50
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 3.333333333333333333333333 -o 50
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 5 -o 50
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c 10 -o 50
python launcher.py -n 256random_diameter79test.edgelist -r 50 -c inf -o 50


@REM REM - 512 node graph —
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 2 -o 25
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 2.5 -o 25
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 3.333333333333333333333333 -o 25
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 5 -o 25
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 10 -o 25
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c inf -o 25

python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 2 -o 50
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 2.5 -o 50
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 3.333333333333333333333333 -o 50
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 5 -o 50
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c 10 -o 50
python launcher.py -n 512random_diameter48test.edgelist -r 50 -c inf -o 50

@REM REM - 1024 node graph —
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 2 -o 25
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 2.5 -o 25
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 3.333333333333333333333333 -o 25
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 5 -o 25
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 10 -o 25
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c inf -o 25

python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 2 -o 50
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 2.5 -o 50
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 3.333333333333333333333333 -o 50
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 5 -o 50
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c 10 -o 50
python launcher.py -n 1024random_diameter30test.edgelist -r 50 -c inf -o 50