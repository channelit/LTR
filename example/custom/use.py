import sagemaker as sage

sess = sage.Session()
WORK_DIRECTORY = "/tmp/cifar-10-data"

data_location = sess.upload_data(WORK_DIRECTORY, key_prefix=prefix)