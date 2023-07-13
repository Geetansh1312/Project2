from datetime import date
import pandas as pd
from jugaad_data.nse import stock_csv, stock_df

# Download as pandas dataframe
def sdata():
 df = stock_df(symbol="SBIN", from_date=date(2023, 1, 1),
 to_date=date(2023, 3, 30), series="EQ")
 return(pd.DataFrame(df))