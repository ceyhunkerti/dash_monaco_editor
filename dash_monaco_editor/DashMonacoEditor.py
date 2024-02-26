# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashMonacoEditor(Component):
    """A DashMonacoEditor component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- code (string; default "")

- defaultLanguage (string; default "sql")

- height (string; default "100%")

- language (string; default "sql")

- options (dict; optional)

- theme (string; default "vs-dark")

- width (string; default "100%")"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_monaco_editor'
    _type = 'DashMonacoEditor'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, code=Component.UNDEFINED, options=Component.UNDEFINED, theme=Component.UNDEFINED, language=Component.UNDEFINED, defaultLanguage=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'code', 'defaultLanguage', 'height', 'language', 'options', 'theme', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'code', 'defaultLanguage', 'height', 'language', 'options', 'theme', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashMonacoEditor, self).__init__(**args)
