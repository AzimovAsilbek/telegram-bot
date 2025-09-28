# import sqlite3
#
# conn = sqlite3.connect("pyment_system.db")
# cursor = conn.cursor()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Pyment_users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     deposit INTEGER,
#     withdraw INTEGER,
#     transfer INTEGER,
# )
# """)
# cursor.close()
# conn.close()

Users = {}
Deposits = {}

def add_users(userId, username):
    # user_band = Users.values()
    if userId in Users:
        print(f"ushbu id: {userId} band! ID egasi: {Users[userId]}")
    else:
        Users[userId] = username
        Deposits[userId] = 0
        print(f"Users List\n {Users}")


def deposit_users(userId,  username, deposits_amount):
    if userId in Users and Users[userId] == username:
        if deposits_amount > 0:
            Deposits[userId] += deposits_amount
            print(f"Depozit muvofaqiyatli tushdi: ${Deposits[userId]}")
        else:
            print("depozit 0 dan katta bo'lishi kere!")
    else:
        print(f"Ushbu {userId} va {username} topilmadi!")

def withdraw_users(userId, yourId, username, yourname, withdraw_amount):
    if userId and yourId in Users and Users[userId] == username and Users[yourId] == yourname:
        if withdraw_amount <= 0:
            if Deposits[userId] == 0:
                print(f"{Deposits[userId]} atiga shuncha mablag' bor!")
            print("Withdraw 0 dan katta bo'lishi kere!")
        else:
            Deposits[userId] -= withdraw_amount
            print(f"Withdraw muvofaqiyatli yechildi: ${withdraw_amount} va {Users[userId]} da ${Deposits[userId]} qoldi")
            Deposits[yourId] += withdraw_amount
            print(f"Withdraw muvofaqiyatli o'tkazildi: {Users[yourId]} ga ${withdraw_amount} o'tkazildi!")
    else:
        print(f"Ushbu {userId} va {username} topilmadi!")

def transfer_users(userId, userId2, username, username2, transfer_amount):
    if userId and userId2 in Users and Users[userId] == username and Users[userId2] == username2:
        if transfer_amount > 0:
            if Deposits[userId] < 0:
                print(f"Deposit {Deposits[userId]} atiga shuncha mablag' bor bundan ortiq yecha olmaysiz!")
                Deposits[userId] = transfer_amount
            Deposits[userId] -= transfer_amount
            print(f"Transfer muvofaqaiyatli yechildi: ${Deposits[userId]} {Users[userId]} da ${Deposits[userId]} qoldi! va")
            Deposits[userId2] += transfer_amount
            print(f"Transfer muvofaqaiyatli o'tkazildi: ${Deposits[userId2]}, {Users[userId2]} foydalanuvchiga!")
        else:
            print("Transfer 0 dan katta bo'lishi kere!")
    else:
        print(f"Ushbu {userId} va {username} topilmadi!")

def Display_users(users, deposits):
    print(f"\nUser List: {users} \nDeposits List: {deposits}")

def pyment_system():
    while True:
        print("\n ushbu tizim faqat dollor ($) da ishledi!")
        print("1. Add User")
        print("2. Deposit")
        print("3. withdraw")
        print("4. transfer")
        print("5. Display Users")
        print("6. Quit\n")
        inp1 = int(input("Enter your choise: "))
        if inp1 == 1:
            user_id_input = int(input("User id: "))
            user_name_input = input("User name: ")
            add_users(user_id_input, user_name_input)
        elif inp1 == 2:
            user_id = int(input("User id: "))
            user_name = input("User name: ")
            deposit = int(input(f"Deposit: "))
            print(deposit_users(user_id, user_name, deposit))
        elif inp1 == 3:
            user_id_withdraw = int(input("User id dan: "))
            your_id_withdraw = int(input("Your id ga: "))
            user_name_withdraw = input("User name dan: ")
            your_name_withdraw = input("Your name ga: ")
            withdraw = int(input("Withdraw: "))
            withdraw_users(user_id_withdraw, your_id_withdraw, user_name_withdraw, your_name_withdraw, withdraw)
        elif inp1 == 4:
            user_id1_trancfer = int(input("Your id dan: "))
            user_name1_trancfer = input("Your name dan: ")
            user_id2_trancfer = int(input("User id ga: "))
            user_name2_trancfer = input("User name ga: ")
            transfer = int(input("Transfer: "))
            transfer_users(user_id1_trancfer, user_id2_trancfer, user_name1_trancfer, user_name2_trancfer, transfer)
        elif inp1 == 5:
            Display_users(Users, Deposits)
        elif inp1 == 6:
            break
        else:
            print("invalid input. try again.")



if __name__ == "__main__":
    pyment_system()
