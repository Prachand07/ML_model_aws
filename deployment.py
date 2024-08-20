from sagemaker.sklearn.model import SKLearnModel

model_uri = 's3://bucket_name/model.tar.gz'   #Bucket that has the model
entry_point = 'inference.py'                  #entry point script

model = SKLearnModel(
    model_data=model_uri,
    role=role,
    entry_point=entry_point,
    framework_version='1.2-1',                    #scikit-learn version
    sagemaker_session=sagemaker_session
)

predictor = model.deploy(
    instance_count=1,
    instance_type='ml.m5.large'
)