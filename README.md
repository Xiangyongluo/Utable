
# Utable 使用说明


```python
Utable是一个基于Utopia平台开发出来的可以对复杂json文件进行转换成table的一个python工具(library).
Utopia: http://129.89.35.212/Utopia/
使用版本：
1. Utable for local PC:
    通过pip install Utable 到本地python的library中。
2. Utable for Utopia platform:
    安装 Utable.py 到 Utopia 服务器的 python library.(Github：link)
    
命名方法： 
根据Utopia前端定义的方式方式，我们将各个表格命名为：

p0_1,p0_2,...p1_1,p1_2,...p2_1,p2_1,p2_3...

说明：
p0_1 : 对应Utopia前端为 第一各分页的第一个问题所对应的数据。同理，p0_2 为前端第一个页面第二个问题所对应的数据。
    
如果问题是一个单一的输入，则对应的是一个一行一列的表格。如果输入的是一个矩阵，则输出的是该矩阵的表格。如果是多行多列输入，则输出的是多行多列的表格。

数据样例：
{"a0":{"b1":'value1',
       "b1_2":[1,2,3,4]
      }
 "a1":{"b2":'value2',
       "b2_1":{"row1":{"col1":"value3","col2":"value4","col3":"value5"},
               "row2":{"col1":"value6","col2":"value7","col3":"value8"},
               "row3":{"col1":"value9","col2":"value10","col3":"value11"}
               }
      }
}

p0_1 : 一行一列的表格， 值为：value1
p0_2 : 一行四列的表格， 值为：1，2，3，4     # 样例中，p0只有两个表格
      
p1_1 : 一行一列的表格， 值为：value2
p1_2 : 三行三列的表格， 值为：从 value3 到 value11
```

## json 数据样本


