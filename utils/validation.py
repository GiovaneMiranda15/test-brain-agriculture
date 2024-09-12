import re
from validate_docbr import CPF, CNPJ

def validar_cpf_cnpj(cpf_cnpj):
    """
    Valida se o CPF ou CNPJ é válido.
    
    Parâmetros:
    cpf_cnpj (str): CPF ou CNPJ a ser validado.
    
    Retorna:
    bool: True se o CPF ou CNPJ for válido, False caso contrário.
    """
    # Expressão regular para verificar o formato de CPF (11 dígitos) ou CNPJ (14 dígitos)
    padrao = r'^\d{11}$|^\d{14}$'
    
    # Verifica se o formato está correto e se é um CPF ou CNPJ válido
    if re.match(padrao, cpf_cnpj):
        return CPF().validate(cpf_cnpj) or CNPJ().validate(cpf_cnpj)
    return False

def validar_dados(produtor):
    """
    Valida os dados do produtor rural.
    
    Parâmetros:
    produtor (dict): Dicionário contendo os dados do produtor rural.
    
    Levanta:
    ValueError: Se CPF/CNPJ é inválido ou se a soma das áreas é inconsistente.
    """
    # Verifica a validade do CPF ou CNPJ
    if not validar_cpf_cnpj(produtor['cpf_cnpj']):
        raise ValueError("CPF ou CNPJ inválido.")
    
    # Verifica se a soma das áreas agricultável e vegetação é menor ou igual à área total
    if produtor['area_agricultavel'] + produtor['area_vegetacao'] > produtor['area_total']:
        raise ValueError("A soma da área agricultável e vegetação não pode ser maior que a área total da fazenda.")
