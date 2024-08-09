""" Validators"""


class DocumentValidation:

    def document_validation(self, document: str):
        if document:
            value = document.replace(".", "").replace("-", "").replace("/", "")
            if not value.isdigit():
                return False
            if len(value) == 11:
                return self.validate_cpf(value)
            elif len(value) == 14:
                return self.validate_cnpj(value)
            else:
                return False

        if not document:
            return False
        return True

    @staticmethod
    def validate_cpf(cpf: str):
        """Return the value of the cpf valid"""
        cpf = cpf.replace(".", "").replace("-", "")

        # Verifica se o CPF tem 11 dígitos, se todos os caracteres são dígitos e se todos os dígitos não são iguais
        if not cpf.isdigit() or len(cpf) != 11 or len(set(cpf)) == 1:
            return False

        # Cálculo do primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = 11 - (soma % 11)
        digito1 = 0 if digito1 >= 10 else digito1

        # Cálculo do segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = 11 - (soma % 11)
        digito2 = 0 if digito2 >= 10 else digito2

        # Verifica se os dígitos calculados correspondem aos dígitos do CPF
        if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
            return False

        return True

    @staticmethod
    def validate_cnpj(cnpj: str):
        """Return the value of the cnpj valid"""
        cnpj = cnpj.replace(".", "").replace("-", "").replace("/", "")

        if not cnpj.isdigit() or len(cnpj) != 14:
            return False

        # Verificando se todos os dígitos são iguais
        if len(set(cnpj)) == 1:
            return False

        # Pesos para o primeiro e segundo dígito verificador
        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        # Calculando o primeiro dígito verificador
        soma = sum(int(cnpj[i]) * peso for i, peso in enumerate(pesos1))
        digito1 = 11 - (soma % 11)
        digito1 = 0 if digito1 >= 10 else digito1

        # Calculando o segundo dígito verificador
        soma = sum(int(cnpj[i]) * peso for i, peso in enumerate(pesos2))
        digito2 = 11 - (soma % 11)
        digito2 = 0 if digito2 >= 10 else digito2

        # Verifica se os dígitos calculados correspondem aos dígitos do CNPJ
        if int(cnpj[12]) != digito1 or int(cnpj[13]) != digito2:
            return False

        return True


class ValidateCheckDigit:

    def validate(self, numero_processo: str):
        # Extrai o dígito verificador do número do processo

        check_digit = numero_processo.split('-')[1].split('.')[0]

        # Calcula o dígito verificador correto
        calculated_digit = self.__calculate_check_digit(numero_processo)

        # Compara o dígito verificador fornecido com o calculado
        return check_digit == calculated_digit

    @staticmethod
    def __calculate_check_digit(process_number):
        # Remove os caracteres de separação
        process_number = process_number.replace('-', '').replace('.', '')
        if not process_number.isdigit():
            return False

        # Coloca os dígitos verificadores (DD) no final e substitui por "00"
        numero_processo_modificado = process_number[:7] + process_number[9:] + "00"

        # Converte para inteiro
        number_int = int(numero_processo_modificado)

        # Calcula o dígito verificador
        check_digit = 98 - (number_int % 97)

        # Formata o resultado com dois dígitos
        return f"{check_digit:02}"


def validate_uf(uf):
    brazilian_states = (
        'AC',  # Acre
        'AL',  # Alagoas
        'AP',  # Amapá
        'AM',  # Amazonas
        'BA',  # Bahia
        'CE',  # Ceará
        'DF',  # Distrito Federal
        'ES',  # Espírito Santo
        'GO',  # Goiás
        'MA',  # Maranhão
        'MT',  # Mato Grosso
        'MS',  # Mato Grosso do Sul
        'MG',  # Minas Gerais
        'PA',  # Pará
        'PB',  # Paraíba
        'PR',  # Paraná
        'PE',  # Pernambuco
        'PI',  # Piauí
        'RJ',  # Rio de Janeiro
        'RN',  # Rio Grande do Norte
        'RS',  # Rio Grande do Sul
        'RO',  # Rondônia
        'RR',  # Roraima
        'SC',  # Santa Catarina
        'SP',  # São Paulo
        'SE',  # Sergipe
        'TO'  # Tocantins
    )

    if uf.upper() not in brazilian_states:
        return False
    return True


def validate_person_type(tipo: str):
    if tipo.lower() not in ('cpf', 'cnpj'):
        return False
    return True


def validate_culture_option(culture: str):
    if culture.lower() not in ('soja', 'milho', 'algodao', 'cafe', 'cana de acucar'):
        return False
    return True
