from __future__ import annotations
import typing as t

from asciimatics.widgets import ListBox, TextBox, Widget

from .frames.menu_frame import MenuFrame

if t.TYPE_CHECKING:
    from asciimatics.screen import Screen

class WorldView(MenuFrame):
    
    def __init__(self, screen: Screen):
        
        self._view_frame = TextBox(Widget.FILL_FRAME)
        self._inv_list = ListBox(
            Widget.FILL_FRAME,
            [("TESTING", None)]
        )
        
        super().__init__(
            screen,
            active_pane = self._view_frame,
            side_bar    = self._inv_list,
            on_load     = self.on_load,
        )
        
        self.fix()
    
    def on_load(self) -> None:
        pass