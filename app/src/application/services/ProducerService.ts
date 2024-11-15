import { ProducerDTO } from '../../presentation/dto/ProducerDTO';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import ProducerRepository from '../../infrastructure/repositories/ProducerRepository';
import { ProducerEntity } from '../../infrastructure/database/entities/ProducerEntity';
import CpfCnpjValueObject from '../../domain/valueObjects/CpfCnpjValueObject';

class ProducerService {
  private producerRepository = new ProducerRepository();

  constructor() {
    this.producerRepository = new ProducerRepository();
  }

  async getProducer(id: number): Promise<ProducerEntity | null> {
    try {
      const producer = await this.producerRepository.findById(id);
      return producer;
    } catch (error) {
      throw new Error('Error retrieving producer: ' + error.message);
    }
  }

  async createProducer(data: ProducerDTO): Promise<ProducerEntity> {
    new CpfCnpjValueObject(data.cpf_cnpj);

    const hashedPassword = await bcrypt.hash(data.password, 10);
    const producer = new ProducerEntity();
    producer.name = data.name;
    producer.email = data.email;
    producer.password = hashedPassword;
    producer.cpf_cnpj = data.cpf_cnpj;

    return this.producerRepository.save(producer);
  }

  async updateProducer(
    id: number,
    producerData: ProducerDTO
  ): Promise<ProducerEntity | null> {
    try {
      const producer = await this.producerRepository.findById(id);
      if (!producer) {
        return null;
      }

      new CpfCnpjValueObject(producerData.cpf_cnpj);

      producer.name = producerData.name;
      producer.email = producerData.email;
      producer.password = producerData.password;

      const updatedProducer = await this.producerRepository.save(producer);
      return updatedProducer;
    } catch (error) {
      throw new Error('Error updating producer: ' + error.message);
    }
  }

  async deleteProducer(id: number): Promise<boolean> {
    try {
      const producer = await this.producerRepository.findById(id);
      if (!producer) {
        return false;
      }

      await this.producerRepository.delete(id);
      return true;
    } catch (error) {
      throw new Error('Error deleting producer: ' + error.message);
    }
  }
}

export default ProducerService;
