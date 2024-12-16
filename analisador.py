import re
import argparse

# Definição dos tokens e seus padrões
token_patterns = [
    ("BUILTIN_FUNC", r"\b(print|io\.write|math\.sin|math\.cos|math\.log)\b"),
    ("LIT_INT", r"\b\d+\b"),
    ("LIT_FLOAT", r"\b\d+(\.\d+)?([eE][-+]?\d+)?\b"),
    ("STRING", r'".*?"|\'.*?\''),
    ("KEYWORD", r"\b(if|then|else|elseif|end|for|while|repeat|until|function|local|return|do|not)\b"),
    ("OP_ARITH", r"[+\-*/%^]"),
    ("OP_REL", r"[<>=~]=|<[=>]?|>[=]?"),
    ("OP_ASSIGN", r"="),
    ("OP_LOGIC", r"and|or|not"),
    ("DELIM", r"[.,:;{}()[\]]"),
    ("ID", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("WHITESPACE", r"\s+")
]

# Compilação dos padrões
token_regex = [(name, re.compile(pattern)) for name, pattern in token_patterns]


def lex_analyzer(code):
    """Realiza a análise léxica do código Lua."""
    tokens = []

    # Ignorar comentários linha por linha
    lines = code.split("\n")
    processed_code = []
    for line in lines:
        if "--" in line:
            line = line.split("--")[0]  # Remove o comentário e mantém o código antes dele
        processed_code.append(line)
    code = "\n".join(processed_code)

    position = 0
    while position < len(code):
        match_found = False

        for token_name, token_re in token_regex:
            match = token_re.match(code, position)
            if match:
                lexeme = match.group(0)
                if token_name != "WHITESPACE":
                    tokens.append((lexeme, token_name))
                position = match.end()
                match_found = True
                break
        if not match_found:
            # Capturar o trecho exato do erro para maior clareza
            end_position = position + 10 if position + 10 < len(code) else len(code)
            raise ValueError(f"Erro léxico: sequência inválida no código próximo a '{code[position:end_position]}'")
    return tokens


def main():
    """Função principal para execução via linha de comando."""
    parser = argparse.ArgumentParser(description="Analisador léxico para código Lua.")
    parser.add_argument("input", help="Arquivo de entrada ou código em Lua como string.")
    args = parser.parse_args()

    try:
        # Verifica se é um arquivo ou código diretamente
        try:
            with open(args.input, "r") as file:
                code = file.read()
        except FileNotFoundError:
            code = args.input

        result = lex_analyzer(code)
        print("\n".join([f"{lexeme:>15} -> {token}" for lexeme, token in result]))
    except ValueError as e:
        print(e)
    except Exception as ex:
        print(f"Erro inesperado: {ex}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        if e.code == 2:
            print(
                "Uso incorreto do script. Certifique-se de fornecer a entrada corretamente.\nExemplo: python script.py \"seu_codigo_lua\"")
        else:
            raise
