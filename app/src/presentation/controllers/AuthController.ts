import { Request, Response, RequestHandler } from 'express';
import AuthService from '../../application/services/AuthService';

class AuthController {
  private authService = new AuthService();

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
