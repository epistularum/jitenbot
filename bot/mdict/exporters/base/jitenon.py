from bot.mdict.exporters.base.exporter import BaseExporter


class JitenonExporter(BaseExporter):
    def _get_revision(self, entries):
        modified_date = None
        for entry in entries:
            if modified_date is None or entry.modified_date > modified_date:
                modified_date = entry.modified_date
        revision = modified_date.strftime("%Y年%m月%d日閲覧")
        return revision

    def _get_attribution(self, entries):
        modified_date = None
        for entry in entries:
            if modified_date is None or entry.modified_date > modified_date:
                attribution = entry.attribution
        return attribution
