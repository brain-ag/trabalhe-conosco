export class Producer {
  constructor(
    public name: string,
    public city: string,
    public state: string,
    public areaHectaresFarm: number,
    public arableAreaHectares: number,
    public vegetationAreaFarm: number,
    public producer: number,
    public crop: number,
    public id?: number,
    public createdAt?: Date,
    public updatedAt?: Date,
    public deletedAt?: Date
  ) {}
}