```python
import json
with open("data.json") as f:
    print(json.loads(f.read()))
```

    {'_intro': {'_user': 'abc', '_time': '2019-04-12'}, '_cost_regulate_config': {'Salary_Insurance': {'SE_Salary': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}, 'SE_Driver': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}, 'SE_Manager': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}, 'SE_Employer': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}, 'SE_Others': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}, 'SE_Old': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}, 'SE_Hurt': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}, 'SE_Hospital': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}, 'SE_Jobless': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}, 'SE_Born': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}, 'SE_House': {'chkSE': ['1'], 'txt_SE_Value2': '123', 'txt_SE_Value1': '456', 'txt_SE_Value': '789', 'regulate_methods': '2'}}, 'Subsidies_Funds': {'SF_Labor': {'chkSA': ['1'], 'chk_SA_value2': '234', 'chk_SA_value1': '567', 'chk_SA_Value': '890', 'regulate_methods': '2'}, 'SF_Education': {'chkSA': ['1'], 'chk_SA_value2': '234', 'chk_SA_value1': '567', 'chk_SA_Value': '890', 'regulate_methods': '2'}, 'SF_Subsides': {'chkSA': ['1'], 'chk_SA_value2': '234', 'chk_SA_value1': '567', 'chk_SA_Value': '890', 'regulate_methods': '2'}}, 'Materials_Maintains': {'MM_CY': {'chk_MM': ['1'], 'chk_MM_Value2': '345.5', 'chk_MM_Value1': '678.9', 'chk_MM_Value': '123.4', 'regulate_methods': '2'}, 'MM_TRQ': {'chk_MM': ['1'], 'chk_MM_Value2': '345.5', 'chk_MM_Value1': '678.9', 'chk_MM_Value': '123.4', 'regulate_methods': '2'}, 'MM_EV': {'chk_MM': ['1'], 'chk_MM_Value2': '345.5', 'chk_MM_Value1': '678.9', 'chk_MM_Value': '123.4', 'regulate_methods': '2'}, 'MM_Tram': {'chk_MM': ['1'], 'chk_MM_Value2': '345.5', 'chk_MM_Value1': '678.9', 'chk_MM_Value': '123.4', 'regulate_methods': '2'}, 'MM_Maitains': {'chk_MM': ['1'], 'chk_MM_Value2': '345.5', 'chk_MM_Value1': '678.9', 'chk_MM_Value': '123.4', 'regulate_methods': '2'}, 'MM_Tires': {'chk_MM': ['1'], 'chk_MM_Value2': '345.5', 'chk_MM_Value1': '678.9', 'chk_MM_Value': '123.4', 'regulate_methods': '2'}}, 'ZJ_fei': {'ZJ_vehicle': {'chk_ZJ': ['0'], 'chk_ZJ_Values': '12', 'chk_ZJ_Value1': '34', 'chk_ZJ_Value': '56', 'regulate_methods': '2'}, 'ZJ_GDZC': {'chk_ZJ': ['0'], 'chk_ZJ_Values': '12', 'chk_ZJ_Value1': '34', 'chk_ZJ_Value': '56', 'regulate_methods': '2'}}, 'Incidents_Security': {'IS_Insurance': {'chk_IS': ['1'], 'chk_IS_Value2': '7645', 'chk_IS_Value1': '563', 'chk_IS_Value': '544', 'regulate_methods': '2'}, 'IS_Loss': {'chk_IS': ['1'], 'chk_IS_Value2': '7645', 'chk_IS_Value1': '563', 'chk_IS_Value': '544', 'regulate_methods': '2'}}, 'OtherCost': {'OC_IC_rate': {'chkOC': ['1'], 'chk_OC_value2': '109', 'chk_OC_value1': '208', 'chk_OC_value': '307', 'regulate_methods': '2'}, 'OC_otherOperation': {'chkOC': ['1'], 'chk_OC_value2': '109', 'chk_OC_value1': '208', 'chk_OC_value': '307', 'regulate_methods': '2'}, 'OC_Manage': {'chkOC': ['1'], 'chk_OC_value2': '109', 'chk_OC_value1': '208', 'chk_OC_value': '307', 'regulate_methods': '2'}, 'OC_FinacialFee': {'chkOC': ['1'], 'chk_OC_value2': '109', 'chk_OC_value1': '208', 'chk_OC_value': '307', 'regulate_methods': '2'}, 'OC_Tax': {'chkOC': ['1'], 'chk_OC_value2': '109', 'chk_OC_value1': '208', 'chk_OC_value': '307', 'regulate_methods': '2'}}}, '_efficiency_indicators': {'PassengerVol': {'passengerAll': {'last2YearValue': '306', 'last1YearValue': '407.5', 'lastYearValue': '67.9'}, 'passengerCash': {'last2YearValue': '306', 'last1YearValue': '407.5', 'lastYearValue': '67.9'}, 'passengerCard': {'last2YearValue': '306', 'last1YearValue': '407.5', 'lastYearValue': '67.9'}, 'passengerStu': {'last2YearValue': '306', 'last1YearValue': '407.5', 'lastYearValue': '67.9'}, 'passengerElder': {'last2YearValue': '306', 'last1YearValue': '407.5', 'lastYearValue': '67.9'}}, 'RoutesSum': {'RoutesCount': {'last2YearValue': '25.8', 'last1YearValue': '56.9', 'lastYearValue': '27.5'}, 'TotalMiles': {'last2YearValue': '25.8', 'last1YearValue': '56.9', 'lastYearValue': '27.5'}}, 'VehicleSum': {'OperationVehs': {'last2YearValue': '6365', 'last1YearValue': '6858', 'lastYearValue': '7413'}, 'diselVehs': {'last2YearValue': '6365', 'last1YearValue': '6858', 'lastYearValue': '7413'}, 'GasVehs': {'last2YearValue': '6365', 'last1YearValue': '6858', 'lastYearValue': '7413'}, 'EVVehs': {'last2YearValue': '6365', 'last1YearValue': '6858', 'lastYearValue': '7413'}, 'TramVehs': {'last2YearValue': '6365', 'last1YearValue': '6858', 'lastYearValue': '7413'}}, 'EmployerSum': {'TotalEmployee': {'last2YearValue': '563', 'last1YearValue': '853', 'lastYearValue': '967'}, 'TotalDriver': {'last2YearValue': '563', 'last1YearValue': '853', 'lastYearValue': '967'}, 'TotalManager': {'last2YearValue': '563', 'last1YearValue': '853', 'lastYearValue': '967'}, 'TotalOtherManager': {'last2YearValue': '563', 'last1YearValue': '853', 'lastYearValue': '967'}, 'OtherEmployers': {'last2YearValue': '563', 'last1YearValue': '853', 'lastYearValue': '967'}}, 'FuelConsumption': {'DiselConsume': {'last2YearValue': '864', 'last1YearValue': '936', 'lastYearValue': '802'}, 'GasConsume': {'last2YearValue': '864', 'last1YearValue': '936', 'lastYearValue': '802'}, 'EVConsume': {'last2YearValue': '864', 'last1YearValue': '936', 'lastYearValue': '802'}, 'TramConsume': {'last2YearValue': '864', 'last1YearValue': '936', 'lastYearValue': '802'}}, 'OperationMiles': {'TotalMiles': {'last2YearValue': '39847', 'last1YearValue': '35446', 'lastYearValue': '33723'}, 'DeselMiles': {'last2YearValue': '39847', 'last1YearValue': '35446', 'lastYearValue': '33723'}, 'GasMiles': {'last2YearValue': '39847', 'last1YearValue': '35446', 'lastYearValue': '33723'}, 'EVMiles': {'last2YearValue': '39847', 'last1YearValue': '35446', 'lastYearValue': '33723'}, 'TramMiles': {'last2YearValue': '39847', 'last1YearValue': '35446', 'lastYearValue': '33723'}}}, '_benifit_cal': {'ticketIncome': {'ticketsIncomeCaption': {'last2YearValue': '258', 'last1YearValue': '954', 'lastYearValue': '704'}, 'CashCaption': {'last2YearValue': '258', 'last1YearValue': '954', 'lastYearValue': '704'}, 'CardsCaption': {'last2YearValue': '258', 'last1YearValue': '954', 'lastYearValue': '704'}, 'StuCaption': {'last2YearValue': '258', 'last1YearValue': '954', 'lastYearValue': '704'}, 'OldCaption': {'last2YearValue': '258', 'last1YearValue': '954', 'lastYearValue': '704'}}, 'SubIncome': {'capFuelSub': {'last2YearValue': '754', 'last1YearValue': '344', 'lastYearValue': '7884'}, 'capNEsub': {'last2YearValue': '754', 'last1YearValue': '344', 'lastYearValue': '7884'}, 'capFinanialSub': {'last2YearValue': '754', 'last1YearValue': '344', 'lastYearValue': '7884'}}, '_other': {'capOtherIncome': {'last2YearValue': '3455', 'last1YearValue': '6524', 'LastYearValue': '7342'}, 'capOtherProfit': {'last2YearValue': '3455', 'last1YearValue': '6524', 'LastYearValue': '7342'}}}, '_para_config': {'ParameterSalary': {'elderPercent': {'Last2YearValue': '0.19', 'Last1YearValue': '0.19', 'LastYearValue': '0.19'}, 'hosPercent': {'Last2YearValue': '0.19', 'Last1YearValue': '0.19', 'LastYearValue': '0.19'}, 'ensurePercent': {'Last2YearValue': '0.19', 'Last1YearValue': '0.19', 'LastYearValue': '0.19'}, 'workPercent': {'Last2YearValue': '0.19', 'Last1YearValue': '0.19', 'LastYearValue': '0.19'}, 'birthPercent': {'Last2YearValue': '0.19', 'Last1YearValue': '0.19', 'LastYearValue': '0.19'}, 'housePercent': {'Last2YearValue': '0.19', 'Last1YearValue': '0.19', 'LastYearValue': '0.19'}, 'laborPercent': {'Last2YearValue': '0.19', 'Last1YearValue': '0.19', 'LastYearValue': '0.19'}, 'eduPercent': {'Last2YearValue': '0.19', 'Last1YearValue': '0.19', 'LastYearValue': '0.19'}, 'welfarePercent': {'Last2YearValue': '0.19', 'Last1YearValue': '0.19', 'LastYearValue': '0.19'}}, 'fuelPrice': {'diselPrice': {'Last2YearPrice': '4556', 'Last1YearPrice': '234', 'LastYearPrice': '745'}, 'CNG_Price': {'Last2YearPrice': '4556', 'Last1YearPrice': '234', 'LastYearPrice': '745'}, 'LNG_Price': {'Last2YearPrice': '4556', 'Last1YearPrice': '234', 'LastYearPrice': '745'}, 'elecPrice': {'Last2YearPrice': '4556', 'Last1YearPrice': '234', 'LastYearPrice': '745'}}, 'fuel_Efficiency': {'Energy_Consumption': {'para_Diesel_Consupt': '23', 'para_CNG_Consupt': '45', 'para_LNG_Consupt': '85', 'para_Electric_Consupt': '15', 'para_Trolleybus_Consupt': '15'}}, 'Salary_of_City': {'para_of_Name': {'Avg_salary_Year-2': '866', 'Avg_salary_Year-1': '3445', 'Avg_salary_Year-0': '345'}}}, '_analyses': {'StaffTrend': []}, '_bus_routes_info': {'TBL_BusRoutesInfo': []}}


