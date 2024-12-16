# Analisador Léxico para Lua

Este é um analisador léxico para código escrito em Lua, desenvolvido para identificar e classificar tokens como palavras-chave, literais, identificadores, operadores e outros elementos da linguagem. O programa é escrito em Python e pode ser executado diretamente no terminal.

## Funcionalidades

- Suporte a palavras-chave de Lua como `if`, `then`, `else`, `end`, etc.
- Identificação de literais inteiros, de ponto flutuante e em notação científica.
- Suporte a funções internas como `print`, `io.write`, `math.sin`.
- Tratamento de identificadores e operadores aritméticos, lógicos e relacionais.
- Ignora espaços em branco e comentários.
- Exibe mensagens claras para erros léxicos.

## Como Executar

### Pré-requisitos
- Python 3.12 ou superior instalado.

### Instalação
1. Clone este repositório:
   ```bash
    link
      ```
2. Acesse o diretório do projeto:
   ```bash
   cd analisador-lexico-lua
   ```
3. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

### Execução

1. **Com arquivo Lua**:
   ```bash
   python analisador.py "arquivo.lua"
   ```
   Exemplo:
   ```bash
   python analisador.py "test1.lua"
   ```

2. **Com código diretamente**:
   ```bash
   python analisador.py "local x = 10; print(x)"
   ```

### Execução dos Arquivos de Teste
Fornecemos sete arquivos de teste cobrindo os tokens descritos na Seção 1.2 do trabalho:

- `test1.lua`: Declaração de variáveis e funções.
- `test2.lua`: Literais inteiros, de ponto flutuante e operadores.
- `test3.lua`: Comandos de seleção (`if`, `elseif`, `else`).
- `test4.lua`: Comandos de repetição (`for`, `while`, `repeat...until`).
- `test5.lua`: Expressões algébricas e operadores.
- `test6.lua`: Chamadas de função com múltiplos argumentos e retornos.
- `test7.lua`: Exemplo de erro léxico (caractere inválido).

Execute os arquivos de teste com:
```bash
python analisador.py "test1.lua"
```
Substitua `test1.lua` pelo arquivo desejado (`test2.lua`, etc.).
Se o arquivo lua não estiver no mesmo diretório que o arquivo `analisador.py`, certifique-se de inserir o caminho completo para o arquivo.

### Saída
A saída do programa exibe os tokens encontrados no formato:
```
          local -> KEYWORD
              x -> ID
              = -> OP_ASSIGN
             10 -> LIT_INT
              ; -> DELIM
          print -> BUILTIN_FUNC
              ( -> DELIM
              x -> ID
              ) -> DELIM
```

### Casos de Erro
Se o código Lua contiver uma sequência inválida, o analisador exibirá uma mensagem de erro como:
```
Erro léxico: sequência inválida no código próximo a '23e4 '
```

## Estrutura do Código
- `analisador.py`: Arquivo principal contendo o analisador léxico.
- **Tokens suportados**:
  - `KEYWORD`: Palavras-chave de Lua.
  - `LIT_INT`: Literais inteiros.
  - `LIT_FLOAT`: Literais de ponto flutuante e notação científica.
  - `BUILTIN_FUNC`: Funções internas de Lua (`print`, `io.write`, etc.).
  - `ID`: Identificadores.
  - `OP_ARITH`, `OP_REL`, `OP_LOGIC`: Operadores.
  - `DELIM`: Delimitadores como `(`, `)`.

## Testes
Os arquivos de teste cobrem todos os tokens mencionados na Seção 1.2 do trabalho. Execute-os para validar o funcionamento completo do analisador léxico.

## Alunos
- Ayrton Finicelli Lemes - 22053242
- Caroline Soares Braz - 22051417
- Jakeline Gimaque de Mesquita - 22050618
- Luiz Gabriel Favacho de Almeida - 22153921

---

**Professor:** Arcanjo Miguel Mota Lopes

