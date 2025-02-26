"""Template for documentation pages."""

import textwrap
from typing import Any, Callable

import black

import reflex as rx
from pcweb import styles
from pcweb.components.logo import navbar_logo
from pcweb.route import Route, get_path
from pcweb.styles import colors as c
from pcweb.styles import font_weights as fw
from pcweb.styles import text_colors as tc
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *


@rx.memo
def code_block(code: str, language: str):
    return rx.box(
        rx.code_block(
            code,
            border_radius=styles.DOC_BORDER_RADIUS,
            theme="light",
            background="transparent",
            language=language,
            code_tag_props={
                "style": {
                    "fontFamily": "inherit",
                }
            },
        ),
        rx.button(
            rx.icon(tag="copy"),
            on_click=rx.set_clipboard(code),
            position="absolute",
            top="0.5em",
            right="0.5em",
            color=tc["docs"]["body"],
            background="transparent",
            _hover={
                "background": "transparent",
                "color": styles.ACCENT_COLOR,
            },
        ),
        border_radius=styles.DOC_BORDER_RADIUS,
        border="2px solid #F4F3F6",
        position="relative",
        margin_bottom="1em",
        width="100%",
    )


def code_block_markdown(*children, **props):
    language = props.get("language", "none")
    return code_block(code=children[0], language=language)


# Docpage styles.
demo_box_style = {
    "bg": "rgba(255,255,255, 0.5)",
    "border_radius": "8px;",
    "box_shadow": "rgba(99, 99, 99, 0.1) 0px 2px 8px 0px;",
    "padding": 5,
    "width": "100%",
    "overflow_x": "auto",
    "border": "2px solid #F4F3F6",
    "align_items": "center",
    "justify_content": "center",
}
link_style = {
    "color": "#494369",
    "font_weight": "600",
    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
    "background": "radial-gradient(82.06% 100% at 50% 100%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.2) 100%), #FEFEFF;",
    "_hover": {
        "boxShadow": "0px 0px 0px 3px rgba(149, 128, 247, 0.6), 0px 2px 3px rgba(3, 3, 11, 0.2), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.01), inset 0px 0px 0px 1px rgba(32, 17, 126, 0.4), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.36);"
    },
    "padding_x": "0.5em",
    "border_radius": "8px",
}

logo_style = {
    "height": "1em",
    "opacity": 0.2,
}
logo = navbar_logo(**logo_style)


def doc_section(*contents):
    return rx.box(
        *contents,
        margin_top="1em",
        margin_left=".5em",
        border_left="1px #F4F3F6 solid",
        padding_left="1em",
        width="100%",
    )


def my_form():
    from pcweb.components.navbar import NavbarState

    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Email (optional)",
                id="email",
                type_="email",
                width="100%",
                font_size=".8em",
                _active={
                    "border": "none",
                    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
                },
                _focus={
                    "border": "none",
                    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
                },
                _placeholder={
                    "color": "#A9A7B1",
                    "font_weight": "400",
                },
                border_radius="8px",
                border="none",
                box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
            ),
            rx.text_area(
                placeholder="Your Feedback...",
                id="feedback",
                width="100%",
                font_size=".8em",
                _active={
                    "border": "none",
                    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
                },
                _focus={
                    "border": "none",
                    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
                },
                _placeholder={
                    "color": "#A9A7B1",
                    "font_weight": "400",
                },
                border_radius="8px",
                border="none",
                box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
            ),
            rx.hstack(
                rx.spacer(),
                rx.button(
                    "Send",
                    type_="submit",
                    size="sm",
                    style=styles.BUTTON_LIGHT,
                ),
                width="100%",
            ),
            padding_x=".5em",
            width="100%",
        ),
        on_submit=NavbarState.handle_submit,
        padding_bottom=".2em",
        width="100%",
    )


