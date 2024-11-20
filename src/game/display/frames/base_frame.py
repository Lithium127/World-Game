

from asciimatics.widgets import Frame

from ..theme import _THEME_NAME

class BaseFrame(Frame):
    
    def __init__(self, screen, height, width, data=None, on_load=None, has_border=True, hover_focus=False, name=None, title=None, x=None, y=None, has_shadow=False, reduce_cpu=False, is_modal=False, can_scroll=True):
        super().__init__(
            screen, 
            min(45, height), 
            min(150, width), 
            data, 
            on_load, 
            has_border, 
            hover_focus, 
            name, 
            title, 
            x, y, 
            has_shadow, 
            reduce_cpu, 
            is_modal, 
            can_scroll
        )
        self.set_theme(_THEME_NAME)