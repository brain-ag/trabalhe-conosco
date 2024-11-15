FROM node:22-alpine

RUN apk add --no-cache shadow

RUN usermod -u 1000 node && groupmod -g 1000 node

WORKDIR /app

RUN chown -R node:node /app

USER node

EXPOSE 3000

CMD ["sh"]