def docpage(set_path: str | None = None, t: str | None = None) -> rx.Component:
    """A template that most pages on the pynecone.io site should use.

    This template wraps the webpage with the navbar and footer.

    Args:
        set_path: The path to set for the sidebar.
        prop: Props to apply to the template.

    Returns:
        A wrapper function that returns the full webpage.
    """

    def docpage(contents: Callable[[], Route]) -> Route:
        """Wrap a component in a docpage template.

        Args:
            contents: A function that returns a page route.

        Returns:
            The final route with the template applied.
        """
        # Get the path to set for the sidebar.
        path = get_path(contents) if set_path is None else set_path

        # Set the page title.
        title = contents.__name__.replace("_", " ").title() if t is None else t

        def wrapper(*args, **kwargs) -> rx.Component:
            """The actual function wrapper.

            Args:
                *args: Args to pass to the contents function.
                **kwargs: Kwargs to pass to the contents function.

            Returns:
                The page with the template applied.
            """
            # Import here to avoid circular imports.
            from pcweb.components.navbar import feedback_button, navbar
            from pcweb.components.sidebar import get_prev_next
            from pcweb.components.sidebar import sidebar as sb

            # Create the docpage sidebar.
            sidebar = sb(url=path)

            # Set the sidebar path for the navbar sidebar.
            nav_sidebar = sb(url=path)

            # Get the previous and next sidebar links.
            prev, next = get_prev_next(path)
            links = []

            # Create the previous component link.
            if prev:
                next_prev_name = (
                    prev.alt_name_for_next_prev
                    if prev.alt_name_for_next_prev
                    else prev.names
                )
                links.append(
                    rx.link(
                        "← " + next_prev_name,
                        href=prev.link,
                        style=link_style,
                    )
                )
            else:
                links.append(rx.box())

            # Create the next component link.
            if next:
                next_prev_name = (
                    next.alt_name_for_next_prev
                    if next.alt_name_for_next_prev
                    else next.names
                )
                links.append(
                    rx.link(
                        next_prev_name + " →",
                        href=next.link,
                        style=link_style,
                    )
                )
            else:
                links.append(rx.box())

            if not isinstance(contents, rx.Component):
                comp = contents(*args, **kwargs)
            else:
                comp = contents

            # Return the templated page.
            return rx.box(
                navbar(sidebar=nav_sidebar),
                rx.box(
                    rx.flex(
                        rx.desktop_only(
                            sidebar,
                            width=["0", "0%", "25%"],
                            padding_y="2em",
                            padding_left=["1em", "2em", "2em", "2m", "2em"],
                        ),
                        rx.box(
                            rx.box(comp),
                            rx.hstack(
                                *links,
                                justify="space-between",
                                margin_y="3em",
                            ),
                            rx.spacer(),
                            rx.center(
                                feedback_button(),
                                width="100%",
                            ),
                            rx.box(height="2em"),
                            rx.hstack(
                                logo,
                                rx.spacer(),
                                rx.text(
                                    "Copyright © 2023 Pynecone, Inc.", color="#CDCCD1"
                                ),
                                width="100%",
                            ),
                            border_left=[
                                "none",
                                "none",
                                "none",
                                "none",
                                "1px solid #F4F3F6",
                            ],
                            padding_x=styles.PADDING_X,
                            width=["100%", "100%", "100%", "75%"],
                            padding_y="2em",
                            height="100%",
                        ),
                    ),
                    max_width="80em",
                    margin_x="auto",
                    margin_top="1em",
                    height="100%",
                ),
                color=tc["docs"]["body"],
                background="radial-gradient(35.39% 37.5% at 100% 0%, rgba(188, 136, 255, 0.08) 0%, rgba(255, 255, 255, 0) 100%)",
                background_attachment="fixed",
                font_family=styles.SANS,
            )

        # Return the route.
        return Route(
            path=path,
            title=title,
            component=wrapper,
        )

    return docpage


@rx.memo
def text_comp(text: rx.Var[str]) -> rx.Component:
    return rx.text(text, margin_bottom="1em", font_size=styles.TEXT_FONT_SIZE)


@rx.memo
def code_comp(text: rx.Var[str]) -> rx.Component:
    return rx.code(text, color="#1F1944", bg="#EAE4FD")


