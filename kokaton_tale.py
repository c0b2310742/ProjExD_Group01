import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# スタート画面の描画
def start_screen(screen):
    # 画面の背景色
    screen.fill((0, 0, 0))  # 黒色

    # 日本語フォントの指定
    font_path = "meiryo.ttc"  # Windowsの「メイリオ」フォントを使用
    if os.path.exists(font_path):  # フォントファイルが存在するか確認
        title_font = pg.font.Font(font_path, 100)  # 日本語対応フォント（サイズ100）
        button_font = pg.font.Font(font_path, 60)  # STARTボタン用フォント（サイズ60）
    else:
        title_font = pg.font.SysFont("msgothic", 100)  # フォントがない場合はデフォルトフォント
        button_font = pg.font.SysFont("msgothic", 60)

    # タイトルテキスト
    title_text = title_font.render("コウカトンテイル", True, (255, 0, 0))  # オレンジ色の文字
    title_rect = title_text.get_rect(center=(400, 200))
    screen.blit(title_text, title_rect)

    # STARTボタンテキスト
    button_text = button_font.render("スタート", True, (255, 0, 0))  # 白い文字
    button_rect = button_text.get_rect(center=(400, 400))
    screen.blit(button_text, button_rect)

    pg.display.update()
    
    # STARTボタンが押されるまで待機
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:  # Enterキーでゲーム開始
                return  # メイン画面に進む

# ゲームのメイン関数
def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # こうかとんの画像読み込み
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 400, 300

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

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

        # 画面を更新
        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((800, 600))  # 画面の設定
    start_screen(screen)  # スタート画面の呼び出し
    main()  # ゲームのメイン画面を開始
    pg.quit()
    sys.exit()
