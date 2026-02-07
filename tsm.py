from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label, ListItem, ListView


class TerminalServerManager(App):
    ENABLE_COMMAND_PALETTE = False
    CSS_PATH = "styled.tcss"
    BINDINGS = [
        ("Ctrl+Q", "quit", "quit"),
    ]
    def compose(self) -> ComposeResult:
        yield Header()
        yield ListView(
            ListItem(Label("BRAIN")),
            ListItem(Label("HEART")),
            ListItem(Label("VITALS")),
        )
        yield Footer()


if __name__ == "__main__":
    app = TerminalServerManager()
    app.run()