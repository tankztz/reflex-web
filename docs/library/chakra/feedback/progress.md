---
components:
    - rx.chakra.Progress
---

```python exec
import reflex as rx
```

# Progress

Progress is used to display the progress status for a task that takes a long time or consists of several steps.

```python demo
rx.vstack(
    rx.progress(value=0, width="100%"),
    rx.progress(value=50, width="100%"),
    rx.progress(value=75, width="100%"),
    rx.progress(value=100, width="100%"),
    rx.progress(is_indeterminate=True, width="100%"),
    spacing="1em",
    min_width=["10em", "20em"],
)
```
