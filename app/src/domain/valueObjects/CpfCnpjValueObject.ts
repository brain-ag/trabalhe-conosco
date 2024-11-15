class CpfCnpjValueObject {
  private value: string;

  constructor(value: string) {
    this.value = value.replace(/\D/g, '');

    if (!this.isValid()) {
      throw new Error('CPF ou CNPJ inválido');
    }
  }

  private isValid(): boolean {
    const length = this.value.length;

    if (length === 11) {
      return this.isValidCpf();
    }

    if (length === 14) {
      return this.isValidCnpj();
    }

    return false;
  }

  private isValidCpf(): boolean {
    if (this.value.length !== 11) return false;

    let sum = 0;
    let remainder;

    for (let i = 0; i < 9; i++) {
      sum += parseInt(this.value.charAt(i)) * (10 - i);
    }
    remainder = sum % 11;
    if (remainder < 2) {
      if (parseInt(this.value.charAt(9)) !== 0) return false;
    } else {
      if (parseInt(this.value.charAt(9)) !== 11 - remainder) return false;
    }

    sum = 0;
    for (let i = 0; i < 10; i++) {
      sum += parseInt(this.value.charAt(i)) * (11 - i);
    }
    remainder = sum % 11;
    if (remainder < 2) {
      if (parseInt(this.value.charAt(10)) !== 0) return false;
    } else {
      if (parseInt(this.value.charAt(10)) !== 11 - remainder) return false;
    }

    return true;
  }

  private isValidCnpj(): boolean {
    if (this.value.length !== 14) return false;

    let size = this.value.length - 2;
    let numbers = this.value.substring(0, size);
    let digits = this.value.substring(size);
    let sum = 0;
    let pos = size - 7;
    let i;

    for (i = size; i >= 1; i--) {
      sum += parseInt(this.value.charAt(i - 1)) * pos--;
      if (pos < 2) pos = 9;
    }

    let remainder = sum % 11;
    if (remainder < 2) {
      if (parseInt(digits.charAt(0)) !== 0) return false;
    } else {
      if (parseInt(digits.charAt(0)) !== 11 - remainder) return false;
    }

    sum = 0;
    pos = size - 7;
    for (i = size + 1; i >= 1; i--) {
      sum += parseInt(this.value.charAt(i - 1)) * pos--;
      if (pos < 2) pos = 9;
    }

    remainder = sum % 11;
    if (remainder < 2) {
      if (parseInt(digits.charAt(1)) !== 0) return false;
    } else {
      if (parseInt(digits.charAt(1)) !== 11 - remainder) return false;
    }

    return true;
  }

  getValue(): string {
    return this.value;
  }
}

export default CpfCnpjValueObject;
