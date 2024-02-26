from dash import Dash, Input, Output, callback, html

import dash_monaco_editor

app = Dash(__name__)

app.layout = html.Div(
    [
        dash_monaco_editor.DashMonacoEditor(
            id="sql-editor",
            language="sql",
            theme="vs-light",
            options={"minimap": {"enabled": False}},
        ),
        html.Div(id="output"),
    ],
    className="layout",
    style={
        "width": "100%",
        "height": "100vh",
        "margin": "auto",
    },
)


@callback(Output("output", "children"), Input("sql-editor", "code"))
def display_output(value):
    return "You have entered {}".format(value)


if __name__ == "__main__":
    app.run_server(debug=True)