def h_comp_common(
    text: rx.Var[str],
    heading: str,
    font_size: list[str] | str,
    font_weight: str,
    margin_top: str,
    scroll_margin: str,
) -> rx.Component:
    id_ = text.to(list[str])[0].lower().split().join("-")
    href = rx.State.router.page.full_path + "#" + id_

    return rx.box(
        rx.link(
            rx.hstack(
                rx.heading(
                    text,
                    id=id_,
                    as_=heading,
                    font_size=font_size,
                    font_weight=font_weight,
                    scroll_margin=scroll_margin,
                ),
                rx.icon(
                    tag="link",
                    color="#696287",
                    _hover={
                        "color": styles.ACCENT_COLOR,
                    },
                ),
                align_items="center",
            ),
            _hover={
                "cursor": "pointer",
                "textDecoration": "none",
            },
            href=href,
            on_click=lambda: rx.set_clipboard(href),
        ),
        rx.divider(margin_y="1em"),
        margin_top=margin_top,
        color=tc["docs"]["header"],
        width="100%",
    )


@rx.memo
def h1_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        font_size=styles.H1_FONT_SIZE,
        font_weight=fw["heading"],
        margin_top="0",
        scroll_margin="4em",
    )


@rx.memo
def h2_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        font_size=styles.H3_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1.5em",
        scroll_margin="5em",
    )


@rx.memo
def h3_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h3",
        font_size=styles.H4_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1.5em",
        scroll_margin="5em",
    )


@rx.memo
def h4_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h4",
        font_size=styles.H4_FONT_SIZE,
        font_weight=fw["subheading"],
        margin_top="1.5em",
        scroll_margin="6em",
    )


def doccmdoutput(
    command: str,
    output: str,
) -> rx.Component:
    """Create a documentation code snippet.

    Args:
        command: The command to display.
        output: The output of the command.
        theme: The theme of the component.

    Returns:
        The styled command and its example output.
    """
    return flex(
        flex(
            icon(tag="double_arrow_right", color="white", width=18, height=18),
            rx.code_block(
                command,
                border_radius=styles.DOC_BORDER_RADIUS,
                background="transparent",
                theme="a11y-dark",
                language="bash",
                code_tag_props={
                    "style": {
                        "fontFamily": "inherit",
                    }
                },
            ),
            rx.button(
                rx.icon(tag="copy"),
                on_click=rx.set_clipboard(command),
                position="absolute",
                top="0.5em",
                right="0.5em",
                color=tc["docs"]["body"],
                background="transparent",
                _hover={
                    "background": "transparent",
                    "color": styles.ACCENT_COLOR,
                },
            ),
            direction="row",
            align="center",
            gap="1",
            margin_left="1em",
        ),
        separator(size="4", color_scheme="green"),
        flex(
            rx.code_block(
                output,
                border_radius=styles.DOC_BORDER_RADIUS,
                background="transparent",
                theme="a11y-dark",
                language="log",
                code_tag_props={
                    "style": {
                        "fontFamily": "inherit",
                    }
                },
            ),
        ),
        direction="column",
        gap="2",
        border_radius=styles.DOC_BORDER_RADIUS,
        border="2px solid #F4F3F6",
        position="relative",
        margin="1em",
        width="100%",
        background_color="black",
    )


def doccode(
    code: str,
    language: str = "python",
    lines: tuple[int, int] | None = None,
    theme: str = "light",
) -> rx.Component:
    """Create a documentation code snippet.

    Args:
        code: The code to display.
        language: The language of the code.
        lines: The start/end lines to display.
        props: Props to apply to the code snippet.

    Returns:
        The styled code snippet.
    """
    # For Python snippets, lint the code with black.
    if language == "python":
        code = black.format_str(
            textwrap.dedent(code), mode=black.FileMode(line_length=60)
        ).strip()

    # If needed, only display a subset of the lines.
    if lines is not None:
        code = textwrap.dedent(
            "\n".join(code.strip().split("\n")[lines[0] : lines[1]])
        ).strip()

    # Create the code snippet.
    cb = code_block
    return cb(
        code=code,
        language=language,
    )


