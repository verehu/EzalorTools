class Style(object):
    def __init__(self, workbook) -> None:
        super().__init__()

        # column auto fit
        self.column_auto_fit = workbook.add_format({'text_justlast': True})

        # specific
        self.table_headers = workbook.add_format(
            {'bold': True, 'bg_color': '#9ACEEC', 'border': 1})
        # common
        self.common = workbook.add_format({'border': 1})
