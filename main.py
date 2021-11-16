
import pandas as pd

df = pd.read_csv("jejuquize.csv",encoding='utf-8')
num = 0
list_from_df = df.values.tolist()
for data in list_from_df:
    print("{}번 문제 : {}".format(num+1,list_from_df[num][0]))
    print("{}번 정답 : {}".format(num+1,list_from_df[num][1]))
    print("{}번문제의 첫번째 선택지 : {}".format(num+1,list_from_df[num][2]))
    print("{}번문제의 두번째 선택지 : {}".format(num+1,list_from_df[num][3]))
    print("{}번문제의 세번째 선택지 : {}".format(num+1,list_from_df[num][4]))
    print("{}번문제의 네번째 선택지 : {}".format(num+1,list_from_df[num][5]))
    num=num+1
    # print("{}번 문제 : {}".format(num+1,list_from_df[num][0]))

# print(list_from_df[0][0])

