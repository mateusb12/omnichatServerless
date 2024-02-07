1. Retrieve an authentication token and authenticate your Docker client to your registry.
Use the AWS CLI
```bash
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 590183930877.dkr.ecr.us-east-2.amazonaws.com
```

2. Build your Docker image using the following command.
```bash
docker build -t docker-lambda .
````

3. After the build completes, tag your image so you can push the image to this repository
```bash
docker tag docker-lambda:latest 590183930877.dkr.ecr.us-east-2.amazonaws.com/docker-lambda:latest
```
4. Run the following command to push this image to your newly created AWS repository
```bash
docker push 590183930877.dkr.ecr.us-east-2.amazonaws.com/docker-lambda:latest
```