import logging

import os
from flask import Flask
from flask import render_template
from flask import request

from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource

logger_provider = LoggerProvider(
    resource=Resource.create(
        {
            "service.name": "flask_test",
            "service.instance.id": os.uname().nodename,
        }
    ),
)
set_logger_provider(logger_provider)

otlp_exporter = OTLPLogExporter(endpoint="http://collector:4317", insecure=True)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(otlp_exporter))

handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)
logging.getLogger().addHandler(handler)
main_logger = logging.getLogger("flask.main")
main_logger.setLevel(logging.INFO)


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        log_level = str(request.form['optLogLevel'])
        log_message = request.form['txtMessage']
        if log_level == '1':
            main_logger.debug(log_message)
        elif log_level == '2':
            main_logger.info(log_message)
        elif log_level == '3':
            main_logger.warning(log_message)
        elif log_level == '4':
            main_logger.error(log_message)
        elif log_level == '5':
            main_logger.critical(log_message)
        else:
            pass                                                

        return render_template('index.html')
    else:        
        return render_template('index.html')

if __name__ == '__main__':
    main_logger.info("Starting Flask")
    app.run()