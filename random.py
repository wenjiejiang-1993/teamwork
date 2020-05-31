phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],['Galaxy S21', 'Samsung', 6.2, 3300, 1348],['Nova 5T', 'Huawei', 6.26, 3700, 497],['P30 Pro', 'Huawei', 6.4, 3500, 398],['R17 Pro', 'Oppo', 6.6, 3200, 457], ['Pixel 3', 'Google', 6.3, 3800, 688]]
preference=[(3,1),(4,-1)]

def relevant(products, preferences):
    res=[]
    n=len(products)
    for i in range(0,n):
        prolist=products.copy()
        prolist.remove(prolist[i])
        for j in range(0,len(prolist)):
            prod1=products[i]
            pr=[]
            c=choosee(prod1,prolist,preferences)
        if True in c:
            products.remove(products[i])
    return products

def choosee(phone1,phones,preferences):
    res=[]
    re=[]
    for i in range(0,len(phones)):
        for j in range(0,len(preferences)):
            k=preferences[j][0]
            n=len(preferences[0])
            if phone1[k] > phones[i][k] and preferences[j][1]==1 :
                res.append(True)
            elif preferences[j][1]!=1 and phone1[k] < phones[i][k]:
                res.append(True)
            else: 
                res.append(False)
    x=0
    while x<len(res):
        re.append(res[x]==res[x+1])
        x=x+2
    return re


print(relevant(phones, preference))

