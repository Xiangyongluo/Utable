class Utable:
    def __init__(self,name):
        import json
        import pandas as pd
        import sys
        data = json.loads(sys.argv[1])
        for i in data:
            if data[i] is not None:
                for j in data[i]:
                    if type(data[i][j]) in [str]:
                        #print(pd.DataFrame([data[i][j]]))
                        #names['p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)] = pd.DataFrame([data[i][j]])
                        setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),pd.DataFrame([data[i][j]])) #第一个参数是对象，这里的self其实就是test.第二个参数是变量名，第三个是变量值
                    elif type(data[i][j]) in [list]:
                        #print(pd.DataFrame(data[i][j]))
                        #names['p' + str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)] = pd.DataFrame(data[i][j])
                        setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),pd.DataFrame(data[i][j]))
                    else:
                        tabbb = []
                        #print()
                        for k in data[i][j]:
                            temp = []
                            temp_d =[]
                            for m in data[i][j][k]:
                                temp.append([m])
                                temp_d.append(data[i][j][k][m])
                            tabbb.append(temp_d)
                        #print(pd.DataFrame(tabbb))
                        #names['p' + str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)]= pd.DataFrame(tabbb)
                        setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),pd.DataFrame(tabbb))
        else:
            setattr(self,('p'+str(tuple(data).index(i))),0)
