import { Request as ExpressRequest } from 'express';

declare global {
  namespace Express {
    export interface Request {
      user: { id: number };
    }
  }
}
