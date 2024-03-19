def calculate_damage(prices, entry_point, item_type):
    left_sum = 0
    right_sum = 0

    if item_type == "cheap":
        for i in range(entry_point):
            if prices[i] < prices[entry_point]:
                left_sum += prices[i]
        for i in range(entry_point + 1, len(prices)):
            if prices[i] < prices[entry_point]:
                right_sum += prices[i]
    elif item_type == "expensive":
        for i in range(entry_point):
            if prices[i] >= prices[entry_point]:
                left_sum += prices[i]
        for i in range(entry_point + 1, len(prices)):
            if prices[i] >= prices[entry_point]:
                right_sum += prices[i]

    if left_sum >= right_sum:
        return f"Left - {left_sum}"
    else:
        return f"Right - {right_sum}"

if __name__ == "__main__":
    price = list(map(int, input().split(", ")))
    entryPoint = int(input())
    itemType = input()

    print(calculate_damage(price, entryPoint, itemType))