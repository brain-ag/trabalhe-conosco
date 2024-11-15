import { Crop } from '../entities/Crop';

export interface ICropRepository {
  save(crop: Crop): Promise<Crop>;
  findByName(name: string): Promise<Crop | null>;
}
