import os
from etcFunc import InputData, FindData, PrRows, connect, fmt

class ReadOne:
    def __init__(self, sel, selNum):
        self.sel = sel
        self.selNum = selNum
        if self.selNum == '3': self.readType = '코드'
        elif self.selNum == '4': self.readType = '이름'
        
    def readOne(self):
        os.system('cls')
        print(f'{self.readType}별 조회입니다')
        readAll(self.sel, '2')
        ind = InputData()
        if self.readType == '코드':
            in_data = ind.setcCode()
        elif self.readType == '이름':
            in_data = ind.setcName()
        fd = FindData(self.sel, self.selNum, in_data)
        rows = fd.findData()
        if len(rows) > 0:
            os.system('cls')
            pr1 = PrRows(rows)
            if self.sel == '1':
                print(f"===고객 조회({self.readType}별)===")
                pr1.prCustomer()
            else:
                print(f"===서비스 이용내역 조회({self.readType}별)===")
                pr1.prService()
        else:
            print(f"입력한 {self.readType}에 맞는 정보가 없습니다.")  
      
# ---------------------------------
def readAll(sel, selNum):
    fd = FindData(sel, selNum)
    rows = fd.findData()
    if len(rows) > 0:
        if sel == '1':
            if selNum == '8':
                print("<<고객정보조회(삭제내역)>>")
            else:
                print("<<고객 목록>>")
            pr1 = PrRows(rows)
            pr1.prCustomer()
        elif sel == '2':
            pr2 = PrRows(rows)
            if selNum == '8':
                print("<<서비스이용건수조회(기획팀용)>>")
                pr2.prServiceMax()
            elif selNum == '9':
                print("<<서비스이용내역조회(경영팀용)>>")
                pr2.prService()
                pr2.prServiceCnt()
            elif selNum == '10':
                print("<<서비스이용내역조회(사업팀용)>>")
                pr2.prService()
                pr2.prServiceCnt()
            else: 
                print("<<서비스 이용 내역>>")
                pr2.prService()
    else:
        print('조회할 내용이 없습니다.')
