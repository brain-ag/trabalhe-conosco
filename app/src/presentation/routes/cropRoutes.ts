import { Router } from 'express';
import CropController from '../controllers/CropController';

const router = Router();

router.get('/crop', CropController.getAllCrop);
router.get('/crop/:id', CropController.getCrop);
router.post('/crop', CropController.createCrop);
router.put('/crop/:id', CropController.updateCrop);
router.delete('/crop/:id', CropController.deleteCrop);

export default router;
