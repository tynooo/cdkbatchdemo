
# Simple AWS Batch demo in CDK Python




## Getting it running

Assuming you have Python3 and CDK installed

Clone this repo and get your environment ready

```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
npm -g upgrade
```



Then run ```cdk deploy CdkbatchdemoStack``` to deploy to your account, it'll also deploy the infra stack which provisions a fresh VPC

When you're done run ```cdk destroy CdkbatchdemoStack``` to tear it all down