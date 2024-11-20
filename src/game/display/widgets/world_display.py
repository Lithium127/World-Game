


"""
Methods that must be overriden to make a functional widget

reset() - This is where you should reset any state for your widget. It gets called whenever the owning Frame is initialised, which can be when it is first displayed, when the user moves to a new Scene or when the screen is resized.

update() - This is where you should put the logic to draw your widget. It gets called every time asciimatics needs to redraw the screen (and so should always draw the entire widget).

process_event() - This is where you should put your code to handle mouse and keyboard events.

value - This must return the current value for the widget.

required_height() - This returns the minimum required height for your widget. It is used by the owning Layout to determine the size and location of your widget.
"""