import random

# task 1


# def guess_random_number(tries, start, stop):
#     random_num = random.randint(start, stop)
#     while tries != 0:
#         print(f"Number of tries remaining: {tries}")
#         user_guess = int(
#             input(f"Guess a number betwween {start} and {stop}: "))
#         if user_guess == random_num:
#             print("You guessed the corret number")
#             return
#         elif user_guess < random_num:
#             print("Guess higher")
#             tries -= 1
#         elif user_guess > random_num:
#             print("Guess lower.")
#             tries -= 1
#     else:
#         print(f"You have failed to guess the number: {random_num}")


# task 2
# def guess_random_num_linear(tries: int, start: int, stop: int) -> None:
#     computer_guess = random.randint(start, stop)
#     print(f"The random number is: {computer_guess}")
#     for number in range(start, stop+1):
#         print(f"Number of tries left: {tries}")
#         if number != computer_guess:
#             print(f"Wrong guess: {number}")
#             tries -= 1
#         else:
#             print(
#                 f"The program has guessed the right number: {number}")
#             return  # return None

#         if tries == 0:
#             print("Ran out of tries")
#             return


# Task 3
def guess_random_num_binary(tries, start, stop):
    random_num = random.randint(start, stop)
    low = start
    high = stop
    mid = (high + low)//2

    while tries > 0:
        print(f"Tries left: {tries}")
        print(f"Number to guess: {random_num}")
        if random_num == mid:
            print(f"Successful Guess: {random_num}")
            return
        elif random_num < mid:
            print(f"Guess lower: {random_num}, Tries left: {tries}")
            high = mid - 1
            tries -= 1
        elif random_num > mid:
            print(f"Guess higher: {random_num}, Tries left: {tries}")
            low = mid + 1
            tries -= 1
        else:
            print(f"Ran out of tries: {tries}")
            break


# TASK 1: test for success
# guess_random_number(5, 0, 10)
# TASK 2:
# guess_random_num_linear(5, 0, 10)
# TASK 3:
guess_random_num_binary(5, 0, 100)
