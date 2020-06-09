class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, data):
        '''
        Emit a single row of data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain test format.
    '''

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''

    def headings(self, headers):
        s = ''
        for h in headers:
            s += f'<th>{h}</th>'
        print(f'<tr>{s}</tr>')

    def row(self, rowdata):
        s = ''
        for r in rowdata:
            s += f'<td>{r}</td>'
        print(f'<tr>{s}</tr>')



class FormatError(Exception):
    pass


def create_formatter(fmt):
    '''
    Create a formatter based on the fmt, e.g. 'txt', 'csv', 'html'
    '''
    if fmt not in ['txt', 'csv', 'html']:
        raise FormatError('Unknown table format %s' % fmt)
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    return formatter


def print_table(objects, columns, formatter):
    '''
    Columns designate what to print with formatter object.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)
