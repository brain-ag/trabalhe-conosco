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
const farmService = new FarmService(
  farmRepository,
  producerRepository,
  cropRepository
);
const farmController = new FarmController(farmService);

/**
 * @swagger
 * tags:
 *   - name: Farm
 *     description: Operations related to farms
 */

/**
 * @swagger
 * /farm:
 *    post:
 *      tags: [Farm]
 *      summary: Create a new farm
 *      description: Create a new farm with the provided data.
 *      requestBody:
 *        required: true
 *        content:
 *          application/json:
 *            schema:
 *              type: object
 *              properties:
 *                name:
 *                  type: string
 *                  description: The name of the farm
 *                areaHectaresFarm:
 *                  type: number
 *                  format: float
 *                  description: The total area of the farm in hectares
 *                arableAreaHectares:
 *                  type: number
 *                  format: float
 *                  description: The arable area of the farm in hectares
 *                vegetationAreaFarm:
 *                  type: number
 *                  format: float
 *                  description: The vegetation area of the farm in hectares
 *                producer:
 *                  type: number
 *                  format: int
 *                  description: The producer ID
 *                crop:
 *                  type: array
 *                  items:
 *                    type: integer
 *                  description: Array of crop IDs
 *      responses:
 *        201:
 *          description: Farm created successfully
 *        500:
 *          description: Internal server error
 */
router.post('/farm', farmController.createFarm.bind(farmController));

/**
 * @swagger
 *  /farm:
 *    get:
 *      tags: [Farm]
 *      summary: Get all farms
 *      description: Retrieve a list of all farms.
 *      responses:
 *        200:
 *          description: List of all farms
 *        500:
 *          description: Internal server error
 */
router.get('/farm', farmController.getAllFarms.bind(farmController));

/**
 * @swagger
 *  /farm/{id}:
 *    get:
 *      tags: [Farm]
 *      summary: Get a farm by ID
 *      description: Retrieve the details of a specific farm by its ID.
 *      parameters:
 *        - in: path
 *          name: id
 *          required: true
 *          description: The farm ID
 *          schema:
 *            type: integer
 *      responses:
 *        200:
 *          description: Farm found
 *        404:
 *          description: Farm not found
 *        500:
 *          description: Internal server error
 */
router.get('/farm/:id', farmController.getFarmById.bind(farmController));

/**
 * @swagger
 *  /farm/{id}:
 *    put:
 *      tags: [Farm]
 *      summary: Update farm details
 *      description: Update the details of an existing farm.
 *      parameters:
 *        - in: path
 *          name: id
 *          required: true
 *          description: The farm ID
 *          schema:
 *            type: integer
 *      requestBody:
 *        required: true
 *        content:
 *          application/json:
 *            schema:
 *              type: object
 *              properties:
 *                name:
 *                  type: string
 *                areaHectaresFarm:
 *                  type: number
 *                  format: float
 *                arableAreaHectares:
 *                  type: number
 *                  format: float
 *                vegetationAreaFarm:
 *                  type: number
 *                  format: float
 *                crop:
 *                  type: array
 *                  items:
 *                    type: integer
 *      responses:
 *        200:
 *          description: Farm updated successfully
 *        404:
 *          description: Farm not found
 *        500:
 *          description: Internal server error
 */
router.put('/farm/:id', farmController.updateFarm.bind(farmController));

/**
 * @swagger
 *  /farm/{id}:
 *    delete:
 *      tags: [Farm]
 *      summary: Delete a farm by ID
 *      description: Delete a specific farm using its ID.
 *      parameters:
 *        - in: path
 *          name: id
 *          required: true
 *          description: The farm ID
 *          schema:
 *            type: integer
 *      responses:
 *        204:
 *          description: Farm deleted successfully
 *        404:
 *          description: Farm not found
 *        500:
 *          description: Internal server error
 */
router.delete('/farm/:id', farmController.deleteFarm.bind(farmController));

export default router;
