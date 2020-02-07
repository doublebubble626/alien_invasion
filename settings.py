class Settings():
    def __init__(self):
        #初始化游戏设置
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_colour=(230,230,230)

        #飞船的设置
        self.ship_speed_factor=1.5

        #子弹的设置
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_colour=(60,60,60)
        self.bullets_allowed=4

        #外星人设置
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        self.fleet_direction=1



