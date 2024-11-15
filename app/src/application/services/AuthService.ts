import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import ProducerRepository from '../../infrastructure/repositories/ProducerRepository';

class AuthService {
  private producerRepository = new ProducerRepository();

  constructor() {
    this.producerRepository = new ProducerRepository();
  }

  async login(email: string, password: string): Promise<string> {
    const producer = await this.producerRepository.findByEmail(email);
    if (!producer || !(await bcrypt.compare(password, producer.password))) {
      throw new Error('Invalid email or password');
    }

    const token = jwt.sign({ id: producer.id }, process.env.JWT_SECRET, {
      expiresIn: '1h',
    });
    return token;
  }
}

export default AuthService;
