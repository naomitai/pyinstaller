

import time
import os

def game_start():
    print("歡迎來到冒險遊戲！")
    time.sleep(1)
    print("你身處在一個神秘的地方...")
    time.sleep(1)
    print("你的目標是找到通關的方法！")
    time.sleep(1)

def make_choice():
    print("\n選擇:")
    print("1. 開門")
    print("2. 往左走")
    print("3. 往右走")
    choice = input("請輸入選項的編號: ")
    return choice

def game_over():
    print("\n遊戲結束！你失敗了...")

def game_win():
    print("\n恭喜你通關了！")
    time.sleep(1)
    print("現在，準備關機...")
    time.sleep(2)
    os.system("shutdown /s /t 1")

def main():
    game_start()

    while True:
        choice = make_choice()

        if choice == "1":
            print("\n你打開了門，裡面是...")
            time.sleep(1)
            print("一隻巨大的怪物！")
            game_over()
            break
        elif choice == "2":
            print("\n你往左走，看到一扇門...")
            time.sleep(1)
            print("這扇門通向通關的道路！")
            game_win()
            break
        elif choice == "3":
            print("\n你往右走，發現一片迷霧...")
            time.sleep(1)
            print("你迷失在迷霧中...")
            game_over()
            break
        else:
            print("\n請輸入有效的選項！")

if __name__ == "__main__":
    main()
