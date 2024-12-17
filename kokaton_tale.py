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
    menu_options = ["fight", "item", "run"]  # 日本語の選択肢
    selected_option = 0  # 選択中のメニュー番号

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

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if not menu_active:  # メニュー非表示時
                    if event.key == pg.K_SPACE:  # スペースキーでメニュー表示
                        menu_active = True
                else:  # メニュー表示時
                    if event.key == pg.K_LEFT:  # 左キーで選択肢を左に移動
                        selected_option = (selected_option - 1) % len(menu_options)
                    elif event.key == pg.K_RIGHT:  # 右キーで選択肢を右に移動
                        selected_option = (selected_option + 1) % len(menu_options)
                    elif event.key == pg.K_RETURN:  # Enterキーで選択を決定
                        print(f"{menu_options[selected_option]} を選びました！")
                        menu_active = False  # メニューを閉じる
                    elif event.key == pg.K_ESCAPE:  # ESCキーでメニューを閉じる
                        menu_active = False

        if not menu_active:  # メニュー非表示時の移動処理
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
        if menu_active:
            draw_menu()

        # 画面を更新
        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()