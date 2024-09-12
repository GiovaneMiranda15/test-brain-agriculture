import re

def format_string(s: str) -> str:
    """
    Converte uma string para maiúsculas e remove caracteres especiais.

    Args:
        s (str): A string a ser formatada.

    Returns:
        str: A string formatada.
    """
    if s:
        # Remove caracteres não alfanuméricos e espaços e converte para maiúsculas
        s = re.sub(r'[^A-Za-z0-9\s]', '', s)
        s = s.upper()
    return s

import re

def format_cpf_cnpj(s: str) -> str:
    """
    Remove todos os caracteres não numéricos de um CPF ou CNPJ, mantendo apenas os números.

    Args:
        s (str): CPF ou CNPJ com caracteres especiais.

    Returns:
        str: CPF ou CNPJ limpo, contendo apenas números.
    """
    if s:
        # Remove todos os caracteres que não sejam números
        s = re.sub(r'\D', '', s)
    return s
