class Utable:
    def __init__(self,name,pageList=False,tableList=False):
        import json
        import pandas as pd
        with open(name) as f:
            data = json.loads(f.read())
        temp01 = []
        temp02 = []
        try: 
            for i in data:                             # i refer id
                if data[i]:                            # first level
                    temp01.append(i)
                    for j in data[i]:
                        if data[i][j]:
                            temp02.append(j)
                            #print(data[i][j])            # 
                            if type(data[i][j]) in [str]:
                                setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),pd.DataFrame([data[i][j]])) #第一个参数是对象，这里的self其实就是test.第二个参数是变量名，第三个是变量值
                            elif type(data[i][j]) in [list]:
                                setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),pd.DataFrame(data[i][j]))
                            else:
                                tabbb = []
                                temp_multi = []
                                for k in data[i][j]:
                                    if data[i][j][k]:
                                        if type(data[i][j][k]) in [str]:
                                            tabbb.append(data[i][j][k])
                                        elif type(data[i][j][k]) in [list]:
                                            tabbb.append(data[i][j][k])
                                        else:
                                            temp = []
                                            temp_d =[]
                                            for m in data[i][j][k]:
                                                if data[i][j][k][m]:
                                                    temp.append([m])
                                                    temp_d.append(data[i][j][k][m])
                                            temp_multi.append(temp_d)
                                if tabbb:
                                    setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),pd.DataFrame(tabbb))
                                else:
                                    tabbb.append(temp_multi)
                                    setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),pd.DataFrame(tabbb).T)
                        else:
                             setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),0)
                else:
                    setattr(self,('p'+str(tuple(data).index(i))),0)
            #print(temp01)
            #print(temp02)
            if pageList == True:
                setattr(self,"pageList",temp01)
            if tableList == True:
                setattr(self,"tableList",temp02)
        except Exception as err:
            print("Error",err)