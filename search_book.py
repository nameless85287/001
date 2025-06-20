import pandas as pd
import book_IO

def search(ISBN):
    df=pd.read_excel("藏書清冊.xlsx")
    ISBN_clm=df["ISBN"].tolist()
    for item in ISBN_clm:
        if(ISBN==item):
            print("書籍在藏書庫內")
            return

    print("查無此書籍")


def search_by_ISBN():
    book_ISBN=book_IO.input_ISBN()
    if book_ISBN!=None:
        search(int(book_ISBN))
