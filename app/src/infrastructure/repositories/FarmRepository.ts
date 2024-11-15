import { IFarmRepository } from '../../domain/repositories/IFarmRepository';
import { Repository } from 'typeorm';
import { AppDataSource } from '../database/data-source';
import { FarmEntity } from '../database/entities/FarmEntity';

export class FarmRepository implements IFarmRepository {
  private ormRepository: Repository<FarmEntity>;

  constructor() {
    this.ormRepository = AppDataSource.getRepository(FarmEntity);
  }

  async create(farm: FarmEntity): Promise<FarmEntity> {
    return this.ormRepository.save(farm);
  }

  async findAll(): Promise<FarmEntity[]> {
    return this.ormRepository.find();
  }

  async findById(id: number): Promise<FarmEntity | null> {
    return this.ormRepository.findOneBy({ id });
  }

  async update(farm: FarmEntity): Promise<FarmEntity> {
    return this.ormRepository.save(farm);
  }

  async delete(id: number): Promise<void> {
    await this.ormRepository.delete(id);
  }
}
