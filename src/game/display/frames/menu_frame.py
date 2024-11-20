from __future__ import annotations
import typing as t


from asciimatics.widgets import Layout, VerticalDivider, Widget

from .base_frame import BaseFrame

if t.TYPE_CHECKING:
    from asciimatics.screen import Screen

class MenuFrame(BaseFrame):
    
    def __init__(self, screen: Screen, active_pane: Widget, side_bar: Widget | list[Widget], top_bar = None, bottom_bar = None, on_load = None):
        super(MenuFrame, self).__init__(
            screen,
            screen.height, # Take the entire screen on load
            screen.width,
            can_scroll = False,
            on_load    = on_load,
            reduce_cpu = True,
        )
        
        if top_bar is not None:
            top_layout = Layout([1, 1, 1, 1, 1, 1])
            self.add_layout(top_layout)
            for wgt in top_bar:
                top_layout.add_widget(wgt[0], wgt[1])
        
        middle = Layout([70, 5, min(20, self.screen.width // 5)])
        self.add_layout(middle)
        middle.add_widget(active_pane, 0)
        
        middle.add_widget(VerticalDivider(Widget.FILL_FRAME), 1)
        
        if isinstance(side_bar, list):
            for wgt in side_bar:
                middle.add_widget(wgt, 2)
        else:
            middle.add_widget(side_bar, 2)
        
        if bottom_bar is not None:
            bottom_layout = Layout([1, 1, 1, 1, 1, 1])
            self.add_layout(bottom_layout)
            for wgt in bottom_bar:
                bottom_layout.add_widget(wgt[0], wgt[1])