def docdemobox(*children, **props) -> rx.Component:
    """Create a documentation demo box with the output of the code.

    Args:
        children: The children to display.

    Returns:
        The styled demo box.
    """
    return rx.vstack(
        *children,
        style=demo_box_style,
        **props,
    )


def docdemo(
    code: str,
    state: str | None = None,
    comp: rx.Component | None = None,
    context: bool = False,
    demobox_props: dict[str, Any] | None = None,
    **props,
) -> rx.Component:
    """Create a documentation demo with code and output.

    Args:
        code: The code to render the component.
        state: Code for any state needed for the component.
        comp: The pre-rendered component.
        context: Whether to wrap the render code in a function.
        props: Additional props to apply to the component.

    Returns:
        The styled demo.
    """
    # Render the component if necessary.
    if comp is None:
        comp = eval(code)

    # Wrap the render code in a function if needed.
    if context:
        code = f"""def index():
        return {code}
        """

    # Add the state code
    if state is not None:
        code = state + code

    # Create the demo.
    return rx.vstack(
        docdemobox(comp, **(demobox_props or {})),
        doccode(code),
        width="100%",
        padding_bottom="2em",
        spacing="1em",
        **props,
    )


def doclink(text: str, href: str, **props) -> rx.Component:
    """Create a styled link for doc pages.

    Args:
        text: The text to display.
        href: The link to go to.
        props: Props to apply to the link.

    Returns:
        The styled link.
    """
    return rx.link(text, href=href, style=styles.LINK_STYLE, **props)


def doclink2(text: str, **props) -> rx.Component:
    """Create a styled link for doc pages.

    Args:
        text: The text to display.
        href: The link to go to.
        props: Props to apply to the link.

    Returns:
        The styled link.
    """
    return rx.link(text, style=styles.LINK_STYLE, **props)


def definition(title: str, *children) -> rx.Component:
    """Create a definition for a doc page.

    Args:
        title: The title of the definition.
        children: The children to display.

    Returns:
        The styled definition.
    """
    return rx.box(
        rx.heading(title, font_size="1em", margin_bottom="0.5em", font_weight="bold"),
        *children,
        padding="1em",
        border=styles.DOC_BORDER,
        border_radius=styles.DOC_BORDER_RADIUS,
        _hover={
            "box_shadow": styles.DOC_SHADOW_LIGHT,
            "border": f"2px solid {c['violet'][200]}",
        },
    )


tab_style = {
    "color": "#494369",
    "font_weight": 600,
    "_selected": {
        "color": "#5646ED",
        "bg": "#F5EFFE",
        "padding_x": "0.5em",
        "padding_y": "0.25em",
        "border_radius": "8px",
    },
}


def docgraphing(
    code: str,
    comp: rx.Component | None = None,
    data: str | None = None,
):
    return rx.vstack(
        rx.flex(
            comp,
            height="15em",
            style=demo_box_style,
        ),
        rx.tabs(
            rx.tab_list(
                rx.tab("Code", style=tab_style),
                rx.tab("Data", style=tab_style),
                padding_x=0,
            ),
            rx.tab_panels(
                rx.tab_panel(
                    doccode(code), width="100%", padding_x=0, padding_y=".25em"
                ),
                rx.tab_panel(
                    doccode(data or ""), width="100%", padding_x=0, padding_y=".25em"
                ),
                width="100%",
            ),
            variant="unstyled",
            color_scheme="purple",
            align="end",
            width="100%",
            padding_top=".5em",
        ),
        width="100%",
    )


class RadixDocState(rx.State):
    """The app state."""

    color: str = "red"

    def change_color(self, color: str) -> None:
        self.color = color


def hover_item(component: rx.Component, component_str: str) -> rx.Component:
    return hovercard_root(
        hovercard_trigger(flex(component)),
        hovercard_content(
            rx.code_block(f"{component_str}", can_copy=True, language="python"),
        ),
    )


def dict_to_formatted_string(input_dict):
    # List to hold formatted string parts
    formatted_parts = []

    # Iterate over dictionary items
    for key, value in input_dict.items():
        # Format each key-value pair
        if isinstance(value, str):
            formatted_part = f'{key}="{value}"'  # Enclose string values in quotes
        else:
            formatted_part = f"{key}={value}"  # Non-string values as is

        # Append the formatted part to the list
        formatted_parts.append(formatted_part)

    # Join all parts with a comma and a space
    return ", ".join(formatted_parts)


