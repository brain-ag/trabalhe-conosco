import { DataSource } from 'typeorm';
import { CreateProducer1731602156990 } from './migration/1731602156990-CreateProducer';
import { CreateCrops1731605242579 } from './migration/1731605242579-CreateCrops';
import { CreateFarmsAndFarmCrops1731606890406 } from './migration/1731606890406-CreateFarmsAndFarmCrops';
import { ProducerEntity } from './entities/ProducerEntity';
import { CropEntity } from './entities/CropEntity';
import { FarmEntity } from './entities/FarmEntity';

export const AppDataSource = new DataSource({
  type: 'postgres',
  host: process.env.DB_HOST,
  port: parseInt(process.env.DB_PORT, 10),
  username: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  entities: [ProducerEntity, CropEntity, FarmEntity],
  migrations: [
    CreateProducer1731602156990,
    CreateCrops1731605242579,
    CreateFarmsAndFarmCrops1731606890406,
  ],
  synchronize: false,
  subscribers: [],
});
