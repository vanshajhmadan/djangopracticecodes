# Specify Base image
FROM node:alpine

WORKDIR /code/simpleweb/

# install the dependencies 
COPY package.json /code/

RUN npm install


# Default command 
CMD ["npm", "start"]