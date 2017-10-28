import reader.ParamHandler

config = reader.ParamHandler.ParamHandler.get_instance('./params.pickle')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()

#config = reader.ParamHandler.ParamHandler.get_instance('./params.pickle')
config.read() # читаем данные из текстового файла

config = reader.ParamHandler.ParamHandler.get_instance('./params.json')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()

#config = reader.ParamHandler.ParamHandler.get_instance('./params.pickle')
config.read()