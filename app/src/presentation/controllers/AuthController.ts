import { Request, Response, RequestHandler } from 'express';
import AuthService from '../../application/services/AuthService';
import { ProducerDTO } from '../dto/ProducerDTO';
import ProducerService from '../../application/services/ProducerService';

class AuthController {
  private authService = new AuthService();
  private producerService = new ProducerService();

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

  login: RequestHandler = async (
    req: Request,
    res: Response
  ): Promise<void> => {
    try {
      const { email, password } = req.body;
      const token = await this.authService.login(email, password);

      res.status(200).json({ message: 'Login successful', token: token });
    } catch (error) {
      res.status(401).json({ error: 'Invalid email or password' });
    }
  };
}

export default new AuthController();
