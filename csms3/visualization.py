import os
import matplotlib.pyplot as plt
import pandas as pd
from etcFunc import connect

class PrVisual:
    def __init__(self):
        os.system('cls')
        self.prVisual()
    
    def prVisual(self):
        data_lst = self.preprocessing()
        self.writeFile(data_lst)
        while True:
            print("날짜 별 이용 횟수 : 1")
            print("고객 별 이용 횟수 : 2")
            print("이전 메뉴로 돌아가기 : 0")
            in_sel = input("원하는 항목을 선택하세요 : ")
            if in_sel == '1':
                self.prGraph('sDate')
            elif in_sel == '2':
                self.prGraph('cCode')
            elif in_sel == '0':
                print("이전 메뉴로 돌아갑니다.")
                break
            else:
                os.system('cls')
                print('입력한 항목이 존재하지 않습니다.')
            print()

    def prGraph(self, col):
        df = pd.read_csv('data/service_all.txt', header = None, sep = ',')
        df.columns = ['sNo', 'cCode', 'cName', 'sDate', 'departure', 'arrival', 'fee', 'type']
        df1 = df.set_index('sDate')
        sr1 = df1.groupby(col)['sNo'].count()
        x_lst = sr1.index.to_list()
        y_lst = list(sr1)
        plt.figure(figsize = (11, 5))
        plt.xlabel(col)
        plt.ylabel('Service Use')
        plt.bar(x_lst, y_lst)
        plt.show()

    def writeFile(self, row_lst):
        try:
            with open('data/service_all.txt', mode = 'w', encoding = 'utf-8') as s_all:
                for row in row_lst:
                    s_all.write(row)
        except Exception as e:
            print('error :', e)
        finally:
            pass

    def preprocessing(self):
        sql = f"select * from service"
        rows = connect(sql)
        # -------------------------------------------------
        ### 06 - 데이터 형변환 ### map() 함수 사용
        row_lst = []
        for row in rows:
            row = list(row)
            row[3] = row[3].date()
            row_lst.append(','.join(list(map(str, row)))+'\n')
        return row_lst
            