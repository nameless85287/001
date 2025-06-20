import hand_input as HI
import search_book as SB
import book_IO
import auto_input_book_by_ISBN as Auto_Input
import book_name_sort


def Decide_Input_Way():
    hint_str=("請決定執行下列何種程序:\n"+
          "1.手動輸入書籍資料\n"+
          "2.查詢書籍是否在庫\n"+
          "3.用ISBN(10碼或13碼)快速輸入資料\n"+
          "請輸入數字1,2,3")
    print(hint_str)

    count=3
    while(count>0):
        way=input()

        if way=="1" or way=="2" or way=="3":
            break
        else:
            print("請輸入1~3之間的數值")
            print(hint_str)
            count-=1

    match (way):
        case "1":
            tuple1=HI.hand_input()
            password="N"
            while(password!="Y"):
                print("您希望輸入的資料如下嗎？")
                book_IO.print_book_info(*tuple1)
                password=input("是請輸入Y,否請輸入其他字元")
                if password=="Y":
                    break
                else:
                    tuple1 = HI.hand_input()
            book_IO.write_data_to_excel(*tuple1) #將資料寫入excel

            book_name_sort.name_sort()  # 操作完資料庫輸入資料後都排序資料

        case "2":
            SB.search_by_ISBN()
        case "3":
            Auto_Input.AIBBI()
            book_name_sort.name_sort()  # 操作完資料庫輸入資料後都排序資料
        case _:
            print("請照要求輸入!程序結束!下次再見")
