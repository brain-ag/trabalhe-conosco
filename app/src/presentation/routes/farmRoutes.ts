import { Router } from 'express';
import { FarmController } from '../controllers/FarmController';
import { FarmRepository } from '../../infrastructure/repositories/FarmRepository';
import FarmService from '../../application/services/FarmService';
import ProducerRepository from '../../infrastructure/repositories/ProducerRepository';
import CropRepository from '../../infrastructure/repositories/CropRepository';
import { AppDataSource } from '../../infrastructure/database/data-source';

const router = Router();
const entityManager = AppDataSource.manager;  
const farmRepository = new FarmRepository();
const producerRepository = new ProducerRepository();
const cropRepository = new CropRepository(entityManager);
const farmService = new FarmService(farmRepository, producerRepository,cropRepository);
const farmController = new FarmController(farmService);

router.post('/farm', farmController.createFarm.bind(farmController));
router.get('/farm', farmController.getAllFarms.bind(farmController));
router.get('/farm/:id', farmController.getFarmById.bind(farmController));
router.put('/farm/:id', farmController.updateFarm.bind(farmController));
router.delete('/farm/:id', farmController.deleteFarm.bind(farmController));

export default router;
