from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)
from random import randint


metric_reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
provider = MeterProvider(metric_readers=[metric_reader])

# Sets the global default meter provider
metrics.set_meter_provider(provider)

# Creates a meter from the global meter provider
meter = metrics.get_meter("my.meter.name")

roll_counter = meter.create_counter(
    "dice.rolls",
    description="The number of rolls by roll value",
)

def roll():
    return randint(1, 2)

for i in range(5):
    result = str(roll())
    roll_counter.add(1, {"roll.value": result})

