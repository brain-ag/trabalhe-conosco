import { Request, Response } from 'express';
import FarmService from '../../application/services/FarmService';

export class FarmController {
  constructor(private readonly farmService: FarmService) {}

  async createFarm(req: Request, res: Response): Promise<void> {
    try {
      const data = req.body;
      const producerId = req.user.id;
      const farm = await this.farmService.createFarm(data, producerId);

      res.status(201).json(farm);
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  }

  async getAllFarms(req: Request, res: Response): Promise<void> {
    try {
      const farms = await this.farmService.getAllFarms();
      res.status(200).json(farms);
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  }

  async getFarmById(req: Request, res: Response): Promise<void> {
    try {
      const farm = await this.farmService.getFarmById(Number(req.params.id));
      if (!farm) {
        res.status(404).json({ message: 'Farm not found' });
      } else {
        res.status(200).json(farm);
      }
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  }

  async updateFarm(req: Request, res: Response): Promise<void> {
    try {
      const farm = await this.farmService.updateFarm(
        Number(req.params.id),
        req.body
      );
      res.status(200).json(farm);
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  }

  async deleteFarm(req: Request, res: Response): Promise<void> {
    try {
      await this.farmService.deleteFarm(Number(req.params.id));
      res.status(204).send();
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  }
}
