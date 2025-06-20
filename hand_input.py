import book_IO

#手動輸入書籍資訊並回傳tuple出去
def hand_input():
    book_name=input("請輸入書名：")
    book_writer=input("請輸入作者名稱：")
    book_publisher=input("請輸入出版社名稱：")
    book_publish_year_month=input("請輸入出版年月(ex格式:112/01)：")
    book_ISBN=book_IO.input_ISBN()
    if book_ISBN!=None:
        return (book_name, book_writer, book_publisher,
                book_publish_year_month, book_ISBN)

