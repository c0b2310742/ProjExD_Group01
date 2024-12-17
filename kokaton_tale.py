import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

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
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()