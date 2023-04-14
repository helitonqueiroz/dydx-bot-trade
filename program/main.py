from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED, PLACE_TRADES, MANAGE_EXITS
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results
from func_entry_pairs import open_positions
from func_exit_pairs import manage_trade_exits
from func_messaging import send_message

# MAIN FUNCTION
if __name__ == "__main__":

    # Message on Start
    success = send_message("Bot Launch successful")

    # Connect to client
    try:
        print("Conectando ao cliente")
        client = connect_dydx()
    except Exception as e:
        print("Erro de conexão ao cliente: ", e)
        send_message("Erro de conexão ao cliente")
        exit(1)

    # Abort al  open positions
    if ABORT_ALL_POSITIONS:
        try:
            print("Fechando todas as posições...")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("Erro fechando todas as posições! ", e)
            send_message(f"Erro fechando todas as posições {e}")
            exit(1)

    # Find Cointegrated Pairs
    if FIND_COINTEGRATED:

        # Construct Market Prices
        try:
            print("Buscando preços de mercado, por favor, aguarde 3 minutos....")
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print("Erro construindo os preços de mercado...", e)
            send_message(f"Erro construindo os preços de mercado {e}")
            exit(1)

    while True:

        # Place Trades for opening positions
        if MANAGE_EXITS:
            try:
                print("Gerenciando saídas...")
                manage_trade_exits(client)
            except Exception as e:
                print("Erro saindo das posições ", e)
                send_message(f"Erro saindo das posições {e}")
                exit(1)

        # Place Trades for opening positions
        if PLACE_TRADES:
            try:
                print("Procurando oportunidades de Trading...")
                open_positions(client)
            except Exception as e:
                print("Erro trading pares! ", e)
                send_message(f"Erro trading pares! {e}")
                exit(1)
