from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup

import book_IO

def find_ISBN_and_Volume(book_ISBN,datas):
    for loc,data in enumerate(datas):
        if book_ISBN in data.text:
            print("找到index與data")
            return loc+4,data.text    #根據資料結構<出版年月>會在ISBN搜尋到的位置往下4個index，直接在此回傳
    return 29,"None None"   #根據網頁資料結構<出版年月>會在index29的地方



def AIBBI():
    book_ISBN=book_IO.input_ISBN() #要求輸入ISBN

    if book_ISBN!=None:
        #以下網址為台灣國家圖書館全國新書資訊網
        url = "https://isbn.ncl.edu.tw/NEW_ISBNNet/"

        options = Options()
        options.add_argument("--headless")  # 無頭模式，不開瀏覽器視窗
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        time.sleep(3)  # 等待 JavaScript 載入

        select_element = driver.find_element(By.NAME, "FO_SearchField0")

        dropdown = Select(select_element)
        dropdown.select_by_visible_text("ISBN")

        search_box = driver.find_element(By.NAME, "FO_SearchValue0")
        search_box.clear()  # 清空原有內容
        search_box.send_keys(book_ISBN) #輸入ISBN進入查詢內容欄位

        driver.execute_script("document.F1.submit();") #點擊搜尋按鈕

        time.sleep(3) # 等待 JavaScript 載入

        #在link選取下一個頁面並點擊進入
        link = driver.find_element(By.CSS_SELECTOR, 'table.table-searchbooks tr:nth-of-type(2) a')
        link.click()

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        # print(soup.text)
        datas = soup.find_all('td')

        # for i,data in enumerate(datas):
        #     print(i,data.text)
        #     print("--"*15)

        book_publish_ym_Loc,book_ISBN_and_Volume=find_ISBN_and_Volume(book_ISBN,datas)
        # print(book_publish_ym_Loc,book_ISBN_and_Volume)
        #
        # 用下面這行指令拆分ISBN跟冊數為LIST內容
        split_ISBN_and_Volume=list(book_ISBN_and_Volume.split())

        #

        #print(split_ISBN_and_Volume)
        #
        if split_ISBN_and_Volume[1]=="None":
            book_name = datas[1].text
        else:
            book_name=datas[1].text+split_ISBN_and_Volume[1]
        book_writer=datas[3].text
        book_publisher=datas[5].text
        book_publish_year_month=datas[book_publish_ym_Loc].text

        book_IO.print_book_info(book_name,book_writer,book_publisher,
                                book_publish_year_month,book_ISBN)

        decide=input("您要輸入的書籍資料符合請輸入Y,否請按其他鍵")
        if(decide=="Y"):
            book_IO.write_data_to_excel(book_name,book_writer,book_publisher,
                                book_publish_year_month,book_ISBN)
        else:
            print("請重啟本程式以輸入新ISBN碼")
