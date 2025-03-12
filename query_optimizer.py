import sqlparse

def optimize_query(query):
    recommendations = []
    if "SELECT *" in query.upper():
        recommendations.append("Gunakan SELECT spesifik untuk meningkatkan performa.")
    if "JOIN" in query.upper() and "WHERE" not in query.upper():
        recommendations.append("Gunakan WHERE untuk filter data sebelum JOIN.")
    return recommendations
