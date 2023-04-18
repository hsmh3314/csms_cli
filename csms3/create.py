import os
from etcFunc import InputData, FindData, connect

class Create:
    def __init__(self, sel, selNum):
        os.system('cls')
        self.ind = InputData()
        self.in_data = self.ind.setcCode()
        fd = FindData(sel, selNum, self.in_data)
        self.rows = fd.findData()
# -----------------------------------------------
class CreateCus(Create):
    def __init__(self, sel, selNum):
        super().__init__(sel, selNum)
        
    def createCus(self):
        if len(self.rows) < 1:
            in_cName = self.ind.setcName()
            in_birth = self.ind.setBirth()
            in_phoneNum = self.ind.setPhoneNum()
            in_address = self.ind.setAddress()
            sql = f"insert into customer(cCode, cName, birth, phoneNum, address) values('{self.in_data}','{in_cName}', '{in_birth}', '{in_phoneNum}', '{in_address}')"
            connect(sql, 'commit')

            print("고객 등록에 성공했습니다")
        else:
            print("이미 등록되어 있는 코드입니다.")
# ---------------------------------------------------        
class CreateService(CreateCus):
    def __init__(self, sel, selNum):
        super().__init__(sel, selNum)
        
    def createService(self):
        if len(self.rows) < 1:
            self.createCus()
        in_sDate = self.ind.setsDate()
        in_departure = self.ind.setDeparture()
        in_arrival = self.ind.setArrival()
        in_fee = self.ind.setFee()
        in_type = self.ind.setType()
        sql = f"""insert into service (cCode, cName, sDate, departure, arrival, fee, type) 
            values('{self.in_data}', (select cName from customer where cCode = '{self.in_data}'),'{in_sDate}','{in_departure}', '{in_arrival}', '{in_fee}', '{in_type}')"""
        connect(sql, 'commit')
        # if in_type == '왕복':
        #     cr = CreateRows(self.in_data, in_sDate)
        #     cr.createRow()
        print("서비스 이용 내역 등록에 성공하였습니다")