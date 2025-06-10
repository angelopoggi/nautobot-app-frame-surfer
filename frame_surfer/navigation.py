"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:frame_surfer:frametv_list",
        name="Frame Surfer",
        permissions=["frame_surfer.view_frametv"],
        buttons=(
            NavMenuAddButton(
                link="plugins:frame_surfer:frametv_add",
                permissions=["frame_surfer.add_frametv"],
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:frame_surfer:unsplashmodel_list",
        name="Unsplash Model",
        permissions=["frame_surfer.view_unsplashmodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:frame_surfer:unsplashmodel_add",
                permissions=["frame_surfer.add_unsplashmodel"],
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
