from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import QCoreApplication as QCApp

class Action(QAction):

    def __init__(self, *args, icon=None, action_name="Test", tip="Test tip",
                 func=lambda: None,
                 parent=None):

        print(f"[DEBUG]: Action > __init__: func is: {type(func)}")

        if icon is None:
            super().__init__(action_name, parent)
        else:
            super().__init__(QIcon(icon), action_name, parent)

        self.setStatusTip(tip)

        self.icon_initial = QIcon(icon)

        if str(type(func)) == "<class 'builtin_function_or_method'>":
            self.triggered.connect(func)
        else:
            self.triggered.connect(
                lambda checked: self.handle_trigger(checked, func, *args)
            )


    def handle_trigger(self, checked, func, *args):
        icon_pref = f"./icon/{self.text()}"
        icon_ext = "png"

        icon_checked = f"{icon_pref}_checked.{icon_ext}"
        icon_unchecked = f"{icon_pref}.{icon_ext}"

        print((f"[DEBUG] Action > handle_trigger:  toggled for {self.text()}"
               f" with checked state = {checked}"
               f", func type: {type(func)} " f", args: {args}")
              )

        # Reset icons to initial icon:
        toolbar = QCApp.instance().active_window.toolbar
        toolbar_actions = toolbar.get_group_actions("root")
        for action in toolbar_actions:
            print(f"[DEBUG]: Action > handle_trigger: actions w/ action: {action.text()}")
            action.setIcon(action.icon_initial)

        if checked:
            self.setIcon(QIcon(icon_checked))

        # Lastly call our pass-thru function with any args
        if len(args) > 0:
            func(checked, *args)
        else:
            func(checked)
