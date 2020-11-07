# -*- coding:utf-8 -*-

"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃　　　　　　　    ┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛
"""

import tensorflow as tf


def load_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data_line = f.read()
    data_line = data_line.split('\n')
    text = []
    label = []
    for each in data_line:
        a, b = each.split('\t')
        text.append(a)
        label.append(b)
    return text, label


def load_data(config):
    train_text, train_label = load_file(config.train_path)
    dev_text, dev_label = load_file(config.dev_path)
    test_text, test_label = load_file(config.test_path)

    tokenizer = config.tokenizer

    # train_text = tokenizer
