import pymysql
from re import match, findall
from wcwidth import wcswidth 
import calendar

config = {                  
    'host' : '127.0.0.1',   
    'user' : 'root',        
    'passwd' : 'root1234',  
    'database' : 'test_db3', 
    'port' : 3306,   
    'charset' : 'utf8',    
    'use_unicode' : True   
    }

class CreateHis:
    def __init__(self, table, in_data):
        self.table = table
        if table == 'customer':
            sel_sql = f"select * from service where cCode = '{in_data}'"
        elif table == 'service':
            sel_sql = f"select * from service where sNo = '{in_data}'"
        self.row = connect(sel_sql)
                        
    def createHis(self):
        for row in self.row:
            sql = f"""insert into service_backup values('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}')"""
            connect(sql, 'commit')

class FindData:
    def __init__(self, sel, selNum, in_data = ''):
        if sel == '1' or (sel == '2' and selNum == '1'):
            if selNum == '2':
                self.sql = f"select * from customer"
            elif selNum == '1' or selNum == '3' or selNum == '5' or selNum == '6':
                self.sql = f"select * from customer where cCode = '{in_data}'"
            elif selNum == '4':
                self.sql = f"select * from customer where cName = '{in_data}'"
            elif selNum == '8':
                self.sql = f"select * from customer_backup"
        elif sel == '2':
            if selNum == '2' or selNum == '10':
                self.sql = f"""select * from service"""
            elif selNum == '3' or selNum == '5' or selNum == '6':
                self.sql = f"select * from service where cCode = '{in_data}'"
            elif selNum == '4':
                self.sql = f"""select * from service where cName = '{in_data}'"""
            elif selNum == '8':
                self.sql = f"select * from service_max order by sDate"
            elif selNum == '9':
                self.sql = f"select * from service union select * from service_backup order by sDate"
    def findData(self):
        return connect(self.sql)
# -------------------------------------------  
class InputData():
    def __init__(self):
        self.if1 = InputFilter()

    def setcCode(self):
        while True:
            if self.if1.filtcCode(input("고객 코드를 입력해주세요 : ")):
                in_cCode = self.if1.cCode
                break
            else:
                continue
        return in_cCode

    def setcName(self):
        while True:
            if self.if1.filtcName(input("고객명을 입력해주세요 : ")):
                in_cName = self.if1.cName
                break
            else:
                continue
        return in_cName
    
    def setBirth(self):
        while True:
            if self.if1.filtBirth(input("생년월일 8자리를 입력해주세요(기호 생략) : ")):
                in_birth = self.if1.birth
                break
            else:
                continue
        return in_birth
    
    def setPhoneNum(self):
        while True:
            if self.if1.filtPhoneNum(input("전화번호를 입력해주세요 : ")):
                in_phoneNum = self.if1.phoneNum
                break
            else:
                continue
        return in_phoneNum

    def setAddress(self):
        while True:
            if self.if1.filtAddress(input("주소를 입력해주세요 : ")):
                in_address = self.if1.address
                break
            else:
                continue
        return in_address

    def setsDate(self):
        while True:
            if self.if1.filtsDate(input("예약 일시를 입력해주세요 (예시 : 2023-02-12 13:40) : ")):
                in_sDate = self.if1.sDate
                break
            else:
                continue
        return in_sDate

    def setDeparture(self):
        while True:
            if self.if1.filtDeparture(input("출발지를 입력해주세요 : ")):
                in_departure = self.if1.departure
                break
            else:
                continue
        return in_departure
    
    def setArrival(self):
        while True:
            if self.if1.filtArrival(input("도착지를 입력해주세요 : ")):
                in_arrival = self.if1.arrival
                break
            else:
                continue
        return in_arrival
    
    def setFee(self):
        while True:
            if self.if1.filtFee(input("요금을 입력해주세요 : ")):
                in_fee = self.if1.fee
                break
            else:
                continue
        return in_fee
    
    def setsNo(self):
        while True:
            if self.if1.filtsNo(input("서비스 번호를 입력해주세요 : ")):
                in_sNo = self.if1.sNo
                break
            else:
                continue
        return in_sNo
    
    def setType(self):
        while True:
            if self.if1.filtType(input("운행 타입을 입력해주세요 (편도, 왕복): ")):
                in_type = self.if1.type
                break
            else:
                continue
        return in_type
