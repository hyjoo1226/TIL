def permute(arr, start, end, result):
    if start == end:
        result.append(arr.copy())  # 현재 순열을 리스트에 추가
    else:
        for i in range(start, end + 1):
            arr[start], arr[i] = arr[i], arr[start]  # Swap
            permute(arr, start + 1, end, result)  # 재귀 호출
            arr[start], arr[i] = arr[i], arr[start]  # Swap back

def generate_permutations(elements):
    result = []
    permute(elements, 0, len(elements) - 1, result)
    return result

# 예제 사용
elements = [1, 2, 3, 4]
permutations = generate_permutations(elements)
print(permutations)

for perm in permutations:
    print(perm)