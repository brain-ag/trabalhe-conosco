import { Repository } from 'typeorm';
import { IProducerRepository } from '../../domain/repositories/IProducerRepository';
import { AppDataSource } from '../database/data-source';
import { ProducerEntity } from '../database/entities/ProducerEntity';

class ProducerRepository implements IProducerRepository {
  private ormRepository: Repository<ProducerEntity>;

  constructor() {
    this.ormRepository = AppDataSource.getRepository(ProducerEntity);
  }

  async save(producer: ProducerEntity): Promise<ProducerEntity> {
    return this.ormRepository.save(producer);
  }

  async findByEmail(email: string): Promise<ProducerEntity | null> {
    return this.ormRepository.findOne({ where: { email, deleted_at: null } });
  }

  async findById(id: number): Promise<ProducerEntity | null> {
    return this.ormRepository.findOne({ where: { id, deleted_at: null } });
  }

  async update(producer: ProducerEntity): Promise<ProducerEntity> {
    const existingProducer = await this.findById(producer.id);
    if (!existingProducer) {
      throw new Error('Producer not found');
    }
    return this.ormRepository.save(producer);
  }

  async delete(id: number): Promise<boolean> {
    const producer = await this.findById(id);
    if (!producer) {
      return false;
    }

    producer.deleted_at = new Date();
    await this.ormRepository.save(producer);
    return true;
  }

  async findAll(): Promise<ProducerEntity[]> {
    return this.ormRepository.find({ where: { deleted_at: null } });
  }
}

export default ProducerRepository;