# -------------------------------------
class InputFilter():
    def __init__(self):
        self.inputResult = ''
        self.cCode = ''
        self.cName = ''
        self.birth = ''
        self.phoneNum = ''
        self.address = ''
        self.sDate = ''
        self.departure = ''
        self.arrival = ''
        self.fee = ''
        self.sNo = ''
        self.type = ''
            
    def filtcCode(self, cCode):
        if len(cCode) <= 0:
            print('다시 입력해주세요')
            self.inputResult = False
        elif len(cCode) > 4:
            print("제품 코드가 너무 깁니다. 'a001'의 형식으로 입력해주세요")
            self.inputResult = False
        elif findall('[\'";!@#|$%^&*()_+/= ]+|select|insert|update|delete|drop|from|where|join', cCode):
            print('특수문자를 제외하고 입력해주세요')
            self.inputResult = False
        elif not match('[a-z][0-9]{3}', cCode):
            print("'a001'의 형식으로 입력해주세요")
            self.inputResult = False
        else:
            self.inputResult = True
            self.cCode = cCode        
        return self.inputResult
    
    def filtcName(self, cName):
        if len(cName) <= 0:
            print('다시 입력해주세요')
            self.inputResult = False
        elif findall('[\'";!@#|$%^&*()_+/= ]+|select|insert|update|delete|drop|from|where|join', cName):
            print('특수문자를 제외하고 입력해주세요')
            self.inputResult = False
        else:
            self.inputResult = True
            self.cName = cName
        return self.inputResult
    
    def filtBirth(self, birth):
        if len(birth) <= 0:
            print('다시 입력해주세요')
            self.inputResult = False
        elif not birth.isdigit() :        
            print("숫자로 입력해주세요.")
            self.inputResult = False
        else:
            self.inputResult = True
            self.birth = birth
        return self.inputResult
    
    def filtPhoneNum(self, phoneNum):
        if len(phoneNum) <= 0:
            print('다시 입력해주세요')
            self.inputResult = False
        else:
            self.inputResult = True
            self.phoneNum = phoneNum
        return self.inputResult
    
    def filtAddress(self, address):
        if len(address) <= 0:
            print("다시 입력 해주세요")
            self.inputResult = False
        else:
            self.inputResult = True
            self.address = address
        return self.inputResult

    def filtsDate(self, sDate):
        if len(sDate) <= 0:
            print('다시 입력해주세요')
            self.inputResult = False
        else:
            self.inputResult = True
            self.sDate = sDate
        return self.inputResult
    
    def filtDeparture(self, departure):
        if len(departure) <= 0:
            print('다시 입력해주세요')
            self.inputResult = False
        else:
            self.inputResult = True
            self.departure = departure
        return self.inputResult
    
    def filtArrival(self, arrival):
        if len(arrival) <= 0:
            print('다시 입력해주세요')
            self.inputResult = False
        else:
            self.inputResult = True
            self.arrival = arrival
        return self.inputResult
    
    def filtFee(self, fee):
        if len(fee) <= 0:
            print('다시 입력해주세요')
            self.inputResult = False
        elif not fee.isdigit() :        
            print("숫자로 입력해주세요.")
            self.inputResult = False
        else:
            self.inputResult = True
            self.fee = fee
        return self.inputResult
    
    def filtsNo(self, sNo):
        if len(sNo) <= 0:
            print('다시 입력해주세요')
            self.inputResult = False
        elif not sNo.isdigit() :        
            print("숫자로 입력해주세요.")
            self.inputResult = False
        else:
            self.inputResult = True
            self.sNo = sNo
        return self.inputResult
    
    def filtType(self, type):
        if len(type) <= 0:
            print('다시 입력해주세요')
            self.inputResult = False
        else:
            self.inputResult = True
            self.type = type
        return self.inputResult
# --------------------------------------------
class PrRows:
    def __init__(self, rows):
        self.rows = rows
                    
    def prCustomer(self):
        print("---cCode---cName------birth-----------phoneNum-----------address----------")
        for row in self.rows :
            print("{} {} {} {} {}".format(fmt(row[0],10,'c'),fmt(row[1],10,'l'),fmt(row[2],12,'l'),fmt(row[3], 14, 'l'), row[4]))

    def prService(self):
        print("-sNo--cCode---cName------sDate--------------------------departure--------------------------------arrival---------------------fee-----type----")
        for row in self.rows:
            print("{} {} {} {} {} {} {} {}".format(fmt(row[0],5,'c'),fmt(row[1],7,'l'),fmt(row[2],10,'l'),fmt(row[3],20,'l'),\
                                            fmt(row[4],41,'l'),fmt(row[5],35,'l'),fmt(format(row[6], ','), 8, 'l'), row[7]))
    
    def prServiceMax(self):
        print("--cCode---cName--------sDate------------------departure--------------------------arrival------------")
        for row in self.rows:
            print("{} {} {} {} {}".format(fmt(row[0],9,'c'),fmt(row[1],10,'l'),fmt(row[2].date(),14,'l'),fmt(row[3],42,'l'), row[4]))
        self.prServiceCnt()
    
    def prServiceCnt(self):
        print("-"*90)
        print("서비스 이용 건수 :", len(self.rows))
                                            
# --------------------------------------------
def connect(sql, commit=''):
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        cursor.execute(sql)
        if commit:
            conn.commit()
        else:
            return cursor.fetchall()
    except Exception as e:
        print("db error :", e)
        conn.rollback()
    finally: 
        cursor.close()
        conn.close()
# --------------------------------------
def fmt(txt, width, align='r'):
    txt = str(txt)
    wid_txt = wcswidth(txt)
    space = width-wid_txt
    if space <= 0:
        return txt
    if align == 'l':
        return txt + ' '*space
    if align == 'c':
        sl = space//2
        sr = space - sl
        return ' '*sl + txt + ' '*sr
    return ' '*space + txt

