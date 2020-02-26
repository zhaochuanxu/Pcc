#第一步：调用pandas包
import pandas as pd
from pandas import DataFrame as DF
from datetime import datetime
import numpy as np
import  csv

from scipy.stats import pearsonr


#手写皮尔逊相关系数代码
def cal_pccs(x, y, n):
    """
    warning: data format must be narray
    :param x: Variable 1
    :param y: The variable 2
    :param n: The number of elements in x
    :return: pccs
    """
    sum_xy = np.sum(np.sum(x*y))
    sum_x = np.sum(np.sum(x))
    sum_y = np.sum(np.sum(y))
    sum_x2 = np.sum(np.sum(x*x))
    sum_y2 = np.sum(np.sum(y*y))
    pcc = (n*sum_xy-sum_x*sum_y)/np.sqrt((n*sum_x2-sum_x*sum_x)*(n*sum_y2-sum_y*sum_y))
    return pcc




if __name__ == "__main__":

    #第二步：读取数据
    iris = pd.read_excel('./expression.xlsx',None)#读入数据文件
    keys = list(iris.keys())
    data= iris[keys[0]]#第一个sheet中的数据
    print(type(data))

    #读取行数
    #print(data.shape[0])
    len = data.shape[0]

    for i in range(0,len+1):
        for j in range(i+1,len):
            s1 = data.iloc[i,0]
            s2 = data.iloc[j,0]
            d1 = data.iloc[i,1:37]
            d2 = data.iloc[j,1:37]
            d1 = d1.tolist()
            d2 = d2.tolist()
            d1 = np.array(d1)
            d2 = np.array(d2)
            r2 = cal_pccs(d1, d2,37)
            #print(r2)

            #print(s1)
            #print(s2)
            r  = [s1,s2,r2]
            #print(type(r))
            #0.33991348499411833
            print(r)

            name ="./pcc_result/"+s1+".csv"
            #print(name)


            with open(name, "a", newline='', encoding='utf-8') as file:
                writer = csv.writer(file ,delimiter=',')
                writer.writerow(r)

            print("写入完成")






"""
            print(type(d1))
            print(type(d2))
            d1 = d1.tolist()
            d2 = d2.tolist()
            print(type(d1))
            print(type(d2))
            print(d1)
            print(d2)
"""

"""
    #读取列数
    #print(data.shape[1])

    #print(type(data))
    #print(data)


    #提取某行 以下

    #某行是从0 开始
    #print(data.iloc[3])
    #print(data.iloc[0])

    #d1  = data.iloc[0]
    #print(type(d1))
"""
#注释部分是对单一行列进行试验
"""
    #相当于提取某一行然后将这一行切片
    d1 = data.iloc[0,1:37]
    #print(data.iloc[0,1:25])
    #print(d1)
    #print(type(d1))


    #读取第二列
    d2 = data.iloc[1,1:37]
    #print(d2)
    #print(type(d2))


    #print(d1.tolist())


    #转化
    d1 = d1.tolist()
    d2 = d2.tolist()
"""

"""

    r =np.corrcoef(d1,d2)

    print(type(r))
    print(r)


    d11 = np.array(d1)
    d22 = np.array(d2)


    r2 = cal_pccs(d11, d22, 37)

    print(r2)

"""







