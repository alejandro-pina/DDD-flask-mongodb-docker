from dataclasses import dataclass
from datetime import datetime


@dataclass
class DateVO:
  value: datetime


@dataclass(frozen=True)
class DateVO:
    value: datetime

    def __post_init__(self) -> None:
        if not isinstance(self.value, datetime):
            raise ValueError('Error VO: DateVO - Incorrect date.')

    def today() -> datetime:
        return DateVO(datetime.today())

    def today_europe_str() -> datetime:
        return datetime.strftime(datetime.today(), "%d/%m/%Y %H:%M")

    def date_to_comparate(self) -> datetime:
        return datetime.strftime(self.value, '%Y-%m-%d %H:%M:%S.%f')

    def date_to_string(self) -> str:
        return datetime.strftime(self.value, '%Y-%m-%d %H:%M:%S.%f')

    def date_iso_format(date: str) -> datetime:
        try:
            try:
                date_time = datetime.fromtimestamp(float(date))
            except:
                if len(date) == 16:
                    date_time = datetime.strptime(
                        str(date), '%Y-%m-%dT%H:%M:%S')
                elif len(date) == 10:
                    try:
                        date_obj = datetime.strptime(date, '%d-%m-%Y')
                        new_date_string = date_obj.strftime('%Y-%m-%d')
                        date_time = datetime.strptime(
                            new_date_string, '%Y-%m-%d')
                    except:
                        date_time = datetime.strptime(date, '%Y-%m-%d')
            return DateVO(date_time)
        except:
            raise ValueError('Error VO: DateVO - Incorrect date.')

    def date_convert_europe(self) -> str:
        try:
            date_time_obj = datetime.strptime(
                str(self.value), '%Y-%m-%d %H:%M:%S.%f')
        except:
            date_time_obj = datetime.strptime(
                str(self.value), '%Y-%m-%d %H:%M:%S')
        return datetime.strftime(date_time_obj, "%d/%m/%Y %H:%M")

    def date_iso_format_string(self) -> str:
        return str(datetime.strptime(str(datetime.strftime(self.value, '%Y-%m-%d %H:%M:%S.%f')), '%Y-%m-%d %H:%M:%S.%f').isoformat())

    def __str__(self) -> datetime:
        return str(datetime.strftime(self.value, '%Y-%m-%d %H:%M:%S.%f'))
