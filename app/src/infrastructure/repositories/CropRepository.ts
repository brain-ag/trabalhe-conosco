import { EntityManager, Repository } from 'typeorm';
import { AppDataSource } from '../database/data-source';
import { ICropRepository } from '../../domain/repositories/ICropRepository';
import { CropEntity } from '../database/entities/CropEntity';

class CropRepository implements ICropRepository {
  private ormRepository: Repository<CropEntity>;

  constructor(private entityManager: EntityManager) {
    this.ormRepository = AppDataSource.getRepository(CropEntity);
  }

  async save(crop: CropEntity): Promise<CropEntity> {
    return this.ormRepository.save(crop);
  }

  async findByName(name: string): Promise<CropEntity | null> {
    return this.ormRepository.findOne({ where: { name, deleted_at: null } });
  }

  async findById(id: number): Promise<CropEntity | null> {
    return this.ormRepository.findOne({ where: { id, deleted_at: null } });
  }

  async update(crop: CropEntity): Promise<CropEntity> {
    const existingCrop = await this.findById(crop.id);
    if (!existingCrop) {
      throw new Error('Crop not found');
    }
    return this.ormRepository.save(crop);
  }

  async delete(id: number): Promise<boolean> {
    const crop = await this.findById(id);
    if (!crop) {
      return false;
    }
    crop.deleted_at = new Date();
    await this.ormRepository.save(crop);
    return true;
  }

  async findAll(): Promise<CropEntity[]> {
    return this.ormRepository.find({ where: { deleted_at: null } });
  }

  async findCropsByIds(ids: number[]): Promise<CropEntity[]> {
    return this.entityManager
      .createQueryBuilder(CropEntity, 'crop')
      .where('crop.id IN (:...ids)', { ids })
      .getMany();
  }
}

export default CropRepository;
