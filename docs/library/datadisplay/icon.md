---
components:
    - rx.radix.themes.Icon
    - rx.lucide.Icon
---

```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```

# Icon

The Icon component is used to display an icon from a library of icons. This implementation is based on the [Lucide Icons](https://lucide.dev/icons) where you can find a list of all available icons.


## Basic Example

To display an icon, specify the `tag` prop from the list of available icons.
Passing the tag as the first children is also supported and will be assigned to the `tag` prop.

The `tag` is expected to be in `snake_case` format, but `kebab-case` is also supported to allow copy-paste from [https://lucide.dev/icons](https://lucide.dev/icons).

```python demo
rdxt.flex(
    rx.lucide.icon("calendar"),
    rx.lucide.icon(tag="calendar"),
    gap="2",
)
```

## Styling

Icon from Lucide can be customized with the following props `stroke_width`, `size` and `color`.

### Stroke Width

```python demo
rdxt.flex(
    rx.lucide.icon("moon", stroke_width=1),
    rx.lucide.icon("moon", stroke_width=1.5),
    rx.lucide.icon("moon", stroke_width=2),
    rx.lucide.icon("moon", stroke_width=2.5),
    gap="2"
)
```


### Size

```python demo
rdxt.flex(
    rx.lucide.icon("zoom_in", size=15),
    rx.lucide.icon("zoom_in", size=20),
    rx.lucide.icon("zoom_in", size=25),
    rx.lucide.icon("zoom_in", size=30),
    align="center",
    gap="2",
)
```

### Color

Here is an example using basic colors in icons.

```python demo
rdxt.flex(
    rx.lucide.icon("zoom_in", size=18, color="indigo"),
    rx.lucide.icon("zoom_in", size=18, color="cyan"),
    rx.lucide.icon("zoom_in", size=18, color="orange"),
    rx.lucide.icon("zoom_in", size=18, color="crimson"),
    gap="2",
)
```

A radix color with a scale may also be specified using the `var()` token syntax seen below.

```python demo
rdxt.flex(
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-1)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-2)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-3)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-4)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-5)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-6)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-7)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-8)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-9)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-10)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-11)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--purple-12)"),
    gap="2",
)
```

Here is another example using the `accent` color with scales. The `accent` is the most dominant color in your theme.

```python demo
rdxt.flex(
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-1)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-2)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-3)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-4)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-5)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-6)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-7)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-8)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-9)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-10)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-11)"),
    rx.lucide.icon("zoom_in", size=18, color="var(--accent-12)"),
    gap="2",
)
```

## Final Example

Icons can be used as child components of many other components. For example, adding a magnifying glass icon to a search bar.

```python demo
rdxt.badge(
    rdxt.flex(
        rx.lucide.icon("search", size=18),
        rdxt.text("Search documentation...", size="3", weight="medium"),
        direction="row",
        gap="1",
        align="center",
    ),
    size="2",
    radius="full",
    color_scheme="gray",
)
```
