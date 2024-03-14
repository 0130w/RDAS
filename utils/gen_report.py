from pyspark.sql.dataframe import DataFrame


def generate_report(percentage: float, average_sentiment: float,
                    all_keywords: list, hourly_checkin: DataFrame, response: str) -> str:
    """ Generate a report based on stars, average_sentiment, keywords, hourly_checkin and llm response
    Parameters:
        percentage (float) : percentage of stars distribution
        average_sentiment (float) : average sentiment scores
        all_keywords (list) : list of keywords
        hourly_checkin (DataFrame) : hourly checkin data of a given business
        response (str) : advice from llm
    Returns:
        Report (str)
    """
    report = f"""Business Analytics Report
    - Merchant star ratings are over a percent {percentage:.2f} percent of merchants.
    - The average sentiment score is {average_sentiment:.2f}.
    - Keywords: {', '.join(all_keywords)}.
    - Hourly checkin distribution:
    """
    for hour, count in hourly_checkin.collect():
        report += f"      - {hour} hour: {count} times checkin\n"
    report += f'- Advice: {response}'
    return report
