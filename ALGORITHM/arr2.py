# arr1 = [0] * 3
#
# arr2 = [[0] * 3 for _ in range(2)]
# # print(arr1)
# # print(*arr1)
# # for i in range(2):
# #     print(*arr2[i])
# for i in range(2):
#     for j in range(3):
#         print(arr2[i][j], end = ' ')
#     print()
# arr = [[1,2,3], [4,5,6]]
# print(len(arr))
# print(len(arr[0]))

# arr - [[0]*3]*2 #한 곳이 아니라 두 곳 다 바뀌므로 사용x(arr[0]과 arr[1]이 같은 곳을 가리킴
# print(arr)
# arr[0][0]=1
# print(arr)