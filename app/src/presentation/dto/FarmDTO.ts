export interface FarmDTO {
  id: number;
  city: string;
  state: string;
  areaHectaresFarm: number;
  arableAreaHectares: number;
  vegetationAreaFarm: number;
  producerId: number;
  crop: number[];
  createdAt: Date;
  updatedAt: Date | null;
  deletedAt: Date | null;
}
