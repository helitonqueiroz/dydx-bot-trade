from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices

if __name__ == "__main__":

    # Connect to client
    try:
        print("Conectando ao cliente")
        client = connect_dydx()
    except Exception as e:
        print("Erro de conexão ao cliente: ", e)
        exit(1)
    # Abort al  open positions
    if ABORT_ALL_POSITIONS:
        try:
            print("Fechando todas as posições...")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("Erro fechando todas as posições! ", e)
            exit(1)

    # Find Cointegrated Pairs
    if FIND_COINTEGRATED:

        # Construct Market Prices
        try:
            print("Buscando preços de mercado, por favor, aguarde 3 minutos....")
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print("Erro construindo os preços de mercado...", e)
            exit(1)
