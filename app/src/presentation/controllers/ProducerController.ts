import { Request, Response, RequestHandler } from 'express';
import ProducerService from '../../application/services/ProducerService';
import { ProducerDTO } from '../dto/ProducerDTO';

class ProducerController {
  private producerService = new ProducerService();

  getProducer: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const { id } = req.params;
      const producer = await this.producerService.getProducer(Number(id));

      if (!producer) {
        res.status(404).json({ error: 'Producer not found' });
        return;
      }

      res
        .status(200)
        .json({ message: 'Producer retrieved successfully', producer });
    } catch (error) {
      res.status(500).json({ error: 'Error retrieving producer' });
    }
  };

  updateProducer: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const { id } = req.params;
      const producerData: ProducerDTO = req.body;

      const updatedProducer = await this.producerService.updateProducer(
        Number(id),
        producerData
      );

      if (!updatedProducer) {
        res
          .status(404)
          .json({ error: 'Producer not found or failed to update' });
        return;
      }

      res.status(200).json({
        message: 'Producer updated successfully',
        producer: updatedProducer,
      });
    } catch (error) {
      res.status(500).json({ error: 'Error updating producer' });
    }
  };

  deleteProducer: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const { id } = req.params;

      const deletedProducer = await this.producerService.deleteProducer(
        Number(id)
      );

      if (!deletedProducer) {
        res
          .status(404)
          .json({ error: 'Producer not found or failed to delete' });
        return;
      }

      res.status(200).json({ message: 'Producer deleted successfully' });
    } catch (error) {
      res.status(500).json({ error: 'Error deleting producer' });
    }
  };
}

export default new ProducerController();
