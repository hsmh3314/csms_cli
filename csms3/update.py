import os
from read import readAll
from etcFunc import InputData, FindData, PrRows, connect

class Update:
    def __init__(self, sel, selNum):
        os.system('cls')
        readAll(sel, '2')
        self.ind = InputData()
        self.in_data = self.ind.setcCode()
        fd = FindData(sel, selNum, self.in_data)
        self.rows = fd.findData()
# -------------------------------------------------
class UpdateCus(Update):    
    def __init__(self, sel, selNum):
        super().__init__(sel, selNum)
    
    def update(self):
        if len(self.rows) > 0:
            pr = PrRows(self.rows)    
            pr.prCustomer()
            in_cName = self.ind.setcName()
            in_birth = self.ind.setBirth()
            in_phoneNum = self.ind.setPhoneNum()
            in_address = self.ind.setAddress()
            sql = f"""update customer set cName = '{in_cName}', birth = '{in_birth}', phoneNum = '{in_phoneNum}', 
                    address = '{in_address}' where cCode = '{self.in_data}'"""
            connect(sql, 'commit')
            print('수정을 완료했습니다')
        else:
            print('입력한 제품 코드에 해당하는 제품이 없습니다')
# ---------------------------------------------------        
class UpdateService(Update):
    def __init__(self, sel, selNum):
        super().__init__(sel, selNum)

    def update(self):
        if len(self.rows) > 0:
            pr = PrRows(self.rows)    
            pr.prService()
            in_no = self.ind.setsNo()
            if int(in_no) in [row[0] for row in self.rows]:
                in_data = self.ind.setcCode()
                in_sDate = self.ind.setsDate()
                in_departure = self.ind.setDeparture()
                in_arrival = self.ind.setArrival()
                in_fee = self.ind.setFee()
                in_type = self.ind.setType()
                sql = f"""update service set cCode = '{in_data}', cName = (select cName from customer where cCode = '{in_data}'), 
                        sDate = '{in_sDate}', departure = '{in_departure}', arrival='{in_arrival}',fee='{in_fee}', type='{in_type}' where sNo = '{in_no}'"""
                connect(sql, 'commit')
                print('수정이 완료되었습니다')
            else:
                print('수정할 목록이 없습니다')
        else:
            print('입력한 제품 코드에 해당하는 제품이 없습니다')