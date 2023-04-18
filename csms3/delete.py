import os
from read import readAll
from etcFunc import InputData, FindData, connect, PrRows, CreateHis

class Delete:
    def __init__(self, sel, selNum):
        os.system('cls')
        readAll(sel, '2')
        self.ind = InputData()
        self.in_data = self.ind.setcCode()
        fd = FindData(sel, selNum, self.in_data)
        self.rows = fd.findData()
# ----------------------------------------------
class DeleteCus(Delete):
    def __init__(self, sel, selNum):
        super().__init__(sel, selNum)

    def delete(self):
        if len(self.rows) > 0:
            del_yn = input("정말 삭제하시겠습니까? Y/N : ")
            if del_yn == 'Y' or del_yn == 'y':
                sql = f"delete from customer where cCode = '{self.in_data}'"
                ch = CreateHis('customer', self.in_data)
                connect(sql, 'commit')
                ch.createHis()
                print('삭제를 완료했습니다')
            else:
                print('삭제를 취소했습니다')
        else:
            print('입력한 고객 코드에 해당하는 고객이 없습니다')
# -------------------------------------------------
class DeleteService(Delete):
    def __init__(self, sel, selNum):
       super().__init__(sel, selNum)
    
    def delete(self):
        pr = PrRows(self.rows)
        pr.prService()
        if len(self.rows) > 0:
            in_no = self.ind.setsNo()
            if int(in_no) in [row[0] for row in self.rows]:
                del_yn = input("정말 삭제하시겠습니까? Y/N : ")
                if del_yn == 'Y' or del_yn == 'y':
                    sql = f"delete from service where sNo = '{in_no}'"
                    ch = CreateHis('customer', in_no)
                    connect(sql, 'commit')
                    ch.createHis()
                    print('삭제를 완료했습니다')
                else:
                    print('삭제를 취소했습니다')
            else:
                print('삭제할 목록이 없습니다')
        else:
            print('입력한 고객 코드에 해당하는 내역이 없습니다')