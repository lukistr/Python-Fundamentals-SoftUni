def next_version(version):
    nums = version.split('.')
    nums = list(map(int, nums))
    nums[-1] += 1

    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == 10:
            nums[i] = 0
            nums[i - 1] += 1
        else:
            break

    return '.'.join(map(str, nums))

input_version = input()
print(next_version(input_version))
