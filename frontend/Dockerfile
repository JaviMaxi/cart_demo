FROM node:16 AS compilacion_frontend

COPY ./ /frontend
WORKDIR /frontend
RUN npm install
RUN npm run build

FROM nginx:latest
COPY --from=compilacion_frontend /frontend/dist  /usr/share/nginx/html