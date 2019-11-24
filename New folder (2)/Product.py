# List of elements
li=[{
    "pid":1,
    "name":"Elite",
    "cost":1200,
    "brand":"HP",
    "rating":"3.4",
    "discount":"80%",
    "category":"Laptop"
},
{
    "pid":2,
    "name":"Elite2.1",
    "cost":20032,
    "brand":"HP",
    "rating":"5",
    "discount":"50%",
    "category":"Laptop"
},
{
    "pid":3,
    "name":"Hp basic",
    "cost":13000,
    "brand":"HP",
    "rating":"4",
    "discount":"40%",
    "category":"Laptop"
},
{
    "pid":4,
    "name":"Redmi Note4",
    "cost":8000,
    "brand":"Redmi",
    "rating":"4.2",
    "discount":"60%",
    "category":"Mobile"
},
{
    "pid":5,
    "name":"Moto E4",
    "cost":7000,
    "brand":"Moto",
    "rating":"4.1",
    "discount":"89%",
    "category":"Mobile"
},
{
    "pid":6,
    "name":"realme U1",
    "cost":10000,
    "brand":"Realme",
    "rating":"4.5",
    "discount":"83%",
    "category":"Mobile"
}
]

print("        MENU       ")
print("1.Sort Cost in H to L ")
print("2.Sort Cost in L to H ")
print("3.Sort Discount in H to L ")
print("4.Sort Discount in L to H ")
print("5.Sort Rating in H to L")
n=int(input("Enter the option to Sort: "))


# list of options
l2=[["cost",True],["cost",False],["rating",True],["discount",True],["discount",False]]
li.sort(key=lambda el: el[l2[n-1][0]],reverse=l2[n-1][1])
print(li)

# to filter
n1=int(input("Enter which field to filter"))
name=input("Enter the name to Filter")
dic=[
    "brand",
    "name",
    "category",
   ]

newobj=filter(lambda el:el[dic[n1-1]]==name,li)
for i in newobj:
    print('{pid} {name} {cost} {rating}'.format(**i))


# else:
#     li.sort(True, key=lambda el: )
#     print(li)

#print("Sorting Cost in Low to High Order")


"""elif(n==2):
    # sort by cost H to L
    li.sort(reverse=True, key=lambda el: el["cost"])
    print(li)
elif(n==3):
    # sort by rating
    li.sort(reverse=True, key=lambda el: el["rating"])
    print(li)
elif(n==4):
    # sort by disc l to h
    li.sort(key=lambda el: el["discount"])
    print(li)
elif(n==5):
    # sort by disc h to l
    li.sort(reverse=True, key=lambda el: el["discount"])
    print(li)
else:
    print("Enter Valid Option")
"""


