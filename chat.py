import os
import sys
import pygame as pg
import random
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 新機能の関数追加
def handle_kk_movement(kk_rct, key_lst):
    move_x, move_y = 0, 0
    if key_lst[pg.K_w]:  # 上
        move_y -= 5
    if key_lst[pg.K_s]:  # 下
        move_y += 5
    if key_lst[pg.K_a]:  # 左
        move_x -= 5
    if key_lst[pg.K_d]:  # 右
        move_x += 5
    kk_rct.move_ip(move_x, move_y)
    return kk_rct

def display_attack_effect(screen, kk_rct, attack_img):
    effect_rect = attack_img.get_rect()
    effect_rect.center = kk_rct.centerx + 50, kk_rct.centery
    screen.blit(attack_img, effect_rect)

def enemy_attack(screen, enemy_rct, attack_img):
    effect_rect = attack_img.get_rect()
    effect_rect.center = enemy_rct.centerx - 50, enemy_rct.centery + random.randint(-30, 30)
    screen.blit(attack_img, effect_rect)

def draw_status(screen, score, hp):
    font = pg.font.Font(None, 36)
    score_text = font.render(f"Units: {score}", True, (255, 255, 255))
    hp_text = font.render(f"HP: {hp}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(hp_text, (10, 50))

def use_healing_item(hp, healing_amount):
    return min(100, hp + healing_amount)  # HP最大値を100とする

def drop_item():
    items = ["healing", "none"]  # ドロップするアイテム
    return random.choice(items)

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    attack_img = pg.Surface((10, 10))  # 攻撃エフェクト（仮のSurface）
    attack_img.fill((255, 0, 0))

    kk_rct = kk_img.get_rect()
    kk_rct.center = 400, 300
    tmr = 0
    score = 0
    hp = 100

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_lst = pg.key.get_pressed()
        kk_rct = handle_kk_movement(kk_rct, key_lst)

        # 背景描画
        screen.blit(bg_img, (0, 0))
        screen.blit(kk_img, kk_rct)

        # 攻撃エフェクト表示
        if key_lst[pg.K_SPACE]:
            display_attack_effect(screen, kk_rct, attack_img)
        
        # ステータス表示
        draw_status(screen, score, hp)

        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()