import { FarmEntity } from '../../infrastructure/database/entities/FarmEntity';

export interface IFarmRepository {
  create(farm: FarmEntity): Promise<FarmEntity>;
  findAll(): Promise<FarmEntity[]>;
  findById(id: number): Promise<FarmEntity | null>;
  update(farm: FarmEntity): Promise<FarmEntity>;
  delete(id: number): Promise<void>;
}
