# fastapi-aws-lambda
This repository is a demo for hosting a FastAPI application on AWS Lambda using Mangum.

Project Structure
. ├── .gitignore 
  ├── main.py 
  ├── README.md 
  └── requirements.txt
Requirements
Python 3.9+
AWS Account
Installation
Clone the repository:

git clone https://github.com/rishabkumar7/fastapi-aws-lambda.git
cd fastapi-aws-lambda
Create a virtual environment and activate it:

python -m venv .venv
.venv\Scripts\Activate  # On Linux/Mac use `source .venv/bin/activate`
Install the dependencies:

pip install -r requirements.txt
Running Locally
You can run the FastAPI application locally using Uvicorn, but will need to install uvicorn:

pip install uvicorn
uvicorn main:app --reload
Deploying to AWS Lambda
Zip your FastAPI application and upload the zip to an AWS Lambda Function.

Zip on Windows:

Compress-Archive .\.venv\Lib\site-packages\* aws_lambda.zip
Compress-Archive .\main.py -Update aws_lambda.zip
