---
components:
    - rx.chakra.Switch
---

```python exec
import reflex as rx
```

# Switch

The Switch component is used as an alternative for the Checkbox component.
You can switch between enabled or disabled states.

```python demo exec
class SwitchState1(rx.State):
    checked: bool = False
    is_checked: bool = "Switch off!"

    def change_check(self, checked: bool):
        self.checked = checked
        if self.checked:
            self.is_checked = "Switch on!"
        else:
            self.is_checked = "Switch off!"


def switch_example():
    return rx.vstack(
        rx.heading(SwitchState1.is_checked),
        rx.switch(
            is_checked=SwitchState1.checked, on_change=SwitchState1.change_check
        ),
    )
```

You can also change the color scheme of the Switch component by passing the `color_scheme` argument.
The default color scheme is blue.

```python demo
rx.hstack(
    rx.switch(color_scheme="red"),
    rx.switch(color_scheme="green"),
    rx.switch(color_scheme="yellow"),
    rx.switch(color_scheme="blue"),
    rx.switch(color_scheme="purple"),
)
```