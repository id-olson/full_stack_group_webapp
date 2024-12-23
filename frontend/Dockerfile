FROM node:21-alpine
ENV NODE_ENV production
WORKDIR /app/frontend
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --omit=dev
# Fix for node_modules root permission https://stackoverflow.com/a/67540612
RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache
USER node
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
