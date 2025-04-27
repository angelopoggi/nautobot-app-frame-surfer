"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:frame_surfer:framesurferexamplemodel_list",
        name="Frame Surfer",
        permissions=["frame_surfer.view_framesurferexamplemodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:frame_surfer:framesurferexamplemodel_add",
                permissions=["frame_surfer.add_framesurferexamplemodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Frame Surfer", items=tuple(items)),),
    ),
)
