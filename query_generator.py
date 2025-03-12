import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_sql_query(user_query, table_schema):
    prompt = f"Convert the following natural language request into an SQL query:\n\nRequest: {user_query}\nSchema: {table_schema}\n\nSQL Query:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
