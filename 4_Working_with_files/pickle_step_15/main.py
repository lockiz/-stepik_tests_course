import pickle

file_name, check_sum = input(), int(input())
answer = ('Контрольные суммы не совпадают', 'Контрольные суммы совпадают')

with open(file_name, mode='rb') as file_pkl:
    data = pickle.load(file_pkl)
    nums = [i for i in data if isinstance(i, int)]

    if isinstance(data, dict):
        print(answer[sum(nums) == check_sum])
    else:
        print(answer[min(nums, default=0) * max(nums, default=0) == check_sum])
