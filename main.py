"""
寫一個程式可以
1.手動輸入書籍資料並加入資料庫(excel的xlsx檔)
2.查詢書籍是否在庫
3.用爬蟲程式以ISBN快速加入資料庫(excel的xlsx檔)
4.用Bar Code條碼掃描就能快速入庫
"""

#寫一個手動輸入資料庫的程式

# -*- coding: utf-8 -*-

import sub_function as SF
import xlwings as xw

SF.Decide_Input_Way() #進入操作選單

#此段程式碼旨在每次結束程式前先自動設定欄寬配合資料內容
app = xw.App(visible=False, add_book=False)
wb= app.books.open('藏書清冊.xlsx')
ws = wb.sheets['Sheet1']
ws.autofit()
wb.save('藏書清冊.xlsx')
wb.close()
app.quit()
