Predict Server

Run
- docker build -t test-deploy-server:1 .

- docker run -p 80:80 test-deploy-server:1 



TODO

- Add Kubernetes Helm charts to deploy.


Potential Improvements-

- Upload predict function to a pickle and upload it to repository.
- Deploy model to kubernetes using k8 wrapper/kServe
