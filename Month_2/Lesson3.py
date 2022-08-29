# import random
# count = 0
# a = 0
# while count <= 100:
#     print(a, count)
#     a += 1
#     count += random.randrange(20)
# print("done")


# import random
# total = 0
# while total >= 0:
#     print(total)
#     total += random.randrange(20)
# print("done")
# a = 0
# while True:
#     print(a)
#     a += 10
# import random
#
# player = input('Please enter your name ')
# player_count = 0
# bot_count = 0
# tie = 0
# while True:
#     print(f"Kalit so'zlar\n"
#           f"1-Tosh\n"
#           f"2-Qaychi\n"
#           f"3-Qog'oz\n")
#     response = input(f"{player} Kalit so'zlar raqamini kiriting>> ")
#     bot = random.choice(['Tosh', 'Qaychi', 'Qog\'oz'])
#     if (response == '1' and bot == 'Qaychi') or (response == '2' and bot == 'Qog\'oz') or (
#             response == '3' and bot == 'Tosh'):
#         print(f"{player} is winner!!!")
#         player_count += 1
#         choice = input('Whould you like play again? ')
#         if choice == 'Yes':
#             pass
#         elif choice == 'No':
#             print(f"{player} : {player_count}\n"
#                   f"Bot : {bot_count}\n"
#                   f"Tie : {tie}\n"
#                   f"Game end")
#             break
#
#     elif (response == '1' and bot == 'Tosh') or (response == '2' and bot == 'Qaychi') or (
#             response == '3' and bot == 'Qog\'oz'):
#         print("Tie")
#         tie += 1
#         choice = input('Whould you like play again? ')
#         if choice == 'Yes':
#             pass
#         elif choice == 'No':
#             print(f"{player} : {player_count}\n"
#                   f"Bot : {bot_count}\n"
#                   f"Tie : {tie}\n"
#                   f"Game end")
#
#             break
#     elif (response == '1' and bot == 'Qog\'oz') or (response == '2' and bot == 'Tosh') or (
#             response == '3' and bot == 'Qaychi'):
#         bot_count += 1
#         print("Bot is winner!!!")
#         choice = input('Whould you like play again? ')
#         if choice == 'Yes':
#             pass
#         elif choice == 'No':
#             print(f"{player} : {player_count}\n"
#                   f"Bot : {bot_count}\n"
#                   f"Tie : {tie}\n"
#                   f"Game end")
#             break
#     else:
#         print("Is not DEFINED!!!")
#         print("Please enter again ")
# a = 27
# b = 5
# while a > b:
#     a = a - b
# print(a)
a = 38
b = 5
result = 0
while a >= b:
    a = a - b
    result += 1
print(result, ".", a)
