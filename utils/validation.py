import re

def validar_cpf_cnpj(cpf_cnpj):
    return re.match(r'^\d{11}|\d{14}$', cpf_cnpj) is not None

def validar_dados(produtor):
    if not validar_cpf_cnpj(produtor['cpf_cnpj']):
        raise ValueError("CPF ou CNPJ inválido.")
    if produtor['area_agricultavel'] + produtor['area_vegetacao'] > produtor['area_total']:
        raise ValueError("A soma da área agricultável e vegetação não pode ser maior que a área total da fazenda.")
