FROM node:20-alpine as build
WORKDIR /app
COPY package.json /app/package.json
RUN npm install
COPY . /app
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/dist /app/dist
RUN npm i -g serve
EXPOSE 5173
CMD ["serve", "-s", "dist", "-l", "5173"]
