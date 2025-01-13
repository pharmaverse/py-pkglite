# Why pkglite for Python?

## Differentiators

Building on our experience developing pkglite for R, we resolved several
longstanding, unmet needs with pkglite for Python:

- **Broader scope**. Extend support for packing and unpacking packages
  across **any** programming language, without R-specific assumptions.
- **Optimized tooling**. Simplify packing logic by classifying files
  based on content rather than file extensions.
  UTF-8 in and UTF-8 out for all text files on all platforms.
- **Engineering-friendly interface**. Besides the language-specific API,
  provide a command-line interface (CLI) to better integrate with
  standard engineering workflows.

## Design choices

We made a few key design changes from pkglite for R to implement the above goals:

- Introduced a `.pkgliteignore` configuration file to control packing scope,
  following the gitignore standard.
- Adopted content-based file type classification for unsupervised file discovery.
- Built with Python for better flexibility and accessibility.
