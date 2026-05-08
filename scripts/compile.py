import argparse
import subprocess
import os
import sys
import io

# Force UTF-8 stdout to avoid cp1252 crashes on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def compile_document(input_md, output_format):
    if not os.path.exists(input_md):
        print(f"Error: Input file '{input_md}' not found.")
        sys.exit(1)
        
    base_name = os.path.splitext(input_md)[0]
    output_file = f"{base_name}.{output_format}"
    
    cmd = ["pandoc", input_md, "-o", output_file]
    
    # Add format-specific flags
    if output_format == "pdf":
        # Assumes xelatex or pdflatex is installed
        cmd.extend(["--pdf-engine=xelatex", "-V", "geometry:margin=1in"])
    elif output_format == "docx":
        # Standard docx conversion
        pass
        
    print(f"Executing: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True, text=True, capture_output=True)
        print(f"✅ Successfully compiled to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Pandoc Compilation Failed!\n{e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Pandoc is not installed or not in PATH. Please install Pandoc.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Antigravity Pandoc Compiler")
    parser.add_argument("input", help="The source Markdown file")
    parser.add_argument("--format", choices=["pdf", "docx", "all"], default="all", help="Output format")
    
    args = parser.parse_args()
    
    if args.format in ["pdf", "all"]:
        compile_document(args.input, "pdf")
    if args.format in ["docx", "all"]:
        compile_document(args.input, "docx")
