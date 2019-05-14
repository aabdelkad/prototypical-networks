#!/usr/bin/env bash

export CUDA_VISIBLE_DEVICES=0

python scripts/original_script.py --images_base_dir '.' --split_txt_dir 'data/omniglot/splits/original' --validation_size 0.25


python scripts/train/few_shot/run_train.py \
 --data.split original \
 --data.way 10 \
 --data.shot 1 \
 --data.query 5 \
 --data.test_way 10 \
 --data.test_shot 0 \
 --log.exp_dir results_orginal \
 --data.cuda


python scripts/predict/few_shot/run_eval.py \
--model.model_path results_orginal/best_model.pt
