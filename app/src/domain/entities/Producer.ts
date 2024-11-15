export class Producer {
  constructor(
    public name: string,
    public email: string,
    public password: string,
    public cpf_cnpj: string,
    public id?: number,
    public createdAt?: Date,
    public updatedAt?: Date,
    public deletedAt?: Date
  ) {}
}
