# Machine Learning

## TF-Serving Deployment use Docker

Build the docker image by running this command

```bash
docker build -t snackscan-tf-serving .
```

Then run the image and expose the port. Note that TensorFlow Serving is using port 8501 in the container.

```bash
docker run -p 8080:8501 snackscan-tf-serving
```
