import {
  Entity,
  Column,
  PrimaryGeneratedColumn,
  CreateDateColumn,
  UpdateDateColumn,
  DeleteDateColumn,
  ManyToOne,
  OneToMany,
  JoinColumn,
  ManyToMany,
  JoinTable,
} from 'typeorm';
import { ProducerEntity } from './ProducerEntity';
import { CropEntity } from './CropEntity';

@Entity('farms')
export class FarmEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  city: string;

  @Column()
  state: string;

  @Column({ name: 'area_hectares_farm', type: 'float' })
  areaHectaresFarm: number;

  @Column({ name: 'arable_area_hectares', type: 'float' })
  arableAreaHectares: number;

  @Column({ name: 'vegetation_area_farm', type: 'float' })
  vegetationAreaFarm: number;

  @ManyToOne(() => ProducerEntity, (producer) => producer.farms)
  @JoinColumn({ name: 'producer_id' })
  producer: ProducerEntity;

  @CreateDateColumn({ name: 'created_at' })
  createdAt: Date;

  @UpdateDateColumn({ name: 'updated_at', nullable: true })
  updatedAt: Date;

  @DeleteDateColumn({ name: 'deleted_at', nullable: true })
  deletedAt: Date | null;

  @ManyToMany(() => CropEntity, (crop) => crop.farms)
  @JoinTable({
    name: 'farm_crops',
    joinColumn: {
      name: 'farm_id',
      referencedColumnName: 'id',
    },
    inverseJoinColumn: {
      name: 'crop_id',
      referencedColumnName: 'id',
    },
  })
  crops: CropEntity[];
}
