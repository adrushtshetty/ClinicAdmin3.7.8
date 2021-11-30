import pandas as pd
df=pd.read_csv("Pt_log.csv")
res=df.loc[df['Phone_Number'] == 123456789]
# print(res['Link'])
# print(res['Locality'])
# res=df[df['Name']=="Adrusht"]
# print(res)
# print(res['Name'])

# for x in res['Name']:
#     print(x)

n=list(res['Name'])
d=list(res['Date'])
l=list(res['Link'])
# l=l[0]
print(n)
print(d)
print(l)
print()
# for x in n :
#     print("Name: ",x)
#     for y in d:
#         print("Date: ", y)
#         for z in l:
#             print("Link: ",z)


# for x in zip(n,d,l):
#     print(x)


# res=[]
# for x in zip(n,d,l):
#     res.append(x)
# print(res)

answer = []
for y in range(len(n)):
    a = n[y]
    b = d[y]
    c = l[y]
    temp = [a, b, c]
    answer.append(temp)

for x in answer:
    print(x)

print()
print(answer)