class product:
    def __init__(p, i, n, c, b, cat, d, r):
        p.id = i
        p.name = n
        p.cost = c
        p.brand = b
        p.category = cat
        p.discount = d
        p.rating = r

    def showitems(self):
        # print(self.id ,self.name , self.cost, self.brand,self.category,self.discount,self.rating)
        print(self.__dict__)


p1 = product(1, "Realme U1", 12000, "Realme", "Mobile", "30%", 3.4)
p2 = product(2, "Realme XT", 15000, "Realme", "Mobile", "45%", 4.3)
p3 = product(3, "EliteBook", 120000, "HP", "Laptop", "50%", 4.1)
p4 = product(4, "Redmi note4", 10000, "Redmi", "Mobile", "60%", 3.8)
productList = list()
productList = [p1, p2, p3, p4]
print("   LIST OF PRODUCTS  ")
for i in productList:
    i.showitems()

print("        MENU       ")
print("1.Sort Cost in H to L ")
print("2.Sort Cost in L to H ")
print("3.Sort Discount in H to L ")
print("4.Sort Discount in L to H ")
print("5.Sort Rating in H to L")
n = int(input("Enter the option to Sort"))

l2 = [["cost", True], ["cost", False], ["discount", True], ["discount", False],["rating", True]]

productList.sort(key=lambda el: el.__getattribute__(l2[n - 1][0]), reverse=l2[n - 1][1])
for i in productList:
    i.showitems()


# To filter
# n1=int(input("Enter which field to filter"))
# name=input("Enter the name to Filter")
# dic=[
#     "brand",
#     "name",
#     "category",
#    ]
#
# newobj=filter(lambda el:el.__getattribute__(dic[n1-1])==name,productList)
# for i in newobj:
#     print('{id} {name} {cost} {rating}'.format(**i))

