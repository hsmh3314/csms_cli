
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
                elif selNum == '8':