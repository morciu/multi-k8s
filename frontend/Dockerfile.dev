FROM node:lts

WORKDIR /app
COPY ./package.json ./
RUN npm install
COPY . .
CMD [ "npm", "start" ]

# Must be run with '--env-file .env' flag
# Ex: docker run --env-file .env 'image-name'
