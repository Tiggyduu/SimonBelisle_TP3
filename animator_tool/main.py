import random
from animator_tool import ui
from maya import cmds

def on_generate():
     print("yo")

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = ui.RandomAnimationGenerator()
    tool_window.build_ui()
    tool_window.generate.clicked.connect(on_generate)

    tool_window.show()

main()