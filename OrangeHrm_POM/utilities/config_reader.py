from configparser import ConfigParser

def get_config_data(property,key):
    config=ConfigParser()
    config.read("C:\page_object_model\OrangeHrm_POM\configurations\config.ini")
    return config.get(property,key)
