# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashMonacoEditor <- function(id=NULL, code=NULL, defaultLanguage=NULL, height=NULL, language=NULL, options=NULL, theme=NULL, width=NULL) {
    
    props <- list(id=id, code=code, defaultLanguage=defaultLanguage, height=height, language=language, options=options, theme=theme, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashMonacoEditor',
        namespace = 'dash_monaco_editor',
        propNames = c('id', 'code', 'defaultLanguage', 'height', 'language', 'options', 'theme', 'width'),
        package = 'dashMonacoEditor'
        )

    structure(component, class = c('dash_component', 'list'))
}
