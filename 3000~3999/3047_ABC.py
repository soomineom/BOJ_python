num1, num2, num3 = map(int, input().split())
seq = input()

nums = []
nums.append(num1)
nums.append(num2)
nums.append(num3)
nums.sort()

if seq == 'ABC':
    for i in range(3):
        print(nums[i], end=' ')
elif seq == 'ACB':
    print(nums[0], nums[2], nums[1])
elif seq == 'BAC':
    print(nums[1], nums[0], nums[2])
elif seq == 'BCA':
    print(nums[1], nums[2], nums[0])
elif seq == 'CAB':
    print(nums[2], nums[0], nums[1])
elif seq == 'CBA':
    print(nums[2], nums[1], nums[0])
