#!/usr/bin/env python3
"""
Example usage of the Jasmin Pygments lexer in various contexts.

This script demonstrates how to use the Jasmin lexer for syntax highlighting
in web applications, documentation generators, and other tools.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from pygments import highlight
from pygments.formatters import HtmlFormatter, TerminalFormatter, LatexFormatter
from jasmin_lexer import JasminLexer


def example_terminal_highlighting():
    """Example: Terminal syntax highlighting."""
    print("=== Terminal Highlighting Example ===")
    
    code = '''
// Kyber polynomial addition
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
'''
    
    # Terminal output with colors
    terminal_formatter = TerminalFormatter(bg="dark")
    highlighted = highlight(code, JasminLexer(), terminal_formatter)
    print(highlighted)


def example_html_highlighting():
    """Example: HTML syntax highlighting for web pages."""
    print("=== HTML Highlighting Example ===")
    
    code = '''
param int KYBER_K = 3;

export fn jade_kem_kyber_keypair(reg u64 public_key secret_key) -> reg u64
{
    reg u64 r;
    stack u8[KYBER_SYMBYTES] coins;
    
    coins = #randombytes(coins);
    _crypto_kem_keypair_derand_jazz(public_key, secret_key, coins);
    ?{}, r = #set0();
    return r;
}
'''
    
    # HTML formatter with line numbers and CSS classes
    html_formatter = HtmlFormatter(
        style='github-dark',
        linenos=True,
        linenostart=1,
        cssclass='jasmin-highlight',
        wrapcode=True
    )
    
    html_output = highlight(code, JasminLexer(), html_formatter)
    
    # Create a complete HTML page
    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jasmin Code Example</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #0d1117;
            color: #c9d1d9;
        }}
        h1 {{
            color: #58a6ff;
            border-bottom: 1px solid #30363d;
            padding-bottom: 10px;
        }}
        .description {{
            background-color: #161b22;
            padding: 15px;
            border-radius: 6px;
            margin: 20px 0;
            border: 1px solid #30363d;
        }}
        .jasmin-highlight {{
            margin: 20px 0;
            border-radius: 6px;
            overflow: hidden;
            border: 1px solid #30363d;
        }}
    </style>
</head>
<body>
    <h1>Jasmin Syntax Highlighting Example</h1>
    
    <div class="description">
        <strong>About this example:</strong><br>
        This shows a Jasmin function for Kyber key generation with proper syntax highlighting.
        Notice how keywords, types, functions, and comments are highlighted differently.
    </div>
    
    {html_output}
    
    <div class="description">
        <strong>Syntax Elements Highlighted:</strong>
        <ul>
            <li><strong>Keywords:</strong> export, fn, reg, stack, return</li>
            <li><strong>Types:</strong> u64, u8</li>
            <li><strong>Constants:</strong> KYBER_K, KYBER_SYMBYTES</li>
            <li><strong>Built-ins:</strong> #randombytes, #set0</li>
            <li><strong>Functions:</strong> _crypto_kem_keypair_derand_jazz</li>
            <li><strong>Special syntax:</strong> ?{{}} for flags</li>
        </ul>
    </div>
</body>
</html>'''
    
    # Save the HTML file
    with open('jasmin_example.html', 'w') as f:
        f.write(full_html)
    
    print("HTML example saved to: jasmin_example.html")
    print("You can open this file in a web browser to see the highlighted code.")


def example_documentation_integration():
    """Example: Integration with documentation systems."""
    print("=== Documentation Integration Example ===")
    
    code = '''
#[returnaddress="stack"]
inline fn __keccak1600_absorb(
    reg ptr u64[25] state,
    reg u64 in inlen,
    reg u8 trail_byte,
    reg u64 rate
) -> reg ptr u64[25]
{
    /* Absorb input into Keccak state */
    while (inlen >= rate) {
        state, in, inlen = __add_full_block(state, in, inlen, rate);
        state = _keccakf1600(state);
    }
    
    // Handle final partial block
    state = __add_final_block(state, in, inlen, trail_byte, rate);
    return state;
}
'''
    
    print("Sphinx/reStructuredText integration:")
    print("You can use this in Sphinx documentation by adding 'jasmin' as a supported language.")
    print("Example directive:")
    print(".. code-block:: jasmin")
    print()
    for line in code.strip().split('\n'):
        print(f"   {line}")
    
    print("\nMarkdown integration:")
    print("```jasmin")
    print(code.strip())
    print("```")


def example_latex_highlighting():
    """Example: LaTeX output for academic papers."""
    print("=== LaTeX Highlighting Example ===")
    
    code = '''
export fn jade_hash_sha3_256(reg u64 hash input input_length) -> reg u64
{
    reg u64 r;
    __sha3_256_impl(hash, input, input_length);
    ?{}, r = #set0();
    return r;
}
'''
    
    latex_formatter = LatexFormatter(style='colorful')
    latex_output = highlight(code, JasminLexer(), latex_formatter)
    
    print("LaTeX output (for inclusion in academic papers):")
    print(latex_output)


def example_custom_styles():
    """Example: Custom styling for different themes."""
    print("=== Custom Styling Example ===")
    
    code = '''
from Jade require "common/keccak.jinc"

inline fn __sha3_256(reg u64 out in inlen)
{
    reg u64 outlen rate;
    reg u8 trail_byte;
    
    outlen = 32;  // 256 bits
    trail_byte = 0x6;
    rate = 136;   // 1088 bits
    
    _keccak1600(out, outlen, in, inlen, trail_byte, rate);
}
'''
    
    # Different style themes
    styles = ['github-dark', 'monokai', 'solarized-dark', 'vim', 'colorful']
    
    for style in styles:
        print(f"\n--- Style: {style} ---")
        formatter = HtmlFormatter(style=style, noclasses=True)
        html_output = highlight(code, JasminLexer(), formatter)
        
        # Extract just the highlighted code (remove extra div wrapper)
        import re
        code_match = re.search(r'<pre[^>]*>(.*?)</pre>', html_output, re.DOTALL)
        if code_match:
            print(f"CSS styling for {style} theme applied successfully")
        else:
            print(f"Could not extract styling for {style}")


def main():
    """Run all examples."""
    print("Jasmin Pygments Lexer - Usage Examples")
    print("=" * 50)
    
    # Terminal highlighting
    example_terminal_highlighting()
    
    print("\n" + "=" * 50)
    
    # HTML highlighting
    example_html_highlighting()
    
    print("\n" + "=" * 50)
    
    # Documentation integration
    example_documentation_integration()
    
    print("\n" + "=" * 50)
    
    # LaTeX highlighting
    example_latex_highlighting()
    
    print("\n" + "=" * 50)
    
    # Custom styles
    example_custom_styles()
    
    print("\n" + "=" * 50)
    print("All examples completed!")
    print("\nUsage Summary:")
    print("- Terminal: TerminalFormatter()")
    print("- Web/HTML: HtmlFormatter(style='github-dark', linenos=True)")
    print("- Documentation: Integration with Sphinx, Markdown")
    print("- Academic: LatexFormatter()")
    print("- Custom: Various style themes available")


if __name__ == "__main__":
    main()