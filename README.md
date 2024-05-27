# microservices-deployment-eks

## Use Case:

A scalable and resilient e-commerce platform which utilises microservices to breakdown each service into the following: user management, product catalog, payment processing, and order fulfillment. 

Each microservice will be deployed as a Docker container on Amazon EKS, allowing for independent scaling, updates, and fault isolation. This architecture enables the e-commerce platform to handle varying loads and ensure high availability during peak times.

## Repository Structure

- `src/`: Contains the source code for microservices.
  - `user-management/`: Contains Dockerfile and source code for the user management microservice.
  - `product-catalog/`: Contains Dockerfile and source code for the product catalog microservice.
  - `payment-processing/`: Contains Dockerfile and source code for the payment processing microservice.
  - `order-fulfillment/`: Contains Dockerfile and source code for the order fulfillment microservice.
- `kubernetes-manifests/`: Contains Kubernetes manifests for deploying microservices.
  - `user-management.yaml`: Kubernetes manifest for deploying the user management microservice.
  - `product-catalog.yaml`: Kubernetes manifest for deploying the product catalog microservice.
  - `payment-processing.yaml`: Kubernetes manifest for deploying the payment processing microservice.
  - `order-fulfillment.yaml`: Kubernetes manifest for deploying the order fulfillment microservice.
- `README.md`: Documentation for setting up and deploying microservices on Amazon EKS.

