from tree_sitter import Language, Parser

# Language.build_library(
#   # Store the library in the `build` directory
#   'build/my-languages.so',

#   # Include one or more languages
#   [
#     # 'Languages/tree-sitter-go',
#     'Languages/tree-sitter-javascript',
#     'Languages/tree-sitter-python'
#   ]
# )

# GO_LANGUAGE = Language('build/my-languages.so', 'go')
# JS_LANGUAGE = Language('build/my-languages.so', 'javascript')
# PY_LANGUAGE = Language('build/my-languages.so', 'python')

# parser = Parser()
# parser.set_language(PY_LANGUAGE)
Language.build_library(
  # Store the library in the `build` directory
  'build/my-languages.so',

  # Include one or more languages
  [
    # 'languages/tree-sitter-go',
    'languages/tree-sitter-javascript',
    'languages/tree-sitter-python'
  ]
)

JS_LANGUAGE = Language('build/my-languages.so', 'javascript')
PY_LANGUAGE = Language('build/my-languages.so', 'python')