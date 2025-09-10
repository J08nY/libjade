# Jasmin Pygments Lexer

This directory contains a Pygments lexer for the Jasmin programming language, as used in the libjade cryptographic library.

## Overview

Jasmin is a low-level programming language designed for high-assurance cryptographic software. This lexer provides syntax highlighting for Jasmin source files (`.jazz`) and include files (`.jinc`).

## Features

The lexer recognizes and highlights:

- **Keywords**: `export`, `fn`, `inline`, `param`, `require`, `from`, `stack`, `reg`, etc.
- **Types**: `u8`, `u16`, `u32`, `u64`, `int`, `bool`, `ptr`, `const`
- **Control flow**: `if`, `else`, `while`, `for`, `return`
- **Special constructs**: `#bounded`, `#returnaddress`, `#init_msf`, `#set0`, etc.
- **Comments**: Both single-line (`//`) and multi-line (`/* */`)
- **Numbers**: Decimal and hexadecimal literals
- **Operators**: Arithmetic, comparison, logical, and assignment operators
- **Memory access**: Array indexing and type casting syntax
- **Include statements**: `require "file"` and `from Jade require "path/file"`
- **Function attributes**: `#[returnaddress="stack"]`
- **Parameters**: `param int NAME = value;`

## Installation

### Using pip (recommended)

```bash
cd tools/pygments
pip install -e .
```

### Manual installation

1. Copy the `jasmin_lexer.py` file to your Python environment
2. Install Pygments: `pip install Pygments>=2.0`

## Usage

### With Python code

```python
from pygments import highlight
from pygments.formatters import HtmlFormatter, TerminalFormatter
from jasmin_lexer import JasminLexer

# Read Jasmin code
with open('example.jazz', 'r') as f:
    code = f.read()

# Highlight for terminal
print(highlight(code, JasminLexer(), TerminalFormatter()))

# Generate HTML
html_formatter = HtmlFormatter(style='colorful', linenos=True)
html_output = highlight(code, JasminLexer(), html_formatter)
```

### With command line

After installation, you can use the lexer with the `pygmentize` command:

```bash
# Highlight to terminal
pygmentize -l jasmin example.jazz

# Generate HTML
pygmentize -l jasmin -f html -o example.html example.jazz

# List available styles
pygmentize -L styles
```

### With web frameworks

The lexer integrates with any system that uses Pygments for syntax highlighting:

- **Sphinx**: Add `jasmin` to your highlighting languages
- **Jekyll/GitHub Pages**: Use `{% highlight jasmin %}` blocks
- **Django**: Use with `django-pygments`
- **Flask**: Use with `flask-pygments`

## Testing

Run the test script to see the lexer in action:

```bash
cd tools/pygments
python test_lexer.py
```

This will:
1. Test the lexer with sample code snippets
2. Generate highlighted output for terminal and HTML
3. Process actual Jasmin files from the libjade repository

## Example Output

Here's what highlighted Jasmin code looks like:

```jasmin
// Export function with proper highlighting
export fn jade_scalarmult_curve25519_amd64_ref4(reg u64 qp np pp) -> reg u64
{
  reg u64 r;
  
  _ = #init_msf();
  __curve25519_ref4_ptr(qp, np, pp);
  ?{}, r = #set0();
  return r;
}
```

## Supported File Extensions

- `.jazz` - Jasmin source files
- `.jinc` - Jasmin include files

## Supported MIME Types

- `text/x-jasmin`

## Dependencies

- Python 3.6+
- Pygments 2.0+

## License

This lexer is part of the libjade project and follows the same license terms.

## Contributing

To improve the lexer:

1. Edit `jasmin_lexer.py` to add new token patterns
2. Test with `test_lexer.py`
3. Update this README if needed
4. Submit a pull request

Common improvements might include:
- Better recognition of built-in functions
- Enhanced support for assembly-like constructs
- Improved handling of complex type declarations
- Additional operator patterns