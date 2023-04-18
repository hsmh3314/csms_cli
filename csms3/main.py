import os
import sys
from create import CreateCus, CreateService
from update import UpdateCus, UpdateService
from delete import DeleteCus, DeleteService
from read import ReadOne, readAll
from etcFunc import connect
import visualization as vs

class ResetTable:
    def __init__(self, sel):
        if sel == '1':
            self.table = 'customer'
        elif sel == '2':
            self.table = 'service'
        self.sel = sel

    def resetTable(self):
        os.system('cls')
        readAll(self.sel, '2')
        resetYN = input('모두 삭제하고 초기화 하시겠습니까? y/n : ')
        if resetYN == 'Y' or resetYN == 'y':
            if self.table == 'customer':
                sql = f"delete from customer"
            else:
                sql = "truncate service"
            connect(sql, 'commit')
            print(f"{self.table} 테이블이 초기화되었습니다")

# -------------------------------------------
if __name__ == "__main__" :
    while True:
        os.system('cls')
        print("<고객 정보 및 서비스 이용 내역 관리>")
        print("고객   정보   관리 : 1")
        print("서비스이용내역관리 : 2")
        print("시각화    출력 : 3")
        print("프로그램  종료 : 0")
        sel = input("작업을 선택하세요 : ")
        if sel == '1':
            while True:
                os.system('cls')
                print("----고객 정보 관리----")
                print("고객  정보  등록 : 1")
                print("고객  목록  조회 : 2")
                print("코드별      조회 : 3")
                print("이름별      조회 : 4")
                print("고객  정보  수정 : 5")
                print("고객  정보  삭제 : 6")
                print("고객 정보 초기화 : 7")
                print("고객목록조회(삭제내역) : 8")
                print("고객정보관리종료 : 0")
                selNum = input("작업을 선택하세요 : ")
                if selNum == '1' :
                    cr1 = CreateCus(sel, selNum)
                    cr1.createCus()
                    os.system("pause")
                elif selNum == '2' or selNum == '8':
                    os.system('cls')
                    readAll(sel, selNum)
                    os.system("pause")
                elif selNum == '3' :
                    ro3 = ReadOne(sel, selNum)
                    ro3.readOne()
                    os.system("pause")
                elif selNum == '4' :
                    ro4 = ReadOne(sel, selNum)
                    ro4.readOne()
                    os.system("pause")
                elif selNum == '5' :
                    up5 = UpdateCus(sel, selNum)
                    up5.update()
                    os.system("pause")
                elif selNum == '6' :
                    del6 = DeleteCus(sel, selNum)
                    del6.delete()
                    os.system("pause")
                elif selNum == '7' :
                    rt = ResetTable(sel)
                    rt.resetTable()
                    os.system("pause")
                elif selNum == '0' :
                    print("고객 정보 관리를 종료합니다.")
                    os.system("pause")
                    break
                else :
                    print("잘못 선택했습니다. ")
                    os.system("pause")
        elif sel == '2':
            while True:
                os.system('cls')
                print("----서비스 이용 내역 관리----")
                print("내역        등록 : 1")
                print("내역        조회 : 2")
                print("코드별 내역 조회 : 3")
                print("이름별 내역 조회 : 4")
                print("내역        수정 : 5")
                print("내역        삭제 : 6")
                print("내역      초기화 : 7")      
                print("서비스이용건수조회(기획팀용) : 8")  
                print("서비스이용내역조회(경영팀용) : 9")
                print("서비스이용내역조회(사업팀용) : 10")
                print("서비스이용내역관리 종료 : 0 ")
                selNum = input("작업을 선택하세요 : ")
                if selNum == '1' :
                    cr1 = CreateService(sel, selNum)
                    cr1.createService()
                    os.system("pause")
                elif selNum == '2' or selNum == '8' or selNum == '9' or selNum == '10':
                    os.system('cls')
                    readAll(sel, selNum)
                    os.system("pause")
                elif selNum == '3' :
                    ro3 = ReadOne(sel, selNum)
                    ro3.readOne()
                    os.system("pause")
                elif selNum == '4' :
                    ro4 = ReadOne(sel, selNum)
                    ro4.readOne()
                    os.system("pause")
                elif selNum == '5' :
                    up5 = UpdateService(sel, selNum)
                    up5.update()
                    os.system("pause")
                elif selNum == '6' :
                    del6 = DeleteService(sel, selNum)
                    del6.delete()
                    os.system("pause")
                elif selNum == '7' :
                    rt = ResetTable(sel)
                    rt.resetTable()
                    os.system("pause")
                elif selNum == '0' :
                    print("서비스이용내역 관리를 종료합니다.")
                    os.system("pause")
                    break
                else :
                    print("잘못 선택했습니다. ")
                    os.system("pause")
        elif sel == '3':    
            pv = vs.PrVisual()
            os.system("pause")
        elif sel == '0':
            print("프로그램을 종료합니다. ")
            os.system("pause")
            os.system('cls')
            sys.exit(0)
        else :
            print("잘못 선택했습니다. ")
            os.system("pause")
        
        