"""Processes portfolio data from investor

Clients are the starting unit of the API. Clients requests kick-off all the subsequent
requests to the API.

    Typical usage example:
    Portfolio.get_balanced_allocation(["ITSA4","B3SA3","ITUB3","BMGB4","WEGE3","NINJ3","EMBR3","NUBR34","MXRF11","HASH11"])
"""

class Portfolio():

    def get_recommended_allocation(portfolio,investment,user_risk=1,user_e_w=6,user_r_w=4):
        result = [
            {
                "ticker":"PETR4",
                "value":0.07087190132351276
            },
            {
                "ticker":"ITSA4",
                "value":0.057903537892886214
            },
            {
                "ticker":"ITUB3",
                "value":0.09799527153050935
            },
            {
                "ticker":"HASH11",
                "value":0.09799527153050935
            },
            {
                "ticker":"MXRF11",
                "value":0.09799527153050935
            }
            ]
        return result


