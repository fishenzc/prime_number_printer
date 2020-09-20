#
# count_point = 0
# while count_point < 12:
#     speed1 = int(input("enter the car speed: "))
#
#
#     def speed_checking(speed):
#         if speed < 70:
#             print('your speed is good')
#         elif speed > 70:
#             if count_point == 12:
#                 print(f'you recorded {count_point} points, so License Suspended')
#             else:
#                 print(f'you recorded {count_point} points, slow your speed!!')
#     count_point += 1
#
#     speed_checking(speed1)


num = int(input('Enter any number: '))


def prime_number(limit):
    noOfPrimeNo = 0
    for i in range(limit + 1):
        count = 0
        for j in range(i + 1):
            if i % (j + 1) == 0:
                count += 1
        if count < 3:
            noOfPrimeNo += 1
            print(f'{i} is prime number')
    print(f'no of prime number between 0 to {limit} is {noOfPrimeNo}')


prime_number(num)
