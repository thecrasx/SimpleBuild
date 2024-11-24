
t_config = """CREATE TABLE IF NOT EXISTS Config (
    file_hash TEXT,
    date_modified DATETIME
)"""

t_includes = """CREATE TABLE IF NOT EXISTS Includes (
    file TEXT,
    date_modified DATETIME
)"""