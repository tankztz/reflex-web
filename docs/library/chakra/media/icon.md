---
components:
    - rx.chakra.Icon
---

```python exec
import reflex as rx
from reflex.components.media.icon import ICON_LIST
```

# Icon

The Icon component is used to display an icon from a library of icons.

```python demo
rx.icon(tag="calendar")
```

Use the tag prop to specify the icon to display.

```md alert success
Below is a list of all available icons.
```

```python eval
rx.box(
    rx.divider(),
    rx.responsive_grid(
        *[
            rx.vstack(
                rx.icon(tag=icon),
                rx.text(icon),
                bg="white",
                border="1px solid #EAEAEA",
                border_radius="0.5em",
                padding=".75em",
            )
            for icon in ICON_LIST
        ],
        columns=[2, 2, 3, 3, 4],
        spacing="1em",
    )
)
```