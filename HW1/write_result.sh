#!/bin/bash

echo Write To File...
python bisection.py > ./result/bisection.txt
python false_pos.py > ./result/false_pos.txt
python modify_false_pos.py > ./result/modify_false_pos.txt
python secant.py > ./result/secant.txt
python newten.py > ./result/newten.txt
python fix_point.py > ./result/fix_point.txt
echo FINISHED