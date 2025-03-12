from backend.query_generator import generate_sql_query

def test_generate_sql():
    schema = "users(id INT PRIMARY KEY, name TEXT, age INT, city TEXT)"
    query = "Tampilkan semua pengguna yang berusia di atas 25 tahun"
    sql = generate_sql_query(query, schema)
    assert "SELECT" in sql and "WHERE age > 25" in sql
