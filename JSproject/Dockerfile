# Use Node base image
FROM node:18

# Create app directory
WORKDIR /usr/src/app

# Copy package files and install dependencies (including dev dependencies)
COPY package*.json ./ 
RUN npm install

# Install mocha globally to ensure the test environment is available
RUN npm install -g mocha

# Copy the rest of the project
COPY . .

# Run tests using Mocha
RUN mocha test.js

# Expose app port
EXPOSE 8000

# Run app
CMD ["npm", "start"]