## 本地端运行Utable


```python
from Utable import Utable
Utable("data.json").p1_1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
    <tr>
      <th>10</th>
      <td>[1]</td>
      <td>123</td>
      <td>456</td>
      <td>789</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



## 本地端程度代码如下：


```python
class Utable:
    def __init__(self,name):
        import json
        import pandas as pd
        with open(name) as f:
            data = json.loads(f.read())
        for i in data:
            if data[i] is not None:
                for j in data[i]:
                    if type(data[i][j]) in [str]:
                        setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),pd.DataFrame([data[i][j]])) #第一个参数是对象，这里的self其实就是test.第二个参数是变量名，第三个是变量值
                    elif type(data[i][j]) in [list]:
                        setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),pd.DataFrame(data[i][j]))
                    else:
                        tabbb = []
                        for k in data[i][j]:
                            temp = []
                            temp_d =[]
                            for m in data[i][j][k]:
                                temp.append([m])
                                temp_d.append(data[i][j][k][m])
                            tabbb.append(temp_d)
                        setattr(self,('p'+str(tuple(data).index(i))+"_"+str(tuple(data[i]).index(j)+1)),pd.DataFrame(tabbb))
        else:
            setattr(self,('p'+str(tuple(data).index(i))),0)
```


```python
Utable("data.json").p1_2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[1]</td>
      <td>234</td>
      <td>567</td>
      <td>890</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[1]</td>
      <td>234</td>
      <td>567</td>
      <td>890</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[1]</td>
      <td>234</td>
      <td>567</td>
      <td>890</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



## Utopia平台代码如下：


```python
class Utable:
    def __init__(self,name):
        import json
        import pandas as pd
        import sys
        data = json.loads(name)
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
            
Utable(sys.argv[1])    #sys.argv[1] 平台读取的前端数据
```
