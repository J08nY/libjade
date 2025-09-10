"""
Pygments lexer for the Jasmin programming language.

Jasmin is a low-level programming language for verified cryptography implementations,
as used in the libjade library.
"""

from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import (
    Text, Comment, Keyword, Name, String, Number, Operator,
    Punctuation, Generic, Whitespace
)

__all__ = ['JasminLexer']


class JasminLexer(RegexLexer):
    """
    For Jasmin source code (.jazz files).
    
    Jasmin is a programming language for high-assurance cryptographic software,
    designed for formal verification and compilation to assembly.
    """
    
    name = 'Jasmin'
    aliases = ['jasmin', 'jazz']
    filenames = ['*.jazz', '*.jinc']
    mimetypes = ['text/x-jasmin']
    
    # Keywords
    keywords = (
        'export', 'fn', 'inline', 'param', 'require', 'from', 'stack', 'reg',
        'if', 'else', 'while', 'for', 'return', 'const', 'ptr',
        'true', 'false'
    )
    
    # Type keywords
    types = (
        'u8', 'u16', 'u32', 'u64', 'int', 'bool'
    )
    
    # Special built-in functions/macros
    builtins = (
        '#bounded', '#returnaddress', '#init_msf', '#set0', '#randombytes',
        '__fqmul', '__add_full_block', '__absorb', '__keccak_init'
    )
    
    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Whitespace),
            
            # Comments
            (r'//.*$', Comment.Single),
            (r'/\*', Comment.Multiline, 'comment'),
            
            # Preprocessor-like directives
            (r'(param)(\s+)(int|u8|u16|u32|u64)(\s+)([A-Z_][A-Z0-9_]*)(\s*=)',
             bygroups(Keyword.Reserved, Whitespace, Keyword.Type, Whitespace,
                     Name.Constant, Operator)),
                     
            # Include statements
            (r'(require)(\s+)(")', bygroups(Keyword.Namespace, Whitespace, String),
             'string'),
            (r'(from)(\s+)(Jade)(\s+)(require)(\s+)(")',
             bygroups(Keyword.Namespace, Whitespace, Name.Namespace, Whitespace,
                     Keyword.Namespace, Whitespace, String), 'string'),
            
            # Function attributes
            (r'#\[[^\]]+\]', Generic.Decorator),
            
            # Special constructs with # prefix (must come before normal identifiers)
            (r'#\w+', Name.Builtin),
            
            # Keywords (must come before identifiers)
            (words(keywords, prefix=r'\b', suffix=r'\b'), Keyword),
            
            # Types (must come before identifiers)
            (words(types, prefix=r'\b', suffix=r'\b'), Keyword.Type),
            
            # Array type syntax: type[size]
            (r'\b(u8|u16|u32|u64|int)\s*\[', Keyword.Type),
            
            # Function names (typically start with _ for internal functions)
            (r'\b(_+[a-zA-Z_][a-zA-Z0-9_]*)\b', Name.Function),
            
            # Constants (usually ALL_CAPS) - must come before regular identifiers
            (r'\b[A-Z_][A-Z0-9_]*\b', Name.Constant),
            
            # Regular identifiers
            (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', Name),
            
            # Numbers
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'\b\d+\b', Number.Integer),
            
            # String literals
            (r'"', String, 'string'),
            
            # Operators
            (r'(\+\+|--|<<|>>|<=|>=|==|!=|&&|\|\|)', Operator),
            (r'(\+=|-=|\*=|/=|%=|&=|\|=|\^=|<<=|>>=)', Operator),
            (r'[+\-*/%&|^~<>=!]', Operator),
            (r'->', Operator),
            
            # Type casting
            (r'\((u8|u16|u32|u64|int)\)', Keyword.Type),
            
            # Memory access brackets
            (r'[\[\]]', Punctuation),
            
            # Other punctuation
            (r'[{}();,.:?]', Punctuation),
            
            # Flag syntax
            (r'\?\{\}', Operator),
        ],
        
        'comment': [
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline),
        ],
        
        'string': [
            (r'\\[\\"]', String.Escape),
            (r'[^"\\]+', String),
            (r'"', String, '#pop'),
        ],
    }