# list1 = [2,4,6,5,8,10]
# # target=5
def search(target):
    list1 = [2, 4, 6, 5, 8, 10]
    for i in list1:
        if i == target:
            return list1.index(target)
        continue
        # else:
        #     print("value is not present")

target=int(input("enter the target:"))
print(search(target))











