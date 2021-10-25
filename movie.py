import boto3
import pandas
from io import StringIO




client = boto3.client('s3', aws_access_key_id='AKIATJ3NUKQFRXYJNWH4', aws_secret_access_key= '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')

csv_obj = client.get_object(Bucket='awsdatatrainig', Key='movies.csv')
csv_obj_body = csv_obj['Body']
csv_string = csv_obj_body.read().decode('utf-8')
print(csv_string)
df = pandas.read_csv(StringIO(csv_string))

df_comedy  = df[df.Genre=='Comedy']
print(df_comedy.head())
csv_buf = StringIO()
df_comedy.to_csv(csv_buf, header=True, index=False)
csv_buf.seek(0)
client.put_object(Bucket='awsdatatrainig', Body=csv_buf.getvalue(), Key='movies.csv_comedy')