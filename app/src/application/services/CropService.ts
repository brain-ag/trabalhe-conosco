import { AppDataSource } from '../../infrastructure/database/data-source';
import { CropEntity } from '../../infrastructure/database/entities/CropEntity';
import CropRepository from '../../infrastructure/repositories/CropRepository';
import { CropDTO } from '../../presentation/dto/CropDTO';

class CropService {
  private cropRepository: CropRepository;

  constructor() {
    this.cropRepository = new CropRepository(AppDataSource.manager);
  }

  async getAllCrop(): Promise<CropEntity[] | null> {
    try {
      const crop = await this.cropRepository.findAll();

      return crop;
    } catch (error) {
      throw new Error('Error retrieving crop: ' + error.message);
    }
  }

  async getCropById(id: number): Promise<CropEntity | null> {
    try {
      const crop = await this.cropRepository.findById(id);

      return crop;
    } catch (error) {
      throw new Error('Error retrieving crop: ' + error.message);
    }
  }

  async createCrop(data: CropDTO): Promise<CropEntity> {
    const crop = new CropEntity();
    crop.name = data.name;

    return this.cropRepository.save(crop);
  }

  async updateCrop(id: number, cropData: CropDTO): Promise<CropEntity | null> {
    try {
      const crop = await this.cropRepository.findById(id);
      if (!crop) {
        return null;
      }

      crop.name = cropData.name;

      const updatedCrop = await this.cropRepository.save(crop);
      return updatedCrop;
    } catch (error) {
      throw new Error('Error updating crop: ' + error.message);
    }
  }

  async deleteCrop(id: number): Promise<boolean> {
    try {
      const crop = await this.cropRepository.findById(id);
      if (!crop) {
        return false;
      }

      await this.cropRepository.delete(id);
      return true;
    } catch (error) {
      throw new Error('Error deleting crop: ' + error.message);
    }
  }
}

export default CropService;
