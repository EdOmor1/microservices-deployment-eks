# microservices-deployment-eks

## Use Case: Scalable E-Commerce Platform for Water Sales

In the context of an e-commerce platform specializing in selling water products, the goal is to build a scalable and resilient infrastructure using microservices architecture. By breaking down the platform into smaller, independent services, such as user management, product catalog, payment processing, and order fulfillment, the platform aims to enhance agility, scalability, and fault tolerance.

Each microservice will be deployed as a Docker container on Amazon EKS, allowing for independent scaling, updates, and fault isolation. This architecture enables the e-commerce platform to handle varying loads and ensure high availability during peak times.

Note: dockerfiles are sample for this basic project, register for docker (if haven't already) and get the necessary details and input appropriately.

This project has room for growth even further, and will update in due course.

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

