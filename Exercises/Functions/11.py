def generate_loading_bar(number):
    num_blocks = number // 10
    loading_bars = "[" + "%" * num_blocks + "." * (10 - num_blocks) + "]"

    return loading_bars

numb = int(input())
loading_bar = generate_loading_bar(numb)

if numb == 100:
    print("100% Complete!")
    print(loading_bar)
else:
    print(f'{numb}%', loading_bar)
    print("Still loading...")
