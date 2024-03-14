from pyspark.sql import DataFrame


def generate_comprehensive_prompt(df: DataFrame) -> str:
    prompt = "Generate a comprehensive proposal from the merchant based on the following comments: \n"
    rows = df.collect()
    for row in rows:
        text = row['text']
        sentiment = row['sentiment']
        keywords = ', '.join(row['keywords'])
        prompt += f"\nreview contents: ：{text}\n"
        prompt += f"sentiments score: ：{sentiment}\n"
        prompt += f"keywords：{keywords}\n"
    prompt += "\ncomprehensive proposal: \n："
    return prompt


