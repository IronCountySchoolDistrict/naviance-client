naviance-client
########################################

This library enables you to perform data imports with Naviance's SchoolSync REST API.

Usage
===========
::

    from naviance import Naviance

    client = Naviance()
    
    # import parents
    client.import_parents(csv_data)
    # import students
    client.import_students(csv_data)
    