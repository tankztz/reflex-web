---
components:
    - rx.radix.themes.Switch
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from pcweb.templates.docpage import style_grid
from pcweb.pages.docs import vars
```

# Switch


A toggle switch alternative to the checkbox.

## Basic Example

```python demo
text(
    flex(
        switch(default_checked=True),
        "Sync Settings",
        gap="2",
    )
)

```

Here we set the `default_checked` prop to be `True` which sets the state of the switch when it is initially rendered.

## Usage


### Submitting a form using switch

The `name` of the switch is needed to submit with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must check the switch before the owning form can be submitted.

The `value` prop is only used for form submission, use the `checked` prop to control state of the `switch`.

```python demo exec
class FormSwitchState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_switch():
    return rx.vstack(
        rx.form(
            rx.vstack(
                switch(name="s1"),
                switch(name="s2"),
                switch(name="s3", required=True),
                rx.button("Submit", type_="submit"),
                width="100%",
            ),
            on_submit=FormSwitchState.handle_submit,
            reset_on_submit=True,
            width="100%",
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormSwitchState.form_data.to_string()),
        width="100%",
    )
```



### Control the value

The `checked` prop is used to control the state of the switch. 

The event `on_checked_change` is called when the state of the switch changes, when the `change_checked` event handler is called.

The `disabled` prop when `True`, prevents the user from interacting with the switch.

In our example below, even though the third switch is `disabled` we are still able to change whether it is checked or not using the `checked` prop. 


```python demo exec
class SwitchState2(rx.State):

    checked = True

    def change_checked(self, checked: bool):
        """Change the switch checked var."""
        self.checked = checked


def switch_example2():
    return rx.hstack(
        switch(
            checked=SwitchState2.checked,
            on_checked_change=SwitchState2.change_checked,
        ),
        switch(
            checked=~SwitchState2.checked,
            on_checked_change=lambda v: SwitchState2.change_checked(~v),
        ),
        switch(
            checked=SwitchState2.checked,
            on_checked_change=SwitchState2.change_checked,
            disabled=True,
        ),
    )
```

In this example we use the `~` operator, which is used to invert a var. To learn more check out [var operators]({vars.var_operations.path}).



## Styling

```python eval
style_grid(component_used=switch, component_used_str="switch", variants=["classic", "surface", "soft"], disabled=True, default_checked=True)
```


## Real World Example


```python demo exec
class FormSwitchState2(rx.State):
    form_data: dict = {}

    cookie_types: dict[str, bool] = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

    def update_cookies(self, cookie_type: str, enabled: bool):
        self.cookie_types[cookie_type] = enabled


def form_switch2():
    return rx.vstack(
            dialog_root(
                dialog_trigger(
                    button("View Cookie Settings", size="4", variant="outline")
                ),
                dialog_content(
                    rx.form(
                        dialog_title("Your Cookie Preferences"),
                        dialog_description(
                            "Change your cookie preferences.",
                            size="2",
                            margin_bottom="16px",
                        ),
                        flex(
                            text(
                                flex(
                                    "Required",
                                    switch(default_checked=True, disabled=True, name="required"),
                                    gap="2",
                                    justify="between",
                                ),
                                as_="div", size="2", margin_bottom="4px", weight="bold",
                            ),

                            *[flex(
                                text(cookie_type.capitalize(), as_="div", size="2", margin_bottom="4px", weight="bold"),
                                text(
                                    flex(
                                        rx.cond(
                                            FormSwitchState2.cookie_types[cookie_type],
                                            "Enabled",
                                            "Disabled",
                                        ),
                                        switch(
                                            name=cookie_type, 
                                            checked=FormSwitchState2.cookie_types[cookie_type], 
                                            on_checked_change=lambda checked: FormSwitchState2.update_cookies(cookie_type, checked)),
                                        gap="2",
                                    ),
                                    as_="div", size="2", margin_bottom="4px", weight="bold",
                                ),
                                direction="row", justify="between",
                            )
                            for cookie_type in ["functional", "performance", "analytics", "advertisement", "others"]],


                            
                            direction="column",
                            gap="3",
                        ),
                        flex(
                            button("Save & Accept", type_="submit"),
                            dialog_close(
                                button("Exit"),
                            ),
                            gap="3",
                            margin_top="16px",
                            justify="end",
                        ),
                        on_submit=FormSwitchState2.handle_submit,
                        reset_on_submit=True,
                        width="100%",
                    ),
                ),
            ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormSwitchState2.form_data.to_string()),
        width="100%",
    )
```
