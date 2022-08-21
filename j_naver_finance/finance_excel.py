import finance_loop
import pandas as pd

current_list = []
for item in finance_loop.href_list:
    current_list.append(finance_loop.list_crawl(item))
print(current_list)

df = pd.DataFrame(current_list, columns=['종목 이름', '종목 코드', '시가'])
print(df)
df.to_excel('crawl.xlsx')
