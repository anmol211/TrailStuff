import dataclasses
import json
from datetime import datetime


@dataclasses.dataclass
class ExtractionField:
    created_date: datetime


def convert(o: ExtractionField):
    if isinstance(o.created_date, datetime):
        o.created_date = o.created_date.isoformat()
    return o.__dict__


obj = ExtractionField(created_date=datetime.now())
s = json.dumps([obj], default=convert)
print(s)
