import pandas as pd

def name_sort():
    # 讀取excel
    df = pd.read_excel("藏書清冊.xlsx")

    # 依照 '書名' 欄位進行遞增排序並取代內容（ascending=True 是預設）
    df_sorted = df.sort_values(by='書名', ascending=True, inplace=True)

    df.to_excel("藏書清冊.xlsx", index=False)
