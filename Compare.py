 #第一步：调用pandas包
import pandas as pd
from pandas import DataFrame as DF
from datetime import datetime
import numpy as np
import  csv
import matplotlib.pyplot as plt


if __name__ == "__main__":

    #第二步：读取数据
    iris = pd.read_csv("./pcc_result/YJR012C.csv")
    keys = list(iris.keys())
    data= iris[keys[0]]#读取第一列
    #print(data)
    data1 = iris[keys[1]] #读取第二列
    #print(data1)
    num = iris[keys[2]]
    #print(num)
    print(type(num))
    j = 0
    for i in range(len(num)):
          if num[i]>0.8:
              j = j+1

    print(j)
    #YJR012C