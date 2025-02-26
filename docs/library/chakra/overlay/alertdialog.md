---
components:
    - rx.chakra.AlertDialog
    - rx.chakra.AlertDialogOverlay
    - rx.chakra.AlertDialogContent
    - rx.chakra.AlertDialogHeader
    - rx.chakra.AlertDialogBody
    - rx.chakra.AlertDialogFooter
---

```python exec
import reflex as rx
```

# AlertDialog

AlertDialog component is used to interrupt the user with a mandatory confirmation or event.
The component will appear in front of the page prompting the user to conplete an event.

```python demo exec
class AlertDialogState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


def alertdialog_example():
    return rx.vstack(
        rx.button("Show Alert Dialog", on_click=AlertDialogState.change),
        rx.alert_dialog(
            rx.alert_dialog_overlay(
                rx.alert_dialog_content(
                    rx.alert_dialog_header("Confirm"),
                    rx.alert_dialog_body("Do you want to confirm example?"),
                    rx.alert_dialog_footer(
                        rx.button("Close", on_click=AlertDialogState.change)
                    ),
                )
            ),
            is_open=AlertDialogState.show,
        ),
        width="100%",
    )
```