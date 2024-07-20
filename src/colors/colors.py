class Colors:
    dark_gray = (26,31,40)
    green = (33, 175, 75)
    red = (234, 24, 30)
    orange = (250, 125, 41)
    yellow = (250, 198, 13)
    purple = (161, 74, 160)
    cyan = (0, 161, 233)
    blue = (58, 69, 200)
    white = (255,255,255)
    dark_blue = (44,44,127)
    light_blue = (59, 85, 162)
    black = (0, 0, 0)
    turquoise = (52, 241, 232)
    gray = (150,150,150)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_gray,cls.green,cls.red,cls.orange,cls.yellow,cls.purple,cls.cyan,cls.blue]