FROM node:20-alpine

# Set env variables
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL

# Set working directory
WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy package.json and lock file
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy the rest of the application
COPY . .

# Build the application
RUN pnpm build

ENTRYPOINT ["pnpm", "preview", "--host", "0.0.0.0", "--port", "80"]

## Production stage
#FROM nginx:stable-alpine AS production
#
## Copy built assets from build stage
#COPY --from=build /app/build/ /usr/share/nginx/html
#
## Copy nginx config
#RUN rm -rf /etc/nginx/conf.d
#COPY nginx.conf /etc/nginx/conf.d/default.conf
#
## Expose port
#EXPOSE 80
#
#CMD ["nginx", "-g", "daemon off;"]
