import sagemaker as sage
from time import gmtime, strftime
from sagemaker.predictor import csv_serializer


def deploy():
    sess = sage.Session()
    account = sess.boto_session.client("sts").get_caller_identity()["Account"]
    region = sess.boto_session.region_name
    role = 'arn:aws:iam::122936777114:role/cits_sagemaker'

    # image = "{}.dkr.ecr.{}.amazonaws.com/sagemaker-decision-trees:latest".format(account, region)
    image = '122936777114.dkr.ecr.us-east-1.amazonaws.com/cits_byo:latest'

    tree = sage.estimator.Estimator(
        image,
        role,
        1,
        "ml.c4.2xlarge",
        output_path="s3://cits-byotf/output",
        sagemaker_session=sess,
    )
    tree.fit()

    predictor = tree.deploy(1, "ml.m4.xlarge", serializer=csv_serializer)


deploy()
