import { Router } from 'express';
import ProducerController from '../controllers/ProducerController';

const router = Router();

router.get('/producer/:id', ProducerController.getProducer);
router.post('/producer', ProducerController.createProducer);
router.put('/producer/:id', ProducerController.updateProducer);
router.post('/producer/login', ProducerController.login);
router.delete('/producer/:id', ProducerController.deleteProducer);

export default router;
