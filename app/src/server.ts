import 'reflect-metadata';
import express from 'express';
import 'dotenv/config';

import { AppDataSource } from './infrastructure/database/data-source';
import producerRoutes from './presentation/routes/producerRoutes';
import cropRoutes from './presentation/routes/cropRoutes';
import farmRoutes from './presentation/routes/farmRoutes';
import authMiddleware from './infrastructure/security/authMiddleware';
import authRoutes from './presentation/routes/authRoutes';

const app = express();

app.use(express.json());

app.use('/login', authRoutes)

app.use('/api', authMiddleware);
app.use('/api', producerRoutes);
app.use('/api', cropRoutes);
app.use('/api', farmRoutes);

AppDataSource.initialize()
  .then(() => {
    console.log('Data Source has been initialized!');

    app.listen(3000, () => console.log('Server is running!'));
  })
  .catch((error) =>
    console.error('Error during Data Source initialization', error)
  );
