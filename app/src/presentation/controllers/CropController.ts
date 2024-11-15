import { Request, Response, RequestHandler } from 'express';
import CropService from '../../application/services/CropService';
import { CropDTO } from '../dto/CropDTO';

class CropController {
  private cropService = new CropService();

  getAllCrop: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const crop = await this.cropService.getAllCrop();

      res.status(200).json({ message: 'Crop retrieved successfully', crop });
    } catch (error) {
      res.status(500).json({ error: 'Error retrieving crop' });
    }
  };

  getCrop: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const { id } = req.params;
      const crop = await this.cropService.getCropById(Number(id));

      if (!crop) {
        res.status(404).json({ error: 'Producer not found' });
        return;
      }

      res.status(200).json({ message: 'Crop retrieved successfully', crop });
    } catch (error) {
      res.status(500).json({ error: 'Error retrieving crop' });
    }
  };

  createCrop: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const cropData: CropDTO = req.body;
      const crop = await this.cropService.createCrop(cropData);

      res
        .status(200)
        .json({ message: 'Crop created successfully', crop: crop });
    } catch (error) {
      res.status(500).json({ error: 'Error creating crop' });
    }
  };

  updateCrop: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const { id } = req.params;
      const cropData: CropDTO = req.body;

      const updatedCrop = await this.cropService.updateCrop(
        Number(id),
        cropData
      );

      if (!updatedCrop) {
        res.status(404).json({ error: 'Crop not found or failed to update' });
        return;
      }

      res.status(200).json({
        message: 'Crop updated successfully',
        crop: updatedCrop,
      });
    } catch (error) {
      res.status(500).json({ error: 'Error updating Crop' });
    }
  };

  deleteCrop: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const { id } = req.params;

      const deletedCrop = await this.cropService.deleteCrop(Number(id));

      if (!deletedCrop) {
        res.status(404).json({ error: 'Crop not found or failed to delete' });
        return;
      }

      res.status(200).json({ message: 'Crop deleted successfully' });
    } catch (error) {
      res.status(500).json({ error: 'Error deleting Crop' });
    }
  };
}

export default new CropController();
