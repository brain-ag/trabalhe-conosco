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

  createProducer: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const producerData: ProducerDTO = req.body;
      const producer = await this.producerService.createProducer(producerData);

      res
        .status(200)
        .json({ message: 'Producer created successfully', producer: producer });
    } catch (error) {
      res.status(500).json({ error: 'Error creating producer' });
    }
  };

  updateProducer: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const { id } = req.params; // Obtém o ID do produtor da URL
      const producerData: ProducerDTO = req.body; // Dados do produtor a serem atualizados

      const updatedProducer = await this.producerService.updateProducer(
        Number(id),
        producerData
      ); // Chama o serviço para atualizar

      if (!updatedProducer) {
        res
          .status(404)
          .json({ error: 'Producer not found or failed to update' });
        return;
      }

      res
        .status(200)
        .json({
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

      const deletedProducer = await this.producerService.deleteProducer(Number(id));

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

  login: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const { email, password } = req.body;
      const token = await this.producerService.login(email, password);

      res.status(200).json({ message: 'Login successful', token: token });
    } catch (error) {
      res.status(401).json({ error: 'Invalid email or password' });
    }
  };
}

export default new ProducerController();
