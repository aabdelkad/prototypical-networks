#!/usr/bin/env bash

python scripts/train/few_shot/run_train.py \
 --data.split original \
 --data.way 5 \
 --data.shot 1 \
 --data.query 5 \
 --data.test_way 5 \
 --data.test_shot 0 \
 --log.exp_dir results_orginal