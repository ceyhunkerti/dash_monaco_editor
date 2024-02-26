import Editor from '@monaco-editor/react';
import 'monaco-sql-languages/out/esm/sparksql/sparksql.contribution';
import PropTypes from 'prop-types';
import { Component, default as React } from 'react';

export default class DashMonacoEditor extends Component {
    constructor(props) {
        super(props);
      }
      editorDidMount(editor) {
        editor.focus();
      }
      render() {
        const {code, id,defaultLanguage, options, theme, language, width, height, setProps } = this.props;
        return (
          <Editor
            defaultLanguage={defaultLanguage}
            id={id}
            width={width}
            height={height}
            language={language}
            theme={theme}
            value={code}
            options={options|| { selectOnLineNumbers: true }}
            onChange={
              (newValue) => setProps({ code: newValue })
            }
            editorDidMount={this.editorDidMount}
          />
        );
      }
}


DashMonacoEditor.defaultProps = {
    code: "",
    options: {},
    theme: "vs-dark",
    language: "sql",
    defaultLanguage: "sql",
    width: "100%",
    height: "100%"
};

DashMonacoEditor.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    code: PropTypes.string,

    options: PropTypes.object,

    theme: PropTypes.string,

    language: PropTypes.string,

    defaultLanguage: PropTypes.string,

    width: PropTypes.string,

    height: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