def used_component(
    component_used: rx.Component,
    components_passed: rx.Component | str | None,
    color_scheme: str,
    variant: str,
    high_contrast: bool,
    disabled: bool = False,
    **kwargs,
) -> rx.Component:
    if components_passed is None and disabled is False:
        return component_used(
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            **kwargs,
        )

    elif components_passed is not None and disabled is False:
        return component_used(
            components_passed,
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            **kwargs,
        )

    elif components_passed is None and disabled is True:
        return component_used(
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            disabled=True,
            **kwargs,
        )

    else:
        return component_used(
            components_passed,
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            disabled=True,
            **kwargs,
        )


def style_grid(
    component_used: rx.Component,
    component_used_str: str,
    variants: list,
    components_passed: rx.Component | str | None = None,
    disabled: bool = False,
    **kwargs,
) -> rx.Component:
    return rx.vstack(
        grid(
            text("", size="5"),
            *[text(variant, size="5") for variant in variants],
            text("Accent", size="5"),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme=RadixDocState.color,
                        variant=variant,
                        high_contrast=False,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=False, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            text("", size="5"),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme=RadixDocState.color,
                        variant=variant,
                        high_contrast=True,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=True, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            text("Gray", size="5"),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme="gray",
                        variant=variant,
                        high_contrast=False,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=False, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            text("", size="5"),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme="gray",
                        variant=variant,
                        high_contrast=True,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=True, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            (
                rx.fragment(
                    text("Disabled", size="5"),
                    *[
                        hover_item(
                            component=used_component(
                                component_used=component_used,
                                components_passed=components_passed,
                                color_scheme="gray",
                                variant=variant,
                                high_contrast=True,
                                disabled=disabled,
                                **kwargs,
                            ),
                            component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, disabled=True, {dict_to_formatted_string(kwargs)})",
                        )
                        for variant in variants
                    ],
                )
                if disabled
                else ""
            ),
            flow="column",
            columns="5",
            rows=str(len(variants) + 1),
            gap="3",
        ),
        select_root(
            select_trigger(button(size="2", on_click=RadixDocState.change_color())),
            select_content(
                select_group(
                    select_label("Colors"),
                    *[
                        select_item(
                            color,
                            value=color,
                            _hover={"background": f"var(--{color}-9)"},
                        )
                        for color in [
                            "tomato",
                            "red",
                            "ruby",
                            "crimson",
                            "pink",
                            "plum",
                            "purple",
                            "violet",
                            "iris",
                            "indigo",
                            "blue",
                            "cyan",
                            "teal",
                            "jade",
                            "green",
                            "grass",
                            "brown",
                            "orange",
                            "sky",
                            "mint",
                            "lime",
                            "yellow",
                            "amber",
                            "gold",
                            "bronze",
                            "gray",
                        ]
                    ],
                ),
            ),
            ## we need to clearly document how the on_value_change works as it is not obvious at all
            default_value=RadixDocState.color,
            on_value_change=RadixDocState.change_color,
        ),
    )


def icon_grid(
    category_name: str, icon_tags: list[str], columns: str = "4"
) -> rx.Component:
    return flex(
        callout_root(
            callout_icon(
                icon(
                    tag="check_circled",
                    width=18,
                    height=18,
                )
            ),
            callout_text(
                f"Below is a list of all available ",
                text(category_name, weight="bold"),
                " icons.",
                color="black",
            ),
            color="green",
        ),
        separator(size="4"),
        grid(
            *[
                flex(
                    icon(tag=icon_tag, alias="Radix" + icon_tag.title()),
                    text(icon_tag),
                    direction="column",
                    align="center",
                    bg="white",
                    border="1px solid #EAEAEA",
                    border_radius="0.5em",
                    padding=".75em",
                )
                for icon_tag in icon_tags
            ],
            columns=columns,
            gap="1",
        ),
        direction="column",
        gap="2",
    )
