#!/usr/bin/env python3
"""Filtered logger module"""
import logging
import mysql.connector
import os
import re
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        regex = field + f'[^{separator}]*'
        message = re.sub(regex, f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object"""
    # Create logger
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # Add RedactingFormatter to ch
    ch.setFormatter(RedactingFormatter)
    # Add ch to logger
    logger.addHandler(ch)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the database"""
    host = os.environ["PERSONAL_DATA_DB_HOST"]
    user = os.environ["PERSONAL_DATA_DB_USERNAME"]
    passwd = os.environ["PERSONAL_DATA_DB_PASSWORD"]
    db = os.environ["PERSONAL_DATA_DB_NAME"]
    myconn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=db
    )
    return myconn


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''Filter values in incoming log records'''
        message = super().format(record)
        log_message = filter_datum(self.fields, self.REDACTION, message,
                                   self.SEPARATOR)
        return log_message


if __name__ == '__main__':
    db = get_db()
    cursor = db.cursor()
    query = "SELECT group_concat(COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS\
            WHERE TABLE_SCHEMA = 'my_db' AND TABLE_NAME = 'users';"
    cursor.execute(query)

    for row in cursor:
        keys = row[0]

    keys = keys.split(',')

    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        to_join = [f'{k}={v}' for k, v in zip(keys, row)]
        message = "; ".join(to_join)
        message += ';'
        log_record = logging.LogRecord("user_data", logging.INFO, None, None,
                                       message, None, None)

        formatter = RedactingFormatter(fields=("name", "email", "phone", "ssn",
                                               "password"))

        print(formatter.format(log_record))

    cursor.close()
    db.close()
