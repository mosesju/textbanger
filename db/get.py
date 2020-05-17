from airtable import Airtable

def get(base_key, table_name, api_key):
    """
    Gets all data from an airtable

    Parameters
    ----------
    base_key: Key for the base
    table_name: Name of the Table
    api_key: Airtable API Key

    Returns
    -------
    list: of JSON formatted objects that include all data from table
    """
    at = Airtable(base_key, table_name, api_key)
    return at.get_all()