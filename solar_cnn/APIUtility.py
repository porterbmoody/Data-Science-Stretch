#%%
import requests
import bcrypt
import boto3
from pluscodepy import Converter


#%%

# s3 = boto3.client('s3',
    # aws_access_key_id = APIUtility.aws_access_key_id,
    # aws_secret_access_key = APIUtility.aws_secret_access_key)
# plus_code = '85983CHR+RH'
# image_raw = APIUtility.download_static_image(plus_code)
# image_raw


#%%

class APIUtility:

    def __init__(self) -> None:
        pass

    static_map_key = 'AIzaSyBYZHD0dhidkig5nUiiCaDC6dDlEHiCzy8'
    geocoding_key = 'AIzaSyDqmrxYDo6AhcB803AImc6zFRTPBI9r7gk'
    # aws
    aws_access_key_id = 'AKIAXX26BIR4HMUPX4XF'
    aws_secret_access_key = '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'
    s3_bucket = "true-solar"
    access_point_arn = 'arn:aws:s3:us-west-1:532236289144:accesspoint/images'

    # address_validation_key = ''
    images_without_panels_path = 'static/images/images_without_panels/'
    images_with_panels_path = 'static/images/images_without_panels/'
    salt = b'$2b$12$QLSv570.AGknBvpC05/WTO'
    kwargs = {
    'host': 'cis9cbtgerlk68wl.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    'user': 'ter21gfil5dkcw7j',
    'password': 'xwyhh9839rdj3dld',
    'port': 3306,
    'database': 'n47q0x4jkrhbw9cp'
    }

    @staticmethod
    def get_geocode(address):
        geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={APIUtility.geocoding_key}'
        response = requests.get(geocoding_url).json()
        return response['results'][0]

    @staticmethod
    def get_plus_code(address):
        plus_code_url = f'https://plus.codes/api?address={address}&ekey={APIUtility.geocoding_key}'
        response = requests.get(plus_code_url).json()
        # check if plus code successfully called from google maps api
        if response['status'] == 'OK':
            return response['plus_code']['global_code']
        else:
            raise ValueError("Could not retrieve plus code")

    @staticmethod
    def get_static_image(coordinates):
        zoom = '20'
        size = '400x400'
        maptype = 'satellite'
        center = f'{coordinates[0]},{coordinates[1]}'
        static_map_url = f'https://maps.googleapis.com/maps/api/staticmap?center={center}&zoom={zoom}&size={size}&maptype={maptype}&key={APIUtility.static_map_key}'
        response = requests.get(static_map_url, stream=True)
        return response.raw
    
    @staticmethod
    def plus_code_to_coordinates(plus_code):
        converter = Converter()
        return converter.decode(plus_code)

    @staticmethod
    def get_s3_folder_list(folder):
        s3 = boto3.client('s3',
            aws_access_key_id=APIUtility.aws_access_key_id,
            aws_secret_access_key=APIUtility.aws_secret_access_key)
        response = s3.list_objects_v2(
        Bucket = APIUtility.bucket,
        Prefix = folder,
        Delimiter = '/'
        )
        return list(response['Contents'])

    @staticmethod
    def download_static_image(plus_code) -> None:
        """ Stores image in s3 bucket then gets predesigned url to be rendered in html file.
        """
        s3 = boto3.client('s3',
            aws_access_key_id=APIUtility.aws_access_key_id,
            aws_secret_access_key=APIUtility.aws_secret_access_key)
        print("getting static image")
        coordinates = APIUtility.plus_code_to_coordinates(plus_code)
        image_raw = APIUtility.get_static_image(coordinates)
        print("uploading image to s3")
        s3.upload_fileobj(image_raw, APIUtility.access_point_arn, "images_without_panels/" + plus_code + '.png')
        # with open("images_without_panels/" + static_image_filename, 'rb') as key:
            # s3.upload_fileobj(image_raw, 'true-solar', Key = key)

    @staticmethod
    def predesigned_url(static_image_filename):
        s3 = boto3.client('s3',
            aws_access_key_id=APIUtility.aws_access_key_id,
            aws_secret_access_key=APIUtility.aws_secret_access_key)
        s3.generate_predesigned_url(
            'get_object', 
            Params = {'Bucket' : APIUtility.bucket,
                      'Key' : "images_without_panels/" + static_image_filename}
            )