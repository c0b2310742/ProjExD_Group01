import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # こうかとんの画像読み込み
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 400, 300

    # メニュー関連の変数
    menu_active = False  # メニューが表示中か
    item_menu_active = False  # アイテム選択メニューが表示中か
    menu_options = ["戦う", "アイテム", "逃げる"]  # メインメニューの選択肢
    item_options = ["カレー", "かつ丼"]  # アイテム選択メニューの選択肢
    selected_option = 0  # メインメニューの選択中番号
    selected_item_option = 0  # アイテムメニューの選択中番号

    # アイテムの所持数
    inventory = {"カレー": 2, "かつ丼": 1}

    font = pg.font.SysFont("msgothic", 50)

    def draw_menu():
        """メニューを画面に表示する関数"""
        base_y = 550
        option_spacing = 200
        start_x = 200
        for i, option in enumerate(menu_options):
            color = (255, 0, 0) if i == selected_option else (255, 255, 255)
            text = font.render(option, True, color)
            rect = text.get_rect(center=(start_x + i * option_spacing, base_y))
            screen.blit(text, rect)

    def draw_item_menu():
        """アイテム選択メニューを画面に表示する関数"""
        base_y = 300
        option_spacing = 300
        start_x = 150
        for i, option in enumerate(item_options):
            # アイテムの所持数を表示
            item_count = inventory.get(option, 0)
            display_text = f"{option} ({item_count})"
            color = (0, 255, 0) if i == selected_item_option else (255, 255, 255)
            text = font.render(display_text, True, color)
            rect = text.get_rect(center=(start_x + i * option_spacing, base_y))
            screen.blit(text, rect)

    def use_item(item):
        """アイテムを使用する処理"""
        if inventory.get(item, 0) > 0:
            # アイテムを使用
            inventory[item] -= 1
            print(f"{item} を使用しました！")
        else:
            # アイテムがない場合のメッセージ
            print(f"{item} を持っていません！")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if item_menu_active:  # アイテム選択メニューが表示中の場合
                    if event.key == pg.K_LEFT:  # 左キーで選択肢を左に移動
                        selected_item_option = (selected_item_option - 1) % len(item_options)
                    elif event.key == pg.K_RIGHT:  # 右キーで選択肢を右に移動
                        selected_item_option = (selected_item_option + 1) % len(item_options)
                    elif event.key == pg.K_RETURN:  # Enterキーでアイテムを使用
                        selected_item = item_options[selected_item_option]
                        use_item(selected_item)
                        item_menu_active = False
                        menu_active = False  # メインメニューも閉じる
                    elif event.key == pg.K_ESCAPE:  # ESCキーでアイテム選択メニューを閉じる
                        item_menu_active = False
                elif menu_active:  # メインメニューが表示中の場合
                    if event.key == pg.K_LEFT:  # 左キーで選択肢を左に移動
                        selected_option = (selected_option - 1) % len(menu_options)
                    elif event.key == pg.K_RIGHT:  # 右キーで選択肢を右に移動
                        selected_option = (selected_option + 1) % len(menu_options)
                    elif event.key == pg.K_RETURN:  # Enterキーで選択を決定
                        if menu_options[selected_option] == "アイテム":
                            item_menu_active = True  # アイテムメニューを表示
                        else:
                            print(f"{menu_options[selected_option]} を選びました！")
                            menu_active = False  # メニューを閉じる
                    elif event.key == pg.K_ESCAPE:  # ESCキーでメニューを閉じる
                        menu_active = False
                else:  # メニュー非表示時
                    if event.key == pg.K_SPACE:  # スペースキーでメニュー表示
                        menu_active = True

        if not menu_active and not item_menu_active:  # メニュー非表示時の移動処理
            # キー操作
            key_lst = pg.key.get_pressed()
            move_x, move_y = 0, 0
            if key_lst[pg.K_UP]:
                move_y -= 1
            if key_lst[pg.K_DOWN]:
                move_y += 1
            if key_lst[pg.K_RIGHT]:
                move_x += 2
            if key_lst[pg.K_LEFT]:
                move_x -= 2

            # こうかとんの移動処理
            kk_rct.move_ip(move_x, move_y)

        # 背景を黒に塗りつぶす
        screen.fill((0, 0, 0))

        # こうかとんを描画
        screen.blit(kk_img, kk_rct)

        # メニューがアクティブならメニューを描画
        if menu_active and not item_menu_active:
            draw_menu()

        # アイテム選択メニューがアクティブならアイテムメニューを描画
        if item_menu_active:
            draw_item_menu()

        # 画面を更新
        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
