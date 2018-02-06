class Style(object):
    def __init__(self, workbook) -> None:
        super().__init__()

        # title
        self.title = workbook.add_format({'align': 'center', 'font_size': 20})

        # specific
        self.table_headers = workbook.add_format(
            {'bold': True, 'bg_color': '#9ACEEC', 'border': 1})
        # common
        self.common = workbook.add_format({'border': 1})
        # error
        self.error = workbook.add_format({'border': 1, 'bg_color': '#FF0000'})
        # warning
        self.warning = workbook.add_format({'border': 1, 'bg_color': '#FFFFE0'})
