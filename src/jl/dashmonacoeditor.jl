# AUTO GENERATED FILE - DO NOT EDIT

export dashmonacoeditor

"""
    dashmonacoeditor(;kwargs...)

A DashMonacoEditor component.

Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `code` (String; optional)
- `defaultLanguage` (String; optional)
- `height` (String; optional)
- `language` (String; optional)
- `options` (Dict; optional)
- `theme` (String; optional)
- `width` (String; optional)
"""
function dashmonacoeditor(; kwargs...)
        available_props = Symbol[:id, :code, :defaultLanguage, :height, :language, :options, :theme, :width]
        wild_props = Symbol[]
        return Component("dashmonacoeditor", "DashMonacoEditor", "dash_monaco_editor", available_props, wild_props; kwargs...)
end

