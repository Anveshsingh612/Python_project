def countTriplets(arr,n):
    new_arr=[0 for i in range(100)]

    for i in range(n):
        new_arr[arr[i]] += 1
    count = 0
    for i in range(n):
        for j in range(i+1,n,1):
            if(new_arr[arr[i]+arr[j]]):
                count += 1
    return count
arr = []
n=int(input("enter no of list"))

for i in range(0,n):
    ele = int(input())
    arr.append(ele)
print("Given array is",arr)

print("No of Triplets:",countTriplets(arr,n))

