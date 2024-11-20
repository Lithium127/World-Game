"""
Overrides for Asciimatics themes

import for each frame definition is not required, 
as long as this module is imported before 
"""


from asciimatics.widgets.utilities import THEMES

_THEME_NAME = "gametheme"

game_theme: dict[str,dict] = THEMES["bright"]
game_theme.update({
    
})

THEMES[_THEME_NAME] = game_theme