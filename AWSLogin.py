import subprocess

def aws_login(access_key_id, secret_access_key, region):
    try:
        subprocess.run(['aws', 'configure', 'set', 'aws_access_key_id', access_key_id], check=True)
        subprocess.run(['aws', 'configure', 'set', 'aws_secret_access_key', secret_access_key], check=True)
        subprocess.run(['aws', 'configure', 'set', 'region', region], check=True)
        print("AWS CLI configured successfully.")
    except subprocess.CalledProcessError as e:
        print("Error configuring AWS CLI:", e)

# Replace these values with your AWS Access Key ID, Secret Access Key, and preferred region
access_key_id = "YOUR_ACCESS_KEY_ID"
secret_access_key = "YOUR_SECRET_ACCESS_KEY"
region = "YOUR_PREFERRED_REGION"

aws_login(access_key_id, secret_access_key, region)

"""
Replace "YOUR_ACCESS_KEY_ID", "YOUR_SECRET_ACCESS_KEY", and "YOUR_PREFERRED_REGION" with your actual AWS IAM user credentials and preferred region. After running this script, your AWS CLI will be configured with the provided credentials, allowing you to interact with AWS services via the CLI. 
"""