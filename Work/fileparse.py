import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    #_delimiter = delimeter
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        indices = []

        if has_headers:
            headers = next(rows)
            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
            if not has_headers:
                records.append(tuple(row))
            else:
                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)

    return records
