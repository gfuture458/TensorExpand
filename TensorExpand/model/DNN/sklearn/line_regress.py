#! /usr/bin/python
# -*- coding: utf8 -*-

import numpy as np
from sklearn import datasets,preprocessing
from sklearn.model_selection import train_test_split
# from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

loaded_data=datasets.load_boston()
data_X=loaded_data.data
data_y=loaded_data.target

model=LinearRegression(normalize=True)
model.fit(data_X,data_y)

# print(model.coef_) # 直线系数
# print(model.intercept_) # 直线截距

print(model.get_params()) # model定义的参数

print(model.score(data_X,data_y)) # R^2 coefficient of determination
