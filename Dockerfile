
FROM node:20-slim

WORKDIR /app

RUN apt update && apt install -y \
  ffmpeg \
  libsodium-dev \
  && rm -rf /var/lib/apt/lists/*

COPY package.json ./
RUN npm install --production

COPY . .

CMD ["npm", "start"]
