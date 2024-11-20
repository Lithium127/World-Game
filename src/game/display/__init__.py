from __future__ import annotations
import typing as t
import sys

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError

from . import theme
from .worldview import WorldView

if t.TYPE_CHECKING:
    pass

def _start_gui(screen: Screen, last_scene: Scene):
    scenes = [
        Scene([WorldView(screen)], -1, True, "worldview")
    ]
    
    screen.play(scenes, stop_on_resize=True, start_scene=last_scene)


def start_resizable():
    last_scene = None
    
    while True:
        try:
            Screen.wrapper(_start_gui, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene