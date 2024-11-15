import path from 'path';
import { OpenAPIV3 } from 'openapi-types';
import swaggerJsdoc from 'swagger-jsdoc';

const isProduction = process.env.NODE_ENV === 'production';
const routeExtension = isProduction ? '*.js' : '*.ts';

const swaggerOptions: swaggerJsdoc.Options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Brian Agriculture API',
      version: '1.0.0',
      description: 'API para gerenciamento',
    },
    servers: [
      {
        url: process.env.URL,
      },
    ],
  },
  apis: [path.resolve(__dirname, `../routes/${routeExtension}`)],
};

const swaggerDocs: OpenAPIV3.Document = swaggerJsdoc(swaggerOptions);

export default swaggerDocs;
