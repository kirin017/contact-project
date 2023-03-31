

from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtSql import QSqlDatabase,QSqlQuery

def _createContactsTable():
    """Create the contacts table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXIST contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(50),
            email VATCHAR(40) NOT NULL
            )
            """
    )

def createConnection(databaseName):
    """Create and open a data bse connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _createContactsTable()
    return True