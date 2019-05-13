#!/usr/bin/env bash

python scripts/original_script \
--images_base_dir '.'\
--split_txt_dir 'data/omniglot/splits/original' \
--validation_size 0.50


python scripts/train/few_shot/run_train.py \
 --data.split original \
 --data.way 5 \
 --data.shot 1 \
 --data.query 5 \
 --data.test_way 5 \
 --data.test_shot 0 \
 --log.exp_dir results_orginal


python scripts/predict/few_shot/run_eval.py \
--model.model_path results_orginal/best_model.pt
