def get_all(at):
    """
    Gets all data from an airtable

    Parameters
    ----------
    at: airtable instance

    Returns
    -------
    list: of JSON formatted objects that include all data from table
    """
    return at.get_all()

def get_fields(at, fields):
    """
    Gets all data from an airtable

    Parameters
    ----------
    at: airtable instance
    fields: the fields which are you going to query

    Returns
    -------
    list: of JSON formatted objects that include all data from table
    """
    return at.get_all(fields=fields)