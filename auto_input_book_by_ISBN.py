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
            return data.text    #直接在此回傳<ISBN> 與<裝訂方式和冊數>
    return "None None"   #沒有則回傳兩個None字串



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
        book_ISBN_and_Volume=find_ISBN_and_Volume(book_ISBN,datas)
        # print(book_publish_ym_Loc,book_ISBN_and_Volume)
        # 用下面這行指令拆分ISBN跟冊數為LIST內容
        split_ISBN_and_Volume=list(book_ISBN_and_Volume.split())



        #print(split_ISBN_and_Volume)

        #找出書名
        book_name_td = soup.find("td", {"aria-label": "書名"})
        true_book_name_td = book_name_td.find_next_sibling('td')
        book_name = true_book_name_td.text

        #加入書本的裝訂方式與冊數內容
        if split_ISBN_and_Volume[1]!="None":
            book_name=book_name+split_ISBN_and_Volume[1]
        #print(book_name)

        #找出作者名稱
        book_writer_td = soup.find("td", {"aria-label": "作者"})
        true_book_writer_td = book_writer_td.find_next_sibling('td')
        book_writer = true_book_writer_td.text
        #print(book_writer)

        #找出出版機構
        book_publisher_td = soup.find("td", {"aria-label": "出版機構"})
        true_book_publisher_td = book_publisher_td.find_next_sibling('td')
        book_publisher = true_book_publisher_td.text
        #print(book_publisher)

        #找出出版年月
        book_year_month_td = soup.find("td", {"aria-label": "出版年月"})
        book_publish_year_month= book_year_month_td.text
        print(book_publish_year_month)

        #印出搜尋到的所有資料供使用者檢查
        book_IO.print_book_info(book_name,book_writer,book_publisher,
                                book_publish_year_month,book_ISBN)

        #讓使用者在檢查資料後決定是否存取資料
        decide=input("您要輸入的書籍資料符合請輸入Y,否請按其他鍵")
        if(decide=="Y"):
            book_IO.write_data_to_excel(book_name,book_writer,book_publisher,
                                book_publish_year_month,book_ISBN)
        else:
            print("請重啟本程式以輸入新ISBN碼")
