# 16. Write a function that takes a callback and applies it to every second element in a list.
def apply_every_second(lst, callback):
    return [callback(lst[i]) if i % 2 == 1 else lst[i] for i in range(len(lst))]

print(apply_every_second([1,2,3,4,5], lambda x: x*10))  # Output: [1, 20, 3, 40, 5]