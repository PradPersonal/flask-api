Description
1. Jenkins CI CD pipeline for flask application
Objective:
Set up a Jenkins pipeline that automates the testing and deployment of a simple Python web application.
Requirements:
1. Setup:
   - Install Jenkins on a virtual machine or use a cloud-based Jenkins service.
   - Configure Jenkins with Python and any necessary libraries.
 <img width="654" height="495" alt="image" src="https://github.com/user-attachments/assets/5f11ef43-aec2-4c53-a5f6-21304e438b6d" />

2. Source Code:
  - Fork the provided Python web application repository on GitHub (provide a link to a sample Python web application repository).
 <img width="771" height="547" alt="image" src="https://github.com/user-attachments/assets/5cc81484-d372-4bbe-aa85-2f27992f813e" />

  - Clone the forked repository into your Jenkins server.

3. Jenkins Pipeline:
   - Create a Jenkinsfile in the root of your Python application repository.
   - Define a pipeline with the following stages:
    - Build: Install dependencies using pip.
    - Test: Run unit tests using a testing framework like pytest.
    - Deploy: If tests pass, deploy the application to a staging environment.
 <img width="940" height="518" alt="image" src="https://github.com/user-attachments/assets/ef8aae3e-aee9-428d-9a6d-51b90cb38a3f" />


4. Triggers:
   - Configure the pipeline to trigger a new build whenever changes are pushed to the main branch of the repository.
 
 
5. Notifications:
   - Set up a notification system to alert via email when the build process fails or succeeds.


