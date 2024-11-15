import { Producer } from '../entities/Producer';

export interface IProducerRepository {
  save(producer: Producer): Promise<Producer>;
  findByEmail(email: string): Promise<Producer | null>;
}
