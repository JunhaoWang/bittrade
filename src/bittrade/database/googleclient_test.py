from googleclient import getClosePriceTable
# Getting the date we need from google finance API
# currencyTicker represents the bitcoin price, and the most tradable currency include Japanese Yen, Swiss Franc,
# Australian Dollar, Canadian Dollar, Indian Rupee, Euro. The price data for these currency are all quoted in dollar.
currencyTickers = [
    "CURRENCY:BTCUSD", "CURRENCY:GBPUSD", "CURRENCY:JPYUSD", "CURRENCY:CHFUSD",
    "CURRENCY:AUDUSD", "CURRENCY:CADUSD", "CURRENCY:INRUSD", "CURRENCY:EURUSD",
]
# 24 Most Liquid ETFs:
# SPDR S&P 500 (SPY)
# Financial Select Sector SPDR (XLF)
# Russell 2000 Index Fund Profile (IWM)
# MSCI Emerging Markets Index Fund (EEM)
# PowerShares QQQ (QQQ)
# Vanguard MSCI Emerging Markets ETF (VWO)
# MSCI EAFE Index Fund (EFA)
# FTSE China 25 Index Fund (FXI)
# Industrial Select Sector SPDR Fund (XLI)
# Daily Small Cap Bear 3X Shares Fundamentals (TZA)
# Energy Select Sector SPDR Fund (XLE)
# UltraShort S&P500 (SDS)
# Silver Trust ETF (SLV)
# Direxion Daily Financial Bear 3x Shares (FAZ)
# Market Vectors TR Gold Miners ETF (GDX)
# MSCI Japan Index Fund (EWJ)
# UltraPro Short S&P500 (SPXU)
# MSCI Brazil Index Fund (EWZ)
# Daily Financial Bull 3X Shares (FAS)
# VelocityShares Daily 2x VIX Short-Term ETN (TVIX)
# United States Oil Fund (USO)
# SPDR Gold Shares (GLD)
# UltraShort Barclays 20+ Year Treasury (TBT)
# United States Natural Gas Fund (UNG)
etfTickers = [
    "NYSEARCA:XLF", "NYSEARCA:IWM", "NYSEARCA:EEM", "NASDAQ:QQQ", "NYSEARCA:VWO", "NYSEARCA:EFA",
    "NYSEARCA:FXI", "NYSEARCA:XLI", "NYSEARCA:TZA", "NYSEARCA:XLE", "NYSEARCA:SDS", "NYSEARCA:SLV",
    "NYSEARCA:FAZ", "NYSEARCA:GDX", "NYSEARCA:EWJ", "NYSEARCA:SPXU", "NYSEARCA:EWZ", "NYSEARCA:FAS",
    "NASDAQ:TVIX", "NYSEARCA:USO", "NYSEARCA:GLD", "NYSEARCA:TBT", "NYSEARCA:UNG",
]

table = getClosePriceTable(
    currencyTickers + etfTickers, interpolation=True, period='1Y',
)
print(table.head())
