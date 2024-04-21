# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ConversationDesign(Component):
    """A ConversationDesign component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- API_URL (string; optional)

- directLineEndpoint (string; default '')

- directLineSecret (string; default 'localhost')

- session_id (string; optional)

- user_id (string; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, user_id=Component.UNDEFINED, session_id=Component.UNDEFINED, API_URL=Component.UNDEFINED, directLineEndpoint=Component.UNDEFINED, directLineSecret=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'API_URL', 'directLineEndpoint', 'directLineSecret', 'session_id', 'user_id']
        self._type = 'ConversationDesign'
        self._namespace = 'custom_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'API_URL', 'directLineEndpoint', 'directLineSecret', 'session_id', 'user_id']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ConversationDesign, self).__init__(**args)
