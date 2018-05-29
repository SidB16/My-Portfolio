import boto3
import zipfile
import StringIO

s3 = boto3.resource('s3')

portfolio_bucket = s3.Bucket('sidportfolio')
build_bucket = s3.Bucket('portfoliobuild.sidportfolio')

portfolio_zip = StringIO.StringIO()
build_bucket.download_fileobj('portfolio.zip', portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm)
        portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
