import pandas as pd
from rest_framework import status


class AnalysisService():

    def __init__(self):
        self.df = pd.read_csv("./data/mockupinterviewdata.csv")

    def conversion_rate_calculation(self):
        try:
            grouped_by_customer = self.df.groupby('customer_id').sum()
            grouped_by_customer["conversion_rate"] = (
                grouped_by_customer['conversions'] / grouped_by_customer['revenue']) * 100

            max_rate = grouped_by_customer['conversion_rate'].idxmax()
            min_rate = grouped_by_customer['conversion_rate'].idxmin()

            return {
                "data": {
                    "grouped": grouped_by_customer["conversion_rate"].to_dict(),
                    "max": {max_rate: grouped_by_customer.loc[max_rate, 'conversion_rate']},
                    "min": {min_rate: grouped_by_customer.loc[min_rate, 'conversion_rate']}
                },
                "status": status.HTTP_200_OK
            }
        except Exception as e:
            return {"error": str(e), "status": status.HTTP_500_INTERNAL_SERVER_ERROR}

    def status_based_analysis(self):
        try:
            status_distribution = self.df.groupby(
                ['status', 'type', 'category']).size().reset_index(name='count')

            result = {"statuses": {}}

            status_summary_df = self.df.groupby('status').agg(
                total_revenue=('revenue', 'sum'),
                total_conversions=('conversions', 'sum')
            ).reset_index()

            result["status_summary"] = {
                row['status']: {
                    "total_revenue": row['total_revenue'],
                    "total_conversions": row['total_conversions']
                }
                for _, row in status_summary_df.iterrows()
            }

            for _, row in status_distribution.iterrows():
                status_ = row['status']
                type_ = row['type']
                category = row['category']
                count = row['count']

                if status_ not in result["statuses"]:
                    result["statuses"][status_] = {"type": {}}

                if type_ not in result["statuses"][status_]["type"]:
                    result["statuses"][status_]["type"][type_] = {
                        "category": {}}

                result["statuses"][status_]["type"][type_]["category"][category] = {
                    "count": count}

            return {"data": result, "status": status.HTTP_200_OK}

        except Exception as e:
            return {"error": str(e), "status": status.HTTP_500_INTERNAL_SERVER_ERROR}

    def category_type_analysis(self):
        try:
            category_type_summary = self.df.groupby(['type', 'category']).agg(
                total_revenue=('revenue', 'sum'),
                total_conversions=('conversions', 'sum')
            ).reset_index()

            result = {
                "category_type_summary": {
                    type_: {
                        "category": {
                            row['category']: {
                                "total_revenue": row['total_revenue'],
                                "total_conversions": row['total_conversions']
                            }
                            for _, row in group.iterrows()
                        }
                    }
                    for type_, group in category_type_summary.groupby('type')
                }
            }

            max_conversions_combination = category_type_summary.loc[
                category_type_summary['total_conversions'].idxmax()
            ]

            return {
                "data": {
                    "category_type_summary": result["category_type_summary"],
                    "max_conversions_combination": {
                        "type": max_conversions_combination['type'],
                        "category": max_conversions_combination['category'],
                        "total_revenue": max_conversions_combination['total_revenue'],
                        "total_conversions": max_conversions_combination['total_conversions']
                    }
                },
                "status": status.HTTP_200_OK
            }

        except Exception as e:
            return {"error": str(e), "status": status.HTTP_500_INTERNAL_SERVER_ERROR}

    def filter_and_aggregate(self):
        try:
            filtered_df = self.df[self.df['type'] == 'CONVERSION']

            average_summary = filtered_df.groupby('customer_id').agg(
                average_revenue=('revenue', 'mean'),
                average_conversions=('conversions', 'mean')
            ).reset_index()

            average_summary = {
                row['customer_id']: {
                    "average_revenue": row['average_revenue'],
                    "average_conversions": row['average_conversions']
                }
                for _, row in average_summary.iterrows()
            }

            return {"data": {"average_summary": average_summary}, "status": status.HTTP_200_OK}

        except Exception as e:
            return {"error": str(e), "status": status.HTTP_500_INTERNAL_SERVER_ERROR}
