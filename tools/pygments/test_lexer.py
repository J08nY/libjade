#!/usr/bin/env python3
"""
Test script for the Jasmin Pygments lexer.

This script demonstrates the lexer by highlighting a sample Jasmin file
and some example code snippets.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from pygments import highlight
from pygments.formatters import TerminalFormatter, HtmlFormatter
from jasmin_lexer import JasminLexer


def test_lexer_with_code(code, description):
    """Test the lexer with a code snippet."""
    print(f"\n=== {description} ===")
    print("Original code:")
    print(code)
    print("\nHighlighted (terminal):")
    print(highlight(code, JasminLexer(), TerminalFormatter()))


def test_lexer_with_file(filename):
    """Test the lexer with a Jasmin file."""
    if not os.path.exists(filename):
        print(f"File {filename} not found")
        return
    
    with open(filename, 'r') as f:
        code = f.read()
    
    print(f"\n=== Testing with file: {filename} ===")
    print("Highlighted (terminal):")
    print(highlight(code, JasminLexer(), TerminalFormatter()))
    
    # Also create an HTML version
    html_filename = filename.replace('.jazz', '_highlighted.html').replace('.jinc', '_highlighted.html')
    html_formatter = HtmlFormatter(style='colorful', linenos=True)
    html_output = highlight(code, JasminLexer(), html_formatter)
    
    with open(html_filename, 'w') as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
    <title>Jasmin Syntax Highlighting - {os.path.basename(filename)}</title>
    <style>
        body {{ font-family: monospace; margin: 40px; }}
        .header {{ font-size: 18px; margin-bottom: 20px; }}
    </style>
</head>
<body>
    <div class="header">Jasmin Syntax Highlighting - {os.path.basename(filename)}</div>
    {html_output}
</body>
</html>""")
    
    print(f"HTML output saved to: {html_filename}")


def main():
    """Main test function."""
    print("Testing Jasmin Pygments Lexer")
    print("=" * 50)
    
    # Test with sample code snippets
    test_code_snippets = [
        ("""
// Simple Jasmin function
export fn jade_example_function(reg u64 input output) -> reg u64
{
    reg u64 result;
    result = input;
    result += 42;
    (u64)[output] = result;
    ?{}, result = #set0();
    return result;
}
""", "Simple Function"),
        
        ("""
param int KYBER_N = 256;
param int KYBER_Q = 3329;

from Jade require "common/tofromstack.jinc"
require "params.jinc"

fn _poly_add(reg ptr u16[KYBER_N] ap bp) -> reg ptr u16[KYBER_N]
{
    reg u16 a b r;
    reg u64 i;
    
    i = 0;
    #bounded
    while (i < KYBER_N) {
        a = ap[(int)i];
        b = bp[(int)i];
        r = a + b;
        ap[(int)i] = r;
        i += 1;
    }
    return ap;
}
""", "Complex Function with Parameters"),
        
        ("""
#[returnaddress="stack"]
inline fn __keccak_absorb(reg ptr u64[25] state, reg u64 in inlen) -> reg ptr u64[25]
{
    stack u8 trail_byte;
    reg u64 rate i t;
    
    /* Process full blocks */
    while (inlen >= rate) {
        i = 0;
        while (i < rate) {
            t = [in + 8*i];
            state[(int)i] ^= t;
            i += 1;
        }
        in += rate;
        inlen -= rate;
    }
    
    return state;
}
""", "Inline Function with Attributes")
    ]
    
    for code, description in test_code_snippets:
        test_lexer_with_code(code, description)
    
    # Test with actual files if they exist
    test_files = [
        "../../src/crypto_scalarmult/curve25519/amd64/ref4/scalarmult.jazz",
        "../../src/crypto_stream/chacha/chacha20/amd64/ref/stream.jazz",
        "../../src/crypto_kem/kyber/kyber768/amd64/ref/kem.jazz",
        "../../src/crypto_kem/kyber/kyber768/amd64/ref/params.jinc"
    ]
    
    for filename in test_files:
        full_path = os.path.join(os.path.dirname(__file__), filename)
        if os.path.exists(full_path):
            test_lexer_with_file(full_path)
            break  # Test with just one file to avoid too much output
    
    print("\n" + "=" * 50)
    print("Lexer testing completed!")
    print("\nTo use this lexer:")
    print("1. Install: pip install -e .")
    print("2. Use in code: from jasmin_lexer import JasminLexer")
    print("3. Use with pygments command: pygmentize -l jasmin file.jazz")


if __name__ == "__main__":
    main()