# Why pkglite for Python?

Building on our experience with pkglite for R,
we identified several limitations and unmet needs:

- **Broader scope**: Extend support for packing and unpacking packages
  across any programming language, without R-specific assumptions.
- **Optimized tooling**: Simplify packing logic by classifying files
  based on content rather than file extensions.
- **Engineering-friendly interface**: Besides the language-specific API,
  provide a command-line interface (CLI) to better integrate with
  standard engineering workflows.

We made a few key design changes from pkglite for R to implement the above goals:

- Introduced a `.pkgliteignore` configuration file to control packing scope,
  following the gitignore standard.
- Adopted content-based file type classification for unsupervised file discovery.
- Built in Python for better flexibility and accessibility.
