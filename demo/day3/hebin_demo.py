df = {'name':'小花姐姐','sex':'女'}
hj = {'hone':'187584569','high':'156'}

df.update(hj)
print(df)
print(dict(df,**hj))
sd = dict(df,**hj)
print(sd)