import csv
import datetime
import logging

from pep_parse.constants import BASE_DIR, DT_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = {}

    def process_item(self, item, spider):
        key = item.get('status')
        self.statuses[key] = self.statuses.get(key, 0) + 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        time = datetime.datetime.now().strftime(DT_FORMAT)
        file_name = results_dir / f'status_summary_{time}.csv'
        try:
            results_dir.mkdir(exist_ok=True)
            with open(file_name, 'w', encoding='utf-8') as file:
                results_writer = csv.writer(file)
                results_writer.writerows(
                    (
                        ('Статус', 'Количество'),
                        *sorted(self.statuses.items()),
                        ('Total', sum(self.statuses.values()))
                    )
                )
        except PermissionError:
            logging.exception(
                f'Недостаточно прав для создания файлов в {BASE_DIR}',
                exc_info=True
            )
            raise
        except OSError:
            logging.exception(
                f'Ошибка при работе с файлами в {BASE_DIR}',
                exc_info=True
            )
            raise
